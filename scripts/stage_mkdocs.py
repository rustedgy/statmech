"""Stage book directories for MkDocs without modifying source files."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / ".mkdocs-docs"
IGNORED_DIRS = {
    ".git", ".github", ".venv", "node_modules", "site",
    ".mkdocs-docs", "__pycache__",
}
INLINE_DOLLAR_MATH = re.compile(r"(?<!\$)\$\$(.+?)\$\$(?!\$)")
LECTURE_FILE = re.compile(r".*_lecture_(\d+).*_notes\.md$", re.IGNORECASE)
TRANSCRIPT_MARKER = "transcript_based"


def display_name(name: str) -> str:
    return re.sub(r"[_-]+", " ", name).strip().title()


def lecture_number(path: Path):
    match = LECTURE_FILE.fullmatch(path.name)
    return int(match.group(1)) if match else None


def lecture_label(path: Path) -> str:
    number = lecture_number(path)
    variant = " — transcript-based" if TRANSCRIPT_MARKER in path.stem else (
        " — topic-based" if number == 2 and "leonard_susskind" in path.as_posix() else ""
    )
    return f"Lecture {number}{variant}"


def make_readmes_directory_indexes(folder: Path) -> None:
    """MkDocs uses index.md for directory landing pages; source READMEs stay untouched."""
    for readme in sorted(folder.rglob("README.md")):
        index = readme.with_name("index.md")
        if not index.exists():
            readme.rename(index)


def normalize_inline_math(folder: Path) -> None:
    """Convert same-line inline $$...$$ to \\(...\\) in staged copies only.

    Standalone $$...$$ lines are left alone as display math. Fenced code blocks
    are also preserved. This avoids changing the Markdown source files.
    """
    for markdown in sorted(folder.rglob("*.md")):
        original = markdown.read_text(encoding="utf-8")
        output = []
        in_fence = False
        for line in original.splitlines(keepends=True):
            stripped = line.strip()
            if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
                in_fence = not in_fence
                output.append(line)
                continue
            if in_fence or re.fullmatch(r"\$\$.+?\$\$", stripped):
                output.append(line)
                continue
            output.append(INLINE_DOLLAR_MATH.sub(lambda match: r"\\(" + match.group(1) + r"\\)", line))
        updated = "".join(output)
        if updated != original:
            markdown.write_text(updated, encoding="utf-8")


def add_lecture_navigation(folder: Path) -> None:
    """Add staged-copy links between lecture numbers and alternate note versions."""
    lecture_files = [
        path for path in folder.glob("*.md")
        if lecture_number(path) is not None
    ]
    by_number = {}
    for path in lecture_files:
        by_number.setdefault(lecture_number(path), []).append(path)

    # Prefer the regular topic-based notes as the main route through the course.
    canonical = {}
    for number, paths in by_number.items():
        canonical[number] = sorted(
            paths,
            key=lambda path: (TRANSCRIPT_MARKER in path.stem, path.name.casefold()),
        )[0]
    ordered_numbers = sorted(canonical)

    for number, paths in by_number.items():
        previous_number = next((n for n in reversed(ordered_numbers) if n < number), None)
        next_number = next((n for n in ordered_numbers if n > number), None)
        for path in paths:
            content = path.read_text(encoding="utf-8").rstrip()
            if "<!-- generated lecture navigation -->" in content:
                content = content.split("<!-- generated lecture navigation -->", 1)[0].rstrip()

            links = []
            if previous_number is not None:
                target = canonical[previous_number]
                links.append(f"[← Previous: Lecture {previous_number}]({target.name})")
            if next_number is not None:
                target = canonical[next_number]
                links.append(f"[Next: Lecture {next_number} →]({target.name})")

            alternatives = [other for other in paths if other != path]
            if alternatives:
                alt_links = " · ".join(
                    f"[{lecture_label(other)}]({other.name})" for other in alternatives
                )
                links.append(f"**Other version:** {alt_links}")

            if links:
                content += (
                    "\n\n---\n\n<!-- generated lecture navigation -->\n"
                    + " · ".join(links)
                    + "\n"
                )
                path.write_text(content, encoding="utf-8")


def lecture_links_for_book(book_dir: Path, staged_dir: Path) -> list[str]:
    files = [
        path for path in staged_dir.glob("*.md")
        if lecture_number(path) is not None
    ]
    files.sort(key=lambda path: (lecture_number(path), TRANSCRIPT_MARKER in path.stem, path.name.casefold()))
    lines = []
    for path in files:
        lines.append(f"- [{lecture_label(path)}]({book_dir.name}/{path.name})")
    return lines


def main() -> None:
    # This directory is generated only in the GitHub Actions runner.
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    books = []
    for source in sorted(ROOT.iterdir(), key=lambda p: p.name.casefold()):
        if not source.is_dir() or source.name in IGNORED_DIRS or source.name.startswith("."):
            continue
        # A top-level directory is a book when it has its own README.md.
        if not (source / "README.md").is_file():
            continue
        destination = DOCS / source.name
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns(
                ".git", ".DS_Store", "__pycache__", ".venv", "node_modules"
            ),
        )
        make_readmes_directory_indexes(destination)
        normalize_inline_math(destination)
        add_lecture_navigation(destination)
        books.append(source.name)

    if not books:
        raise SystemExit(
            "No book directories found (expected a top-level directory with README.md)."
        )

    lines = [
        "# Statistical Mechanics — Lecture Notes",
        "",
        "A searchable reading site for statistical mechanics lecture notes. "
        "Choose a collection below, or jump directly to a lecture.",
        "",
        "The Markdown files in this repository are the source of truth. The published "
        "site is built automatically by GitHub Actions; no local setup is needed.",
        "",
        "## Lecture collections",
        "",
    ]
    for book in books:
        lines.append(f"### [{display_name(book)}]({book}/)")
        lines.append("")
        staged_book = DOCS / book
        links = lecture_links_for_book(staged_book, staged_book)
        if links:
            lines.extend(links)
        else:
            lines.append(f"[Open the collection overview]({book}/)")
        lines.append("")

    lines.extend([
        "## How to use these notes",
        "",
        "- Use the collection sidebar to move between topics and lectures.",
        "- Lecture pages include previous/next links; where two versions exist, "
        "they are linked as alternate notes rather than treated as separate lectures.",
        "- Search the site for a concept or equation using the search control.",
        "",
        "## Reading and notation",
        "",
        "These are study notes, not a substitute for the original lectures. Each "
        "collection overview describes its sources and known limitations.",
        "",
        "Math is rendered with MathJax. Display equations use standalone $$ delimiters; "
        "same-line inline $$...$$ expressions are normalized to \\(...\\) in the "
        "temporary publishing copy only.",
        "",
        "## Source repository",
        "",
        "[Browse the Markdown source on GitHub](https://github.com/rustedgy/statmech).",
        "",
    ])
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

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


def display_name(name: str) -> str:
    return re.sub(r"[_-]+", " ", name).strip().title()


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
        books.append(source.name)

    if not books:
        raise SystemExit(
            "No book directories found (expected a top-level directory with README.md)."
        )

    lines = [
        "# Statistical Mechanics — Lecture Notes",
        "",
        "A searchable reading site for statistical mechanics lecture notes. "
        "Choose a collection below, then use the navigation to move between lectures.",
        "",
        "The Markdown files in this repository are the source of truth. The published "
        "site is built automatically by GitHub Actions; no local setup is needed.",
        "",
        "## Lecture collections",
        "",
    ]
    for book in books:
        lines.append(f"- [{display_name(book)}]({book}/)")
    lines.extend([
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
    (DOCS / "index.md").write_text("\\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
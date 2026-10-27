"""Stage each top-level book directory for MkDocs without changing source files."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / ".mkdocs-docs"
IGNORED_DIRS = {
    ".git", ".github", ".venv", "node_modules", "site",
    ".mkdocs-docs", "__pycache__",
}


def display_name(name: str) -> str:
    return re.sub(r"[_-]+", " ", name).strip().title()


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
        shutil.copytree(source, DOCS / source.name, ignore=shutil.ignore_patterns(
            ".git", ".DS_Store", "__pycache__", ".venv", "node_modules"
        ))
        books.append(source.name)

    if not books:
        raise SystemExit("No book directories found (expected a top-level directory with README.md).")

    lines = [
        "# Statistical Mechanics — Lecture Notes",
        "",
        "Books and lecture-note collections in this repository:",
        "",
    ]
    for book in books:
        lines.append(f"- [{display_name(book)}]({book}/)")
    lines.append("")
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

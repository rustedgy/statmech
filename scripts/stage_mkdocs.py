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
LECTURE_FILE = re.compile(r".*_lecture_(\d+).*_notes\.md$", re.IGNORECASE)
TRANSCRIPT_MARKER = "transcript_based"

# Keep the generated homepage's topic list in the same order as mkdocs.yml.
MISC_TOPIC_PARTS = {
    "Part I — Foundations and Ensembles": (
        "notation_and_symbols.md",
        "indicator_functions_statmech.md",
        "temperature_from_statistical_mechanics.md",
        "partition_function_thermodynamics_generator.md",
        "grand_canonical_ensemble_chemical_potential.md",
        "two_level_system_schottky_anomaly.md",
    ),
    "Part II — Classical and Quantum Statistics": (
        "equipartition_of_energy.md",
        "maxwell_boltzmann_statistics.md",
        "maxwell_boltzmann_speed_distribution.md",
        "bose_einstein_statistics_derivation.md",
        "fermi_dirac_statistics_derivation.md",
    ),
    "Part III — Applications to Matter and Radiation": (
        "blackbody_radiation_planck_law.md",
        "paramagnetism_canonical_ensemble.md",
        "ising_model_ferromagnetism.md",
        "einstein_model_of_a_solid.md",
        "debye_model_of_a_solid.md",
    ),
    "Part IV — Stochastic Processes and Relaxation": (
        "markov_processes_statmech.md",
        "newtons_law_of_cooling_statmech.md",
    ),
}
MISC_TOPIC_ORDER = tuple(name for part in MISC_TOPIC_PARTS.values() for name in part)
MISC_TOPIC_ORDER_INDEX = {name: index for index, name in enumerate(MISC_TOPIC_ORDER)}
MISC_PART_BY_FILE = {
    name: part for part, names in MISC_TOPIC_PARTS.items() for name in names
}


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
        add_lecture_navigation(destination)
        books.append(source.name)

    if not books:
        raise SystemExit(
            "No book directories found (expected a top-level directory with README.md)."
        )

    lines = [
        "# Statistical Mechanics: Principles and Applications",
        "",
        "A developing, unnumbered book on statistical mechanics, alongside organized lecture-note collections. "
        "The book is grouped into thematic parts; chapter numbers are intentionally omitted while its contents grow.",
        "",
        "The Markdown files in this repository are the source of truth. The published "
        "site is built automatically by GitHub Actions; no local setup is needed.",
        "",
        "## Book and lecture collections",
        "",
    ]
    for book in books:
        book_title = "Statistical Mechanics: Principles and Applications" if book == "miscellaneous_topics" else display_name(book)
        lines.append(f"### [{book_title}]({book}/index.md)")
        lines.append("")
        staged_book = DOCS / book
        links = lecture_links_for_book(staged_book, staged_book)
        if links:
            lines.extend(links)
        else:
            if book == "miscellaneous_topics":
                lines.append(f"- [Book overview]({book}/index.md)")
                lines.append("")
                for part, filenames in MISC_TOPIC_PARTS.items():
                    lines.append(f"#### {part}")
                    lines.append("")
                    available = [name for name in filenames if (staged_book / name).is_file()]
                    for filename in available:
                        path = staged_book / filename
                        title = next(
                            (
                                line.lstrip("#").strip()
                                for line in path.read_text(encoding="utf-8").splitlines()
                                if line.startswith("# ")
                            ),
                            display_name(path.stem),
                        )
                        lines.append(f"- [{title}]({book}/{path.name})")
                    lines.append("")
            else:
                lines.append(f"- [Collection overview]({book}/index.md)")
                topic_pages = sorted(
                    (path for path in staged_book.glob("*.md") if path.name != "index.md"),
                    key=lambda path: path.name.casefold(),
                )
                for path in topic_pages:
                    title = next(
                        (
                            line.lstrip("#").strip()
                            for line in path.read_text(encoding="utf-8").splitlines()
                            if line.startswith("# ")
                        ),
                        display_name(path.stem),
                    )
                    lines.append(f"- [{title}]({book}/{path.name})")
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
        "Math is rendered with MathJax. Use single-dollar delimiters (`$..."""Stage book directories for MkDocs without modifying source files."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / ".mkdocs-docs"
IGNORED_DIRS = {
    ".git", ".github", ".venv", "node_modules", "site",
    ".mkdocs-docs", "__pycache__",
}
LECTURE_FILE = re.compile(r".*_lecture_(\d+).*_notes\.md$", re.IGNORECASE)
TRANSCRIPT_MARKER = "transcript_based"

# Keep the generated homepage's topic list in the same order as mkdocs.yml.
MISC_TOPIC_PARTS = {
    "Part I — Foundations and Ensembles": (
        "notation_and_symbols.md",
        "indicator_functions_statmech.md",
        "temperature_from_statistical_mechanics.md",
        "partition_function_thermodynamics_generator.md",
        "grand_canonical_ensemble_chemical_potential.md",
        "two_level_system_schottky_anomaly.md",
    ),
    "Part II — Classical and Quantum Statistics": (
        "equipartition_of_energy.md",
        "maxwell_boltzmann_statistics.md",
        "maxwell_boltzmann_speed_distribution.md",
        "bose_einstein_statistics_derivation.md",
        "fermi_dirac_statistics_derivation.md",
    ),
    "Part III — Applications to Matter and Radiation": (
        "blackbody_radiation_planck_law.md",
        "paramagnetism_canonical_ensemble.md",
        "ising_model_ferromagnetism.md",
        "einstein_model_of_a_solid.md",
        "debye_model_of_a_solid.md",
    ),
    "Part IV — Stochastic Processes and Relaxation": (
        "markov_processes_statmech.md",
        "newtons_law_of_cooling_statmech.md",
    ),
}
MISC_TOPIC_ORDER = tuple(name for part in MISC_TOPIC_PARTS.values() for name in part)
MISC_TOPIC_ORDER_INDEX = {name: index for index, name in enumerate(MISC_TOPIC_ORDER)}
MISC_PART_BY_FILE = {
    name: part for part, names in MISC_TOPIC_PARTS.items() for name in names
}


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
        add_lecture_navigation(destination)
        books.append(source.name)

    if not books:
        raise SystemExit(
            "No book directories found (expected a top-level directory with README.md)."
        )

    lines = [
        "# Statistical Mechanics: Principles and Applications",
        "",
        "A developing, unnumbered book on statistical mechanics, alongside organized lecture-note collections. "
        "The book is grouped into thematic parts; chapter numbers are intentionally omitted while its contents grow.",
        "",
        "The Markdown files in this repository are the source of truth. The published "
        "site is built automatically by GitHub Actions; no local setup is needed.",
        "",
        "## Book and lecture collections",
        "",
    ]
    for book in books:
        book_title = "Statistical Mechanics: Principles and Applications" if book == "miscellaneous_topics" else display_name(book)
        lines.append(f"### [{book_title}]({book}/index.md)")
        lines.append("")
        staged_book = DOCS / book
        links = lecture_links_for_book(staged_book, staged_book)
        if links:
            lines.extend(links)
        else:
            if book == "miscellaneous_topics":
                lines.append(f"- [Book overview]({book}/index.md)")
                lines.append("")
                for part, filenames in MISC_TOPIC_PARTS.items():
                    lines.append(f"#### {part}")
                    lines.append("")
                    available = [name for name in filenames if (staged_book / name).is_file()]
                    for filename in available:
                        path = staged_book / filename
                        title = next(
                            (
                                line.lstrip("#").strip()
                                for line in path.read_text(encoding="utf-8").splitlines()
                                if line.startswith("# ")
                            ),
                            display_name(path.stem),
                        )
                        lines.append(f"- [{title}]({book}/{path.name})")
                    lines.append("")
            else:
                lines.append(f"- [Collection overview]({book}/index.md)")
                topic_pages = sorted(
                    (path for path in staged_book.glob("*.md") if path.name != "index.md"),
                    key=lambda path: path.name.casefold(),
                )
                for path in topic_pages:
                    title = next(
                        (
                            line.lstrip("#").strip()
                            for line in path.read_text(encoding="utf-8").splitlines()
                            if line.startswith("# ")
                        ),
                        display_name(path.stem),
                    )
                    lines.append(f"- [{title}]({book}/{path.name})")
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
        ") for inline "
        "math and standalone double-dollar delimiters (`$...$`) for display equations.",
        "",
        "## Source repository",
        "",
        "[Browse the Markdown source on GitHub](https://github.com/rustedgy/statmech).",
        "",
    ])
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

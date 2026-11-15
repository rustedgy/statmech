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
        "from_microstates_to_statistical_ensembles.md",
        "temperature_from_statistical_mechanics.md",
        "canonical_ensemble_boltzmann_distribution.md",
        "partition_function_thermodynamics_generator.md",
        "grand_canonical_ensemble_chemical_potential.md",
        "two_level_system_schottky_anomaly.md",
    ),
    "Part II — Classical and Quantum Statistics": (
        "equipartition_of_energy.md",
        "maxwell_boltzmann_statistics.md",
        "maxwell_boltzmann_speed_distribution.md",
        "bose_einstein_statistics_derivation.md",
        "bose_einstein_condensation_ideal_gas.md",
        "fermi_dirac_statistics_derivation.md",
    ),
    "Part III — Applications to Matter and Radiation": (
        "blackbody_radiation_planck_law.md",
        "paramagnetism_canonical_ensemble.md",
        "ising_model_ferromagnetism.md",
        "liquid_gas_phase_transitions_condensation.md",
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

    def page_title(folder: Path, filename: str) -> str:
        path = folder / filename
        if not path.is_file():
            return display_name(path.stem)
        return next(
            (
                line[2:].strip()
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.startswith("# ")
            ),
            display_name(path.stem),
        )

    book_dir = DOCS / "miscellaneous_topics"
    counting_chapters = (
        "counting_framework_finite_systems.md",
        "large_n_counting_stirling_approximation.md",
        "counting_factorization_and_interactions.md",
        "counting_equilibrium_exchange.md",
    )
    part_descriptions = {
        "Part I — Foundations and Ensembles":
            "Build the language of statistical mechanics, from microscopic states and entropy to temperature, equilibrium, and the major statistical ensembles.",
        "Part II — Classical and Quantum Statistics":
            "Develop the classical and quantum rules governing how particles occupy available states, and explore their physical consequences.",
        "Part III — Applications to Matter and Radiation":
            "Apply ensemble methods and quantum statistics to radiation, magnetic systems, phase transitions, and the heat capacity of solids.",
        "Part IV — Stochastic Processes and Relaxation":
            "Study probabilistic time evolution, Markov processes, detailed balance, and the approach to thermal equilibrium.",
    }

    lines = [
        "# Statistical Mechanics: Principles and Applications",
        "",
        "This is a developing, unnumbered textbook for undergraduate study. It builds statistical mechanics from microscopic descriptions and counting arguments through ensembles, quantum statistics, and applications to physical systems.",
        "",
        "The book is organized by subject rather than by a particular course. Chapters are kept unnumbered while the content and sequence continue to develop. The Markdown files in this repository are the source of truth.",
        "",
        "## Start reading",
        "",
        "Begin with the [book overview](miscellaneous_topics/index.md), then read [Microstates, Macrostates, and the Microcanonical Ensemble](miscellaneous_topics/from_microstates_to_statistical_ensembles.md). This opening chapter establishes the basic language used throughout the book.",
        "",
        "## The book at a glance",
        "",
        "[Open the complete book contents](miscellaneous_topics/index.md). The four Parts provide the main route through the material:",
        "",
    ]
    for part, filenames in MISC_TOPIC_PARTS.items():
        lines.extend([
            f"### {part}",
            "",
            part_descriptions[part],
            "",
            f"[Start this Part](miscellaneous_topics/{filenames[0]})",
            "",
        ])

    lines.extend([
        "## Supplementary mathematical tools",
        "",
        "A small set of mathematical methods supports the main development without being tied to one particular Part.",
        "",
        f"- [Indicator Functions]({ 'miscellaneous_topics/indicator_functions_statmech.md' }) — a practical tool for expressing conditions, counting states, and restricting sums.",
        "",
        "## A separate counting framework",
        "",
        "These self-contained chapters develop a counting-based framework that can be read independently or alongside the book. They focus on finite systems, large-number limits, factorization, interactions, and equilibrium by exchange.",
        "",
    ])
    for filename in counting_chapters:
        if (book_dir / filename).is_file():
            lines.append(f"- [{page_title(book_dir, filename)}](miscellaneous_topics/{filename})")
    lines.extend([
        "",
        "## Lecture-note collections",
        "",
        "The lecture notes are companion study resources based on specific courses. They are separate from the textbook and include source information and collection-specific caveats.",
        "",
        "- [John Preskill — lecture-note collection](john_preskill/index.md)",
        "- [Leonard Susskind — lecture-note collection](leonard_susskind/index.md)",
        "",
        "## Using the site",
        "",
        "- Use the navigation sidebar for the full chapter and lecture lists.",
        "- Use the search control to find a topic, term, or equation.",
        "- Read lecture notes alongside the original lectures; they are study aids, not substitutes for the source material.",
        "",
        "## Mathematics and notation",
        "",
        "The site renders mathematics with MathJax. Inline expressions use single-dollar delimiters ($...$); display equations use double-dollar delimiters ($$...$$) on separate lines. Individual chapters explain their notation and assumptions where needed.",
        "",
        "## Source repository",
        "",
        "[Browse the Markdown source, report an issue, or suggest a correction on GitHub](https://github.com/rustedgy/statmech).",
        "",
    ])
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

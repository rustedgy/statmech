# Statistical Mechanics: Principles and Applications

A developing book of self-contained chapters on statistical mechanics, accompanied by lecture notes from selected courses.

**Read the published site:** https://rustedgy.github.io/statmech/

## Book structure

The book is organized thematically into parts covering foundations and ensembles, classical and quantum statistics, applications to matter and radiation, and stochastic processes and relaxation. Chapter numbers are intentionally omitted while the contents and ordering continue to evolve.

The Markdown files in `miscellaneous_topics/` are the source of truth for the book. The directory name is retained for source-path stability; the published site presents it under the book title rather than as miscellaneous material.

## Lecture-note collections

- [John Preskill lecture notes](john_preskill/README.md)
- [Leonard Susskind lecture notes](leonard_susskind/README.md)

Each lecture collection documents its sources, credits, contents, and known caveats.

## Publishing and contributing

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) builds the reading site.
- GitHub Actions builds and publishes the site to GitHub Pages whenever changes are pushed to `main`.
- The build stages copies of the source directories in the Actions runner; it does not rewrite source files.
- No local Python, MkDocs, or theme installation is required to contribute.

Corrections and improvements are welcome. Open an issue or submit a pull request with changes to the Markdown source files. The GitHub Actions workflow builds the site for pull requests so build problems can be caught before merging.

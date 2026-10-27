# Statistical Mechanics — Lecture Notes

Study notes for statistical mechanics lecture series, with one directory per lecture collection.

**Read the published notes:** https://rustedgy.github.io/statmech/

## How it works

- The Markdown files in each book directory are the source of truth.
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) builds the reading site.
- GitHub Actions builds and publishes the site to GitHub Pages whenever changes are pushed to `main`.
- The build stages copies of the book directories in the Actions runner; it does not rewrite or generate files in the source directories.
- No local Python, MkDocs, or theme installation is required to contribute.

## Books

- [John Preskill lecture notes](john_preskill/README.md)
- [Leonard Susskind lecture notes](leonard_susskind/README.md)

Each book README documents its sources, credits, contents, and known caveats. The published homepage links directly to each available lecture. Lecture pages include previous/next links, and alternate versions of a lecture are linked together.

## Contributing

Corrections and improvements are welcome. Open an issue or submit a pull request with changes to the Markdown source files. The GitHub Actions workflow builds the site for pull requests so build problems can be caught before merging.

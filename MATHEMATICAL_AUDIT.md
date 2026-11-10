# Mathematical and notation audit

This file records the scope and status of the book's mathematical consistency review. A successful MkDocs build checks that the source can be rendered and linked; it does **not** establish that a derivation is mathematically or physically correct. Mathematical checks are recorded separately below.

## Review standard

For each derivation, check:

- the model, assumptions, ensemble, and constraints are stated before use;
- every derivative identifies the variables held fixed;
- combinatorial factors, degeneracies, Jacobians, signs, and boundary terms are included;
- dimensions and normalizations agree on both sides of each equation;
- limiting cases and numerical coefficients are reproduced independently;
- approximations are distinguished from exact finite-system statements;
- notation is defined locally and used consistently;
- displayed mathematics, prose mathematics, figures, axes, units, and internal links render as intended.

## Focused corrections tracked in GitHub

The first review pass identified the following mathematical or explanatory work. These are deliberately separate, reviewable changes rather than one large unstructured manuscript edit.

| Topic | GitHub issue | Scope |
|---|---:|---|
| Maxwell–Boltzmann multiplicity | [#50](https://github.com/rustedgy/statmech/issues/50) | Reconcile labelled and Gibbs-corrected counting, entropy, and extensivity. |
| Microcanonical entropy | [#51](https://github.com/rustedgy/statmech/issues/51) | Distinguish shell multiplicity/density of states from cumulative phase-space volume and compare finite-size temperatures. |
| Liquid–gas coexistence | [#52](https://github.com/rustedgy/statmech/issues/52) | Derive Maxwell equal area from equality of chemical potentials and state nucleation assumptions. |
| Debye model | [#53](https://github.com/rustedgy/statmech/issues/53) | Check polarization counting, mode normalization, differentiation, integration by parts, and limiting coefficients. |
| BE/FD statistics | [#54](https://github.com/rustedgy/statmech/issues/54) | Separate exact multiplicities from Stirling approximations and coarse-grained most-probable occupations from exact orbital means. |
| Foundations and ensembles | [#55](https://github.com/rustedgy/statmech/issues/55) | Make the probability, entropy, reservoir, ensemble, and thermodynamic-potential chain explicit. |
| Ideal Bose gas condensation | [#56](https://github.com/rustedgy/statmech/issues/56) | Derive the density of states, excited-state saturation, critical temperature, and condensate fraction. |

## Checks made in this pass

- Corrected literal backslash-n sequences in the review-question lists of the Maxwell–Boltzmann, Bose–Einstein, and Fermi–Dirac chapters. These were source-text formatting defects that could cause multiple questions to render on the same line.
- Added or expanded explicit assumptions and intermediate steps in the focused chapter corrections listed above. Those changes remain independently reviewable in their issue-specific pull requests.
- Kept mathematical verification distinct from CI/build success. The audit is not complete merely because the site builds.

## Global conventions to maintain

- Use $U$ for internal energy unless a chapter has a clearly stated reason to use $E$; define any local distinction.
- Distinguish pressure $p$ from probability $P$ by context and notation.
- Distinguish particle mass $m$ from total mass $M$.
- Distinguish chemical potential $\mu$ from magnetic moment (use a separate symbol such as $\mathfrak m$ or $\mu_{\rm mag}$ where needed).
- Distinguish a degeneracy $g_i$ (a number of states) from a density of states $g(\epsilon)$ (states per unit energy).
- State whether heat capacities are at fixed $V$, $p$, $B$, or $H$ where that distinction matters.
- State whether zero-point energies are included in $U$; they do not affect heat capacity when temperature-independent.

## Remaining work

This is an initial audit register, not a certification that every equation, figure, or reference in the repository has been independently re-derived. The remaining chapters and figures still require a systematic pass for dimensions, normalization, boundary terms, assumptions, notation, and rendering. Record a check as complete only after the relevant calculation has been reproduced independently and the source and published rendering have both been inspected.

---
title: Lecture 1 Notes
---

# Statistical Mechanics — Lecture 1

## The central question

Statistical mechanics connects the microscopic description of matter to the macroscopic world of temperature, pressure, and entropy.

## Microstates and macrostates

A microstate is a detailed microscopic specification of a system. A macrostate is a description in terms of coarse-grained variables such as total energy, volume, or particle number. Many microstates may correspond to the same macrostate.

The multiplicity $\Omega$ of a macrostate is the number of compatible microstates.

If the microstates are equally probable, a macrostate with larger multiplicity is more likely:

$$
P(\text{macrostate}) \propto \Omega.
$$

## Coins as a model

With $N$ fair coins, the number of sequences with exactly $n$ heads is:

$$
\Omega(n)=\binom{N}{n} = \frac{N!}{n!(N-n)!}.
$$

For large $N$, the most likely outcomes are near the center, where the multiplicity is largest. This is the basic intuition behind statistical mechanics: typical outcomes are not special; they are simply overwhelmingly more numerous.

## Entropy and multiplicity

Boltzmann entropy is:

$$
S = k_B \ln \Omega.
$$

The logarithm is useful because multiplicities of independent subsystems multiply, while entropies add.

## Equilibrium and direction of processes

A system in equilibrium is one whose macroscopic properties are stable under the given constraints. One reason macroscopic processes have a direction is that equilibrium states generally correspond to enormously larger multiplicities than specially prepared non-equilibrium states.

## Key takeaways

- macrostates are coarse descriptions
- multiplicity counts compatible microstates
- entropy is related to multiplicity
- the most probable macrostates are typically the ones that dominate large systems

## Full markdown source

The original note file is here:

- [Lecture 1 markdown source](https://github.com/rustedgy/statmech/blob/main/leonard_susskind/statistical_mechanics_lecture_1_notes.md)

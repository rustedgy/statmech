---
title: Lecture 2 Transcript Notes
permalink: /lecture-2-transcript/
---

<script type="text/javascript" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Statistical Mechanics — Lecture 2 Transcript-Based Notes

This version follows the supplied transcript more closely and emphasizes the relation between temperature, entropy, and thermal equilibrium.

## Temperature and energy units

The lecture begins by emphasizing that temperature is naturally connected to energy. In SI units, the Boltzmann constant provides the conversion between Kelvin temperature and microscopic energy scales:

$$
k_B \approx 1.38 \times 10^{-23}\ \mathrm{J\,K^{-1}}.
$$

A useful re-expression is that temperature in energy units is:

$$
T = k_B T_K.
$$

This makes many statistical-mechanical formulas cleaner.

## Statistical entropy

For a probability distribution $p_i$, the dimensionless statistical entropy is:

$$
S = -\sum_i p_i \ln p_i.
$$

For a uniform distribution over $\Omega$ states,

$$
S = \ln \Omega.
$$

The thermodynamic entropy in conventional units is then related by:

$$
S_{\mathrm{th}} = k_B S.
$$

## Temperature as $dE/dS$

The lecture defines temperature by the way the average energy changes as entropy changes:

$$
T = \frac{dE}{dS}.
$$

This leads to the familiar differential relation:

$$
dE = T\,dS.
$$

## Heat flow and equilibrium

For two systems that can exchange energy, total energy is conserved and entropy adds. The second law implies that spontaneous evolution tends to increase total entropy. This gives the familiar result:

- energy flows from hotter to colder systems
- equilibrium occurs when the two temperatures are equal

In other words, thermal equilibrium occurs when there is no net energy flow between systems at the same temperature.

## Main lesson

The lecture recasts temperature as a statistical quantity derived from the structure of the probability distribution and the amount of accessible microstates, rather than only as a thermometer reading.

## Full markdown source

The original transcript-based note is here:

- [Lecture 2 transcript-based markdown source](https://github.com/rustedgy/statmech/blob/main/leonard_susskind/statistical_mechanics_lecture_2_transcript_based_notes.md)

[Back to overview](./overview/)

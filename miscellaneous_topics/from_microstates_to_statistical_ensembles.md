# Microstates, Macrostates, and the Microcanonical Ensemble

## 1. Microscopic states and macroscopic descriptions

A **microstate** specifies the microscopic configuration of a system at the level of detail used by a model. A **macrostate** specifies a smaller set of macroscopic quantities—such as energy, volume, particle number, or magnetization. Many distinct microstates can be compatible with the same macrostate.

The number of microstates compatible with a macrostate is its **multiplicity**, commonly denoted by $W$ or $\Omega$. Statistical mechanics connects this microscopic counting to probabilities and, ultimately, thermodynamic behavior.

An **ensemble** is a probability distribution over possible microstates under specified constraints. It is a mathematical description of the statistical state of a system, not a separate physical system and not automatically a time average. Equating time and ensemble averages requires additional dynamical assumptions.

## 2. The microcanonical description

For an isolated system in equilibrium with fixed energy $E$, volume $V$, and particle number $N$, the microcanonical ensemble assigns equal probability to every accessible microstate in the specified energy range. If there are $W(E,V,N)$ such states, then

$$
P_r=\frac{1}{W(E,V,N)}
$$

for each accessible state $r$, and zero for inaccessible states.

The **equal-a-priori-probability postulate** is a foundational equilibrium assumption. It is not a theorem that follows from counting alone. It is used when the system is isolated on the timescale of interest and the specified macroscopic constraints are the only known restrictions on its accessible states.

For a classical system with continuous energies, an exact energy surface has zero phase-space volume. One therefore counts states in a finite shell, for example $E\leq H<E+\Delta E$. For a quantum system, one counts energy eigenstates in the chosen energy window. The choice between a shell count and a cumulative count of all states below $E$ can matter for finite systems; the distinction and its consequences for temperature are examined in [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md).

## 3. Boltzmann entropy and the most probable macrostate

For $W$ equally likely accessible states, the Boltzmann entropy is

$$
\boxed{S=k_B\ln W.}
$$

The logarithm is useful because multiplicities multiply for independent systems. If $W_{AB}=W_AW_B$, then

$$
S_{AB}=k_B\ln(W_AW_B)=S_A+S_B.
$$

Suppose two weakly coupled systems can exchange energy while their total energy remains fixed. If system A has energy $E_A$ and system B has energy $E_{\mathrm{tot}}-E_A$, and if their multiplicities multiply, the multiplicity of that energy split is

$$
W_{\mathrm{tot}}(E_A)
=W_A(E_A)W_B(E_{\mathrm{tot}}-E_A).
$$

The probability of a macrostate is proportional to its multiplicity under the equal-probability assumption. Thus the most probable energy split is the one that maximizes $W_{\mathrm{tot}}$, or equivalently the total entropy. The detailed equilibrium condition and its interpretation as equality of temperatures are developed in [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md).

For macroscopic systems, the multiplicity is typically enormous and the probability is sharply concentrated near the entropy maximum. Equilibrium therefore describes the overwhelmingly likely macrostate, even though many microscopic configurations remain possible.

## 4. From isolated systems to reservoirs: the ensemble roadmap

The microcanonical ensemble describes an isolated system. Other ensembles describe a subsystem that can exchange conserved quantities with a much larger reservoir:

| Ensemble | Fixed control variables | Quantities that may fluctuate |
|---|---|---|
| Microcanonical | $E,V,N$ | None of these constraints |
| Canonical | $T,V,N$ | Energy |
| Grand canonical | $T,V,\mu$ | Energy and particle number |

The canonical and grand canonical distributions are not introduced here by repeating their reservoir derivations. The canonical Boltzmann distribution is derived in [The Canonical Ensemble and the Boltzmann Distribution](canonical_ensemble_boltzmann_distribution.md), and the grand canonical distribution is derived in [The Grand Canonical Ensemble and Chemical Potential](grand_canonical_ensemble_chemical_potential.md).

The chapters that follow build the ideas in a deliberate order: first the entropy definition of temperature and thermal equilibrium; then the canonical distribution; then the partition function as a generator of thermodynamic properties; and finally particle exchange and the grand canonical ensemble.

## Summary

- A microstate is a complete microscopic specification within a model; a macrostate specifies macroscopic constraints.
- Multiplicity counts the microstates compatible with a macrostate.
- The microcanonical ensemble assigns equal probability to accessible states of an isolated system at fixed $E,V,N$.
- Boltzmann entropy is $S=k_B\ln W$.
- The most probable macrostate maximizes multiplicity, equivalently entropy.
- Canonical and grand canonical reservoir derivations are treated in their own chapters, rather than duplicated in this introduction.

## Review questions

1. Distinguish a microstate from a macrostate, and give an example of many microstates corresponding to one macrostate.
2. Why is an energy shell used when counting states in a classical system with continuous energies?
3. State the equal-a-priori-probability postulate and explain why it is an assumption.
4. Show that Boltzmann entropy is additive when the multiplicity of two independent systems factorizes.
5. Explain why the most probable energy division of two weakly coupled systems maximizes total entropy.
6. What quantities are fixed, and what quantities may fluctuate, in the microcanonical, canonical, and grand canonical ensembles?

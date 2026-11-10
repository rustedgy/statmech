# From Microstates to Statistical Ensembles

## 1. Why statistical mechanics needs both counting and probability

A macroscopic system is described by a small number of variables—such as energy, volume, particle number, magnetization, and temperature—but its microscopic description contains an enormous number of degrees of freedom. A **microstate** specifies the microscopic state completely at the level of the model. A **macrostate** specifies only the macroscopic constraints or measured quantities.

Many microstates can correspond to the same macrostate. The number of compatible microstates is its **multiplicity**, often denoted by $W$ or $\Omega$. A central task of statistical mechanics is to connect this multiplicity, together with a probability rule for microscopic states, to observable thermodynamic behavior.

An ensemble is a probability distribution over the possible microstates of a system under specified constraints. It is a mathematical description of uncertainty about the system's microscopic state, not a separate physical system and not, by definition, a time average. A time average equals an ensemble average only under additional dynamical assumptions, such as suitable ergodic behavior.

## 2. Equal a priori probabilities and the microcanonical description

For an isolated system in equilibrium, with fixed energy $E$, volume $V$, and particle number $N$, the microcanonical ensemble assigns equal probability to all accessible microstates compatible with those constraints. If there are $W(E,V,N)$ such states, then

$$
P_r=\frac{1}{W(E,V,N)}
$$

for each accessible state $r$, and zero for inaccessible states.

The equal-a-priori-probability postulate is a foundational equilibrium assumption, not a theorem that follows from counting alone. It is appropriate when the system is isolated on the timescale of interest, its macroscopic constraints are specified, and the accessible states are sampled without a further known bias. In classical systems with continuous energies, one must specify a finite energy shell, for example $E\leq H<E+\Delta E$; an exact energy surface has zero phase-space volume. For quantum systems, one counts energy eigenstates in the chosen energy window.

The Boltzmann entropy for a discrete set of equally likely accessible states is

$$
S=k_B\ln W.
$$

The logarithm makes entropy additive for independent systems: if the combined multiplicity factorizes as $W_{AB}=W_AW_B$, then $S_{AB}=S_A+S_B$. The choice of state-counting convention (energy shell or cumulative phase-space volume, for example) must be stated when finite-size effects matter; see [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md).

The equilibrium macrostate is overwhelmingly likely when its multiplicity is much larger than that of competing macrostates. This is a probabilistic statement: equilibrium is not necessarily the only possible microstate, but the number of microstates compatible with equilibrium macroscopic values is typically dominant for a large system.

## 3. From multiplicity to equilibrium and temperature

Suppose two weakly coupled systems can exchange energy while their combined energy is fixed. If subsystem A has energy $E_A$, subsystem B has energy $E_{\\rm tot}-E_A$, and their multiplicities are $W_A(E_A)$ and (W_B$E_{\\rm tot}-E_A$), then the multiplicity of the combined macrostate is

$$
W_{\rm tot}$E_A$=W_A$E_A$W_B(E_{\rm tot}-E_A).
$$

The most probable energy division maximizes this product, equivalently its logarithm. With $S_i=k_B\ln W_i$, stationarity gives

$$
\left(\frac{\partial S_A}{\partial E_A}\right)_{V_A,N_A}
=
\left(\frac{\partial S_B}{\partial E_B}\right)_{V_B,N_B}.
$$

This motivates the thermodynamic definition

$$
\boxed{\frac{1}{T}=\left(\frac{\partial S}{\partial U}\right)_{V,N}.}
$$

The derivative is taken at fixed volume and particle number. Equality of temperature is therefore the condition for no first-order entropy gain from a small energy transfer between systems. The curvature of the total entropy determines whether the stationary point is a maximum and hence stable.

This argument illustrates the logic of equilibrium: count compatible states, form the probability of a macrostate, and identify the overwhelmingly likely energy division. The temperature chapter discusses the subtleties of entropy conventions and finite systems.

## 4. The canonical ensemble: a system in a heat reservoir

Now let a small system exchange energy with a much larger reservoir. The combined system is isolated, so if the small system is in microstate $r$ with energy $E_r$, the reservoir energy is $E_R=E_{\\rm tot}-E_r$.

The probability of microstate $r$ is proportional to the number of reservoir states compatible with that energy:

$$
P_r\propto \exp\left(\frac{S_R(E_{\rm tot}-E_r)}{k_B}\right).
$$

If the reservoir is large and its entropy is smooth over the energy range exchanged, expand to first order:

$$
S_R(E_{\rm tot}-E_r)
\simeq S_R(E_{\rm tot})
-\left(\frac{\partial S_R}{\partial E_R}\right)_{V_R,N_R}E_r.
$$

Using $(\partial S_R/\partial E_R)_{V_R,N_R}=1/T$,

$$
P_r\propto e^{-E_r/(k_BT)}=e^{-\beta E_r},
\qquad \beta=\frac{1}{k_BT}.
$$

The normalized probability is

$$
\boxed{P_r=\frac{e^{-\beta E_r}}{Z}},
\qquad
Z=\sum_r e^{-\beta E_r}.
$$

The partition function $Z$ is the sum of the unnormalized weights. Dividing by it makes the probabilities sum to one. It also generates thermodynamic quantities: $F=-k_BT\ln Z$, $U=-\partial_\beta\ln Z$ at fixed external parameters, and $S=k_B(\ln Z+\beta U)$. The logarithm appears because independent subsystems have factorizing partition functions, so their logarithms—and therefore their free energies—add.

The reservoir derivation assumes weak enough coupling that the subsystem energy is well defined, a reservoir much larger than the subsystem, and negligible higher-order terms in the reservoir entropy expansion. If the reservoir is not large, or the exchanged energy is not small on the reservoir's thermodynamic scale, the canonical exponential need not be an accurate description.

## 5. The grand canonical ensemble: energy and particles can be exchanged

If the subsystem can exchange particles as well as energy, its reservoir changes both energy and particle number. For subsystem energy $E_r$ and particle number $N$, the reservoir has $E_R=E_{\\rm tot}-E_r$ and $N_R=N_{\\rm tot}-N$. A first-order expansion gives

$$
S_R\simeq S_{R,0}
-\left(\frac{\partial S_R}{\partial E_R}\right)_{N_R,V_R}E_r
-\left(\frac{\partial S_R}{\partial N_R}\right)_{E_R,V_R}N.
$$

Using

$$
\left(\frac{\partial S}{\partial E}\right)_{V,N}=\frac{1}{T},
\qquad
\left(\frac{\partial S}{\partial N}\right)_{E,V}=-\frac{\mu}{T},
$$

the subsystem weight becomes

$$
P_{r,N}\propto e^{-\beta(E_r-\mu N)}.
$$

The sign is important: removing $N$ particles from the reservoir changes its entropy by (+\mu N/T), which favors larger subsystem particle number when the reservoir chemical potential is larger. After normalization,

$$
\boxed{P_{r,N}=\frac{e^{-\beta(E_r-\mu N)}}{\Xi}},
\qquad
\Xi=\sum_{N,r}e^{-\beta(E_r-\mu N)}.
$$

Here $\Xi$ is the grand partition function. It normalizes the probabilities over states with all allowed particle numbers. The grand potential is $\Omega_G=-k_BT\ln\Xi$, and for homogeneous bulk matter in the thermodynamic limit, $\Omega_G=-pV$.

The chemical potential is the thermodynamic variable conjugate to particle number. At fixed temperature and volume, a positive change in $N$ changes the Helmholtz free energy by approximately $\mu\,dN$. Particle exchange between two regions proceeds in the direction that lowers the appropriate total thermodynamic potential, until their chemical potentials agree.

## 6. What the different ensembles hold fixed

| Ensemble | Controlled variables | Quantities that fluctuate | Natural thermodynamic potential |
|---|---|---|---|
| Microcanonical | $E,V,N$ | None of these constraints | Entropy $S$ |
| Canonical | $T,V,N$ | Energy | Helmholtz free energy $F=U-TS$ |
| Grand canonical | $T,V,\mu$ | Energy and particle number | Grand potential $\Omega_G=U-TS-\mu N$ |

These are different probability descriptions of a system under different constraints. They are not three different kinds of physical matter. The appropriate ensemble is chosen to match the constraints and exchanges relevant to the problem.

## 7. Ensemble equivalence—and its limits

For many short-range systems in the thermodynamic limit, the ensembles give the same predictions for bulk thermodynamic observables. The reason is that relative fluctuations of extensive quantities often become small as system size grows. For example, if energy fluctuations scale as $N^{1/2}$ while mean energy scales as $N$, the relative fluctuation scales as $N^{-1/2}$.

Equivalence is not automatic. It can fail or require care for small systems, near critical points, in systems with long-range interactions, in non-additive systems, or when constraints select different macroscopic states. Even when bulk averages agree, fluctuation distributions and finite-size corrections can differ. An ensemble should therefore be selected from the physical constraints, not merely because one calculation is algebraically convenient.

## 8. Summary

- A microstate specifies a microscopic configuration; a macrostate specifies macroscopic constraints.
- An ensemble is a probability distribution over microstates.
- The microcanonical ensemble describes an isolated system with fixed $E,V,N$; equal a priori probabilities are an equilibrium postulate.
- Entropy is related to the logarithm of the number of accessible states, with the state-counting convention stated explicitly.
- A large heat reservoir leads, under a smooth-entropy expansion, to canonical weights $e^{-\beta E}$.
- Allowing particle exchange adds the term $+\beta\mu N$ to the exponent, giving grand-canonical weights $e^{-\beta(E-\mu N)}$.
- Partition functions normalize probabilities; their logarithms generate additive thermodynamic potentials.
- Ensemble equivalence is a thermodynamic-limit result under conditions, not an identity valid for every system.

## Review questions

1. Why is an ensemble a probability distribution rather than a description of a distinct physical system?
2. What is assumed by equal a priori probabilities, and why is it not simply a consequence of counting?
3. Starting from the reservoir multiplicity, derive the canonical Boltzmann weight and identify the approximation used.
4. Repeat the reservoir expansion when particles can be exchanged. Explain the sign of the chemical-potential term.
5. Why does the logarithm of a partition function generate an additive thermodynamic potential?
6. Give two situations in which equivalence of ensembles may fail or require special care.
7. Explain why a time average need not automatically equal an ensemble average.

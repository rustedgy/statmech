# Notation and Symbols

This page collects the notation used across the supplementary statistical-mechanics chapters. Symbols can be reused with different meanings in different models; the definition given in the relevant chapter takes precedence.

## General thermodynamics and probability

| Symbol | Meaning | Notes |
|---|---|---|
| $E$, $U$ | Energy; internal energy | $E$ often labels a microstate or energy level, while $U$ often denotes an average or macroscopic internal energy. |
| $S$ | Entropy | For a uniform set of $\Omega$ accessible states, $S=k_B\ln\Omega$. |
| $T$ | Absolute temperature | Thermodynamic temperature, measured in kelvin. |
| $k_B$ | Boltzmann constant | Converts temperature to an energy scale. |
| $p_i$ | Probability of microstate $i$ | Probabilities obey $\sum_i p_i=1$. |
| $\Omega$ | Multiplicity | Number of accessible microstates in a specified macrostate or energy range. |
| $V$ | Volume | Held fixed in derivatives marked with a subscript $V$. |
| $N$ | Particle or atom number | The meaning depends on the model. |
| $C_V$ | Heat capacity at constant volume | $C_V=(\partial U/\partial T)_V$ when the relevant state variables are specified. |

## Ensembles and partition functions

| Symbol | Meaning | Notes |
|---|---|---|
| $Z$ | Canonical partition function | $Z=\sum_i e^{-\beta E_i}$ for discrete energy levels, including degeneracies if states are summed individually. |
| $\Xi$ | Grand partition function | Commonly $\Xi=\sum_N e^{\beta\mu N}Z_N$. |
| $\beta$ | Inverse thermal energy | $\beta=1/(k_BT)$ for conventional positive-temperature equilibrium. |
| $\mu$ | Chemical potential | Controls particle exchange in the grand canonical ensemble. |
| $F$ | Helmholtz free energy | $F=-k_BT\ln Z$. |
| $G$ | Gibbs free energy | Commonly $G=U+PV-TS$ for a simple compressible system. |
| $\Phi_G$ or $\Omega_G$ | Grand potential | Often $-k_BT\ln\Xi$; the symbol $\Omega$ is also used for multiplicity elsewhere. |
| $\langle A\rangle$ | Expectation value of observable $A$ | The average is taken over the distribution or ensemble under discussion. |

## Quantum statistics and radiation

| Symbol | Meaning | Notes |
|---|---|---|
| $\epsilon_i$ | Energy of single-particle state $i$ | Sometimes written $E_i$. |
| $g_i$ | Degeneracy or number of states in level $i$ | Some chapters instead use $g(\epsilon)$ for a density of states. |
| $\bar n_i$ | Mean occupation of state or level $i$ | Depends on the ensemble and particle statistics. |
| $\hbar$ | Reduced Planck constant | $\hbar=h/(2\pi)$. |
| $\omega$ | Angular frequency | Related to energy by $\hbar\omega$. |
| $\nu$ | Ordinary frequency | Related to angular frequency by $\omega=2\pi\nu$. |
| $c$ | Speed of light in vacuum | Used in blackbody-radiation formulas. |

## Solids and magnetism

| Symbol | Meaning | Notes |
|---|---|---|
| $\omega_D$ | Debye cutoff angular frequency | Chosen to count $3N$ vibrational modes in the three-dimensional Debye model. |
| $\Theta_D$ | Debye temperature | $\Theta_D=\hbar\omega_D/k_B$. |
| $\omega_E$ | Einstein oscillator angular frequency | A single characteristic frequency in the Einstein model. |
| $J$ | Ising nearest-neighbour coupling | The sign convention and whether $J$ is positive for ferromagnetic coupling should be stated in each model. |
| $m$ or $M$ | Magnetization or mean spin | The normalization (per spin, per unit volume, or total) is model-dependent. |
| $\mu_B$ | Bohr magneton | Magnetic-moment scale for electronic spins. |
| $B$ | Magnetic flux density | Often the external magnetic field in Zeeman energies. |

## Derivative and sign conventions

- A subscript on a derivative, such as $(\partial S/\partial E)_{V,N}$, identifies the variables held fixed.
- In the canonical ensemble, $\beta=1/(k_BT)$ is positive for ordinary positive-temperature systems. Negative-temperature discussions require a system with an appropriate bounded energy spectrum and population inversion; they are not described by simply making an ordinary thermal bath colder than absolute zero.
- For grand-canonical formulas, the fugacity is often $z=e^{\beta\mu}$, and the exponent is conventionally $-\beta(E_i-\mu N_i)$.
- In harmonic-oscillator models, zero-point energy may be included in the total energy or omitted when only temperature-dependent thermodynamics is being discussed. The choice should be stated and does not change heat capacity when the omitted term is temperature-independent.
- A density of states may be written $g(E)$ or $g(\omega)$; its units and integration variable determine its meaning.

This is a guide to common notation, not a guarantee that every symbol has one global meaning. Check the definitions and assumptions at the start of each chapter.

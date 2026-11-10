# Bose–Einstein Statistics

This chapter derives the Bose–Einstein occupation law by counting many-particle microstates and finding the most probable occupation distribution. The argument uses statistical mechanics—state counting, constraints, and entropy maximization—not a postulated distribution law.

## 1. The statistical question

Consider a system of identical, non-interacting bosons in equilibrium. A single-particle energy level $\epsilon_i$ has degeneracy $g_i$: there are $g_i$ distinct one-particle states with that energy. Let $n_i$ be the total number of bosons occupying this energy level.

Bosons are indistinguishable, and any number of bosons may occupy the same one-particle state. We seek the equilibrium values of the occupations $n_i$, subject to fixed total particle number and energy:

$$
\sum_i n_i=N, \qquad \sum_i n_i\epsilon_i=E.
$$

For a large system, the equilibrium occupation distribution is the overwhelmingly most numerous allowed macrostate. We therefore count how many many-particle microstates correspond to a specified set $\{n_i\}$.

## 2. Count the arrangements for one energy level

For a level with energy $\epsilon_i$, there are $g_i$ distinct one-particle states and $n_i$ identical bosons to distribute among them. The number of ways to distribute the bosons is the number of non-negative integer solutions of

$$
n_{i1}+n_{i2}+\cdots+n_{ig_i}=n_i.
$$

The stars-and-bars counting result gives

$$
W_i=\binom{n_i+g_i-1}{n_i}
=\frac{(n_i+g_i-1)!}{n_i!(g_i-1)!}.
$$

The $-1$ in $g_i-1$ is the key counting feature: multiple bosons may occupy the same state, and exchanging identical bosons does not produce a new arrangement. This stars-and-bars expression is an **exact integer multiplicity** for a finite group of $g_i$ distinct states and $n_i$ identical bosons; no large-system approximation has yet been made.

Assuming independent one-particle states, the number of many-particle microstates compatible with the complete occupation list is the product

$$
W(\{n_i\})=\prod_i W_i
=\prod_i\frac{(n_i+g_i-1)!}{n_i!(g_i-1)!}.
$$

## 3. Convert state counting into entropy

The Boltzmann principle assigns entropy

$$
S=k_B\ln W.
$$

For large occupation numbers, use Stirling's approximation, $\ln m!\approx m\ln m-m$. Treating the occupations as continuous variables for the purpose of locating the overwhelmingly probable macrostate,

$$
\begin{aligned}
\ln W
&\approx \sum_i\big[(n_i+g_i)\ln(n_i+g_i)\\
&\qquad -n_i\ln n_i-g_i\ln g_i\big].
\end{aligned}
$$

This approximation requires the factorial arguments to be large: in particular, $n_i\gg1$ and $g_i-1\gg1$ for the terms shown, with $n_i+g_i-1\gg1$. Replacing $g_i-1$ by $g_i$ additionally requires $g_i\gg1$. These conditions describe a highly degenerate energy group with many particles; they do not hold for a single orbital with $g_i=1$. The entropy is therefore approximately

$$
S\approx k_B\sum_i\big[(n_i+g_i)\ln(n_i+g_i)
-n_i\ln n_i-g_i\ln g_i\big].
$$

At fixed $g_i$, its derivative with respect to $n_i$ is

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\ln\left(\frac{n_i+g_i}{n_i}\right)
=\ln\left(1+\frac{g_i}{n_i}\right).
$$

## 4. Maximize entropy subject to fixed $N$ and $E$

The equilibrium macrostate maximizes entropy while satisfying the two constraints. Introduce Lagrange multipliers $\alpha$ and $\beta$ and make stationary

$$
\Phi=S-k_B\alpha\sum_i n_i-k_B\beta\sum_i n_i\epsilon_i.
$$

Differentiating with respect to each $n_i$ gives

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\alpha+\beta\epsilon_i.
$$

Insert the entropy derivative obtained above:

$$
\ln\left(1+\frac{g_i}{n_i}\right)
=\alpha+\beta\epsilon_i.
$$

Exponentiating and solving for $n_i$,

$$
1+\frac{g_i}{n_i}=e^{\alpha+\beta\epsilon_i},
$$

so

$$
n_i=\frac{g_i}{e^{\alpha+\beta\epsilon_i}-1}.
$$

The multipliers are fixed by the total particle number and energy. In thermodynamic equilibrium, $\beta=1/(k_BT)$, and the particle-number multiplier is $\alpha=-\mu/(k_BT)$, where $\mu$ is the chemical potential. Thus the mean occupation of the energy level is

$$
\boxed{n_i=\frac{g_i}{e^{(\epsilon_i-\mu)/(k_BT)}-1}}.
$$

For a single one-particle state (no level degeneracy factor), the mean occupation is

$$
\boxed{\bar n(\epsilon)=\frac{1}{e^{(\epsilon-\mu)/(k_BT)}-1}}.
$$

This is the Bose–Einstein distribution. The minus one in the denominator follows directly from the bosonic state count.

## 5. Exact single-state derivation from the grand partition function

The Stirling derivation above treats $n_i$ as a continuous variable and locates the **most-probable coarse-grained occupation** of a highly degenerate energy group. It is not an exact formula for the mean occupation of a single orbital. For one bosonic state of energy $\epsilon$, every occupation $n=0,1,2,\ldots$ is allowed. Its grand partition function is

$$
\Xi_\epsilon=\sum_{n=0}^{\infty}e^{-n\beta(\epsilon-\mu)}
=\frac{1}{1-e^{-\beta(\epsilon-\mu)}}.
$$

Writing $q=e^{-\beta(\epsilon-\mu)}$, its mean occupation is

$$
\bar n=q\frac{\partial}{\partial q}\ln\Xi_\epsilon
=\frac{q}{1-q}
=\frac{1}{e^{\beta(\epsilon-\mu)}-1}.
$$

This exact single-state route requires only convergence of the geometric series, or $\mu<\epsilon$ for that orbital. It needs neither Stirling's approximation nor large degeneracy and is valid for $g=1$. The resulting quantity is the exact grand-canonical **mean occupation** of that orbital, not the location of a coarse-grained multiplicity maximum. For a group of degenerate orbitals, the exact mean total occupation is the sum of the single-orbital means; it is not obtained by treating the group as one orbital with a degeneracy factor inside the geometric series.

## 6. What the multipliers mean

The multiplier for energy is related to temperature because equilibrium maximizes entropy at fixed energy; in the microcanonical definition, $(\partial S/\partial U)_{V,N}=1/T$. The particle-number constraint introduces a second multiplier, the chemical potential, with

$$
\left(\frac{\partial S}{\partial N}\right)_{E,V}
=-\frac{\mu}{T}.
$$

Together these give the exponent $(\epsilon_i-\mu)/(k_BT)$. The identifications $\beta=1/(k_BT)$ and $(\partial S/\partial N)_{U,V}=-\mu/T$ are derived in the [temperature](temperature_from_statistical_mechanics.md) and [grand canonical ensemble](grand_canonical_ensemble_chemical_potential.md) chapters and used here by reference. The distribution is not assumed in the derivation: it is the occupation profile that maximizes the number of compatible microstates under the macroscopic constraints.

For bosons, every single-orbital geometric series must converge. If $\epsilon_0$ is the lowest one-particle energy, this requires $\mu<\epsilon_0$ for a finite system with finite mean occupation; in the thermodynamic limit the chemical potential can approach $\epsilon_0$ from below, so it is common to state $\mu\leq\epsilon_0$ as the limiting bound. It cannot exceed $\epsilon_0$. When the excited states reach their maximum thermodynamic population at $\mu\to\epsilon_0^{-}$, any additional particles enter the ground state. The ground-state occupation then becomes macroscopic and must be handled separately rather than approximated by a continuum density of excited states. This is the ideal-gas setting for Bose–Einstein condensation.

## 7. Comparing MB, BE, and FD statistics

| Statistics | Allowed occupation of one state | Mean occupation |
|---|---|---|
| Maxwell–Boltzmann (MB) | Classical dilute limit; small occupation per state | $e^{-\beta(\epsilon-\mu)}$ |
| Bose–Einstein (BE) | $n=0,1,2,\ldots$ | $\displaystyle\frac{1}{e^{\beta(\epsilon-\mu)}-1}$ |
| Fermi–Dirac (FD) | $n=0$ or $1$ | $\displaystyle\frac{1}{e^{\beta(\epsilon-\mu)}+1}$ |

The different denominators encode different state-counting rules. Both quantum distributions reduce to MB statistics when occupation per state is much less than one. See [Fermi–Dirac Statistics](fermi_dirac_statistics_derivation.md) for the exclusion-based derivation.

## 8. Physical examples: condensation and photons

Bose–Einstein condensation occurs when a macroscopic number of bosons occupy the lowest-energy state. It is observed in ultracold dilute atomic gases, including trapped rubidium-87. Superfluid helium-4 is another important bosonic system, although interactions in the liquid mean the ideal-gas condensation model is not quantitatively exact for it.

Photons are bosons, but their number is not conserved in thermal equilibrium: radiation can exchange photons with matter. Their equilibrium chemical potential is therefore $\mu=0$, which is why Planck's blackbody spectrum follows from Bose–Einstein occupation with zero chemical potential. See [Blackbody Radiation and Planck's Law](blackbody_radiation_planck_law.md).

## 9. Classical limit

When the typical occupation of each individual state is small, $e^{(\epsilon-\mu)/(k_BT)}\gg1$, the minus one is negligible:

$$
\bar n(\epsilon)\approx e^{-(\epsilon-\mu)/(k_BT)}.
$$

This is the Maxwell–Boltzmann form for the mean occupation per state. The classical limit therefore emerges when quantum occupancy corrections are unimportant, rather than being a separate starting assumption.

## Summary

There are two complementary routes: exact stars-and-bars counting followed by a Stirling/continuous-occupation approximation for large degenerate groups, and an exact grand-partition sum for the mean occupation of one orbital. They agree in their common equilibrium regime, but they answer slightly different statistical questions.\n\nThe derivation follows four steps:

1. Count bosonic arrangements: $W_i=(n_i+g_i-1)!/[n_i!(g_i-1)!]$.
2. Form the entropy $S=k_B\ln W$ and use Stirling's approximation.
3. Maximize entropy while fixing total energy and particle number.
4. Identify the multipliers with temperature and chemical potential.

The result is

$$
\boxed{\bar n_i=\frac{1}{e^{(\epsilon_i-\mu)/(k_BT)}-1}}
$$

per one-particle state, with an additional factor of $g_i$ when reporting the total occupation of a degenerate energy level.

## Review questions

1. Why does bosonic state counting give $\binom{n_i+g_i-1}{n_i}$?
2. Where does the minus one in the Bose–Einstein denominator enter the derivation?
3. Why are both energy and particle number constraints required?
4. What condition leads to the classical Maxwell–Boltzmann limit?
5. Why must the ground state sometimes be treated separately near Bose–Einstein condensation?\n6. Derive the Bose–Einstein mean occupation from the grand partition function of one state without using Stirling's approximation.\n7. How do the MB, BE, and FD occupation rules differ?\n8. Why is the equilibrium chemical potential of photons zero?

---

*This is an original supplementary derivation from statistical-mechanical state counting. It is not a transcript of any particular lecture. The continuum/Stirling treatment assumes a sufficiently large system; finite systems may require exact discrete counting.*

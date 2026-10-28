# Bose–Einstein Statistics

This chapter derives the Bose–Einstein occupation law by counting many-particle microstates and finding the most probable occupation distribution. The argument uses statistical mechanics—state counting, constraints, and entropy maximization—not a postulated distribution law.

## 1. The statistical question

Consider a system of identical, non-interacting bosons in equilibrium. A single-particle energy level \(\epsilon_i\) has degeneracy \(g_i\): there are \(g_i\) distinct one-particle states with that energy. Let \(n_i\) be the total number of bosons occupying this energy level.

Bosons are indistinguishable, and any number of bosons may occupy the same one-particle state. We seek the equilibrium values of the occupations \(n_i\), subject to fixed total particle number and energy:

$$
\sum_i n_i=N, \qquad \sum_i n_i\epsilon_i=E.
$$

For a large system, the equilibrium occupation distribution is the overwhelmingly most numerous allowed macrostate. We therefore count how many many-particle microstates correspond to a specified set \(\{n_i\}\).

## 2. Count the arrangements for one energy level

For a level with energy \(\epsilon_i\), there are \(g_i\) distinct one-particle states and \(n_i\) identical bosons to distribute among them. The number of ways to distribute the bosons is the number of non-negative integer solutions of

$$
n_{i1}+n_{i2}+\cdots+n_{ig_i}=n_i.
$$

The stars-and-bars counting result gives

$$
W_i=\binom{n_i+g_i-1}{n_i}
=\frac{(n_i+g_i-1)!}{n_i!(g_i-1)!}.
$$

The \(-1\) in \(g_i-1\) is the key counting feature: multiple bosons may occupy the same state, and exchanging identical bosons does not produce a new arrangement.

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

For large occupation numbers, use Stirling's approximation, \(\ln m!\approx m\ln m-m\). Treating the occupations as continuous variables for the purpose of locating the overwhelmingly probable macrostate,

$$
\begin{aligned}
\ln W
&\approx \sum_i\big[(n_i+g_i)\ln(n_i+g_i)\\
&\qquad -n_i\ln n_i-g_i\ln g_i\big].
\end{aligned}
$$

Here the replacement of \(g_i-1\) by \(g_i\) is negligible when the degeneracies and relevant factorial arguments are large. The entropy is therefore approximately

$$
S\approx k_B\sum_i\big[(n_i+g_i)\ln(n_i+g_i)
-n_i\ln n_i-g_i\ln g_i\big].
$$

At fixed \(g_i\), its derivative with respect to \(n_i\) is

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\ln\left(\frac{n_i+g_i}{n_i}\right)
=\ln\left(1+\frac{g_i}{n_i}\right).
$$

## 4. Maximize entropy subject to fixed \(N\) and \(E\)

The equilibrium macrostate maximizes entropy while satisfying the two constraints. Introduce Lagrange multipliers \(\alpha\) and \(\beta\) and make stationary

$$
\Phi=S-k_B\alpha\sum_i n_i-k_B\beta\sum_i n_i\epsilon_i.
$$

Differentiating with respect to each \(n_i\) gives

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\alpha+\beta\epsilon_i.
$$

Insert the entropy derivative obtained above:

$$
\ln\left(1+\frac{g_i}{n_i}\right)
=\alpha+\beta\epsilon_i.
$$

Exponentiating and solving for \(n_i\),

$$
1+\frac{g_i}{n_i}=e^{\alpha+\beta\epsilon_i},
$$

so

$$
n_i=\frac{g_i}{e^{\alpha+\beta\epsilon_i}-1}.
$$

The multipliers are fixed by the total particle number and energy. In thermodynamic equilibrium, \(\beta=1/(k_BT)\), and the particle-number multiplier is \(\alpha=-\mu/(k_BT)\), where \(\mu\) is the chemical potential. Thus the mean occupation of the energy level is

$$
\boxed{n_i=\frac{g_i}{e^{(\epsilon_i-\mu)/(k_BT)}-1}}.
$$

For a single one-particle state (no level degeneracy factor), the mean occupation is

$$
\boxed{\bar n(\epsilon)=\frac{1}{e^{(\epsilon-\mu)/(k_BT)}-1}}.
$$

This is the Bose–Einstein distribution. The minus one in the denominator follows directly from the bosonic state count.

## 5. What the multipliers mean

The multiplier for energy is related to temperature because equilibrium maximizes entropy at fixed energy; in the microcanonical definition, \(\partial S/\partial E=1/T\). The particle-number constraint introduces a second multiplier, the chemical potential, with

$$
\left(\frac{\partial S}{\partial N}\right)_{E,V}
=-\frac{\mu}{T}.
$$

Together these give the exponent \((\epsilon_i-\mu)/(k_BT)\). The distribution is not assumed in the derivation: it is the occupation profile that maximizes the number of compatible microstates under the macroscopic constraints.

For bosons, the denominator must remain positive for a finite positive occupation, so in the usual equilibrium setting \(\mu\) cannot exceed the lowest allowed single-particle energy. If the lowest-energy state becomes macroscopically occupied, the continuum approximation for excited states must be supplemented by treating that ground-state population separately; this is the statistical-mechanical setting for Bose–Einstein condensation.

## 6. Classical limit

When the typical occupation of each individual state is small, \(e^{(\epsilon-\mu)/(k_BT)}\gg1\), the minus one is negligible:

$$
\bar n(\epsilon)\approx e^{-(\epsilon-\mu)/(k_BT)}.
$$

This is the Maxwell–Boltzmann form for the mean occupation per state. The classical limit therefore emerges when quantum occupancy corrections are unimportant, rather than being a separate starting assumption.

## Summary

The derivation follows four steps:

1. Count bosonic arrangements: \(W_i=(n_i+g_i-1)!/[n_i!(g_i-1)!]\).
2. Form the entropy \(S=k_B\ln W\) and use Stirling's approximation.
3. Maximize entropy while fixing total energy and particle number.
4. Identify the multipliers with temperature and chemical potential.

The result is

$$
\boxed{\bar n_i=\frac{1}{e^{(\epsilon_i-\mu)/(k_BT)}-1}}
$$

per one-particle state, with an additional factor of \(g_i\) when reporting the total occupation of a degenerate energy level.

## Review questions

1. Why does bosonic state counting give \(\binom{n_i+g_i-1}{n_i}\)?
2. Where does the minus one in the Bose–Einstein denominator enter the derivation?
3. Why are both energy and particle number constraints required?
4. What condition leads to the classical Maxwell–Boltzmann limit?
5. Why must the ground state sometimes be treated separately near Bose–Einstein condensation?

---

*This is an original supplementary derivation from statistical-mechanical state counting. It is not a transcript of any particular lecture. The continuum/Stirling treatment assumes a sufficiently large system; finite systems may require exact discrete counting.*

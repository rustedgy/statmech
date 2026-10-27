# Fermi–Dirac Statistics: A Statistical-Mechanical Derivation

This chapter derives the Fermi–Dirac occupation law by counting allowed many-particle microstates and maximizing entropy under fixed energy and particle number. The exclusion principle enters through the allowed occupancy of one-particle states; the distribution then follows from statistical mechanics.

## 1. States, occupations, and constraints

Consider identical, non-interacting fermions in equilibrium. Let energy level \(\epsilon_i\) have degeneracy \(g_i\), meaning there are \(g_i\) distinct one-particle states at that energy. Let \(n_i\) denote the number of fermions occupying the level.

The Pauli exclusion principle permits at most one fermion in each one-particle state. Therefore,

$$
0\leq n_i\leq g_i.
$$

For fixed total particle number and energy,

$$
\sum_i n_i=N, \qquad \sum_i n_i\epsilon_i=E,
$$

we seek the occupation distribution corresponding to the most numerous allowed macrostate.

## 2. Count the allowed arrangements

For a level with degeneracy \(g_i\), choosing \(n_i\) occupied states from the \(g_i\) available states determines the arrangement. The number of choices is

$$
W_i=\binom{g_i}{n_i}
=\frac{g_i!}{n_i!(g_i-n_i)!}.
$$

Unlike the bosonic count, each one-particle state can be selected at most once. For a complete occupation list, independent state counting gives

$$
W(\{n_i\})=\prod_i\frac{g_i!}{n_i!(g_i-n_i)!}.
$$

This combinatorial factor is where the exclusion constraint enters the calculation.

## 3. Entropy from multiplicity

Using Boltzmann's relation \(S=k_B\ln W\) and Stirling's approximation for large factorial arguments,

$$
\begin{aligned}
\ln W\approx\sum_i\big[&
g_i\ln g_i-n_i\ln n_i\\
&-(g_i-n_i)\ln(g_i-n_i)\big].
\end{aligned}
$$

Thus

$$
S\approx k_B\sum_i\big[g_i\ln g_i-n_i\ln n_i
-(g_i-n_i)\ln(g_i-n_i)\big].
$$

For fixed \(g_i\), differentiating with respect to \(n_i\) gives

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\ln\left(\frac{g_i-n_i}{n_i}\right).
$$

The factor \(g_i-n_i\) counts the unoccupied one-particle states. Its appearance is the statistical signature of exclusion.

## 4. Maximize entropy at fixed energy and particle number

The equilibrium occupation maximizes entropy subject to the two macroscopic constraints. Introduce Lagrange multipliers \(\alpha\) and \(\beta\):

$$
\Phi=S-k_B\alpha\sum_i n_i-k_B\beta\sum_i n_i\epsilon_i.
$$

Stationarity with respect to every \(n_i\) requires

$$
\frac{1}{k_B}\frac{\partial S}{\partial n_i}
=\alpha+\beta\epsilon_i.
$$

Substituting the entropy derivative yields

$$
\ln\left(\frac{g_i-n_i}{n_i}\right)
=\alpha+\beta\epsilon_i.
$$

Exponentiating,

$$
\frac{g_i-n_i}{n_i}=e^{\alpha+\beta\epsilon_i}.
$$

Rearranging,

$$
g_i=n_i\left(1+e^{\alpha+\beta\epsilon_i}\right),
$$

and hence

$$
n_i=\frac{g_i}{e^{\alpha+\beta\epsilon_i}+1}.
$$

At equilibrium, \(\beta=1/(k_BT)\) and \(\alpha=-\mu/(k_BT)\), where \(T\) is temperature and \(\mu\) is chemical potential. Therefore,

$$
\boxed{n_i=\frac{g_i}{e^{(\epsilon_i-\mu)/(k_BT)}+1}}.
$$

The mean occupation of an individual one-particle state is

$$
\boxed{\bar n(\epsilon)=\frac{1}{e^{(\epsilon-\mu)/(k_BT)}+1}}.
$$

This is the Fermi–Dirac distribution. The plus one is a direct consequence of counting only arrangements with no more than one fermion in each one-particle state.

## 5. Interpreting the result

The mean occupation per one-particle state lies between zero and one, as required by exclusion:

$$
0\leq\bar n(\epsilon)\leq1.
$$

At \(\epsilon=\mu\), the occupation is one half. For positive temperature, states far below the chemical potential are likely to be occupied, while states far above it are unlikely to be occupied.

In the zero-temperature limit for a system with a conventional ground-state filling, the distribution approaches a step:

$$
\bar n(\epsilon)\longrightarrow
\begin{cases}
1,&\epsilon<\mu,\\
0,&\epsilon>\mu.
\end{cases}
$$

At zero temperature, \(\mu\) approaches the Fermi energy for the usual ground state. The value exactly at the step depends on how the limiting case is represented and does not change bulk counting.

## 6. Classical limit

When \(e^{(\epsilon-\mu)/(k_BT)}\gg1\), the plus one is negligible, giving

$$
\bar n(\epsilon)\approx e^{-(\epsilon-\mu)/(k_BT)}.
$$

This is the Maxwell–Boltzmann limit. It applies when the occupation per one-particle state is small, so the distinction caused by exclusion is negligible for the distribution.

## 7. Comparison with Bose–Einstein counting

The derivations for bosons and fermions have the same statistical structure:

- Count microstates compatible with a proposed set of level occupations.
- Take \(S=k_B\ln W\).
- Maximize entropy while enforcing fixed total energy and particle number.
- Interpret the Lagrange multipliers as inverse temperature and chemical potential.

The difference lies in the allowed occupancy and therefore the combinatorics:

$$
\begin{array}{ll}
\text{Bosons:}&W_i=\dfrac{(n_i+g_i-1)!}{n_i!(g_i-1)!},\\[6pt]
\text{Fermions:}&W_i=\dfrac{g_i!}{n_i!(g_i-n_i)!}.
\end{array}
$$

The resulting distributions differ only by the sign in the denominator:

$$
\bar n_{\mathrm{BE}}(\epsilon)
=\frac{1}{e^{(\epsilon-\mu)/(k_BT)}-1},
\qquad
\bar n_{\mathrm{FD}}(\epsilon)
=\frac{1}{e^{(\epsilon-\mu)/(k_BT)}+1}.
$$

These signs are not arbitrary algebraic choices. They encode the different ways identical bosons and fermions may populate one-particle states.

## Summary

Fermi–Dirac statistics follows from the finite occupancy of fermionic one-particle states. For a level with degeneracy \(g_i\), there are \(\binom{g_i}{n_i}\) ways to choose its occupied states. Maximizing the entropy derived from this multiplicity, subject to fixed energy and particle number, gives

$$
\boxed{\bar n_i=\frac{1}{e^{(\epsilon_i-\mu)/(k_BT)}+1}}
$$

per one-particle state. The result is statistical-mechanical: it follows from allowed microstates and equilibrium constraints.

## Review questions

1. How does the Pauli exclusion principle change the multiplicity for a level?
2. Why does the entropy derivative contain \(g_i-n_i\)?
3. Derive the Fermi–Dirac denominator by maximizing entropy with two constraints.
4. Why is the occupation one half at \(\epsilon=\mu\)?
5. Under what conditions does the Fermi–Dirac distribution reduce to the Maxwell–Boltzmann form?

---

*This is an original supplementary derivation from statistical-mechanical state counting. It is not a transcript of any particular lecture. The Stirling approximation is appropriate for large occupation groups; exact finite systems require discrete counting.*

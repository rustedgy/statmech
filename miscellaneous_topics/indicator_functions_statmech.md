# Indicator Functions in Statistical Mechanics

Indicator functions are a compact way to express whether a condition is satisfied. They turn logical statements about a microstate into ordinary numerical quantities, making constraints, particle counts, probabilities, and averages easier to write.

## 1. Definition

For a statement or event (A), define its indicator by

$$
\mathbf{1}_A(x)=
\begin{cases}
1,&\text{if the state }x\text{ satisfies }A,\\
0,&\text{otherwise.}
\end{cases}
$$

The indicator is a function of the state. It is not itself a probability: for a particular state it is either zero or one. Its ensemble average, however, is a probability:

$$
\langle \mathbf{1}_A\rangle
=\sum_x p(x)\mathbf{1}_A(x)
=\Pr(A).
$$

For a continuous state space, replace the sum with an integral over the probability density.

## 2. Counting states and particles

Suppose a system has microstate (x), and (n_i(x)) is the number of particles occupying single-particle state (i). The occupancy can be written as a sum of indicators over particles:

$$
n_i(x)=\sum_{j=1}^{N}\mathbf{1}\{\text{particle }j\text{ occupies }i\}.
$$

Averaging gives the mean occupation number:

$$
\langle n_i\rangle
=\sum_{j=1}^{N}\Pr(\text{particle }j\text{ occupies }i).
$$

For indistinguishable particles, one usually works directly with the occupation numbers (n_i), but the indicator representation makes the counting interpretation explicit.

Indicators also count how many objects satisfy a condition. If (I_j=\mathbf{1}\{\text{object }j\text{ has property }A\}), then

$$
N_A=\sum_{j=1}^{N} I_j
$$

is the number with property (A), and (\langle N_A\rangle=\sum_j\Pr(A_j)). Independence is not needed for this expectation identity.

## 3. Constraints in sums over microstates

Let (x) label possible microstates with energy (E(x)). An unrestricted canonical partition function is

$$
Z(\beta)=\sum_x e^{-\beta E(x)},\qquad
\beta=\frac{1}{k_BT}.
$$

To restrict the sum to states satisfying a condition (A), insert its indicator:

$$
Z_A(\beta)=\sum_x \mathbf{1}_A(x)e^{-\beta E(x)}.
$$

For example, if (A) means that a specified region contains exactly (m) particles, the indicator removes every microstate that fails that condition. If the indicator selects a subset of states, then (Z_A/Z) is the canonical probability of that subset:

$$
\Pr(A)=\frac{Z_A}{Z}.
$$

This is useful for restricted partition functions, probabilities of macrostates, and counting configurations that satisfy boundary or occupancy constraints.

## 4. Example: a two-state paramagnet

Consider (N) independent spins with (s_j\in\{-1,+1\}), magnetic moment magnitude \(\mu\), and energy

$$
E(\{s_j\})=-\mu B\sum_{j=1}^{N}s_j.
$$

The indicator for spin (j) being up is

$$
I_j^{\uparrow}=\mathbf{1}\{s_j=+1\}
=\frac{1+s_j}{2}.
$$

Thus the number of up spins is

$$
N_{\uparrow}=\sum_{j=1}^{N}\frac{1+s_j}{2},
$$

and the number of down spins is (N_{\downarrow}=N-N_{\uparrow}). Since (s_j=2I_j^{\uparrow}-1), magnetization and occupation counts are directly related. In a canonical ensemble,

$$
\langle I_j^{\uparrow}\rangle
=\Pr(s_j=+1)
=\frac{e^{\beta\mu B}}{e^{\beta\mu B}+e^{-\beta\mu B}}
=\frac{1}{1+e^{-2\beta\mu B}}.
$$

The expected number of up spins is (\langle N_{\uparrow}\rangle=N\langle I_j^{\uparrow}\rangle) for identical independent spins.

## 5. Kronecker deltas and discrete indicators

For discrete labels, the Kronecker delta

$$
\delta_{ij}=\begin{cases}1,&i=j,\\0,&i\ne j\end{cases}
$$

is an indicator of equality: (\delta_{ij}=\mathbf{1}\{i=j\}). It can select a term from a sum, for example,

$$
\sum_i a_i\delta_{ij}=a_j.
$$

This should not be confused with the Dirac delta distribution used under integrals over continuous variables. The Dirac delta is a distribution with a different mathematical role; it is not an ordinary zero-or-one function.

## 6. Useful identities

For any events (A) and (B),

$$
\mathbf{1}_{A\cap B}=\mathbf{1}_A\mathbf{1}_B,
\qquad
\mathbf{1}_{A\cup B}=\mathbf{1}_A+\mathbf{1}_B-\mathbf{1}_A\mathbf{1}_B.
$$

The complement satisfies (\mathbf{1}_{A^c}=1-\mathbf{1}_A). Therefore,

$$
\Pr(A\cap B)=\langle\mathbf{1}_A\mathbf{1}_B\rangle.
$$

This last expression also makes correlations transparent: in general, (\langle\mathbf{1}_A\mathbf{1}_B\rangle\) need not equal (\langle\mathbf{1}_A\rangle\langle\mathbf{1}_B\rangle\). Equality holds when the events are independent.

## 7. When indicators are useful—and when they are not

Indicators are especially useful when a calculation involves counting, restricting a sum, defining an event, or converting a logical condition into algebra. They also appear in Monte Carlo estimators: the fraction of sampled configurations satisfying (A) estimates \(\Pr(A)\).

They do not, by themselves, make a sum easier to evaluate, and they do not imply that events are independent. The benefit is clarity: the condition being counted is explicit and can be manipulated algebraically.

## Summary

An indicator is one for states satisfying a condition and zero otherwise. Its average is the probability of that condition; sums of indicators count objects or select allowed microstates. This simple device links microscopic configurations, ensemble averages, and probabilities in a common notation.

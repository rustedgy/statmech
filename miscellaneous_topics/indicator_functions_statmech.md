# Indicator Functions in Statistical Mechanics

Indicator functions express whether a condition is satisfied. They turn logical statements about a microstate into numerical quantities, making constraints, particle counts, probabilities, and averages easier to write.

## 1. Definition

For an event or condition $A$, define its indicator by

$$
\mathbf{1}_A(x)=
\begin{cases}
1,&\text{if state }x\text{ satisfies }A,\\
0,&\text{otherwise.}
\end{cases}
$$

For a particular state, the indicator is either zero or one. Its ensemble average is a probability:

$$
\langle \mathbf{1}_A\rangle
=\sum_x p(x)\mathbf{1}_A(x)
=\Pr(A).
$$

For a continuous state space, replace the sum with an integral over the probability density.

## 2. Counting states and particles

Suppose $x$ labels a microstate and $n_i(x)$ is the number of particles occupying single-particle state $i$. The occupancy can be written as a sum of indicators over particles:

$$
n_i(x)=\sum_{j=1}^{N}\mathbf{1}\{\text{particle }j\text{ occupies }i\}.
$$

Averaging gives the mean occupation number:

$$
\langle n_i\rangle
=\sum_{j=1}^{N}\Pr(\text{particle }j\text{ occupies }i).
$$

For indistinguishable particles, one usually works directly with occupation numbers $n_i$, but the indicator representation makes the counting interpretation explicit.

More generally, if $I_j=\mathbf{1}\{\text{object }j\text{ has property }A\}$, then

$$
N_A=\sum_{j=1}^{N} I_j
$$

counts the objects with property $A$. Its expectation is $\langle N_A\rangle=\sum_j\Pr(A_j)$. Independence is not needed for this expectation identity.

## 3. Constraints in sums over microstates

Let $x$ label possible microstates with energy $E(x)$. The canonical partition function is

$$
Z(\beta)=\sum_x e^{-\beta E(x)},\qquad
\beta=\frac{1}{k_BT}.
$$

To restrict the sum to states satisfying condition $A$, insert its indicator:

$$
Z_A(\beta)=\sum_x \mathbf{1}_A(x)e^{-\beta E(x)}.
$$

For example, if $A$ means that a specified region contains exactly $m$ particles, the indicator removes every microstate that fails the condition. If it selects a subset of states, then

$$
\Pr(A)=\frac{Z_A}{Z}.
$$

This is useful for restricted partition functions, probabilities of macrostates, and counting configurations satisfying boundary or occupancy constraints.

## 4. Example: a two-state paramagnet

Consider $N$ independent spins $s_j\in\{-1,+1\}$, with magnetic moment magnitude $\mu$ and energy

$$
E(\{s_j\})=-\mu B\sum_{j=1}^{N}s_j.
$$

The indicator for spin $j$ being up is

$$
I_j^{\uparrow}=\mathbf{1}\{s_j=+1\}
=\frac{1+s_j}{2}.
$$

Thus the number of up spins is

$$
N_{\uparrow}=\sum_{j=1}^{N}\frac{1+s_j}{2},
$$

and $N_{\downarrow}=N-N_{\uparrow}$. Since $s_j=2I_j^{\uparrow}-1$, magnetization and occupation counts are directly related. In a canonical ensemble,

$$
\langle I_j^{\uparrow}\rangle
=\Pr(s_j=+1)
=\frac{e^{\beta\mu B}}{e^{\beta\mu B}+e^{-\beta\mu B}}
=\frac{1}{1+e^{-2\beta\mu B}}.
$$

For identical independent spins, the expected number of up spins is $\langle N_{\uparrow}\rangle=N\langle I_j^{\uparrow}\rangle$.

## 5. Kronecker deltas and discrete indicators

For discrete labels, the Kronecker delta is an indicator of equality:

$$
\delta_{ij}=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}
$$

It can select a term from a sum, for example,

$$
\sum_i a_i\delta_{ij}=a_j.
$$

This should not be confused with the Dirac delta distribution used under integrals over continuous variables. The Dirac delta has a different mathematical role; it is not an ordinary zero-or-one function.

## 6. Useful identities

For events $A$ and $B$,

$$
\mathbf{1}_{A\cap B}=\mathbf{1}_A\mathbf{1}_B,
\qquad
\mathbf{1}_{A\cup B}=\mathbf{1}_A+\mathbf{1}_B-\mathbf{1}_A\mathbf{1}_B.
$$

The complement satisfies $\mathbf{1}_{A^c}=1-\mathbf{1}_A$. Therefore,

$$
\Pr(A\cap B)=\langle\mathbf{1}_A\mathbf{1}_B\rangle.
$$

In general, $\langle\mathbf{1}_A\mathbf{1}_B\rangle$ need not equal $\langle\mathbf{1}_A\rangle\langle\mathbf{1}_B\rangle$. Equality holds when the events are independent.

## 7. When indicators are useful

Indicators are useful when a calculation involves counting, restricting a sum, defining an event, or converting a logical condition into algebra. They also appear in Monte Carlo estimators: the fraction of sampled configurations satisfying $A$ estimates $\Pr(A)$.

Indicators do not, by themselves, make a sum easier to evaluate, and they do not imply independence. Their main benefit is clarity: the condition being counted is explicit and can be manipulated algebraically.

## Summary

An indicator is one for states satisfying a condition and zero otherwise. Its average is the probability of that condition; sums of indicators count objects or select allowed microstates. This simple device links microscopic configurations, ensemble averages, and probabilities in a common notation.

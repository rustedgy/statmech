# A Counting Framework for Finite Systems

## Purpose and scope

This chapter develops a counting argument from definitions and assumptions alone. It begins with a finite collection of individually identifiable particles. Each particle carries one attribute, whose value is selected from a finite set. The central question is:

**Among all assignments whose total attribute value is equal to, or sufficiently close to, a prescribed target, which occupation-number pattern is compatible with the largest number of assignments?**

The argument uses finite sets, integer occupation numbers, constraints, and direct counting. It does not require a continuous approximation or any thermodynamic interpretation.

A practical point motivates the use of a tolerance. The allowed values of an attribute may be closely spaced without having equal gaps. A finite collection of such values cannot, in general, produce every possible total exactly. If the prescribed total is specified only to a finite resolution, it is natural to group together assignments whose totals lie within that resolution. The tolerance formulation makes this explicit while keeping the entire counting problem discrete.

## 1. Basic objects

### Definition 1: The system

The system contains a fixed finite number $N$ of individually identifiable particles,

$$
P=\{1,2,\ldots,N\}.
$$

The labels distinguish the particles. Assigning a value to particle 1 and assigning the same value to particle 2 are different assignments.

### Definition 2: The attribute and its allowed values

Each particle carries one attribute, denoted by $U$. Its allowed values form a finite set

$$
S_U=\{U_1,U_2,\ldots,U_M\},
$$

where the values are distinct. The values need not be equally spaced and need not be integers. Different particles may carry the same value.

For some applications, the allowed values may be closely spaced over the range of interest. This can make a prescribed total attainable to a chosen accuracy, but closeness of the individual values by itself does not guarantee that every total is attainable. Attainability also depends on $N$, on the actual values in $S_U$, and on the chosen tolerance.

### Definition 3: An assignment

An assignment specifies the value of $U$ for every particle. It is an ordered list

$$
\boldsymbol u=(u_1,u_2,\ldots,u_N),
\qquad u_i\in S_U.
$$

The order matters because the particles are individually identifiable.

## 2. Axioms and assumptions

The counting problem is defined by the following statements.

**Axiom 1 — Fixed number of particles.** The number of particles is the fixed integer $N$.

**Axiom 2 — One allowed value per particle.** Every particle carries exactly one value of $U$, chosen from $S_U$.

**Axiom 3 — Repeated values are permitted.** There is no restriction on how many particles may carry the same allowed value.

**Axiom 4 — A prescribed total, to a specified resolution.** A target value $U_*$ and a non-negative tolerance $\epsilon$ are specified. An assignment is admitted when

$$
\left|\sum_{i=1}^{N}u_i-U_*\right|\leq\epsilon.
$$

The tolerance has the same units as $U$. It represents the resolution with which the total is being specified. The exact-total problem is recovered by setting $\epsilon=0$.

**Axiom 5 — No additional restrictions or weights.** Apart from Axioms 1–4, every assignment is admissible, and all admissible assignments are counted with equal weight.

**Counting convention.** Two assignments are different if at least one labelled particle carries a different value in them.

These statements define the model. Changing the tolerance, introducing restrictions, or assigning different weights to assignments changes the counting problem.

## 3. Microstates and macrostates

### Definition 4: Microstate

A **microstate** is one complete assignment of an allowed value of $U$ to each of the $N$ particles.

For three particles and $S_U=\{0,1,2\}$, for example,

$$
(0,1,2),\qquad (1,0,2),\qquad (2,0,1)
$$

are three different microstates. They contain the same values but assign them to different labelled particles.

### Definition 5: Macrostate

A **macrostate** is a set of microstates selected by specified conditions. The macrostate considered here contains all assignments whose total lies within the prescribed tolerance:

$$
\mathcal M(U_*,\epsilon)
=
\left\{
\boldsymbol u\in S_U^N:
\left|\sum_{i=1}^{N}u_i-U_*\right|\leq\epsilon
\right\}.
$$

The macrostate may be empty. It is non-empty if and only if at least one sum of $N$ allowed values lies in the interval

$$
[U_*-\epsilon,\,U_*+\epsilon].
$$

When $\epsilon=0$, the condition requires the total to equal $U_*$ exactly. For a finite allowed set, exact attainability is a genuine arithmetic constraint; an arbitrary real target need not be attainable.

## 4. Distributions: grouping assignments by occupation numbers

### Definition 6: Occupation numbers

For a microstate, let $n_j$ be the number of particles carrying the value $U_j$:

$$
n_j=\#\{i:u_i=U_j\},
\qquad j=1,2,\ldots,M.
$$

Each $n_j$ is a non-negative integer. Since every particle carries exactly one allowed value,

$$
\boxed{\sum_{j=1}^{M}n_j=N.}
$$

The total carried by an assignment with these occupation numbers is

$$
U(\boldsymbol n)=\sum_{j=1}^{M}n_jU_j.
$$

The tolerance condition becomes

$$
\boxed{
\left|\sum_{j=1}^{M}n_jU_j-U_*\right|\leq\epsilon.
}
$$

### Definition 7: Distribution

A **distribution** is the subset of a macrostate consisting of all microstates with exactly the same occupation-number list

$$
\boldsymbol n=(n_1,n_2,\ldots,n_M).
$$

Thus, two microstates belong to the same distribution if and only if each allowed value occurs the same number of times in both.

The allowed distributions are precisely the integer lists satisfying

$$
n_j\geq0,\qquad
\sum_jn_j=N,\qquad
\left|\sum_jn_jU_j-U_*\right|\leq\epsilon.
$$

Every microstate in the macrostate belongs to exactly one distribution. Different distributions are disjoint, and together they make up the macrostate.

## 5. Counting the microstates in one distribution

Fix an allowed occupation-number list $(n_1,\ldots,n_M)$. To construct an assignment with these occupation numbers, choose which $n_1$ labelled particles carry $U_1$, then which $n_2$ of the remaining particles carry $U_2$, and continue.

The number of assignments is

$$
\binom{N}{n_1}
\binom{N-n_1}{n_2}
\binom{N-n_1-n_2}{n_3}\cdots.
$$

Cancelling factorials gives

$$
\boxed{
W(\boldsymbol n)=\frac{N!}{n_1!n_2!\cdots n_M!}.
}
$$

Here $W(\boldsymbol n)$ is the number of microstates in the distribution $\boldsymbol n$. The expression counts assignments to labelled particles. It does not count permutations of the occupation-number list as new distributions: each $n_j$ is attached to its particular allowed value $U_j$.

The total number of microstates in the macrostate is the sum over all allowed integer lists:

$$
|\mathcal M(U_*,\epsilon)|
=
\sum_{\substack{n_1+\cdots+n_M=N\\
|n_1U_1+\cdots+n_MU_M-U_*|\leq\epsilon}}
\frac{N!}{n_1!\cdots n_M!}.
$$

This is a finite sum. There are only finitely many non-negative integer lists whose entries add to $N$.

## 6. The distribution with the largest number of microstates

The most numerous distribution is found by solving the finite integer problem

$$
\boxed{
\text{Maximize}\quad
W(\boldsymbol n)=\frac{N!}{\prod_{j=1}^{M}n_j!}
}
$$

subject to

$$
n_j\in\{0,1,2,\ldots\},\qquad
\sum_jn_j=N,\qquad
\left|\sum_jn_jU_j-U_*\right|\leq\epsilon.
$$

No replacement of the integers by continuous variables is made. One can, in principle, list all occupation-number lists satisfying the constraints, evaluate their multinomial counts, and select the largest. For large values of $N$ or $M$, more efficient discrete search methods may be useful, but the mathematical problem remains the same.

There may be more than one maximizing distribution. This happens, for example, when distinct occupation-number lists have the same multinomial count. A tie is not a defect in the definition; it means that the counting assumptions do not single out one unique list.

If the tolerance is so small that no allowed occupation list satisfies the constraint, the macrostate is empty and there is no maximizing distribution. If the tolerance is increased, more occupation lists may become admissible, and the maximizing list can change. Thus, the tolerance is part of the specification of the problem, not a parameter that can be chosen after the maximization.

### 6.1 Worked example with unequal gaps

Take four labelled particles and the allowed values

$$
S_U=\{0,\,0.9,\,2.1,\,3.0\}.
$$

The gaps are unequal: they are $0.9$, $1.2$, and $0.9$. Choose target total $U_*=4.0$ and tolerance $\epsilon=0.2$. We seek non-negative integers $(n_0,n_{0.9},n_{2.1},n_3)$ such that

$$
n_0+n_{0.9}+n_{2.1}+n_3=4
$$

and

$$
\left|0.9n_{0.9}+2.1n_{2.1}+3n_3-4.0\right|\leq0.2.
$$

The allowed occupation lists are

| Occupation list $(n_0,n_{0.9},n_{2.1},n_3)$ | Total | Number of assignments |
|---|---:|---:|
| $(1,2,1,0)$ | $3.9$ | $4!/(1!2!1!0!)=12$ |
| $(2,1,0,1)$ | $3.9$ | $4!/(2!1!0!1!)=12$ |
| $(2,0,2,0)$ | $4.2$ | $4!/(2!0!2!0!)=6$ |

These are all the occupation lists satisfying the two constraints. The largest count is 12, attained by the first two lists. There are therefore two most numerous distributions.

This example illustrates three points. First, equal spacing of the allowed values is not required. Second, a tolerance can admit totals on either side of the target. Third, the most numerous distribution is obtained by comparing the integer multinomial counts; it need not be unique.

## 7. Choosing and interpreting the tolerance

The tolerance should express the accuracy with which the total is specified. It must be large enough that at least one attainable total is included, but small enough that assignments with totals regarded as meaningfully different are not grouped together.

For fixed $N$ and $S_U$, the set of attainable totals is finite:

$$
\mathcal A_N=
\left\{
\sum_{j=1}^{M}n_jU_j:
n_j\in\{0,1,2,\ldots\},\;
\sum_jn_j=N
\right\}.
$$

The macrostate is non-empty precisely when

$$
\mathcal A_N\cap[U_*-\epsilon,U_*+\epsilon]\neq\varnothing.
$$

This gives a direct way to check whether a proposed target and tolerance are compatible with the allowed values.

If the allowed single-particle values are closely spaced across a range, sums formed from them may provide a fine set of attainable totals. Unequal gaps do not invalidate the construction. What matters for a particular problem, however, is the spacing of the attainable $N$-particle totals near the target, not just the spacing of neighbouring single-particle values. There is no general guarantee that a finite set of allowed values will reproduce every target exactly, or to an arbitrarily chosen tolerance.

The exact-total formulation is a special case. Setting $\epsilon=0$ restricts the allowed lists to those satisfying

$$
\sum_jn_jU_j=U_*.
$$

If this equation has no non-negative integer solution with $\sum_jn_j=N$, the exact macrostate is empty. A positive tolerance can make the macrostate non-empty without changing any of the definitions of microstate, occupation number, distribution, or multinomial counting.

## 8. More than one attribute

The same construction applies when each particle carries several attributes. Suppose a particle's allowed value is a tuple

$$
\boldsymbol U_j=
\left(U_j^{(1)},U_j^{(2)},\ldots,U_j^{(K)}\right),
$$

chosen from a finite set of distinct allowed tuples. Let the target totals be $U_*^{(a)}$, with non-negative tolerances $\epsilon_a$ for $a=1,\ldots,K$.

The occupation numbers still satisfy

$$
n_j\in\{0,1,2,\ldots\},
\qquad \sum_jn_j=N.
$$

The remaining constraints are

$$
\boxed{
\left|\sum_jn_jU_j^{(a)}-U_*^{(a)}\right|
\leq\epsilon_a,
\qquad a=1,\ldots,K.
}
$$

The number of assignments for a given allowed occupation list remains

$$
W(\boldsymbol n)=\frac{N!}{\prod_jn_j!},
$$

because it depends only on how many labelled particles carry each allowed tuple. The most numerous distribution is again the integer occupation list that maximizes this expression subject to all the stated constraints.

As in the one-attribute case, the macrostate may be empty if no integer occupation list satisfies all the tolerance conditions. Each additional attribute adds a constraint; it does not change the basic counting argument.

## Summary of the logical chain

1. A microstate is a complete assignment of allowed attribute values to the $N$ labelled particles.
2. A macrostate is the set of assignments whose total attribute value lies within a specified tolerance of a target. Exact equality is recovered when the tolerance is zero.
3. A distribution is the subset of a macrostate with a fixed list of integer occupation numbers.
4. The number of microstates in a distribution is the multinomial count $N!/\prod_jn_j!$.
5. The most numerous distribution is found by maximizing this count over the allowed integer occupation lists.
6. Unequal spacing of the allowed values causes no difficulty. Whether a target is attainable to a given accuracy depends on the attainable sums for the specified $N$ and allowed set.
7. With several attributes, one adds a tolerance constraint for each total; the multinomial counting formula is unchanged.

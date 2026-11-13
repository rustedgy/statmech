# A Counting Framework for Finite Systems

## Purpose and scope

This chapter builds a counting argument from a small set of definitions and assumptions. It begins with individually identifiable particles, each of which carries one attribute whose value is chosen from a specified set. It then asks:

**Among all assignments compatible with a fixed total value of the attribute, which pattern of particle counts is compatible with the largest number of microstates?**

The argument below uses only assignments, sets, constraints, and counting. It does not rely on any additional physical interpretation.

## 1. Basic objects

### Definition 1: The system

A system contains a fixed finite number $N$ of individually identifiable particles,

$$
P=\{1,2,\ldots,N\}.
$$

The labels identify the particles. Thus, assigning a value to particle 1 and assigning the same value to particle 2 are different assignments, even if all the assigned values are otherwise identical.

### Definition 2: The attribute and its allowed values

Each particle carries one attribute, denoted by $U$. The allowed values of this attribute form a finite set

$$
S_U=\{U_1,U_2,\ldots,U_M\},
$$

where the values are distinct. For now, $M$ is finite. The values need not be equally spaced, and they need not be integers.

Every particle must carry exactly one value from $S_U$. Different particles may carry the same value.

### Definition 3: An assignment

An assignment specifies the value of $U$ for every particle. It can be written as an ordered list

$$
\boldsymbol{u}=(u_1,u_2,\ldots,u_N),
\qquad u_i\in S_U.
$$

The order matters because the particles are individually identifiable.

## 2. Axioms and assumptions

The counting argument rests on the following statements.

**Axiom 1 — Fixed number of particles.** The number of particles is $N$ and does not change.

**Axiom 2 — One allowed value per particle.** Every particle has exactly one value of $U$, chosen from $S_U$.

**Axiom 3 — Repeated values are allowed.** There is no restriction on how many particles may carry the same value $U_j$.

**Axiom 4 — Fixed total attribute value.** The sum of the values carried by all particles is conserved:

$$
U_{\mathrm{tot}}=\sum_{i=1}^{N}u_i.
$$

**Axiom 5 — No additional restrictions.** Apart from Axioms 1–4, every assignment is admissible. In particular, the allowed assignments are not given different weights.

**Counting convention.** Two assignments are counted as different if at least one labelled particle carries a different value in the two assignments.

Axioms 1–5 define the model considered in this chapter. Additional restrictions can be introduced later, but they would define a different counting problem.

## 3. Microstates and macrostates

### Definition 4: Microstate

A **microstate** is one complete assignment of an allowed value of $U$ to each of the $N$ particles.

For example, for three particles and allowed values $S_U=\{0,1,2\}$, the assignments

$$
(0,1,2),\qquad (1,0,2),\qquad (2,0,1)
$$

are three different microstates. Each assigns the same collection of values, but to different labelled particles.

### Definition 5: Macrostate

A **macrostate** is a set of microstates selected by one or more specified constraints.

The macrostate of interest here is the set of all microstates with the same fixed total value $U_{\mathrm{tot}}$:

$$
\mathcal M(U_{\mathrm{tot}})
=
\left\{
\boldsymbol{u}\in S_U^N:
\sum_{i=1}^{N}u_i=U_{\mathrm{tot}}
\right\}.
$$

Thus, every microstate in this macrostate has the same total attribute value, although the individual particles need not carry the same values.

The macrostate exists only if the chosen $U_{\mathrm{tot}}$ can be obtained from $N$ values drawn from $S_U$.

## 4. Distributions: grouping microstates by particle counts

### Definition 6: Occupation numbers

For a given microstate, define $n_j$ to be the number of particles carrying the value $U_j$:

$$
n_j=\#\{i:u_i=U_j\},
\qquad j=1,2,\ldots,M.
$$

The numbers $n_1,\ldots,n_M$ are non-negative integers. Since every particle carries exactly one allowed value,

$$
\boxed{\sum_{j=1}^{M}n_j=N.}
$$

The total attribute value can be written in terms of these numbers:

$$
\boxed{\sum_{j=1}^{M}n_jU_j=U_{\mathrm{tot}}.}
$$

### Definition 7: Distribution

A **distribution** is the subset of a macrostate consisting of all microstates that have exactly the same occupation numbers $(n_1,n_2,\ldots,n_M)$.

In other words, two microstates belong to the same distribution if and only if, for every allowed value $U_j$, the number of particles carrying $U_j$ is the same in both microstates.

A distribution is therefore specified by its occupation-number list,

$$
\boldsymbol n=(n_1,n_2,\ldots,n_M),
$$

subject to

$$
n_j\in\{0,1,2,\ldots\},\qquad
\sum_j n_j=N,\qquad
\sum_j n_jU_j=U_{\mathrm{tot}}.
$$

Different distributions have different occupation-number lists. Every microstate in the macrostate belongs to exactly one distribution. Consequently, the macrostate is divided into disjoint distributions.

## 5. How many microstates belong to a distribution?

Fix an allowed occupation-number list $(n_1,\ldots,n_M)$. We now count the assignments that realize it.

There are $N$ labelled particles. Choose which $n_1$ particles carry $U_1$, then which $n_2$ of the remaining particles carry $U_2$, and continue in this way. The number of choices is

$$
\binom{N}{n_1}
\binom{N-n_1}{n_2}
\binom{N-n_1-n_2}{n_3}\cdots.
$$

After cancellation of the factorials, this becomes

$$
\boxed{
W(\boldsymbol n)
=
\frac{N!}{n_1!n_2!\cdots n_M!}.
}
$$

Here $W(\boldsymbol n)$ denotes the **number of microstates in the distribution** $\boldsymbol n$.

The formula counts assignments to labelled particles. It does not count different orderings of the occupation-number list as separate distributions: the allowed values $U_j$ are fixed labels, and each $n_j$ belongs to its corresponding $U_j$.

The number of microstates in the entire macrostate is the sum over all its allowed distributions:

$$
|\mathcal M(U_{\mathrm{tot}})|
=
\sum_{\substack{n_1+\cdots+n_M=N\\
n_1U_1+\cdots+n_MU_M=U_{\mathrm{tot}}}}
\frac{N!}{n_1!\cdots n_M!}.
$$

## 6. The distribution with the largest number of microstates

We seek the allowed occupation-number list that maximizes

$$
W(\boldsymbol n)=\frac{N!}{\prod_{j=1}^{M}n_j!}
$$

subject to the two constraints

$$
\sum_j n_j=N,
\qquad
\sum_j n_jU_j=U_{\mathrm{tot}},
$$

with every $n_j$ a non-negative integer.

This is the exact finite-system problem. Because the occupation numbers must be integers, an exact maximizer need not have a simple closed form. There can also be more than one maximizing list.

For a large system, however, the maximizing occupation numbers can be obtained to leading order by treating the fractions as continuous variables. This gives a simple and useful general form.

### 6.1 Replace counts by fractions

Define the fraction of particles carrying value $U_j$ as

$$
p_j=\frac{n_j}{N}.
$$

Then

$$
p_j\geq 0,
\qquad
\sum_jp_j=1,
\qquad
\sum_jp_jU_j=\overline U,
$$

where

$$
\overline U=\frac{U_{\mathrm{tot}}}{N}
$$

is the fixed average value per particle.

The count becomes

$$
W=N!\prod_j\frac{1}{(Np_j)!}.
$$

### 6.2 Use the large-$N$ approximation

For large integer $q$, the factorial can be approximated by

$$
\ln(q!)\simeq q\ln q-q.
$$

Applying this to $N!$ and to each $(Np_j)!$ gives

$$
\begin{aligned}
\ln W
&=\ln(N!)-\sum_j\ln[(Np_j)!]\\
&\simeq N\ln N-N
-\sum_j\left[Np_j\ln(Np_j)-Np_j\right]\\
&=-N\sum_jp_j\ln p_j.
\end{aligned}
$$

The last equality uses $\sum_jp_j=1$.

Since the logarithm increases whenever its argument increases, maximizing $W$ is equivalent to maximizing $\ln W$. In this approximation, we therefore maximize

$$
-\sum_{j=1}^{M}p_j\ln p_j
$$

subject to the two constraints on the fractions.

### 6.3 Apply the constraints

Introduce two multipliers, $a$ and $\lambda$, and form

$$
\mathcal L
=
-\sum_jp_j\ln p_j
-a\left(\sum_jp_j-1\right)
-\lambda\left(\sum_jp_jU_j-\overline U\right).
$$

At an interior maximum, the derivative with respect to each $p_j$ vanishes:

$$
\frac{\partial\mathcal L}{\partial p_j}
=-(\ln p_j+1)-a-\lambda U_j=0.
$$

Rearranging,

$$
\ln p_j=-(1+a)-\lambda U_j,
$$

and hence

$$
p_j=Ae^{-\lambda U_j},
$$

where $A=e^{-(1+a)}$ is the same constant for every allowed value.

The condition $\sum_jp_j=1$ fixes $A$. Define the finite sum

$$
C(\lambda)=\sum_{k=1}^{M}e^{-\lambda U_k}.
$$

Then

$$
A=\frac{1}{C(\lambda)}
$$

and the maximizing fractions take the form

$$
\boxed{
p_j=\frac{e^{-\lambda U_j}}
{\displaystyle\sum_{k=1}^{M}e^{-\lambda U_k}}.
}
$$

The corresponding occupation numbers are

$$
\boxed{
n_j\simeq
N\frac{e^{-\lambda U_j}}
{\displaystyle\sum_{k=1}^{M}e^{-\lambda U_k}}.
}
$$

The value of $\lambda$ is determined by the prescribed average $\overline U$:

$$
\boxed{
\overline U
=
\frac{\displaystyle\sum_j U_j e^{-\lambda U_j}}
{\displaystyle\sum_j e^{-\lambda U_j}}.
}
$$

This equation is the condition that fixes the one remaining parameter. It must be solved for the particular allowed values and the particular conserved total.

## 7. What the result says

The distribution with the largest number of compatible microstates has, for large $N$, fractions of the form

$$
p_j\propto e^{-\lambda U_j}.
$$

The proportionality constant is fixed by requiring that all fractions add to one. The parameter $\lambda$ is fixed by requiring that the average value of the attribute equal the prescribed value $U_{\mathrm{tot}}/N$.

Several points are important:

1. The exponential form was obtained from the counting formula and the two constraints. It was not assumed at the start.
2. The result applies to any finite list of allowed values $U_j$; the values need not be equally spaced.
3. The sign of $\lambda$ is not fixed in advance. It depends on the specified average and the allowed values.
4. The formula gives the leading large-$N$ occupation fractions. For finite $N$, the exact answer is the integer occupation list (or lists) that maximize the factorial expression.
5. The result relies on the assumption that all assignments satisfying the stated constraints are counted equally. If additional restrictions or unequal weights are introduced, the counting formula and the maximizing distribution may change.

### A simple check

Let the allowed values be

$$
S_U=\{0,1,2\}
$$

and suppose the prescribed average is $\overline U=1$. Taking $\lambda=0$ gives

$$
p_0=p_1=p_2=\frac13,
$$

which has average value

$$
0\left(\frac13\right)
+1\left(\frac13\right)
+2\left(\frac13\right)=1.
$$

Thus, for large $N$, the largest-count distribution has approximately equal fractions at the three allowed values. If $N$ is not divisible by three, the occupation numbers must be integers and the exact maximizing list is determined by the original factorial expression and the exact total-value constraint.

## 8. Why the parameter is determined uniquely for an interior average

For completeness, define the average produced by a chosen $\lambda$:

$$
m(\lambda)=
\frac{\sum_jU_je^{-\lambda U_j}}
{\sum_je^{-\lambda U_j}}.
$$

Differentiating this expression gives

$$
\frac{dm}{d\lambda}
=
-\left[
\frac{\sum_jU_j^2e^{-\lambda U_j}}{\sum_je^{-\lambda U_j}}
-
\left(
\frac{\sum_jU_je^{-\lambda U_j}}{\sum_je^{-\lambda U_j}}
\right)^2
\right].
$$

The quantity in square brackets is the weighted mean of $U^2$ minus the square of the weighted mean of $U$. It is non-negative, and it is strictly positive when at least two distinct allowed values have non-zero fractions. Therefore,

$$
\frac{dm}{d\lambda}<0
$$

in the non-degenerate case. The average decreases continuously as $\lambda$ increases. Consequently, for an average strictly between the smallest and largest allowed values, there is at most one finite $\lambda$ that produces it; for a finite allowed set with all values included, such a $\lambda$ exists.

At the two extreme averages, all particles must carry the smallest or the largest allowed value, respectively. These limiting cases correspond to $\lambda$ tending to positive or negative infinity.

## 9. Extending the description to more attributes

The same definitions can accommodate additional attributes. Suppose each particle carries $K$ attributes,

$$
U^{(1)},U^{(2)},\ldots,U^{(K)},
$$

and an allowed particle-value is now a tuple

$$
\boldsymbol U_j=
\left(U_j^{(1)},U_j^{(2)},\ldots,U_j^{(K)}\right).
$$

Suppose the sum of each attribute over all particles is fixed. The occupation numbers then obey one particle-count constraint and $K$ total-value constraints:

$$
\sum_jn_j=N,
\qquad
\sum_jn_jU_j^{(a)}=U_{\mathrm{tot}}^{(a)}
\quad (a=1,\ldots,K).
$$

The same counting formula $W=N!/\prod_jn_j!$ applies when the allowed tuples are the possible values for one particle and all assignments remain admissible. Repeating the constrained maximization gives

$$
\boxed{
p_j=
\frac{
\exp\!\left[-\sum_{a=1}^{K}\lambda_aU_j^{(a)}\right]
}{
\displaystyle\sum_k
\exp\!\left[-\sum_{a=1}^{K}\lambda_aU_k^{(a)}\right]
}.
}
$$

Each multiplier $\lambda_a$ is determined by the prescribed average of its corresponding attribute. Thus, adding attributes adds constraints and corresponding multipliers, while the basic counting argument remains unchanged.

## Summary of the logical chain

1. A microstate is a complete assignment of allowed attribute values to labelled particles.
2. A macrostate is a set of microstates satisfying specified constraints.
3. A distribution is the subset of a macrostate with a fixed list of occupation numbers.
4. The number of microstates in a distribution is $N!/\prod_jn_j!$.
5. The distribution with the largest number of microstates is found by maximizing this expression subject to the fixed particle number and fixed total attribute value.
6. For large $N$, the maximizing fractions have the exponential form $p_j=e^{-\lambda U_j}/C(\lambda)$, with $\lambda$ fixed by the prescribed average.
7. For finite $N$, the exact maximizing occupation numbers remain an integer-constrained counting problem.

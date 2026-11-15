# Large-`N` Counting: Stirling's Approximation and the Most Numerous Distribution

## Purpose and connection with the finite counting framework

The preceding chapter defined a finite collection of labelled particles, a finite set of allowed values

$$
S_U=\{U_1,U_2,\ldots,U_M\},
$$

and the occupation numbers $n_j$, where $n_j$ counts how many particles carry the value $U_j$. It showed that the number of assignments with a specified occupation list is

$$
W(\boldsymbol n)=\frac{N!}{\prod_{j=1}^{M}n_j!}.
$$

For finite $N$, the exact problem is to maximize this expression over the allowed integer occupation lists. This chapter asks what can be said when $N$ is large.

The main idea is to use Stirling's approximation for the factorials. The occupation numbers remain integers in the original counting problem, but when $N$ is large it is useful to describe them by fractions and maximize the leading approximation to their logarithmic count. This gives a simple expression for the most numerous distribution and lets us calculate the approximate fraction of particles at each allowed value, averages, and probabilities.

Only counting and probability are used here. No additional physical interpretation is required.

## 1. Probability assigned to a distribution

We first make the probability convention explicit.

Suppose every complete assignment of values to the $N$ labelled particles is counted with equal probability before imposing a restriction on the total. There are $M^N$ such assignments, so each has probability $M^{-N}$.

For a specified occupation list $\boldsymbol n$, there are $W(\boldsymbol n)$ assignments. Therefore its probability before imposing a total-value condition is

$$
\boxed{
P(\boldsymbol n)=\frac{W(\boldsymbol n)}{M^N}
=\frac{N!}{M^N\prod_j n_j!}.
}
$$

Now impose the condition that the total lies within the tolerance specified in the preceding chapter. Let $\mathcal C$ denote the set of allowed occupation lists:

$$
\mathcal C=
\left\{
\boldsymbol n:
\sum_jn_j=N,\quad
\left|\sum_jn_jU_j-U_*\right|\leq\epsilon
\right\}.
$$

Once we restrict attention to assignments satisfying this condition, every admitted assignment is still counted equally. The conditional probability of an allowed occupation list is consequently

$$
\boxed{
P(\boldsymbol n\mid\mathcal C)
=
\frac{W(\boldsymbol n)}
{\displaystyle\sum_{\boldsymbol m\in\mathcal C}W(\boldsymbol m)},
\qquad \boldsymbol n\in\mathcal C.
}
$$

The denominator is the total number of admitted assignments. It is the same for every allowed occupation list. Hence the most probable occupation list is exactly the list with the largest $W(\boldsymbol n)$.

This also makes clear the distinction between a microstate and a distribution. Every admitted microstate has the same conditional probability, but a distribution containing more microstates has a larger probability because there are more assignments in it.

## 2. Fractions of particles and Stirling's approximation

Define the fraction of particles carrying the value $U_j$ by

$$
p_j=\frac{n_j}{N}.
$$

The fractions satisfy

$$
p_j\geq0,\qquad \sum_{j=1}^{M}p_j=1.
$$

If the total is specified exactly, or within a fixed tolerance that does not grow with $N$, the average value per particle is fixed to leading order:

$$
\sum_jp_jU_j\simeq\overline U,
\qquad
\overline U=\frac{U_*}{N}.
$$

The approximation sign allows for the finite tolerance and for the fact that the fractions come from integer counts. We will return to the scaling of the tolerance in Section 8.

The number of assignments for a given list is

$$
W=\frac{N!}{\prod_j(Np_j)!}.
$$

For large positive integers $r$, Stirling's approximation is

$$
\ln(r!)
=
r\ln r-r+\frac12\ln(2\pi r)+O(r^{-1}).
$$

At leading order, $\ln(r!)\simeq r\ln r-r$. Applying this to $N!$ and to each $(Np_j)!$ gives

$$
\begin{aligned}
\ln W
&\simeq N\ln N-N
-\sum_j\left[Np_j\ln(Np_j)-Np_j\right]\\
&=N\ln N-N
-N\sum_jp_j\ln N
-N\sum_jp_j\ln p_j
+N\sum_jp_j\\
&=-N\sum_{j=1}^{M}p_j\ln p_j.
\end{aligned}
$$

In the last step we used $\sum_jp_j=1$. Thus, to leading order in $N$,

$$
\boxed{
\ln W\simeq -N\sum_jp_j\ln p_j.
}
$$

Since the logarithm is an increasing function, maximizing $W$ is equivalent to maximizing $\ln W$. The large-$N$ problem is therefore to maximize

$$
-\sum_jp_j\ln p_j
$$

subject to

$$
\sum_jp_j=1,
\qquad
\sum_jp_jU_j=\overline U,
\qquad p_j\geq0.
$$

This is a continuous maximization of the leading approximation, not a change to the exact finite counting problem. The actual occupation numbers are still integers. Once the most likely fractions have been found, the corresponding counts are approximately $Np_j$ and must be rounded or adjusted to satisfy the original integer constraints.

### When is the approximation reliable?

The leading Stirling expression is reliable when the occupations that contribute appreciably satisfy $Np_j\gg1$. If a value has an occupation of order one, Stirling's approximation for that particular factorial is not accurate. Boundary cases with $p_j=0$ are handled by omitting that value from the occupied set, using the convention $0\ln0=0$ in the leading expression.

If all $p_j$ are positive and all $Np_j$ are large, retaining the square-root factors in Stirling's formula gives the more detailed approximation

$$
W\simeq
(2\pi N)^{(1-M)/2}
\left(\prod_jp_j^{-1/2}\right)
\exp\left[-N\sum_jp_j\ln p_j\right].
$$

The exponential factor determines the leading large-$N$ comparison between distributions. The remaining factor gives a smaller correction.

## 3. Finding the most numerous fractions

We maximize

$$
F(\boldsymbol p)=-\sum_jp_j\ln p_j
$$

subject to normalization and the prescribed average. Introduce two multipliers, $a$ and $\lambda$, and form

$$
\mathcal L
=
-\sum_jp_j\ln p_j
-a\left(\sum_jp_j-1\right)
-\lambda\left(\sum_jp_jU_j-\overline U\right).
$$

At an interior maximum, the derivative with respect to each fraction is zero:

$$
\frac{\partial\mathcal L}{\partial p_j}
=-(\ln p_j+1)-a-\lambda U_j=0.
$$

Therefore

$$
\ln p_j=-(1+a)-\lambda U_j,
$$

so that

$$
p_j=Ae^{-\lambda U_j},
$$

where $A$ is independent of $j$. The normalization condition determines $A$. Define the finite positive sum

$$
Q(\lambda)=\sum_{k=1}^{M}e^{-\lambda U_k}.
$$

Then $A=1/Q(\lambda)$, and the most numerous fractions are

$$
\boxed{
p_j^*
=
\frac{e^{-\lambda U_j}}{Q(\lambda)}
=
\frac{e^{-\lambda U_j}}
{\displaystyle\sum_{k=1}^{M}e^{-\lambda U_k}}.
}
$$

The corresponding occupation numbers are

$$
\boxed{n_j^*\simeq Np_j^*.}
$$

The multiplier $\lambda$ is chosen so that the prescribed average is reproduced:

$$
\boxed{
\overline U
=
\sum_jU_jp_j^*
=
\frac{\displaystyle\sum_jU_je^{-\lambda U_j}}
{\displaystyle\sum_je^{-\lambda U_j}}.
}
$$

This equation generally determines $\lambda$ numerically once the allowed values and the desired average are specified. The units of $\lambda$ are the reciprocal of the units of $U$.

### Why this is a maximum

The second derivative of $F$ with respect to the fractions is diagonal:

$$
\frac{\partial^2F}{\partial p_j\partial p_k}
=-\frac{\delta_{jk}}{p_j}.
$$

For positive fractions this quadratic form is strictly negative for every nonzero change in the fractions. Thus $F$ is strictly concave. The constraints are linear, so any interior stationary point is the unique maximum among the allowed fractions. If the prescribed average is at an endpoint of the allowed range, the maximum instead lies on the boundary: all particles carry the smallest or the largest allowed value.


### Additive values built from two independent coordinates

The same counting maximization can be applied when the value assigned to each particle is constructed from two coordinates. This gives a useful result: under the assumptions stated below, the joint distribution at the large-$N$ maximum factorizes into two marginal distributions. Independence is a consequence of the maximization; it is not an assumption imposed at the start.

Suppose each labelled particle carries a pair $(x_1,x_2)$, where the first coordinate can take one of the allowed values
$a_1,\ldots,a_r$, and the second can take one of the allowed values $b_1,\ldots,b_s$. The value associated with the pair is additive:

$$
U(a_i,b_j)=f_1(a_i)+f_2(b_j).
$$

Assume that every pair $(a_i,b_j)$ is allowed, that each pair is counted as one distinct category, and that every complete assignment of pairs to the labelled particles is counted equally. We prescribe the average value per particle, $\overline U$.

Let $n_{ij}$ be the number of particles carrying the pair $(a_i,b_j)$. There are $rs$ possible pair categories, so the occupation numbers obey

$$
\sum_{i=1}^{r}\sum_{j=1}^{s}n_{ij}=N,
$$

and the prescribed average gives

$$
\sum_{i,j}n_{ij}\,[f_1(a_i)+f_2(b_j)]
=N\overline U.
$$

For a specified joint occupation list, the number of assignments is the multinomial count

$$
W=\frac{N!}{\displaystyle\prod_{i,j}n_{ij}!}.
$$

Introduce fractions $p_{ij}=n_{ij}/N$. Stirling's approximation reduces the leading large-$N$ maximization to maximizing

$$
F=-\sum_{i,j}p_{ij}\ln p_{ij}
$$

subject to

$$
\sum_{i,j}p_{ij}=1,
\qquad
\sum_{i,j}p_{ij}[f_1(a_i)+f_2(b_j)]=\overline U.
$$

Using multipliers $\alpha$ and $\lambda$, the stationary condition is

$$
-(\ln p_{ij}+1)-\alpha
-\lambda[f_1(a_i)+f_2(b_j)]=0.
$$

It follows that

$$
p_{ij}=A\,
e^{-\lambda f_1(a_i)}
e^{-\lambda f_2(b_j)},
$$

where $A$ is fixed by normalization. Define the two finite sums

$$
Q_1(\lambda)=\sum_{i=1}^{r}e^{-\lambda f_1(a_i)},
\qquad
Q_2(\lambda)=\sum_{j=1}^{s}e^{-\lambda f_2(b_j)}.
$$

Because every pair is allowed, the normalization sum separates:

$$
\begin{aligned}
1
&=\sum_{i,j}p_{ij}\\
&=A\left(\sum_i e^{-\lambda f_1(a_i)}\right)
\left(\sum_j e^{-\lambda f_2(b_j)}\right)\\
&=A Q_1(\lambda)Q_2(\lambda).
\end{aligned}
$$

Thus $A=1/(Q_1Q_2)$, and the maximizing joint fractions are

$$
\boxed{
p_{ij}^*
=
\frac{e^{-\lambda f_1(a_i)}}{Q_1(\lambda)}
\frac{e^{-\lambda f_2(b_j)}}{Q_2(\lambda)}.
}
$$

The multiplier $\lambda$ is common to both factors. It is determined by the single prescribed-average condition

$$
\overline U
=
\sum_{i,j}p_{ij}^*[f_1(a_i)+f_2(b_j)].
$$

**The joint distribution factorizes.** Define its two marginal fractions by summing over the other coordinate:

$$
p_i^{(1)}=\sum_jp_{ij}^*,
\qquad
p_j^{(2)}=\sum_ip_{ij}^*.
$$

Substitution gives

$$
\boxed{
p_i^{(1)}=\frac{e^{-\lambda f_1(a_i)}}{Q_1(\lambda)},
\qquad
p_j^{(2)}=\frac{e^{-\lambda f_2(b_j)}}{Q_2(\lambda)}.
}
$$

Consequently,

$$
\boxed{p_{ij}^*=p_i^{(1)}p_j^{(2)}.}
$$

In the maximizing large-$N$ distribution, the two coordinates are therefore statistically independent in the precise sense that their joint fraction is the product of their marginal fractions. No independence assumption was needed in setting up the maximization. It follows from the additive form of the assigned value and the fact that every combination of coordinate values is allowed.

**How the prescribed average is apportioned.** The mean contribution from the first coordinate is

$$
\begin{aligned}
\overline U_1
&=\sum_i p_i^{(1)}f_1(a_i)\\
&=-\frac{d}{d\lambda}\ln Q_1(\lambda),
\end{aligned}
$$

and, similarly,

$$
\overline U_2
=\sum_j p_j^{(2)}f_2(b_j)
=-\frac{d}{d\lambda}\ln Q_2(\lambda).
$$

Since the normalizing sum for the pair is

$$
Q(\lambda)=
\sum_{i,j}e^{-\lambda[f_1(a_i)+f_2(b_j)]}
=Q_1(\lambda)Q_2(\lambda),
$$

we have

$$
\ln Q=\ln Q_1+\ln Q_2
$$

and hence

$$
\boxed{\overline U=\overline U_1+\overline U_2.}
$$

The two contributions are not generally equal. Equality requires additional conditions. For example, if the two coordinate sets and their contribution functions are identical, then $Q_1=Q_2$, the two marginal distributions have the same form, and

$$
\boxed{\overline U_1=\overline U_2=\frac{\overline U}{2}.}
$$

This equality is a consequence of symmetry, not of factorization alone. Independence and equal sharing are different statements.

**More than two coordinates.** If a particle carries $m$ coordinates and its assigned value is the sum of separate contributions,

$$
U(x_1,\ldots,x_m)=\sum_{k=1}^{m}f_k(x_k),
$$

and all combinations of allowed coordinate values are available, the same argument gives

$$
Q(\lambda)=\prod_{k=1}^{m}Q_k(\lambda),
\qquad
Q_k(\lambda)=\sum_{x_k}e^{-\lambda f_k(x_k)},
$$

and

$$
\boxed{
p^*(x_1,\ldots,x_m)
=\prod_{k=1}^{m}
\frac{e^{-\lambda f_k(x_k)}}{Q_k(\lambda)}.
}
$$

The mean contribution from coordinate $k$ is

$$
\overline U_k
=-\frac{d}{d\lambda}\ln Q_k(\lambda),
\qquad
\overline U=\sum_{k=1}^{m}\overline U_k.
$$

**Scope of the result.** The factorization depends on two structural assumptions: the allowed set of coordinate combinations is a Cartesian product (there are no forbidden pairs or other constraints coupling the coordinates), and the assigned value is a sum of functions of the separate coordinates. If either condition fails, the normalization sum need not factorize and the maximizing joint distribution need not be independent.

As elsewhere in this chapter, this is a large-$N$ result obtained by maximizing the Stirling approximation over continuous fractions. The exact finite-$N$ occupation numbers are integers and must satisfy the exact total-value constraint. Arithmetic restrictions can prevent them from realizing the continuous maximizing fractions exactly. Moreover, conditioning a finite collection of particles on an exact total can correlate the coordinates across particles, even though the single-particle joint fractions at the large-$N$ maximum factorize. The conclusion here is specifically about the factorization of that maximizing joint distribution.

## 4. The probability of a particle carrying a particular value

The result $p_j^*$ has a direct probability interpretation.

Choose one of the $N$ labelled particles at random from an assignment whose occupation list is close to the most numerous list. The fraction of particles carrying $U_j$ is $n_j/N$, which for a most numerous large-$N$ distribution is approximately $p_j^*$. Thus

$$
\boxed{
\Pr(\text{a randomly selected particle carries }U_j)
\simeq p_j^*.
}
$$

There is also an exact finite-$N$ statement when probabilities are taken over all admitted assignments. Let $\mathbb E[n_j\mid\mathcal C]$ be the average occupation number over that set of assignments. Because the particle labels are treated symmetrically,

$$
\Pr(u_i=U_j\mid\mathcal C)
=
\frac{\mathbb E[n_j\mid\mathcal C]}{N}
$$

for any particular label $i$. When the allowed occupation lists are sharply concentrated around the large-$N$ maximizing fractions, this becomes

$$
\Pr(u_i=U_j\mid\mathcal C)\simeq p_j^*.
$$

The probability is the same for every particle label. The particles are distinguishable for counting assignments, but no label is preferred by the constraints.

It is important not to confuse this statement with the probability of one particular complete assignment. Every admitted complete assignment has probability $1/|\mathcal M(U_*,\epsilon)|$. The value $p_j^*$ is instead the approximate probability for the value carried by one selected particle, after all admitted assignments have been considered.

## 5. Probability of an occupation list and concentration near the maximum

For any allowed occupation list, the exact conditional probability is

$$
P(\boldsymbol n\mid\mathcal C)
=
\frac{W(\boldsymbol n)}
{\displaystyle\sum_{\boldsymbol m\in\mathcal C}W(\boldsymbol m)}.
$$

For large $N$, Stirling's approximation shows that lists with fractions near $\boldsymbol p^*$ have much larger counts than lists whose fractions differ substantially from $\boldsymbol p^*$. We can make this comparison more explicit.

For the moment impose the average-value constraint exactly. Define

$$
D(\boldsymbol p\Vert\boldsymbol p^*)
=
\sum_jp_j\ln\left(\frac{p_j}{p_j^*}\right),
$$

with terms having $p_j=0$ understood to be zero. Since

$$
\ln p_j^*=-\lambda U_j-\ln Q(\lambda),
$$

any other allowed fraction list with the same normalization and average obeys

$$
\sum_jp_j\ln p_j^*
=
-\lambda\overline U-\ln Q(\lambda)
=
\sum_jp_j^*\ln p_j^*.
$$

It follows that

$$
\sum_jp_j\ln p_j
-
\sum_jp_j^*\ln p_j^*
=
D(\boldsymbol p\Vert\boldsymbol p^*).
$$

Comparing the leading logarithmic count at $\boldsymbol p$ with its value at the continuous maximum $\boldsymbol p^*$ gives

$$
\boxed{
-N\sum_jp_j\ln p_j
+N\sum_jp_j^*\ln p_j^*
=
-ND(\boldsymbol p\Vert\boldsymbol p^*).
}
$$

The quantity $D$ is non-negative and is zero only when the two fraction lists are identical. One way to establish non-negativity is to use $\ln x\leq x-1$ for positive $x$. Therefore, any fixed departure from the maximizing fractions reduces the count by an exponential factor as $N$ grows.

The number of possible occupation lists grows only as a power of $N$ when $M$ is fixed: it is at most $(N+1)^M$. This is much slower than an exponential in $N$. Consequently, when feasible integer occupation lists exist whose fractions approach $\boldsymbol p^*$ as $N$ grows, the conditional probability is concentrated in a narrow region around the maximizing fractions. In that case the fractions $p_j^*$ describe the occupation of a typical assignment selected from the admitted set, not merely a formal maximum.

This feasibility qualification matters. The continuous fractions $p_j^*$ need not be approached by integer lists satisfying an exact total for every choice of real allowed values. Nor does a fixed total tolerance guarantee this automatically: arithmetic restrictions can leave only a restricted set of occupation lists, or even make the admitted set empty. The large-$N$ formula describes the exact discrete problem when the allowed integer lists sufficiently sample the continuous constraint surface. If they do not, the discrete maximization from the preceding chapter remains decisive.

For a fixed total tolerance $\epsilon$, write the target average at a given $N$ as $\overline U_N=U_*/N$. An admitted occupation list has an average $\mu=\sum_jp_jU_j$ satisfying $|\mu-\overline U_N|\leq\epsilon/N$. If $\lambda_N$ is the finite multiplier associated with the target average $\overline U_N$, the relative-count identity acquires the additional term $N\lambda_N(\mu-\overline U_N)$:

$$
\ln W(\boldsymbol p)-\ln W(\boldsymbol p_N^*)
\simeq
-ND(\boldsymbol p\Vert\boldsymbol p_N^*)
+N\lambda_N(\mu-\overline U_N).
$$

Here $\boldsymbol p_N^*$ is the continuous maximizing fraction list at average $\overline U_N$. The magnitude of the additional term is at most $|\lambda_N|\epsilon$, which is of order one when the target averages remain in the interior of the feasible range and $\lambda_N$ stays bounded. It therefore does not change the leading, order-$N$ comparison of logarithmic counts. This explains why a fixed total tolerance has the same leading large-$N$ concentration result as an exact average constraint, provided the admitted integer lists are feasible and sufficiently sample the relevant continuous fractions. If the tolerance itself grows in proportion to $N$, the constraint must instead be treated as an interval of allowed averages, as discussed in Section 8.

## 6. Average values and their fluctuations in the large-`N` description

For any function $f(U)$ defined on the allowed values, its average under the fractions $p_j^*$ is

$$
\boxed{
\langle f(U)\rangle
=
\sum_jf(U_j)p_j^*
=
\frac{\displaystyle\sum_jf(U_j)e^{-\lambda U_j}}
{Q(\lambda)}.
}
$$

In particular, the average value is

$$
\boxed{
\langle U\rangle
=
\frac{\sum_jU_je^{-\lambda U_j}}
{\sum_je^{-\lambda U_j}}
=
\overline U.
}
$$

The average of the square is

$$
\langle U^2\rangle
=
\frac{\sum_jU_j^2e^{-\lambda U_j}}
{\sum_je^{-\lambda U_j}}.
$$

The spread of the allowed values under these probabilities is measured by

$$
\boxed{
\sigma_U^2
=
\langle U^2\rangle-\langle U\rangle^2.
}
$$

The same results can be obtained by differentiating $Q(\lambda)$. The reason is that differentiating an exponential $e^{-\lambda U_j}$ brings down a factor of $-U_j$. The normalization by $Q$ then turns the resulting sums into averages with the probabilities $p_j^*$.

Since
$$
\frac{dQ}{d\lambda}
=-\sum_jU_je^{-\lambda U_j},
$$
and
$$
\langle U\rangle
=\sum_jU_jp_j^*
=\frac{\sum_jU_je^{-\lambda U_j}}{Q},
$$
we obtain
$$
\frac{d}{d\lambda}\ln Q
=\frac{1}{Q}\frac{dQ}{d\lambda}
=-\langle U\rangle.
$$
Thus
$$
\boxed{
\langle U\rangle
=-\frac{d}{d\lambda}\ln Q(\lambda).
}
$$

**Second derivative: the variance.** To differentiate the mean explicitly, write
$$
A_1(\lambda)=\sum_jU_je^{-\lambda U_j},
\qquad
\langle U\rangle=\frac{A_1}{Q}.
$$
Differentiating the numerator gives
$$
A_1'=-\sum_jU_j^2e^{-\lambda U_j},
\qquad
Q'=-A_1.
$$
Using the quotient rule,
$$
\begin{aligned}
\frac{d\langle U\rangle}{d\lambda}
&=\frac{A_1'Q-A_1Q'}{Q^2}\\
&=-\frac{\sum_jU_j^2e^{-\lambda U_j}}{Q}
+\left(\frac{\sum_jU_je^{-\lambda U_j}}{Q}\right)^2\\
&=-\langle U^2\rangle+\langle U\rangle^2.
\end{aligned}
$$
Because the first derivative of $\ln Q$ is $-\langle U\rangle$, differentiating it once more changes the sign:
$$
\boxed{
\frac{d^2}{d\lambda^2}\ln Q(\lambda)
=\langle U^2\rangle-\langle U\rangle^2
=\sigma_U^2.
}
$$
This is the variance, since expanding the square in its definition gives
$$
\begin{aligned}
\left\langle(U-\langle U\rangle)^2\right\rangle
&=\langle U^2\rangle
-2\langle U\rangle\langle U\rangle
+\langle U\rangle^2\\
&=\langle U^2\rangle-\langle U\rangle^2.
\end{aligned}
$$
It follows in particular that
$$
\boxed{
\frac{d\langle U\rangle}{d\lambda}
=-\sigma_U^2\leq0.
}
$$
If at least two distinct values have nonzero probabilities, the variance is positive and the inequality is strict. Thus the average value decreases continuously as $\lambda$ increases. For an average strictly between the smallest and largest allowed values, this also establishes that there is exactly one finite value of $\lambda$ that produces the required average.

**Third derivative: the negative third central moment.** It is important to distinguish the *raw third moment* $\langle U^3\rangle$ from the *third central moment* $\langle(U-\langle U\rangle)^3\rangle$. The third derivative of $\ln Q$ is not the raw third moment.

The same quotient-rule calculation used above, now applied to the second moment, gives
$$
\frac{d\langle U^2\rangle}{d\lambda}
=-\langle U^3\rangle
+\langle U^2\rangle\langle U\rangle.
$$
We also already have
$$
\frac{d\langle U\rangle}{d\lambda}
=-\langle U^2\rangle+\langle U\rangle^2.
$$
Differentiate the variance expression and substitute these two results:
$$
\begin{aligned}
\frac{d^3}{d\lambda^3}\ln Q
&=\frac{d}{d\lambda}
\left(\langle U^2\rangle-\langle U\rangle^2\right)\\
&=-\langle U^3\rangle
+\langle U^2\rangle\langle U\rangle
-2\langle U\rangle\cdot
\frac{d\langle U\rangle}{d\lambda}\\
&=-\langle U^3\rangle
+3\langle U\rangle\langle U^2\rangle
-2\langle U\rangle^3.
\end{aligned}
$$
On the other hand, expanding the third central moment gives
$$
\begin{aligned}
\left\langle(U-\langle U\rangle)^3\right\rangle
&=\langle U^3\rangle
-3\langle U\rangle\langle U^2\rangle
+3\langle U\rangle^2\langle U\rangle
-\langle U\rangle^3\\
&=\langle U^3\rangle
-3\langle U\rangle\langle U^2\rangle
+2\langle U\rangle^3.
\end{aligned}
$$
Comparing the last two expressions,
$$
\boxed{
\frac{d^3}{d\lambda^3}\ln Q(\lambda)
=-\left\langle
(U-\langle U\rangle)^3
\right\rangle.
}
$$
The minus sign ultimately comes from the factor $e^{-\lambda U_j}$: each differentiation brings down one factor of $-U_j$. The third central moment measures the asymmetry of the distribution about its mean; it is distinct from the raw third moment.

These derivative identities are useful because they generate averages and measures of spread and asymmetry directly from the normalizing sum, without having to evaluate each weighted sum from scratch.

### A point about fluctuations of the total

The variance $\sigma_U^2$ above describes the spread of the value carried by one particle under the probabilities $p_j^*$. If $N$ values were selected independently using these probabilities, the variance of their sum would be $N\sigma_U^2$. That independent-selection statement is a useful way to interpret the fractions, but it is not an exact description of assignments after conditioning on a fixed total. In the exact-total case, the sum is fixed and has no fluctuation at all. The occupation numbers are also linked by both constraints, so their fluctuations cannot be treated as independent.

## 7. Worked example: three allowed values

Let

$$
S_U=\{0,1,2\}
$$

and prescribe the average value

$$
\overline U=0.8.
$$

The large-$N$ fractions are

$$
p_0^*=\frac{1}{Q},\qquad
p_1^*=\frac{e^{-\lambda}}{Q},\qquad
p_2^*=\frac{e^{-2\lambda}}{Q},
$$

where

$$
Q=1+e^{-\lambda}+e^{-2\lambda}.
$$

Put $q=e^{-\lambda}$. The average-value condition becomes

$$
\frac{q+2q^2}{1+q+q^2}=0.8.
$$

Rearranging,

$$
6q^2+q-4=0.
$$

The positive solution is

$$
q=\frac{-1+\sqrt{97}}{12}\simeq0.7374,
$$

so

$$
\lambda=-\ln q\simeq0.3046.
$$

The resulting fractions are

$$
\boxed{
p_0^*\simeq0.4384,\qquad
p_1^*\simeq0.3233,\qquad
p_2^*\simeq0.2384.
}
$$

They add to one, and their average is

$$
0p_0^*+1p_1^*+2p_2^*=0.8.
$$

For $N=10^6$ and exact total $U_{\mathrm{tot}}=800000$, one nearby integer occupation list is

$$
n_0=438371,\qquad
n_1=323258,\qquad
n_2=238371.
$$

These counts add to $10^6$ and give $n_1+2n_2=800000$. They are very close to $Np_j^*$. In this example they are also the exact integer maximizer. To check this directly, write $t=n_2$, so that $n_1=800000-2t$ and $n_0=200000+t$. The ratio of consecutive counts is $W(t+1)/W(t)=n_1(n_1-1)/[(n_0+1)(t+1)]$.

This ratio decreases as $t$ increases. It is approximately $1.0000169$ at $t=238370$ and $0.9999981$ at $t=238371$. Thus the count increases up to $t=238371$ and decreases after it, proving that the displayed list is the exact integer maximizer for this example.

The example also shows that the probabilities need not be equal. The lower allowed values occur in larger fractions when the required average is below the simple arithmetic mean of the three allowed values.

## 8. The role of the tolerance for large $N$

The preceding chapter used a tolerance on the total:

$$
\left|\sum_jn_jU_j-U_*\right|\leq\epsilon.
$$

For large $N$, it is important to say how this tolerance behaves as $N$ changes. There are two distinct possibilities.

### 8.1 Fixed total tolerance

If $\epsilon$ is fixed while $N$ grows, the permitted average lies in the interval

$$
\frac{U_*}{N}-\frac{\epsilon}{N}
\leq
\sum_jp_jU_j
\leq
\frac{U_*}{N}+\frac{\epsilon}{N}.
$$

The width of this interval is $2\epsilon/N$, which tends to zero. Provided $U_*/N$ tends to a value $\overline U$, the leading large-$N$ maximization therefore uses the equality constraint

$$
\sum_jp_jU_j=\overline U.
$$

This is the case treated in Sections 3–7.

### 8.2 Tolerance proportional to the number of particles

A different problem is obtained if the total tolerance grows as $\epsilon=N\delta$, where $\delta$ is fixed. Then the allowed average lies in a non-vanishing interval:

$$
\overline U-\delta
\leq
\sum_jp_jU_j
\leq
\overline U+\delta.
$$

The interval must first overlap the feasible average range from $U_{\min}=\min_jU_j$ to $U_{\max}=\max_jU_j$; otherwise the macrostate is empty. The large-$N$ maximization is then performed over all fractions whose average lies in the allowed part of this interval. If the unconstrained maximum, $p_j=1/M$, already has an average inside the interval, it is the maximum and $\lambda=0$. Otherwise the maximizing average lies at the boundary of the permitted interval nearest to the unconstrained average, and the formula from Section 3 applies with that boundary average. This follows because the maximum value of $-\sum_jp_j\ln p_j$ at a fixed average is a concave function of that average, with its largest value at the uniform fractions.

There is one endpoint qualification. If the selected boundary average is exactly $U_{\min}$ or $U_{\max}$, the maximizing fractions are concentrated entirely on the corresponding extreme value. This is the limiting case $\lambda\to+\infty$ or $\lambda\to-\infty$, respectively; there is no finite multiplier at either endpoint.

Thus, the exponential form in Section 3 applies to an active average-value constraint. The scale of the tolerance determines whether that constraint is active and, if so, which average value must be used.

## 9. Summary

1. The probability of an occupation list is proportional to its number of assignments, $W=N!/\prod_jn_j!$.
2. When all admitted assignments are counted equally, the most probable occupation list is the one with the largest multinomial count.
3. For large $N$, Stirling's approximation gives $\ln W\simeq-N\sum_jp_j\ln p_j$.
4. Maximizing this expression at fixed particle number and fixed average value gives
   $$
   p_j^*=\frac{e^{-\lambda U_j}}{\sum_ke^{-\lambda U_k}},
   $$
   where $\lambda$ is fixed by the required average.
5. The fraction $p_j^*$ is approximately the probability that a randomly selected particle carries the value $U_j$; the expected occupation number is approximately $Np_j^*$.
6. The normalizing sum $Q(\lambda)$ generates averages:
   $$
   \langle U\rangle=-\frac{d}{d\lambda}\ln Q,
   \qquad
   \sigma_U^2=\frac{d^2}{d\lambda^2}\ln Q.
   $$
7. Occupation lists whose fractions differ appreciably from the maximizing fractions have exponentially smaller counts as $N$ grows.
8. A fixed tolerance on the total becomes an exact average constraint to leading order. A tolerance proportional to $N$ instead leaves a finite interval of allowed averages and must be treated as a constrained inequality.
9. The large-$N$ result is an approximation to the discrete finite problem. Integer occupation numbers and exact feasibility remain part of the underlying counting framework.

# Factorization and Interactions in Counting Distributions

This chapter extends the large-$N$ counting argument to particles carrying more than one coordinate. It asks when the most numerous joint distribution factorizes into independent marginal distributions, and what changes when the assigned value contains an interaction between coordinates.

The discussion uses only the counting framework: labelled particles, equally counted complete assignments, occupation numbers, and the large-$N$ Stirling approximation. No physical interpretation is required.

## Additive values built from two coordinates

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
p_{ij}=A\,e^{-\lambda f_1(a_i)}\,e^{-\lambda f_2(b_j)},
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
\frac{e^{-\lambda f_1(a_i)}}{Q_1(\lambda)}\,\frac{e^{-\lambda f_2(b_j)}}{Q_2(\lambda)}.
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

### Worked example: two quadratic coordinate contributions

Consider the additive assigned value

$
U(x_1,x_2)=\alpha_1x_1^2+\alpha_2x_2^2,
$

where each coordinate can take the three values $-1,0,+1$, and take $\alpha_1,\alpha_2>0$. The allowed set is the full Cartesian product, so the additive factorization result applies. For the first coordinate,

$
Q_1(\lambda)
=\sum_{x_1=-1}^{1}e^{-\lambda\alpha_1x_1^2}
=1+2e^{-\lambda\alpha_1},
$

and similarly

$
Q_2(\lambda)=1+2e^{-\lambda\alpha_2}.
$

The marginal probabilities are therefore

$
p_1(0)=\frac{1}{1+2e^{-\lambda\alpha_1}},
\qquad
p_1(+1)=p_1(-1)
=\frac{e^{-\lambda\alpha_1}}{1+2e^{-\lambda\alpha_1}},
$

with the corresponding expressions for $p_2$ obtained by replacing $\alpha_1$ with $\alpha_2$. The joint probability is the product $p(x_1,x_2)=p_1(x_1)p_2(x_2)$.

The mean contribution from the first coordinate is

$
\boxed{
\overline U_1
=\alpha_1\langle x_1^2\rangle
=\frac{2\alpha_1e^{-\lambda\alpha_1}}
{1+2e^{-\lambda\alpha_1}}.
}
$

Likewise,

$
\boxed{
\overline U_2
=\frac{2\alpha_2e^{-\lambda\alpha_2}}
{1+2e^{-\lambda\alpha_2}},
\qquad
\overline U=\overline U_1+\overline U_2.
}
$

The single multiplier $\lambda$ is fixed by the prescribed value of $\overline U$. Notice that the two coordinates are independent even when $\alpha_1\ne\alpha_2$; however, their mean contributions are then generally unequal. If $\alpha_1=\alpha_2$, symmetry gives $\overline U_1=\overline U_2=\overline U/2$. This example shows explicitly that factorization follows from additivity, whereas equal sharing requires symmetry.

### Worked example: independent coordinates need not share the mean equally

For a simpler illustration of unequal sharing, let $x_1,x_2$ each take only the values $0$ and $1$, with

$
U(x_1,x_2)=\alpha_1x_1+\alpha_2x_2,
\qquad \alpha_1,\alpha_2>0.
$

The marginal probabilities of the value $1$ are

$
p_1(1)=\frac{e^{-\lambda\alpha_1}}{1+e^{-\lambda\alpha_1}},
\qquad
p_2(1)=\frac{e^{-\lambda\alpha_2}}{1+e^{-\lambda\alpha_2}}.
$

The joint distribution again factorizes, but the mean contributions are

$
\overline U_1
=\frac{\alpha_1}{1+e^{\lambda\alpha_1}},
\qquad
\overline U_2
=\frac{\alpha_2}{1+e^{\lambda\alpha_2}}.
$

There is no reason for these two quantities to be equal when the coefficients differ. They become equal when the two coordinate contributions are identical, as required by symmetry. Both examples use one common multiplier because there is one constraint on the total mean, not one independent constraint for each coordinate.

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

## When the assigned value contains an interaction

Now suppose the value associated with a pair is

$$
U(a_i,b_j)=f_1(a_i)+f_2(b_j)+g(a_i,b_j),
$$

where $g$ is a general function of both coordinates. The constraints on the fractions are still normalization and the prescribed mean:

$$
\sum_{i,j}p_{ij}=1,
\qquad
\sum_{i,j}p_{ij}
[f_1(a_i)+f_2(b_j)+g(a_i,b_j)]
=\overline U.
$$

The same entropy maximization gives the stationary distribution

$$
\boxed{
p_{ij}^*
=
\frac{
e^{-\lambda[f_1(a_i)+f_2(b_j)+g(a_i,b_j)]}
}{
Q(\lambda)
},
}
$$

where the joint normalizing sum is

$$
Q(\lambda)=
\sum_{i,j}
e^{-\lambda[f_1(a_i)+f_2(b_j)+g(a_i,b_j)]}.
$$

Unlike the case without an interaction, this sum does not generally split into a product of a sum over $i$ and a sum over $j$. Consequently, the maximizing joint distribution does not generally factorize.

### When does factorization survive?

For a fixed value of $\lambda$, define the positive matrix

$$
K_{ij}=e^{-\lambda g(a_i,b_j)}.
$$

The other two factors in the unnormalized joint distribution depend separately on $i$ and $j$. Therefore the joint distribution factorizes if and only if the matrix $K$ has rank one, meaning that all its two-by-two minors vanish. Equivalently, for every choice of indices $i,i',j,j'$,

$$
K_{ij}K_{i'j'}=K_{ij'}K_{i'j}.
$$

For nonzero $\lambda$, this is equivalent to the interaction being expressible in the additive form

$$
g(a_i,b_j)=g_1(a_i)+g_2(b_j)+c,
$$

where $c$ is a constant. Such a term is not a genuine coupling: $g_1$ and $g_2$ can be absorbed into $f_1$ and $f_2$, while the constant changes only the overall normalization.

There is also a special case at $\lambda=0$. Then $K_{ij}=1$ for every pair, so the maximizing distribution is uniform over the allowed pairs and factorizes, regardless of the form of $g$. This occurs when the prescribed mean equals the uniform average of the assigned values over the allowed pair set.

For a genuine interaction that cannot be written as a sum of separate one-coordinate functions, factorization generally fails.

### A two-valued example

Let each coordinate take the values $-1$ and $+1$, let $f_1=f_2=0$, and choose the interaction

$$
g(x_1,x_2)=Jx_1x_2,
$$

where $J$ is a fixed constant. The maximizing distribution is

$$
p(x_1,x_2)
=
\frac{e^{-\lambda Jx_1x_2}}{4\cosh(\lambda J)}.
$$

Each marginal is uniform:

$$
p_1(x_1)=p_2(x_2)=\frac12.
$$

If the coordinates were independent, all four joint probabilities would therefore be $1/4$. But for $\lambda J\ne0$, the joint probabilities are not all equal. In particular,

$$
\boxed{
\langle x_1x_2\rangle
=
-\tanh(\lambda J),
}
$$

which is nonzero. The interaction has produced a correlation even though neither marginal distribution has changed from uniformity.

This example makes the distinction precise: knowing the two marginal distributions does not determine the joint distribution when an interaction is present.

### More than two coordinates

For several coordinates, an assigned value of the form

$$
U(x_1,\ldots,x_m)
=
\sum_{k=1}^{m}f_k(x_k)
+
G(x_1,\ldots,x_m)
$$

gives

$$
p^*(x_1,\ldots,x_m)
=
\frac{
\exp\{-\lambda[\sum_k f_k(x_k)+G(x_1,\ldots,x_m)]\}
}{Q(\lambda)}.
$$

The distribution factorizes into one-coordinate marginals when the interaction contribution can be absorbed into a sum of separate one-coordinate functions (up to a constant). More general interactions couple the coordinates and prevent this factorization.

## Scope and finite-size qualification

All factorization statements in this chapter concern the maximizing fractions obtained from the large-$N$ Stirling approximation. At finite $N$, occupation numbers are integers and must satisfy the exact total-value constraint; arithmetic restrictions can prevent the continuous maximizing fractions from being realized exactly. Also, conditioning a finite collection of particles on an exact total can create correlations between coordinates, even when the large-$N$ maximizing single-particle distribution factorizes.

The key distinction is between a constraint on the sum of separate coordinate contributions, which permits factorization at the large-$N$ maximum when all combinations are allowed, and a genuine interaction term, which generally couples the coordinates.

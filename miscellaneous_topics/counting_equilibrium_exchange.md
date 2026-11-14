# Counting Equilibrium: Exchange Between Systems

## Purpose and scope

The preceding chapters considered one finite collection of labelled particles, first with an exact discrete counting description and then with a large-\(N\) approximation. We now consider two or more such systems that can exchange the attribute \(U\), while the total value of \(U\) remains fixed.

The question is whether counting alone can identify a preferred allocation of the total between the systems. It can. The number of combined assignments is the product of the numbers of assignments available to the separate systems. The preferred allocation is the one for which this product is largest.

This chapter introduces a quantity called the **counting slope**. For a system with fixed particle number \(N\), it measures how rapidly the logarithm of the number of assignments changes when the total value \(U\) changes. We will show that the counting slopes of systems able to exchange \(U\) are equal at an interior equilibrium allocation.

The discussion uses only counting, maximization, and probability based on equal counting of assignments. It does not assume any particular mechanism or speed for the exchange. In particular, counting identifies the direction in which the number of compatible combined assignments increases; it does not by itself describe the time evolution of an exchange.

## 1. Two systems that can exchange \(U\)

Consider two systems, labelled 1 and 2. Their particle numbers are fixed at \(N_1\) and \(N_2\). Initially, their total values of the attribute are \(U_1\) and \(U_2\).

We assume:

1. The particle number of each system remains fixed.
2. The allowed values of \(U\) for each system, and the rules for counting its assignments, are specified.
3. The systems can exchange \(U\), but no other attribute is exchanged.
4. The combined total is conserved:
   $$
   U_1+U_2=U_{\mathrm{tot}}=\text{constant}.
   $$
5. Apart from the constraint on the combined total, an assignment of system 1 can be combined with any assignment of system 2.

Let

$
W_i(N_i,U_i)
$

denote the number of assignments of system \(i\) whose total attribute value is **exactly** \(U_i\). The exact finite counting results below apply when the specified totals are attainable. For brevity, with \(N_i\) fixed, we write this as \(W_i(U_i)\). If a total is not attainable, its exact count is zero and it is not an allowed allocation.

The earlier finite-counting chapter also introduced a tolerance macrostate, in which assignments with totals in a window around a target are grouped together. One must take care when using such windows here: the product of two window counts does not, in general, count only pairs whose actual totals add to the prescribed combined total. With finite-width windows and exact conservation, the correct combined count is a sum over compatible pairs of actual subsystem totals. We use exact attainable totals for the exact product formulas in this chapter; a smooth or finite-resolution description must be constructed consistently with the conservation constraint.

A combined assignment consists of one assignment of system 1 together with one assignment of system 2. Every choice for system 1 can be paired with every choice for system 2. Therefore, at a specified allocation \((U_1,U_2)\), the number of combined assignments is

$$
\boxed{
W_{\mathrm{tot}}(U_1,U_2)=W_1(U_1)W_2(U_2).
}
$$

Since the combined total is fixed, we can write \(U_2=U_{\mathrm{tot}}-U_1\). Thus the number of combined assignments associated with an allocation \(U_1\) is

$$
\boxed{
W_{\mathrm{tot}}(U_1)
=
W_1(U_1)W_2(U_{\mathrm{tot}}-U_1).
}
$$

This product is the central counting result for two systems.

## 2. What we mean by equilibrium

We define the **counting equilibrium allocation** to be an allowed allocation of the conserved total for which the number of combined assignments is largest:

$$
\boxed{
\text{Equilibrium: maximize }
W_1(U_1)W_2(U_{\mathrm{tot}}-U_1)
}
$$

over all allowed allocations.

This definition has a direct probability interpretation for discrete totals. Suppose all combined assignments compatible with the fixed total are counted with equal weight. The probability of an allowed allocation is then

$
P(U_1,U_2)
=
\frac{W_1(U_1)W_2(U_2)}
{\displaystyle\sum_{\text{allowed allocations }(V_1,V_2)}
W_1(V_1)W_2(V_2)}.
$

Consequently, the equilibrium allocation is the most probable allocation under this equal-counting convention. In a continuous approximation, probabilities are instead described by a density with respect to a specified allocation measure (for example, \(dU_1\)); the normalization is then an integral, not a sum. The measure must be stated because a density depends on the variable and measure used.

For a large collection of particles, the number of assignments can be very strongly concentrated around its maximum. In that situation, the equilibrium allocation is not merely the most numerous one: allocations appreciably different from it can have much smaller probabilities. The precise conditions for such concentration depend on the counting functions and on which totals are attainable.

The definition does not assert that no individual exchange ever occurs. It says that the allocation is at the maximum of the combined count. A microscopic exchange may still occur in either direction if a mechanism for exchange is supplied. Counting alone identifies the absence of a preferred direction at the maximum; it does not specify the rates of individual exchanges.

## 3. Maximizing the combined count

For two systems, the number of combined assignments at a specified allocation is

$
W_{\\mathrm{tot}}(U_1)
=
W_1(U_1)W_2(U_{\\mathrm{tot}}-U_1).
$

The counting-equilibrium allocation is the allowed value of $U_1$ that maximizes this product. We therefore maximize the product itself, rather than beginning by postulating a derivative-based quantity.

It is convenient to take its logarithm because the logarithm is a strictly increasing function: maximizing $W_{\\mathrm{tot}}$ is equivalent to maximizing its logarithm. Thus

$
L(U_1)
=
\\ln W_1(U_1)
+
\\ln W_2(U_{\\mathrm{tot}}-U_1).
$

At an interior maximum, with $U_{\\mathrm{tot}}$, $N_1$, and $N_2$ fixed, the first derivative must vanish:

$
\\frac{dL}{dU_1}
=
\\left(\\frac{\\partial\\ln W_1}{\\partial U_1}\\right)_{N_1}
-
\\left(\\frac{\\partial\\ln W_2}{\\partial U_2}\\right)_{N_2}
=0.
$

The minus sign follows from conservation, $U_2=U_{\\mathrm{tot}}-U_1$, so $dU_2/dU_1=-1$. Hence the condition for an interior stationary allocation is

$
\\boxed{
\\left(\\frac{\\partial\\ln W_1}{\\partial U_1}\\right)_{N_1}
=
\\left(\\frac{\\partial\\ln W_2}{\\partial U_2}\\right)_{N_2}.
}
$

This derivation suggests that the logarithmic sensitivity of the count to the total attribute value is an important property of a system. We give this quantity a name.

## 4. The counting slope

For a system with fixed particle number $N$, define the **counting slope**

$
\\boxed{
\\gamma(N,U)
=
\\left(\\frac{\\partial\\ln W(N,U)}{\\partial U}\\right)_N.
}
$

The derivative is taken at fixed particle number. The counting slope has units reciprocal to the units of $U$. For a small change $dU$,

$
d\\ln W=\\gamma\\,dU,
$

so it measures the logarithmic change in the number of assignments per unit change in the total attribute value.

In terms of this named quantity, the condition just derived becomes

$
\\boxed{\\gamma_1(N_1,U_1)=\\gamma_2(N_2,U_2).}
$

Thus **the counting slopes of two systems are equal at an interior maximum of the number of combined assignments**. This equality is a necessary stationary-point condition. To establish that the point is a maximum, one must also check curvature or compare the allowed allocations. If each $\\ln W_i(U_i)$ is concave, their sum under the fixed-total constraint is concave, and an interior stationary point is a global maximum. Without such a condition, equality of slopes alone does not rule out a minimum or another stationary point.

The counting slope depends on the system and its current total; it is not a fixed label attached to the system. Its sign has a direct meaning for the isolated counting function: a positive slope means that increasing $U$ locally increases $W$, while a negative slope means that increasing $U$ locally decreases $W$. A zero slope means that $W$ is locally stationary.

### The exact discrete counterpart

The original counting framework is finite and discrete, so a derivative need not exist. For an allowed increment $\\Delta U>0$, define

$
\\gamma_{\\Delta U}^{+}(N,U)
=
\\frac{1}{\\Delta U}
\\ln\\left[
\\frac{W(N,U+\\Delta U)}{W(N,U)}
\\right],
$

and

$
\\gamma_{\\Delta U}^{-}(N,U)
=
\\frac{1}{\\Delta U}
\\ln\\left[
\\frac{W(N,U)}{W(N,U-\\Delta U)}
\\right].
$

These finite counting slopes are defined only when the totals in their arguments are attainable and the corresponding counts are nonzero. They need not be equal at finite $N$. When allowed increments become small and the counting function admits a smooth interpolation, they approach the derivative $\\gamma(N,U)$.

For discrete totals, the exact test is a comparison of count ratios for every allowed transfer. Equality of derivative-based counting slopes is the smooth description, not a replacement for that finite test.

## 5. Which way does \(U\) tend to move?

The counting slope also tells us which direction of transfer increases the number of combined assignments.

Suppose a small amount \(\delta U>0\) is transferred from system 1 to system 2. The new totals are

$$
U_1'=U_1-\delta U,\qquad
U_2'=U_2+\delta U.
$$

The change in the logarithm of the combined count is, to first order,

$$
\begin{aligned}
\delta\ln W_{\mathrm{tot}}
&=
\gamma_1(-\delta U)+\gamma_2(\delta U)\\
&=(\gamma_2-\gamma_1)\delta U.
\end{aligned}
$$

There are three cases.

1. **If \(\gamma_1>\gamma_2\):** transferring \(U\) from system 1 to system 2 increases the number of combined assignments.
2. **If \(\gamma_1<\gamma_2\):** transferring \(U\) from system 2 to system 1 increases the number of combined assignments.
3. **If \(\gamma_1=\gamma_2\):** there is no first-order increase in the combined count for a small transfer in either direction.

In this precise counting sense, \(U\) is favoured to move from the system with the larger counting slope to the system with the smaller counting slope. The direction of increasing combined count is therefore determined by the difference of the two slopes.

This statement should not be confused with a law for the actual rate of transfer. To calculate a rate, one would need additional information about how exchanges occur and how often each allowed change is attempted. The counting argument determines which direction has the larger number of compatible combined assignments, not how quickly the systems approach the most numerous allocation.

### What does equal flow in the two directions mean?

At the maximum, there is no allowed direction in which a small transfer increases the combined count to first order. In the smooth interior case this is expressed by equal counting slopes. If an exchange mechanism permits moves in both directions, the equilibrium allocation has no net preference for one direction in the counting description.

Equal gross rates of transfer from 1 to 2 and from 2 to 1 are a stronger, dynamical statement. They follow only after specifying suitable transition rules. They are not implied by the static counting argument alone. We therefore use equilibrium here to mean the maximum-count allocation, with no preferred direction of transfer as diagnosed by the counting slope.

## 6. The exact finite condition for two systems

For finite systems, the allowed totals may be discrete, and a transfer may be possible only in certain increments. The exact condition can be written without derivatives.

Consider an allowed transfer of size \(\Delta U>0\) from system 1 to system 2. The ratio of the new combined count to the old combined count is

$$
R_{1\to2}(\Delta U)
=
\frac{
W_1(U_1-\Delta U)W_2(U_2+\Delta U)
}{
W_1(U_1)W_2(U_2)
}.
$$

The transfer increases the combined count if and only if

$$
R_{1\to2}(\Delta U)>1.
$$

Equivalently,

$$
\frac{1}{\Delta U}
\ln\left[
\frac{W_1(U_1)}{W_1(U_1-\Delta U)}
\right]
<
\frac{1}{\Delta U}
\ln\left[
\frac{W_2(U_2+\Delta U)}{W_2(U_2)}
\right].
$$

In terms of the finite slopes defined earlier, this is

$$
\boxed{
\gamma_{\Delta U,1}^{-}(U_1)
<
\gamma_{\Delta U,2}^{+}(U_2).
}
$$

The exact finite equilibrium condition is that no allowed transfer, in either direction, increases the combined count. Thus, for every allowed positive step \(\Delta U\),

$$
R_{1\to2}(\Delta U)\leq1
\quad\text{and}\quad
R_{2\to1}(\Delta U)\leq1,
$$

where the second ratio is defined by reversing the transfer. A global maximum must, in addition, have a count at least as large as that of every other allowed allocation, not merely its immediate neighbours.

When the allowed increments are small and the counting functions are smooth, the finite-slope inequalities reduce to the derivative condition \(\gamma_1=\gamma_2\). This is why equality of counting slopes is the appropriate smooth description, while the ratio test is the exact finite one. If the starting framework uses nonzero tolerance windows rather than exact totals, the exact combined count must additionally enforce conservation across the actual totals inside those windows; it is not generally the simple product of the two window counts.

## 7. Extension to $m$ systems

Consider $m$ systems. The particle number $N_i$ of each system is fixed, and system $i$ has total value $U_i$ and count $W_i(N_i,U_i)$. The systems can exchange the same attribute $U$, subject to conservation:

$$
\\sum_{i=1}^{m}U_i=U_{\\mathrm{tot}}.
$$

An assignment of the combined collection is formed by choosing one assignment independently from each system. At a specified allocation, the number of combined assignments is therefore

$$
\\boxed{
W_{\\mathrm{tot}}(U_1,\\ldots,U_m)
=
\\prod_{i=1}^{m}W_i(N_i,U_i).
}
$$

Counting equilibrium is found by maximizing this product subject to the one conservation constraint. Equivalently, maximize its logarithm,

$$
L(U_1,\\ldots,U_m)
=
\\sum_{i=1}^{m}\\ln W_i(N_i,U_i),
\\qquad
\\sum_{i=1}^{m}U_i=U_{\\mathrm{tot}}.
$$

Introduce a Lagrange multiplier $\\alpha$ for the fixed-total constraint. At an interior stationary point,

$$
\\frac{\\partial}{\\partial U_i}
\\left[
\\sum_{j=1}^{m}\\ln W_j(N_j,U_j)
-
\\alpha\\left(\\sum_{j=1}^{m}U_j-U_{\\mathrm{tot}}\\right)
\\right]
=0
$$

for every $i$. Hence

$$
\\left(\\frac{\\partial\\ln W_i}{\\partial U_i}\\right)_{N_i}
=\\alpha.
$$

Using the counting slope defined above, this gives

$$
\\boxed{
\\gamma_1=\\gamma_2=\\cdots=\\gamma_m=\\alpha.
}
$$

The same result follows by transferring a small amount from any one system to any other: the first-order change in the logarithm of the combined count must vanish for every such pairwise transfer. The Lagrange multiplier makes clear that there is one common value shared by all systems at an interior stationary allocation.

As in the two-system case, stationarity alone does not prove a maximum. Concavity of $L$ on the allowed constraint surface is sufficient for a global maximum; strict concavity gives uniqueness. For exact discrete totals, one must compare the combined-count product for all allowed allocations (or use the corresponding finite-transfer tests). If only certain pairwise transfers are permitted by the exchange mechanism, the allowed set of allocations must reflect those restrictions.

## 8. If two systems already have the same counting slope

We can now address the converse question. Suppose two systems have fixed particle numbers and initial totals \(U_1\) and \(U_2\), and suppose

$$
\gamma_1(N_1,U_1)=\gamma_2(N_2,U_2).
$$

Does bringing them into \(U\)-interaction change their totals?

Consider the combined logarithmic count as a function of a possible transfer \(x\) from system 2 to system 1:

$$
G(x)
=
\ln W_1(U_1+x)+\ln W_2(U_2-x).
$$

The initial allocation corresponds to \(x=0\). Differentiating,

$$
G'(x)
=
\gamma_1(N_1,U_1+x)
-
\gamma_2(N_2,U_2-x).
$$

At the initial allocation,

$$
G'(0)=\gamma_1(N_1,U_1)-\gamma_2(N_2,U_2)=0.
$$

Therefore the initial allocation is a stationary point of the combined count.

To conclude that it is the equilibrium allocation, we need a stability condition. A sufficient condition is that each logarithmic count is concave:

$$
\frac{\partial^2\ln W_i}{\partial U_i^2}\leq0.
$$

Then

$$
G''(x)
=
\frac{\partial^2\ln W_1}{\partial U_1^2}
+
\frac{\partial^2\ln W_2}{\partial U_2^2}
\leq0.
$$

Hence \(G(x)\) is concave. Since its derivative vanishes at \(x=0\), the initial allocation is a global maximum over the allowed interval. Bringing the systems into \(U\)-interaction therefore does not change their most numerous allocation of \(U\).

If the concavity is strict, the maximum is unique. If the logarithmic counts have flat portions, there may be other allocations with the same maximum count.

This qualification is important: equality of counting slopes by itself gives a stationary allocation, not necessarily a maximum. For example, consider smooth positive counting functions with \(\ln W_1(U)=U^2\) and \(\ln W_2(U)=U^2\), on an allowed interval containing zero. At the allocation \(U_1=U_2=0\), the two slopes are equal (both zero), but at fixed combined total zero the logarithm of the combined count after a transfer \(x\) is

$
G(x)=x^2+(-x)^2=2x^2.
$

Thus the initial allocation is a minimum, not a maximum. This simple example illustrates why a curvature or global-count comparison is essential; it is an illustration of the calculus, not a claim that these functions arise from the particular multinomial model in the earlier chapter.

For a finite discrete system, the corresponding statement is that no allowed transfer increases the product \(W_1W_2\). Equality of a pair of finite slopes for one step alone is not enough to establish this for every possible transfer.

## 9. Summary of the results

1. For two independent systems at specified totals, the number of combined assignments is the product:
   $$
   W_{\mathrm{tot}}=W_1(U_1)W_2(U_2).
   $$
2. Counting equilibrium is defined as an allowed allocation that maximizes this product at fixed combined total.
3. The counting slope is
   $$
   \gamma(N,U)=
   \left(\frac{\partial\ln W(N,U)}{\partial U}\right)_N.
   $$
   It measures the logarithmic change in the number of assignments per unit change in \(U\), at fixed \(N\).
4. At an interior equilibrium allocation for two systems,
   $$
   \gamma_1=\gamma_2.
   $$
5. If \(\gamma_1>\gamma_2\), a small transfer from system 1 to system 2 increases the combined count. The preferred direction is from smaller counting slope to larger counting slope.
6. For a finite discrete system, exact equilibrium is determined by comparing the products of counts before and after every allowed transfer. Derivative equality is the smooth limiting condition.
7. For \(m\) systems that can exchange the same conserved attribute, all counting slopes are equal at an interior maximum:
   $$
   \gamma_1=\gamma_2=\cdots=\gamma_m.
   $$
8. If two systems initially have equal counting slopes and their logarithmic counts are concave, their initial allocation is already a maximum-count allocation. Equality of slopes without a stability condition establishes only stationarity.
9. Counting identifies the preferred allocation and the direction in which the number of combined assignments increases. It does not determine exchange rates or the detailed time evolution.

## Questions

1. Two systems have counts \(W_1(U_1)\) and \(W_2(U_2)\), with \(U_1+U_2\) fixed. Starting from the product rule for the combined count, derive the equality of counting slopes at an interior maximum.
2. Explain why the derivative of \(\ln W_2(U_{\mathrm{tot}}-U_1)\) with respect to \(U_1\) carries a minus sign.
3. If \(\gamma_1>\gamma_2\), which direction of transfer increases the combined count? Show this using a small transfer \(\delta U\).
4. Why does equality of counting slopes establish a stationary allocation but not, by itself, prove that the allocation is a maximum?
5. Formulate the exact finite-transfer condition for two systems when only transfers in integer multiples of a fixed increment are allowed.
6. Extend the maximization argument to three systems and show that all three counting slopes must be equal at an interior maximum.
7. Explain why the counting argument alone cannot determine how quickly two systems approach their maximum-count allocation.

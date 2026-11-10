# Ising Model and Ferromagnetism

## 1. Physical question

An ideal paramagnet made of independent two-state moments has a smooth magnetization response, but it cannot explain spontaneous magnetic order caused by interactions between moments. How can local interactions produce a collective phase transition?

The Ising model is a minimal statistical-mechanical model of this phenomenon. It replaces each magnetic moment with a two-valued spin and allows neighbouring spins to interact.

## 2. The microscopic model

Place spins $s_i=\pm1$ on the sites of a lattice. The Hamiltonian is

$$
\boxed{H=-J\sum_{\langle i,j\rangle}s_is_j-h\sum_i s_i.}
$$

The first sum runs over neighbouring pairs, $J$ is the interaction strength, and $h$ is an external field measured in energy units. For $J>0$, neighbouring parallel spins lower the interaction energy, so the interaction favours alignment. The field term favours spins aligned with $h$.

For $N$ spins, the canonical partition function is

$$
Z_N=\sum_{\{s_i=\pm1\}}e^{-\beta H(\{s_i\})},
\qquad \beta=\frac{1}{k_BT}.
$$

There are $2^N$ possible spin configurations. Unlike the independent-spin paramagnet, the energy of a spin depends on its neighbours, so the sum generally does not factor into $N$ identical one-spin partition functions.

## 3. Energy versus entropy

At high temperature, thermal fluctuations make many configurations accessible, and the average magnetization tends to vanish when $h=0$. At low temperature with $J>0$, aligned configurations have lower energy and can dominate. The central question is how this competition changes with temperature.

Define the magnetization per spin as

$$
m=\frac{1}{N}\sum_i\langle s_i\rangle.
$$

With no external field, the Hamiltonian is unchanged when every spin is reversed. Therefore a finite system in exact equilibrium has zero average magnetization at $h=0$, unless a symmetry-breaking convention is introduced. Spontaneous magnetization refers to the thermodynamic limit in which the system can select one of two symmetry-related ordered states as the field is taken to zero.

## 4. Mean-field approximation

### 4.1 The difficulty and the idea

In $H$, the terms that contain a given spin $s_i$ are $-s_i\big(h+J\sum_{j\sim i}s_j\big)$, where $j\sim i$ means that $j$ is a nearest neighbour of $i$. Spin $i$ therefore feels a **local field**

$$
h_i=h+J\sum_{j\sim i}s_j ,
$$

which fluctuates because its neighbours do. The partition function is hard to evaluate precisely because every spin's field depends on other spins that are themselves fluctuating.

**Mean-field theory replaces each neighbouring spin in the local field by its average value.** For a uniform system with $q$ nearest neighbours per site, write $m=\langle s_j\rangle$ (the same for every site). Then $h_i\to h_{\mathrm{eff}}=h+qJm$. The approximation is exact if the neighbours do not fluctuate; its error comes entirely from fluctuations, which the next subsection makes precise.

### 4.2 The approximation stated precisely

Let $m=\langle s_i\rangle$ be the mean spin, taken to be the same on every site, and write each spin as its mean plus a fluctuation,

$$
s_i=m+\delta s_i,\qquad \langle\delta s_i\rangle=0 .
$$

The following identity is exact:

$$
s_is_j=m(s_i+s_j)-m^2+\delta s_i\,\delta s_j .
$$

Mean-field theory drops the last term, the product of the fluctuations of two neighbouring spins. Equivalently, it replaces $\langle s_is_j\rangle=m^2+\langle\delta s_i\,\delta s_j\rangle$ by $\langle s_i\rangle\langle s_j\rangle=m^2$, so it **neglects correlations between neighbouring spins**.

A lattice of $N$ sites with $q$ neighbours each has $Nq/2$ nearest-neighbour bonds, and each spin belongs to $q$ bonds (boundary effects are ignored). Hence $\sum_{\langle i,j\rangle}(s_i+s_j)=q\sum_i s_i$. Substituting the identity into $H$ gives the exact relation $H=H_{\mathrm{MF}}-J\sum_{\langle i,j\rangle}\delta s_i\,\delta s_j$, where

$$
H_{\mathrm{MF}}=\frac{NqJ}{2}m^2-(h+qJm)\sum_{i=1}^{N}s_i .
$$

Mean-field theory approximates $H$ by $H_{\mathrm{MF}}$. In $H_{\mathrm{MF}}$ the spins are independent, each in the effective field $h_{\mathrm{eff}}=h+qJm$, with $m$ treated as a fixed number that is determined afterwards. The partition function factorizes:

$$
Z_{\mathrm{MF}}=e^{-\beta NqJm^2/2}\,\big[2\cosh(\beta h_{\mathrm{eff}})\big]^N .
$$

For one spin the probability of $s=\pm1$ is $e^{\beta s h_{\mathrm{eff}}}/[2\cosh(\beta h_{\mathrm{eff}})]$, so

$$
\langle s\rangle=\frac{e^{\beta h_{\mathrm{eff}}}-e^{-\beta h_{\mathrm{eff}}}}{e^{\beta h_{\mathrm{eff}}}+e^{-\beta h_{\mathrm{eff}}}}=\tanh(\beta h_{\mathrm{eff}}).
$$

The number $m$ was introduced as the average spin, so it must equal $\langle s\rangle$. This **self-consistency condition** determines $m$:

$$
\boxed{m=\tanh\!\left(\frac{h+qJm}{k_BT}\right).}
$$

It is nonlinear because the field that produces the magnetization depends on the magnetization. This feedback is what allows $m\neq0$ at $h=0$.

### 4.3 Why this is the best uncorrelated approximation

Self-consistency alone does not say which solution to choose when there are several. A variational argument does.

For any probability distribution $\rho$ over spin configurations, define

$$
F[\rho]=\langle H\rangle_\rho+k_BT\sum_{\{s\}}\rho\ln\rho .
$$

If $\rho_B=e^{-\beta H}/Z$ is the Boltzmann distribution and $F=-k_BT\ln Z$, then

$$
F[\rho]=F+k_BT\sum_{\{s\}}\rho\ln\frac{\rho}{\rho_B}\;\ge\;F ,
$$

because the last sum (the relative entropy) is never negative, and it vanishes only for $\rho=\rho_B$. The true free energy is therefore the minimum of $F[\rho]$, and minimizing over a restricted family of $\rho$ gives the best approximation within that family.

Take the family of **independent** spins, $\rho_m=\prod_i\tfrac12(1+m s_i)$, in which each spin has $\langle s_i\rangle=m$ and no correlations. Then $\langle s_is_j\rangle=m^2$ for $i\neq j$, so $\langle H\rangle=-N\big(\tfrac{qJ}{2}m^2+hm\big)$, and the entropy is that of $N$ independent two-state spins. The free energy per spin is

$$
f(m)=-\frac{qJ}{2}m^2-hm+k_BT\left[\frac{1+m}{2}\ln\frac{1+m}{2}+\frac{1-m}{2}\ln\frac{1-m}{2}\right].
$$

Setting $f'(m)=0$ gives $-qJm-h+k_BT\,\operatorname{artanh}m=0$, that is,

$$
m=\tanh\!\big[\beta(h+qJm)\big],
$$

the same self-consistency equation. The physical solution is the global minimum of $f(m)$. (On a solution, $f(m)=qJm^2/2-k_BT\ln[2\cosh(\beta h_{\mathrm{eff}})]$, the free energy of the decoupled Hamiltonian in Section 4.2.)

## 5. What mean-field theory predicts

### 5.1 A critical temperature

Set $h=0$. Using $\tfrac12[(1+m)\ln(1+m)+(1-m)\ln(1-m)]=\tfrac{m^2}{2}+\tfrac{m^4}{12}+\tfrac{m^6}{30}+\cdots$,

$$
f(m)=-k_BT\ln2+\tfrac12\,(k_BT-qJ)\,m^2+\frac{k_BT}{12}m^4+\cdots .
$$

The sign of the $m^2$ coefficient decides the behaviour. More rigorously, $f$ is even in $m$ and

$$
f''(m)=\frac{k_BT}{1-m^2}-qJ
$$

increases with $|m|$ on $-1<m<1$, so:

- **If $k_BT\ge qJ$:** $f''(0)\ge0$, so $f''>0$ for $m\ne0$ and $f$ has a single minimum at $m=0$. The only solution is $m=0$.
- **If $k_BT<qJ$:** $f''(0)<0$, so $m=0$ is a local maximum. Since $f'(m)\to+\infty$ as $m\to1$, there is exactly one positive zero $m^*$ of $f'$, and by symmetry a negative one $-m^*$. These are two equal minima, the two symmetry-related ordered states.

Therefore

$$
\boxed{k_BT_c^{\mathrm{MF}}=qJ.}
$$

Panel (a) below shows the same result graphically. The right-hand side $\tanh(mT_c/T)$ has slope $T_c/T$ at the origin. For $T>T_c$ it stays below the line $y=m$, so only $m=0$ is a solution. For $T<T_c$ it starts above the line and, being bounded by 1, crosses it once at $m^*>0$.

![Mean-field Ising model at zero field. Panel (a): the curve y = tanh(m Tc/T) meets the line y = m only at the origin above Tc, and at a second point (marked) below Tc. Panel (b): the free energy per spin has one minimum at m = 0 above Tc and two minima at plus or minus m* below Tc.](images/ising_mean_field.svg)

### 5.2 Spontaneous magnetization below the critical temperature

Near $T_c$, keep the first two terms of $f'(m)=0$: $(k_BT-qJ)\,m+\tfrac13k_BT\,m^3\simeq0$. Then

$$
m^2\simeq3\,\frac{T_c-T}{T}\approx3\left(1-\frac{T}{T_c}\right),
\qquad
m\approx\pm\sqrt3\,\Big(1-\frac{T}{T_c}\Big)^{1/2}.
$$

The magnetization grows continuously from zero, so the transition is continuous, with exponent $1/2$ in mean-field theory. At low temperature $m\to1-2e^{-2T_c/T}$, so the spins are almost completely aligned.

For $T<T_c$ and a small field, the minimum of $f$ with the same sign as $h$ is the global one. The spontaneous magnetization is the limit $h\to0^+$ in the thermodynamic limit, which is how Section 3 defined it.

### 5.3 Above the critical temperature: the Curie–Weiss law

For $T>T_c$ and small $h$, $m$ is small and $\tanh x\approx x$ gives $m=\beta(h+qJm)$, so

$$
m=\frac{h}{k_B(T-T_c)} .
$$

This is the **Curie–Weiss law**: the susceptibility diverges as $T\to T_c^{+}$. For $J=0$ we have $T_c=0$ and the self-consistency equation becomes $m=\tanh(\beta h)$, the independent-spin paramagnet, with the Curie law $m\approx h/k_BT$ at small field. Mean-field theory therefore reduces correctly to the paramagnet when the interaction is switched off.

## 6. How accurate is mean-field theory?

Mean-field theory is exact only when the neglected term $\langle\delta s_i\,\delta s_j\rangle$ vanishes. The local field on a spin is a sum of $q$ neighbouring spins, so its fluctuations are small compared with its average when $q$ is large. Mean-field theory becomes exact in the limit of infinite-range interactions (every spin coupled to every other with strength $J/N$), and it improves with dimension and coordination number. It overestimates $T_c$ because fluctuations make order harder to maintain than the average-field picture suggests.

| Lattice | $q$ | $k_BT_c/J$, mean field | $k_BT_c/J$, exact or numerical |
|---|---|---|---|
| Chain (1D) | 2 | 2 | 0 (no order at $T>0$; Ising 1925) |
| Square (2D) | 4 | 4 | $2/\ln(1+\sqrt2)\approx2.269$ (Onsager 1944) |
| Simple cubic (3D) | 6 | 6 | $\approx4.51$ (Monte Carlo) |

The critical exponents are also not those observed in two and three dimensions (for example, the exact two-dimensional magnetization exponent is $1/8$, not $1/2$). Mean-field exponents become correct above four dimensions. A quantitative treatment of the critical region needs the theory of fluctuations (the renormalization group), which is beyond this chapter.

## 7. What the model teaches us

The Ising model demonstrates that collective behaviour can emerge from simple local interactions. Its key ingredients are a large number of degrees of freedom, a coupling that favours alignment, and thermal fluctuations that compete with that tendency.

It also clarifies the difference between an independent paramagnet and an interacting magnet. Independent spins respond to an external field but do not spontaneously order in this model. Interactions make the response of one spin depend on its surroundings and allow a collective ordered phase.

Mean-field theory is useful but not exact in general. In low dimensions, spatial correlations and fluctuations can be decisive; in particular, the one-dimensional nearest-neighbour Ising model with finite-range interactions has no finite-temperature spontaneous magnetization at zero field. A quantitative description of a specific material also requires more realistic microscopic interactions and degrees of freedom.

## Summary

The Ising Hamiltonian couples neighbouring two-state spins. Mean-field theory neglects correlations between neighbouring spin fluctuations, so each spin sees the average field $h+qJm$. This gives the self-consistency equation $m=\tanh[(h+qJm)/(k_BT)]$, which is also the stationarity condition of the best uncorrelated free energy $f(m)$. At zero field it predicts a continuous transition at $k_BT_c^{\mathrm{MF}}=qJ$, with $m\approx\pm\sqrt3\,(1-T/T_c)^{1/2}$ below it and the Curie–Weiss law $m=h/[k_B(T-T_c)]$ above it. It overestimates $T_c$ and is qualitatively wrong in one dimension, but improves as the number of neighbours grows.

## Review questions

1. What is the physical meaning of each term in the Ising Hamiltonian?
2. Why does the partition function generally fail to factorize into independent single-spin terms?
3. Derive the mean-field self-consistency equation for $m$ from the identity $s_is_j=m(s_i+s_j)-m^2+\delta s_i\,\delta s_j$.
4. Explain why mean-field theory is equivalent to neglecting correlations between neighbouring spins.
5. Use the free energy $f(m)$ to show that $m=0$ is the only minimum for $T>T_c$ and that there are two minima for $T<T_c$.
6. Derive $m\approx\sqrt3\,(1-T/T_c)^{1/2}$ and the Curie–Weiss law.
7. Why can a finite zero-field system have zero average magnetization even when the thermodynamic system exhibits spontaneous order?
8. Why is mean-field theory more accurate for larger $q$, and why does it fail in one dimension?

## References and further reading

- P. Weiss, "L'hypothèse du champ moléculaire et la propriété ferromagnétique", *J. Phys. Théor. Appl.* **6**, 661 (1907). The original molecular-field theory.
- E. Ising, "Beitrag zur Theorie des Ferromagnetismus", *Z. Phys.* **31**, 253 (1925). The exact one-dimensional solution.
- L. Onsager, "Crystal statistics. I. A two-dimensional model with an order–disorder transition", *Phys. Rev.* **65**, 117 (1944). The exact two-dimensional solution.
- A. M. Ferrenberg and D. P. Landau, "Critical behavior of the three-dimensional Ising model: a high-resolution Monte Carlo study", *Phys. Rev. B* **44**, 5081 (1991). The three-dimensional $T_c$ in the table.
- R. K. Pathria and P. D. Beale, *Statistical Mechanics* (Elsevier). Ising model and mean-field theory.
- J. M. Yeomans, *Statistical Mechanics of Phase Transitions* (Oxford University Press, 1992). A short, clear treatment of mean-field theory of the Ising model.
- P. M. Chaikin and T. C. Lubensky, *Principles of Condensed Matter Physics* (Cambridge University Press, 1995). Mean-field theory and its range of validity.
- R. P. Feynman, *Statistical Mechanics: A Set of Lectures* (Benjamin, 1972). The variational principle used in Section 4.3.
- J. P. Sethna, *Statistical Mechanics: Entropy, Order Parameters, and Complexity* (Oxford University Press, 2006). Freely available from the author.

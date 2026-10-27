# Statistical Mechanics — Lecture 1
## Counting states

**Lecturer:** John Preskill  
**Course:** Caltech — Physics 12c, Statistical Mechanics  
**Video:** https://www.youtube.com/watch?v=s7chipjxBFk (lecture recorded 29 March 2011)  
**Basis:** The video could not be accessed and no transcript was available. These notes are based on a typed set of student notes (by Sam Elder) from the 2010 offering of the same course, hosted on Preskill's course page, which covers the corresponding first lecture, "Counting states". They also use the title and description of the video. The 2011 lecture may differ in order and examples, and the student notes are reported to contain typographical errors. The equations below were re-derived and checked.

---

## 0. Summary

This lecture introduces the two halves of thermal physics and then makes the first quantitative step in statistical mechanics: counting microstates.

- A **microstate** is a complete microscopic specification. A **macrostate** is specified by a few macroscopic quantities, such as the energy.
- With the **principle of equal a priori probability**, every accessible microstate is equally likely, so probabilities come from counting.
- A model system of $N$ two-state spins (equivalent to $N$ coin flips) is counted exactly with binomial coefficients.
- Stirling's approximation turns the exact count into a **Gaussian** of width $\sim\sqrt N$ around the mean.
- Because the relative width shrinks as $1/\sqrt N$, large deviations from average behaviour are astronomically unlikely for a macroscopic system.

Entropy and temperature are **not** introduced in this lecture. They begin in the next one.

## 1. Thermodynamics and statistical mechanics

Thermal physics has two complementary parts.

**Thermodynamics** deals with heat, energy, work, temperature and above all **entropy**. It is summarized in a small number of laws, and it brings in **irreversibility** (the arrow of time), which does not appear in Newton's laws or the Schrödinger equation. Its mathematics is mostly total and partial derivatives.

**Statistical mechanics** tries to derive thermodynamic behaviour from the microscopic laws. Its tools are probability theory, applied to a very large number of degrees of freedom, and combinatorics (counting).

Why probability? A box of gas holds of order Avogadro's number of molecules. Following each one is impossible. Even if we could, we would still average over microscopic detail to predict anything we can observe. So we describe the system by macroscopic quantities (energy, volume) and treat the microscopic state statistically.

The central point of the course is that **large deviations from average behaviour are extraordinarily unlikely**. The standard example is all the air in a room spontaneously collecting in one corner.

## 2. Microstates, macrostates and equal probability

Specify a macrostate by macroscopic constraints, for example an energy in the window $[E,E+\Delta E]$. Count the microstates consistent with it. Typically there are still very many.

**Principle of equal a priori probability.** Microstates with (approximately) the same energy are equally likely, because there is no reason to prefer one over another. This is an assumption. It is hard to justify fully, but it is where the theory starts.

If $\Omega$ microstates are accessible,

$$
P(\text{a given microstate})=\frac1\Omega .
$$

The probability of any macrostate is then (number of microstates in it) $/\,\Omega$.

In quantum mechanics the energy levels are discrete, so counting microstates is natural. In classical mechanics it is less natural, since states form a continuum.

## 3. First example: coin flips

For a fair coin, the probabilities of the number of heads are:

| Flips | Number of heads | Probabilities |
|---|---|---|
| 1 | 0, 1 | $\tfrac12,\ \tfrac12$ |
| 2 | 0, 1, 2 | $\tfrac14,\ \tfrac12,\ \tfrac14$ |
| 3 | 0, 1, 2, 3 | $\tfrac18,\ \tfrac38,\ \tfrac38,\ \tfrac18$ |

For $N\gg1$ flips the distribution approaches a **Gaussian** with mean $N/2$ and standard deviation proportional to $\sqrt N$. The width grows more slowly than the mean, so relative fluctuations shrink.

This is an example of the **central limit theorem**: the sum of many independent random variables is distributed approximately as a Gaussian, whose width relative to the mean shrinks as the number of terms grows.

**An illustration (from the video's description).** Flip a fair coin $10^{22}$ times, winning or losing a penny each time. The net result typically has size $\sqrt N=10^{11}$ pennies, about a billion dollars. A net win of ten billion dollars is ten standard deviations out and is effectively impossible.

## 4. Second example: a paramagnet of $N$ spins

Take $N$ spins, each pointing up ($\uparrow$) or down ($\downarrow$) with equal probability. Mathematically this is the same problem as coin flipping.

### 4.1 Definitions

- $N_\uparrow,\ N_\downarrow$: numbers of up and down spins, with $N=N_\uparrow+N_\downarrow$.
- **Spin excess** $2s=N_\uparrow-N_\downarrow$. Flipping one spin changes $2s$ by 2. Then

$$
N_\uparrow=\frac N2+s,\qquad N_\downarrow=\frac N2-s .
$$

- Each spin has magnetic moment $m$, so the total magnetization is

$$
M=(N_\uparrow-N_\downarrow)\,m=2s\,m .
$$

- In a magnetic field $B$ pointing up, $E_\uparrow=-mB$ and $E_\downarrow=+mB$, so the total energy is

$$
E=-mB\,(N_\uparrow-N_\downarrow)=-(2s)\,mB .
$$

The energy is fixed by $s$, so specifying the macrostate by the energy is the same as specifying $s$.

### 4.2 Exact count

Let $g(N,s)$ be the number of microstates with spin excess $2s$. The total number of microstates is $2^N$, because each spin has two states. The number with $N_\uparrow=N/2+s$ is a binomial coefficient:

$$
\boxed{g(N,s)=\binom{N}{N_\uparrow}=\frac{N!}{\left(\frac N2+s\right)!\,\left(\frac N2-s\right)!}} .
$$

Interpretation: there are $N!$ orderings of the spins. Permuting the up spins among themselves, or the down spins among themselves, gives the same configuration, so divide by $N_\uparrow!\,N_\downarrow!$.

## 5. Stirling's approximation

For large $N$,

$$
N!\approx\sqrt{2\pi N}\;N^{N}e^{-N}.
$$

The prefactor $\sqrt{2\pi N}$ needs a more careful argument. The exponential behaviour already follows from

$$
\ln N!=\sum_{k=1}^{N}\ln k\approx\int_1^N\ln k\,dk\approx N\ln N-N .
$$

## 6. The Gaussian approximation for $|s|\ll N$

Apply Stirling's formula to each of the three factorials in $g(N,s)$. The $-N$ terms in the exponentials cancel, because $N=N_\uparrow+N_\downarrow$. Ignoring the prefactors for now,

$$
\ln g\approx N\ln N-\Big(\frac N2+s\Big)\ln\Big(\frac N2+s\Big)-\Big(\frac N2-s\Big)\ln\Big(\frac N2-s\Big).
$$

Write $\frac N2\pm s=\frac N2(1\pm x)$ with $x=2s/N\ll1$. The terms linear in $s$ cancel, leaving

$$
\ln g\approx N\ln2-\frac N2\Big[(1+x)\ln(1+x)+(1-x)\ln(1-x)\Big].
$$

Using $\ln(1\pm x)\approx\pm x-\tfrac12x^2$, the bracket is

$$
(1+x)\Big(x-\tfrac{x^2}2\Big)+(1-x)\Big(-x-\tfrac{x^2}2\Big)\approx x^2 ,
$$

so

$$
\ln g\approx N\ln2-\frac N2x^2=N\ln2-\frac{2s^2}{N}.
$$

Including the Stirling prefactors,

$$
\boxed{g(N,s)\approx2^N\sqrt{\frac{2}{\pi N}}\;e^{-2s^2/N}} .
$$

This is a Gaussian centred at $s=0$. It falls to $1/e$ of its peak when $2s^2/N=1$, i.e. at $s\sim\sqrt{N/2}$.

## 7. The probability distribution

Divide by the total number of states, $2^N$:

$$
P(N,s)=\frac{g(N,s)}{2^N}\approx\sqrt{\frac2{\pi N}}\;e^{-2s^2/N}.
$$

**Normalization check.** Replace the finite sum over $s$ by an integral over all $s$. This changes almost nothing, because the tails near $s=\pm N/2$ are negligible. With $\int_{-\infty}^{\infty}e^{-Au^2}du=\sqrt{\pi/A}$ and $A=2/N$:

$$
\int_{-\infty}^{\infty}ds\,P(N,s)=\sqrt{\frac2{\pi N}}\sqrt{\frac{\pi N}2}=1 .
$$

The prefactor $\sqrt{2/\pi N}$ is exactly what normalization requires, which also confirms the $\sqrt{2\pi N}$ in Stirling's formula.

## 8. Mean and fluctuations

By symmetry, $\langle s\rangle=0$. Using $\int_{-\infty}^{\infty}u^2e^{-u^2}du=\sqrt\pi/2$ (here with $A=2/N$):

$$
\langle s^2\rangle=\frac N4,\qquad \big\langle(2s)^2\big\rangle=N .
$$

So the typical spin excess is of order $\sqrt N$, while the largest possible value is $N$. The **relative** size of the fluctuations is $1/\sqrt N$.

**Numbers for a macroscopic sample.** Take $N\sim10^{22}$ spins.

- A fully magnetized sample has $M\sim Nm\sim10^{22}\,m$.
- An unmagnetized sample typically has $|2s|\sim\sqrt N\sim10^{11}$, so $|M|\sim10^{11}\,m$. Next to $10^{22}\,m$ this is tiny, and an experimenter would measure $M\approx0$.
- A spin excess of $2s\approx10^{12}$ is about ten standard deviations out. Its probability is suppressed by

$$
\exp\!\Big[-\frac{2s^2}{N}\Big]=\exp\!\Big[-\frac{(10^{12})^2}{2\times10^{22}}\Big]=e^{-50}\sim10^{-22}.
$$

**The central idea of the lecture:** for a system with a huge number of degrees of freedom, average behaviour is an excellent description, because the probability of significant deviations is vanishingly small.

## 9. Review questions

1. What is the difference between a microstate and a macrostate? Give an example for the spin system.
2. What does the principle of equal a priori probability assert? Why is it an assumption?
3. Why does $g(N,s)=N!/[(N/2+s)!\,(N/2-s)!]$ count the microstates with spin excess $2s$?
4. In the Gaussian approximation, why do the terms linear in $s$ cancel?
5. Check that $P(N,s)$ is normalized to 1.
6. For $N=10^{22}$ spins, why is a spin excess of $10^{12}$ so unlikely?
7. How does the relative width of the distribution scale with $N$? Why does this make statistical mechanics predictive?

## 10. Known limitations of these notes

- The lecture video was not accessible, and these notes are based on typed student notes of the 2010 offering of the course. The recorded 2011 lecture may order or illustrate things differently.
- The derivation is the standard one. I re-derived the equations and found no errors in them, but I could not compare against the lecture itself.
- Lecture logistics and any announcements are omitted, as requested. Only the physics is included.
- These notes were generated with AI assistance and may contain omissions or errors.

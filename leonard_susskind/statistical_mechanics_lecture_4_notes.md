# Statistical Mechanics — Lecture 4

## The Boltzmann distribution, the partition function, and the ideal gas

**Lecturer:** Leonard Susskind\
**Course:** Stanford University — Statistical Mechanics\
**Video:** https://www.youtube.com/watch?v=rhFkYjaM5kE\
**Basis:** Notes prepared from a caption-based transcript of the lecture (via a third-party transcript page), not from a transcript supplied by the repository owner. Captions contain recognition errors, so some details may be wrong. Check equations against the video.

***

## 0. Summary

Lecture 3 posed a problem: maximize the entropy $S=-\sum\_i p\_i\ln p\_i$ subject to fixed normalization and fixed average energy. This lecture solves it.

* Lagrange multipliers give the **Boltzmann distribution** $p\_i=e^{-\beta E\_i}/Z$.
* The **partition function** $Z(\beta)=\sum\_i e^{-\beta E\_i}$ generates the thermodynamics: $E=-\partial\ln Z/\partial\beta$ and $S=\beta E+\ln Z$.
* Using $1/T=dS/dE$, the multiplier $\beta$ is identified as the inverse temperature.
* The partition function of a classical **ideal gas** is computed, giving $E=\tfrac32NT$. A uniform gravitational field is then added.

Units follow earlier lectures: $T$ is temperature in energy units ($k\_{\mathrm B}=1$). Restoring the constant, $\beta=1/(k\_{\mathrm B}T\_{\mathrm K})$.

## 1. Recap

Take a large collection of $N$ identical replicas of the system. Let $n\_i$ be the number of replicas in state $i$, and $p\_i=n\_i/N$.

* The number of arrangements is $W=N!/\prod\_i n\_i!$.
* With Stirling's approximation, $\ln W\approx NS$ where $S=-\sum\_i p\_i\ln p\_i$.
* The most probable distribution is the one that maximizes $S$ subject to the constraints.

## 2. The constraints

$$
\sum_i p_i=1,\qquad \sum_i p_iE_i=E ,
$$

where $E$ is the fixed average energy per system. (The total energy of the collection is $NE$.)

Control parameters such as volume, shape, or external fields are held fixed. They determine the energy levels $E\_i$, which are treated as given numbers.

## 3. Lagrange multipliers: deriving the Boltzmann distribution

Maximizing $S$ is the same as minimizing $-S=\sum\_i p\_i\ln p\_i$. Introduce one multiplier for each constraint, $\alpha$ and $\beta$, and form

$$
F=\sum_i p_i\ln p_i+\alpha\Big(\sum_i p_i-1\Big)+\beta\Big(\sum_i p_iE_i-E\Big).
$$

Set the derivative with respect to each $p\_i$ to zero. The constants $-\alpha$ and $-\beta E$ do not depend on $p\_i$ and drop out:

$$
\ln p_i+1+\alpha+\beta E_i=0
\;\Longrightarrow\;
p_i=e^{-(1+\alpha)}\,e^{-\beta E_i}.
$$

The factor $e^{-(1+\alpha)}$ is just a normalization constant, fixed by $\sum\_ip\_i=1$. Call it $1/Z$:

$$
\boxed{p_i=\frac{1}{Z}\,e^{-\beta E_i}} \qquad\text{(Boltzmann distribution)}.
$$

(The lecture's board work has a sign slip on $\alpha$ at this step. It does not matter, because $\alpha$ is absorbed into $Z$.)

**What $\beta$ does:** it sets how quickly probability falls off with energy.

* Large $\beta$: low-energy states dominate.
* Small $\beta$: probability spreads to high-energy states.

At this point $\beta$ is only a Lagrange multiplier. It is shown to be the inverse temperature in Section 6.

## 4. The partition function and the average energy

Normalization requires

$$
\boxed{Z(\beta)=\sum_i e^{-\beta E_i}} .
$$

$Z$ is more than a normalization constant: almost all thermodynamic information can be extracted from it.

The average energy fixes $\beta$:

$$
E=\sum_i p_iE_i=\frac{1}{Z}\sum_i E_i\,e^{-\beta E_i}.
$$

Since $\partial\_\beta e^{-\beta E\_i}=-E\_i e^{-\beta E\_i}$, this is a derivative of $Z$:

$$
\boxed{E=-\frac{1}{Z}\frac{\partial Z}{\partial\beta}=-\frac{\partial\ln Z}{\partial\beta}} .
$$

$E$ and $\beta$ determine each other, so either can be used as the independent variable.

Points from the question period:

* Changing a control parameter (volume, a field) changes the $E\_i$, and therefore $Z$.
* A further conserved quantity, such as total momentum, would add another constraint and another multiplier.

## 5. Entropy in terms of $Z$

From $p\_i=e^{-\beta E\_i}/Z$,

$$
\ln p_i=-\beta E_i-\ln Z .
$$

Substitute into $S=-\sum\_i p\_i\ln p\_i$ and use $\sum\_ip\_i=1$ and $\sum\_ip\_iE\_i=E$:

$$
\boxed{S=\beta E+\ln Z} .
$$

Note that $Z$ is a sum of exponentials, so $\ln Z$ does not break up into a sum of logarithms of the individual terms.

(The lecture remarks that $\ln Z$ is, up to a factor of temperature, the Helmholtz free energy: $F=-T\ln Z$. This is left for later.)

## 6. Identifying $\beta$ as the inverse temperature

The definition of temperature from Lecture 3 is $1/T=dS/dE$. Differentiate $S=\beta E+\ln Z$ with $\beta$ as the variable:

$$
dS=\beta\,dE+E\,d\beta+\frac{\partial\ln Z}{\partial\beta}\,d\beta
=\beta\,dE+\big(E-E\big)\,d\beta=\beta\,dE ,
$$

where $\partial\ln Z/\partial\beta=-E$ was used. Hence

$$
\frac{dS}{dE}=\beta
\;\Longrightarrow\;
\boxed{\beta=\frac1T} .
$$

(With $k\_{\mathrm B}$ restored, $\beta=1/k\_{\mathrm B}T\_{\mathrm K}$.)

**Equations of this lecture:**

$$
p_i=\frac{e^{-\beta E_i}}{Z},\quad
Z=\sum_ie^{-\beta E_i},\quad
E=-\frac{\partial\ln Z}{\partial\beta},\quad
S=\beta E+\ln Z,\quad
\beta=\frac1T .
$$

## 7. The ideal gas

**Model.** $N$ point particles in a box of volume $V$, with no interactions, so the energy is entirely kinetic. This is a good approximation for a dilute or weakly interacting gas.

**States.** A state is a point in the $6N$-dimensional phase space of positions and momenta, so the sum over states becomes an integral. With $3N$ momentum components $p\_n$,

$$
E=\sum_{n=1}^{3N}\frac{p_n^2}{2m}.
$$

**Partition function.**

$$
Z=\frac{1}{N!}\int d^{3N}x\;d^{3N}p\;\exp\!\Big(-\beta\sum_{n=1}^{3N}\frac{p_n^2}{2m}\Big).
$$

* The position integrals each run over the box, giving $V^N$.
* The momentum integral factorizes into $3N$ identical one-dimensional Gaussian integrals.

**The factor $1/N!$.** Classically it is a convention: it adds a constant to $\ln Z$ that disappears on differentiating with respect to $\beta$. In quantum mechanics it is essential, because identical particles carry no labels and leaving it out overcounts the states by $N!$.

**The Gaussian integral.** Let $q=\sqrt{\beta/2m},p$ and use $\int\_{-\infty}^{\infty}e^{-q^2}dq=\sqrt\pi$:

$$
\int_{-\infty}^{\infty}dp\;e^{-\beta p^2/2m}=\sqrt{\frac{2\pi m}{\beta}} .
$$

**Result.**

$$
\boxed{Z=\frac{V^N}{N!}\Big(\frac{2\pi m}{\beta}\Big)^{3N/2}} .
$$

With Stirling's approximation $N!\approx(N/e)^N$,

$$
\ln Z=N\ln\frac{eV}{N}+\frac{3N}{2}\ln\frac{2\pi m}{\beta}.
$$

**Energy.** Only the $\beta$-dependent term contributes to the derivative:

$$
E=-\frac{\partial\ln Z}{\partial\beta}=\frac{3N}{2\beta}
\;\Longrightarrow\;
\boxed{E=\tfrac32\,NT} .
$$

Each particle carries $\tfrac32T$, which is $\tfrac12T$ for each of the three directions of motion. This is **equipartition**, and it agrees with the result quoted in Lecture 2.

**Entropy** (left as an exercise in the lecture). Using $S=\beta E+\ln Z$ with $\beta E=\tfrac32N$:

$$
S=N\Big[\ln\frac VN+\frac32\ln(2\pi mT)+\frac52\Big].
$$

This worked result is added in these notes and is not taken from the lecture. Classically the argument of the logarithm is not dimensionless. A factor of $h^3$ per particle in the phase-space measure fixes this and only shifts $S$ by a constant.

## 8. Adding gravity

Add a potential energy $mgy$ for each particle, with $y$ the height above the floor of a box of base area $A$ and (assumed) infinite height.

* The $x$ and $z$ integrals give $A^N$.
* The $y$ integral for each particle is

$$
\int_0^\infty e^{-\beta mgy}\,dy=\frac{1}{\beta mg} .
$$

Then

$$
Z=\frac{1}{N!}\Big(\frac{A}{\beta mg}\Big)^N\Big(\frac{2\pi m}{\beta}\Big)^{3N/2},
$$

and the powers of $\beta$ combine to $\beta^{-5N/2}$. Therefore

$$
E=-\frac{\partial\ln Z}{\partial\beta}=\frac{5N}{2\beta}=\tfrac52NT .
$$

This is $\tfrac32T$ of kinetic energy plus $T$ of average gravitational potential energy per particle. The lecture guessed that the extra term was the potential energy and left the details for later; the integral above is my working from the lecture's setup, not a transcription.

## 9. Wrap-up and questions

The Boltzmann distribution is the equilibrium distribution: the one that maximizes entropy at fixed normalization and average energy.

From the question period:

* **Gravitational collapse and black holes.** Entropy keeps increasing until a limit set by the Bekenstein–Hawking entropy (the captions garble this passage).
* **Fluctuations.** The spread of the energy about its average follows from the second derivative of $\ln Z$ with respect to $\beta$ and is related to the specific heat. The lecture defers the derivation. The standard result in these units is

$$
\langle E^2\rangle-\langle E\rangle^2=\frac{\partial^2\ln Z}{\partial\beta^2}=T^2\,C_V ,
$$

but this is not derived in the lecture.

* Historically, fluctuations were central to showing that statistical mechanics applies to a finite number of atoms, not just to a continuum.

## 10. Homework mentioned

1. Compute the entropy of the ideal gas, and the entropy per particle.
2. Work out the partition function and energy for the gas in a gravitational field.
3. Derive the energy-fluctuation formula from second derivatives of $\ln Z$.

## 11. Review questions

1. Starting from the Lagrangian $F$, derive the Boltzmann distribution. Where does $Z$ come from?
2. Show that $E=-\partial\ln Z/\partial\beta$.
3. Derive $S=\beta E+\ln Z$.
4. Why does $dS=\beta,dE$ follow from $S=\beta E+\ln Z$? What identity makes the $d\beta$ terms cancel?
5. For the ideal gas, why do positions give $V^N$ and each momentum component a factor $\sqrt{2\pi m/\beta}$?
6. Why does the average energy of an ideal gas not depend on $V$ or on the particle mass?
7. In a gravitational field, why is the average energy per particle $\tfrac52T$ and not $\tfrac32T$?
8. Why is the factor $1/N!$ harmless in the classical energy calculation but essential in quantum mechanics?

## 12. Known limitations of these notes

* The source is an automatic caption transcript. Passages that were garbled, such as the Stirling step in the ideal gas, the sign of $\alpha$, and the black-hole remark, were interpreted or reworked from the lecture's setup.
* The lecture restarts its derivation of $\beta=1/T$ partway through. The notes give only the clean version.
* Not every aside or question-period exchange is included.
* Sections 7 (entropy) and 8 contain worked results added in these notes. They are marked as such.
* These notes were generated with AI assistance and may contain omissions or errors.

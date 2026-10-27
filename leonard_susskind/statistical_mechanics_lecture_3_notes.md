# Statistical Mechanics — Lecture 3

## Entropy, the laws of thermodynamics, and maximizing entropy

**Lecturer:** Leonard Susskind\
**Course:** Stanford University — Statistical Mechanics\
**Video:** https://www.youtube.com/watch?v=EmM1jOV1uSY\
**Basis:** Notes prepared from a caption-based transcript of the lecture (via a third-party transcript page), not from a transcript supplied by the repository owner. Captions contain recognition errors, so some details may be wrong. Check equations and the homework statement against the video.

***

## 0. Summary

This lecture sets up the probabilistic core of statistical mechanics.

* Entropy of a probability distribution is defined as $S=-\sum\_i p\_i\ln p\_i$.
* Temperature is introduced through $dE=T,dS$. With the second law, this gives the zeroth law: heat flows from hot to cold.
* A counting argument (replicas of a system, occupation numbers) shows that the most probable distribution is the one that maximizes $S$ subject to fixed total probability and fixed average energy.
* Stirling's approximation and Lagrange multipliers are developed as the tools for solving that problem.

The solution of the maximization problem, and with it the partition function, is **not** reached. It is deferred to the next lecture.

Units follow Lecture 2: $T$ is temperature in energy units, so $k\_{\mathrm B}$ does not appear.

## 1. Probability distributions and entropy

Consider a system with discrete states labelled $i$. Each state has an energy $E\_i$ and a probability $p\_i$.

$$
\sum_i p_i = 1, \qquad \langle E\rangle=\sum_i p_i E_i .
$$

The **entropy** of the distribution is

$$
\boxed{S=-\sum_i p_i\ln p_i } .
$$

Basic properties:

* Since $0\le p\_i\le 1$, each $\ln p\_i\le 0$, so each term $-p\_i\ln p\_i\ge 0$ and $S\ge 0$.
* If all the probability sits on one state (for example the ground state), $S=0$.
* Roughly, $e^{S}$ measures how many states carry significant probability. A broader distribution has larger entropy.

## 2. Entropy and average energy

Raising the average energy generally spreads probability over more states, so the distribution broadens and $S$ increases. For thermal-equilibrium distributions, $S$ increases monotonically with $\langle E\rangle$. This is not true of arbitrary distributions, so it is a property of equilibrium states, not of every probability distribution.

## 3. Thermal equilibrium

A system is in equilibrium when everything that was going to happen has happened: it is quiescent. An equilibrium state can be specified either by its temperature or by its average energy. When two systems are in equilibrium with each other, no net heat flows between them.

## 4. The laws of thermodynamics

### 4.1 First law

The total energy of an isolated system is conserved.

### 4.2 Second law

The total entropy of an isolated system never decreases. A system that starts out of equilibrium has a distribution that tends to broaden as it relaxes. The lecture ties this to **coarse-graining**: one loses track of fine microscopic detail, and the coarse-grained description has higher entropy. (The caption text for this remark is garbled, so this reading is an interpretation.)

### 4.3 Temperature

Temperature is defined through the energy cost of changing entropy:

$$
dE=T\,dS \qquad\Longleftrightarrow\qquad \frac{1}{T}=\frac{\partial S}{\partial E}.
$$

### 4.4 Heat flow and the zeroth law

Let two subsystems A and B, each internally in equilibrium, exchange energy. Suppose $T\_B>T\_A$.

1. Energy conservation: $\Delta E\_A+\Delta E\_B=0$.
2. Second law: $\Delta S\_A+\Delta S\_B\ge 0$.
3. For each subsystem, $\Delta E=T,\Delta S$, so $T\_B\Delta S\_B=-T\_A\Delta S\_A$, i.e.

$$
\Delta S_B=-\frac{T_A}{T_B}\,\Delta S_A .
$$

4. Substituting into the second law:

$$
\Delta S_A\left(1-\frac{T_A}{T_B}\right)\ge 0
\;\Longrightarrow\;
\Delta S_A\,\frac{T_B-T_A}{T_B}\ge 0 .
$$

5. Because $T\_B>T\_A>0$, this requires $\Delta S\_A\ge 0$, hence $\Delta E\_A=T\_A\Delta S\_A\ge 0$.

**Energy flows from the hotter system to the colder one.** Flow stops only when $T\_A=T\_B$. It follows that if A is in equilibrium with B, and B with C, then A is in equilibrium with C. This is the **zeroth law**: equality of temperature is transitive.

The assumption that each subsystem is internally in equilibrium is essential. If it fails, one can divide the system into smaller pieces until each piece is in equilibrium.

## 5. Replicas, occupation numbers, and the heat bath

To find the equilibrium distribution, imagine $N$ identical replicas of the system, all in contact with one another. Any one replica sees the others as a **heat bath**.

Let $n\_i$ be the number of replicas in state $i$. Then

$$
\sum_i n_i=N, \qquad \sum_i n_i E_i=N\bar E ,
$$

where $\bar E$ is the average energy per replica. Identifying $p\_i=n\_i/N$ turns these into

$$
\sum_i p_i=1,\qquad \sum_i p_i E_i=\bar E .
$$

A remark on quantum mechanics: a system in a finite box has discrete energy levels, which is why sums over states are natural. In the classical limit the sums become integrals. The lecture notes this is a subtle point and does not prove it.

## 6. Counting arrangements

The number of ways to assign $N$ distinguishable replicas to states so that state $i$ holds $n\_i$ of them is

$$
\boxed{W=\frac{N!}{\prod_i n_i!}} ,
$$

with $0!=1$ so empty states do not contribute.

Checks:

* All $N$ replicas in a single state: $W=N!/N!=1$. There is only one way.
* Two replicas, one in each of two states: $W=2!/(1!,1!)=2$.

Every individual assignment of replicas to states is equally likely, so the most probable set of occupation numbers is the one with the largest $W$ that still satisfies the two constraints above.

## 7. Stirling's approximation

For large $N$,

$$
\ln N!=\sum_{x=1}^{N}\ln x\;\approx\;\int_1^N\ln x\,dx = N\ln N-N+1 \approx N\ln N-N .
$$

so

$$
\boxed{\ln N!\approx N\ln N-N},\qquad N!\approx N^{N}e^{-N}.
$$

The more precise form is $N!\approx\sqrt{2\pi N},N^{N}e^{-N}$. The extra factor $\sqrt{2\pi N}$ is negligible compared with $N^N e^{-N}$ when $N\sim10^{23}$ (it contributes only $\tfrac12\ln(2\pi N)$ to $\ln N!$), but it matters for small $N$. The lecture remarks that the approximation converges more slowly for small $N$ than one might expect.

### Applying it to $W$

Take the logarithm of $W$:

$$
\ln W=\ln N!-\sum_i\ln n_i!\approx N\ln N-N-\sum_i\left(n_i\ln n_i-n_i\right)
= N\ln N-\sum_i n_i\ln n_i ,
$$

where the $-N$ and $+\sum\_i n\_i=+N$ cancel. Now set $n\_i=Np\_i$:

$$
\sum_i n_i\ln n_i=\sum_i Np_i\left(\ln N+\ln p_i\right)=N\ln N+N\sum_i p_i\ln p_i=N\ln N-NS .
$$

Therefore

$$
\boxed{\ln W\approx N S}, \qquad S=-\sum_i p_i\ln p_i .
$$

**Maximizing the number of arrangements is the same as maximizing the entropy of the distribution.**

## 8. The maximization problem

The most probable distribution is the solution of:

$$
\text{maximize } S=-\sum_i p_i\ln p_i
\quad\text{subject to}\quad
\sum_i p_i=1,\;\; \sum_i p_iE_i=\bar E .
$$

Without the energy constraint, the answer would be the uniform distribution over all states. The energy constraint is what makes low-energy states more probable than high-energy ones.

## 9. Lagrange multipliers

**Problem:** extremize $f(x)$ subject to a constraint $g(x)=0$.

**Method:** form $F=f+\lambda g$, find the stationary point of $F$ with $\lambda$ held fixed, then choose $\lambda$ so that the constraint is satisfied. Geometrically, at the constrained extremum the level curves of $f$ are tangent to the constraint curve, so $\nabla f\parallel\nabla g$.

**Example:** minimize $f=\tfrac12(x^2+y^2)$ subject to $x+y=1$.

$$
F=\tfrac12(x^2+y^2)+\lambda(x+y-1).
$$

$$
\partial_xF=x+\lambda=0,\qquad \partial_yF=y+\lambda=0
\;\Rightarrow\; x=y=-\lambda .
$$

The constraint gives $-2\lambda=1$, so $\lambda=-\tfrac12$ and

$$
x=y=\tfrac12 .
$$

**Several constraints:** introduce one multiplier per constraint. The entropy problem has two constraints, so it will use two multipliers.

**Preview of next lecture:** apply this to the entropy problem. One of the multipliers will turn out to be the temperature (more precisely, $1/T$), and the partition function will appear.

## 10. Homework mentioned in the lecture

Minimize $f=x^2+y^2-z^2$ subject to two constraints. One is $x+y=1$. The second constraint is garbled in the captions (it sounds like $z+x=1$), so check it against the video before attempting the problem.

## 11. Review questions

1. Why is $S=-\sum\_i p\_i\ln p\_i$ never negative? When is it exactly zero?
2. Starting from $dE=T,dS$ and the second law, show that heat flows from hot to cold. Where does the assumption $T>0$ enter?
3. How does the zeroth law follow from the heat-flow argument?
4. In the replica picture, what do the constraints $\sum\_i n\_i=N$ and $\sum\_i n\_iE\_i=N\bar E$ express?
5. Derive $\ln W\approx NS$ from Stirling's approximation. Which terms cancel, and why?
6. What would the entropy-maximizing distribution be without the energy constraint?
7. Use Lagrange multipliers to find the minimum of $x^2+y^2$ subject to $x+2y=1$.

## 12. Known limitations of these notes

* The source is an automatic caption transcript. Garbled passages were interpreted, not verified: the coarse-graining remark, the remark about the missing $\sqrt{2\pi N}$ factor, and the second homework constraint.
* The proof by induction that the lecturer mentions for the counting argument is not reproduced, because it is not recoverable from the captions.
* The lecture runs about 1 hour 53 minutes. The notes follow its order but do not include every aside.
* These notes were generated with AI assistance and may contain omissions or errors.

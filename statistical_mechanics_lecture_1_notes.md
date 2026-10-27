# Statistical Mechanics — Lecture 1
## Lecture notes

**Lecturer:** Leonard Susskind  
**Course:** Stanford University — Statistical Mechanics  
**Video:** https://www.youtube.com/watch?v=D1RzvXDXyqA

> **Scope note:** These are topic-based study notes for the identified first lecture, not a transcript-verified, timestamp-by-timestamp summary. The video page could not be retrieved in full to check every example and emphasis. Use the linked lecture as the authority for the exact sequence of discussion.

---

## 1. The central question of statistical mechanics

Statistical mechanics connects the microscopic description of matter—its constituent particles and their possible states—with macroscopic observations such as temperature, pressure, and entropy.

- **Microscopic description:** specifies the state of individual particles, including their positions and momenta in classical mechanics.
- **Macroscopic description:** uses a small number of measurable variables, such as pressure, volume, and temperature.
- **Key idea:** a macroscopic system can have an enormous number of possible microscopic configurations. Statistical reasoning explains why some macroscopic outcomes are overwhelmingly more likely than others.

## 2. Microstates and macrostates

### Microstate
A **microstate** is a sufficiently detailed specification of the system at the microscopic level.

For a classical gas, this could mean giving the position and momentum of every particle.

### Macrostate
A **macrostate** is specified by macroscopic quantities or constraints, such as the total energy, volume, particle number, or the number of particles in each region.

Many different microstates can correspond to the same macrostate.

### Multiplicity
The **multiplicity** \($\Omega$\) of a macrostate is the number of microstates compatible with it.

A macrostate with larger multiplicity can be realised in more microscopic ways. When the relevant microstates are equally probable, a macrostate's probability is proportional to its multiplicity:

\[
$$ P(\text{macrostate}) \propto \Omega. $$
\]

This is the basic counting idea behind statistical explanations of macroscopic behaviour.

## 3. A simple counting example: coins

Imagine tossing \(N\) fair coins.

- A microstate is one particular sequence of heads and tails.
- A macrostate can be described by the total number \(n\) of heads.
- There are \(2^N\) possible sequences in total.
- The number of sequences with exactly \(n\) heads is

\[
\Omega(n)=\binom{N}{n}=\frac{N!}{n!(N-n)!}.
\]

For a fair-coin model, all individual sequences are equally likely. Therefore,

\[
P(n\text{ heads})=\frac{\binom{N}{n}}{2^N}.
\]

For large \(N\), counts near \(N/2\) have far more possible sequences than counts near 0 or \(N\). Thus, a roughly equal number of heads and tails is overwhelmingly more likely than an extreme outcome.

**Physical lesson:** a common macroscopic outcome need not be enforced by a special force or rule. It may arise because vastly more microstates correspond to it.

## 4. Probability and typical behaviour

Statistical mechanics often predicts what is **typical**, rather than what is logically inevitable.

- A low-multiplicity macrostate is compatible with relatively few microstates.
- A high-multiplicity macrostate is compatible with many microstates.
- If microscopic states are sampled without a strong bias, high-multiplicity macrostates dominate the observed outcomes.

For a large system, the difference in multiplicity can be so enormous that departures from the typical macrostate become practically unobservable, even though they may not be mathematically impossible.

This helps explain why macroscopic laws can be extremely reliable while the underlying microscopic description is probabilistic.

## 5. Entropy and multiplicity

A central quantity in statistical mechanics is entropy. In the Boltzmann description,

\[
S = k_{\mathrm B}\ln \Omega,
\]

where:

- \(S\) is the Boltzmann entropy of the macrostate;
- \(k_{\mathrm B}\) is Boltzmann's constant;
- \(\Omega\) is the number of compatible microstates.

The logarithm is useful because multiplicities of independent subsystems multiply, while their entropies add. If \(\Omega_{AB}=\Omega_A\Omega_B\), then

\[
S_{AB}=k_{\mathrm B}\ln(\Omega_A\Omega_B)
      =S_A+S_B.
\]

Entropy is therefore closely related to the number of microscopic arrangements consistent with the macroscopic information available.

**Important distinction:** entropy is not simply “disorder” in a vague everyday sense. The precise idea here is the logarithm of the number of compatible microstates, subject to the model and constraints being used.

## 6. Why macroscopic processes have a direction

Many familiar processes have a preferred direction:

- heat flows spontaneously from a hotter body to a colder one;
- a gas released into a larger container spreads out;
- mixed substances do not spontaneously separate into their original arrangements under ordinary conditions.

A statistical explanation is that equilibrium macrostates generally correspond to vastly more microstates than specially arranged, non-equilibrium macrostates.

A system evolving from a special macrostate is therefore overwhelmingly likely to enter macrostates of greater multiplicity. Since entropy increases with multiplicity, this gives a statistical interpretation of the tendency for entropy to increase.

This is a statement about overwhelming probability, not an assertion that every microscopic trajectory must move monotonically toward greater entropy at every instant.

## 7. Equilibrium

A system is in **equilibrium** when its macroscopic properties are stable in time under the conditions being considered.

In statistical reasoning, equilibrium is associated with the macrostate—or range of macrostates—with overwhelmingly dominant multiplicity, subject to conserved quantities and constraints such as fixed energy, volume, and particle number.

- Equilibrium does not mean that microscopic motion has stopped.
- Microscopic details can continue to change while macroscopic quantities remain stable.
- Small fluctuations may occur around equilibrium; for a large system, relative fluctuations are often small.

## 8. What statistical mechanics contributes

Statistical mechanics offers a bridge between microscopic laws and macroscopic thermodynamics:

1. Specify the microscopic states and the constraints.
2. Count or estimate the microstates compatible with each macrostate.
3. Use probabilities to determine which macrostates are typical.
4. Relate multiplicity to entropy.
5. Explain macroscopic regularities and the direction of ordinary processes statistically.

The approach does not require tracking every particle individually. Instead, it uses the structure and relative abundance of possible microscopic states.

## 9. Key equations

| Concept | Equation | Meaning |
|---|---|---|
| Total coin sequences | \(2^N\) | Number of sequences for \(N\) independent binary outcomes |
| Multiplicity for \(n\) heads | \(\displaystyle \Omega(n)=\binom{N}{n}\) | Number of sequences with exactly \(n\) heads |
| Probability of \(n\) heads | \(\displaystyle P(n)=\binom{N}{n}/2^N\) | Probability for fair, independent coins |
| Boltzmann entropy | \(\displaystyle S=k_{\mathrm B}\ln\Omega\) | Entropy associated with multiplicity |
| Additivity for independent subsystems | \(S_{AB}=S_A+S_B\) | Follows when \(\Omega_{AB}=\Omega_A\Omega_B\) |

## 10. Common misunderstandings

- **“A high-entropy state is the only possible state.”** No. Lower-entropy states may be possible, but they generally occupy a much smaller fraction of the available microstates.
- **“Entropy increase means disorder must increase in every imaginable sense.”** Entropy has a precise statistical definition; everyday descriptions such as “disorder” are only rough intuition.
- **“Equilibrium means particles stop moving.”** No. Microscopic motion can continue even when macroscopic properties are steady.
- **“Statistical laws are unreliable because they involve probability.”** For systems with huge numbers of constituents, probability distributions can be sharply concentrated around typical macroscopic outcomes.
- **“The second law forbids every local decrease of entropy.”** Entropy can decrease in a subsystem or fluctuate; the thermodynamic statement concerns the appropriate total system and conditions.

## 11. Review questions

1. What is the difference between a microstate and a macrostate?
2. Why can a macrostate be more probable than another even when individual microstates are equally probable?
3. For \(N\) fair coins, why is the number of heads near \(N/2\) typical for large \(N\)?
4. What does the multiplicity \(\Omega\) count?
5. Why is entropy defined using a logarithm of multiplicity?
6. How can entropy increase explain the typical direction of macroscopic processes?
7. Why does equilibrium not require microscopic stillness?
8. Why should entropy increase be understood statistically rather than as a claim about every microscopic step?

## 12. One-paragraph recap

Statistical mechanics explains macroscopic behaviour by considering the many microscopic states compatible with a system's observable constraints. A macrostate's multiplicity counts those compatible microstates; macrostates with much greater multiplicity are typically far more probable. Boltzmann entropy, \(S=k_{\mathrm B}\ln\Omega\), converts this counting into a thermodynamic quantity and makes entropy additive for independent subsystems. The overwhelming dominance of high-multiplicity macrostates provides a statistical explanation for equilibrium and for the observed direction of many macroscopic processes.

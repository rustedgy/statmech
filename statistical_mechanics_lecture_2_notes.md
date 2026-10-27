# Statistical Mechanics — Lecture 2
## Lecture notes

**Course:** Stanford University — Statistical Mechanics  
**Video:** https://www.youtube.com/watch?v=MCRHXHskWnE  
**Playlist:** https://www.youtube.com/playlist?list=PLpGHT1n4-mAsJ123W3fjPzvlDHOvIhHA0

> **Important scope note:** I could not retrieve the full video or its transcript, so these are provisional, topic-based notes for study—not a verified summary of the lecturer's exact sequence, examples, or statements. Check them against the video before treating them as a faithful lecture record.

---

## 1. Statistical reasoning about large systems

Statistical mechanics studies systems with many microscopic degrees of freedom. Tracking every particle individually is usually impractical, so we describe the system through probabilities and macroscopic variables.

The key distinction is between:

- **Microscopic state:** a detailed specification of the system.
- **Macroscopic state:** a description using a limited set of observable quantities and constraints.
- **Multiplicity:** the number of microscopic states consistent with a particular macroscopic description.

If a macrostate has many more compatible microstates than its alternatives, it will usually be observed much more often, provided the microscopic states are sampled without a bias that overwhelms the counting.

## 2. Counting and probability

Suppose all microstates in a set are equally likely. If a macrostate \(A\) contains \(\Omega_A\) microstates out of \(\Omega_{\mathrm{total}}\), then

\[
P(A)=\frac{\Omega_A}{\Omega_{\mathrm{total}}}.
\]

This equation illustrates how probabilities for macroscopic outcomes can arise from counting microscopic possibilities.

The equal-probability assumption matters. If microstates have different probabilities, one must sum their probabilities rather than simply count them.

## 3. A model example: \(N\) binary variables

Consider \(N\) independent variables, each of which can take one of two equally likely values. There are

\[
\Omega_{\mathrm{total}}=2^N
\]

possible configurations.

If the macrostate is specified by exactly \(n\) variables having the first value, its multiplicity is

\[
\Omega(n)=\binom{N}{n}
=\frac{N!}{n!(N-n)!}.
\]

Consequently,

\[
P(n)=\frac{1}{2^N}\binom{N}{n}.
\]

The binomial coefficient is largest near \(n=N/2\). For large \(N\), configurations with approximately equal numbers of the two values dominate the probability distribution. Extreme configurations are possible but much less likely.

This is a simple model of a general statistical-mechanical principle: typical macroscopic behaviour is often determined by the overwhelming number of microscopic configurations that produce it.

## 4. Typicality and large numbers

A result can be overwhelmingly likely without being logically certain.

For a large system:

- The number of possible microstates can be enormous.
- The multiplicities of different macrostates can differ by enormous factors.
- Most compatible microstates may correspond to a narrow range of macroscopic values.

This concentration around typical behaviour helps explain why thermodynamic quantities are stable even though the microscopic system is continually changing.

## 5. Entropy as a measure of multiplicity

Boltzmann entropy is defined by

\[
S=k_{\mathrm B}\ln\Omega,
\]

where \(k_{\mathrm B}\) is Boltzmann's constant and \(\Omega\) is the number of compatible microstates.

The logarithm makes entropy additive for independent subsystems. If

\[
\Omega_{AB}=\Omega_A\Omega_B,
\]

then

\[
S_{AB}=k_{\mathrm B}\ln(\Omega_A\Omega_B)
=S_A+S_B.
\]

Entropy therefore gives a convenient macroscopic measure of microscopic multiplicity.

### Why the logarithm matters

Multiplicities multiply when independent systems are combined, but extensive thermodynamic quantities such as entropy add. The logarithm converts multiplication into addition.

## 6. Equilibrium and constraints

The multiplicity of a macrostate depends on the constraints imposed on the system. Examples include:

- fixed total energy;
- fixed volume;
- fixed number of particles;
- restrictions on which configurations are accessible.

Equilibrium is associated with macrostates that dominate the accessible possibilities under the relevant constraints. This does not mean the particles stop moving; microscopic changes can continue while macroscopic observables remain steady.

## 7. Entropy increase: the statistical perspective

Many spontaneous macroscopic processes proceed toward states with greater multiplicity. Examples include a gas spreading into an available volume and heat flowing from a hotter object to a colder one.

The statistical explanation is that there are generally vastly more microscopic arrangements compatible with the equilibrium-like state than with a specially prepared non-equilibrium state.

This is probabilistic:

- A lower-entropy macrostate may still be possible.
- Entropy need not increase at every microscopic instant.
- For a large system, a sustained macroscopic departure from typical behaviour is extraordinarily unlikely under ordinary conditions.

## 8. Important assumptions to keep track of

When applying statistical arguments, ask:

1. **What counts as a microstate?** The answer depends on the physical model.
2. **What defines the macrostate?** Specify the measured variables and constraints.
3. **Which states are accessible?** Conservation laws and external conditions restrict the possibilities.
4. **Are microstates equally probable?** If not, multiplicity alone does not determine probability.
5. **Is the system large?** Strong concentration around typical macroscopic values is especially important for large systems.

These checks prevent a counting argument from being applied outside its assumptions.

## 9. Key equations

| Idea | Equation | Interpretation |
|---|---|---|
| Probability from counting | \(\displaystyle P(A)=\Omega_A/\Omega_{\mathrm{total}}\) | Valid when the relevant microstates are equally likely |
| Total binary configurations | \(\displaystyle 2^N\) | Number of configurations of \(N\) independent binary variables |
| Multiplicity at fixed count | \(\displaystyle \Omega(n)=\binom{N}{n}\) | Number of configurations with exactly \(n\) variables in one state |
| Boltzmann entropy | \(\displaystyle S=k_{\mathrm B}\ln\Omega\) | Entropy associated with multiplicity |
| Entropy additivity | \(\displaystyle S_{AB}=S_A+S_B\) | For independent subsystems whose multiplicities multiply |

## 10. Common misunderstandings

- **Possible means probable:** A configuration may be possible but extraordinarily unlikely.
- **Entropy means everyday disorder:** “Disorder” is only an informal analogy; the counting definition is more precise.
- **Equilibrium means microscopic inactivity:** Equilibrium can coexist with continuing microscopic motion.
- **Entropy must increase at every instant:** The statistical argument concerns typical macroscopic behaviour, not every microscopic fluctuation.
- **Counting always gives probability:** Simple counting works directly only when the microstates being counted have equal probabilities.

## 11. Review questions

1. Define a microstate, a macrostate, and multiplicity.
2. Under what assumption can a macrostate's probability be found by dividing its multiplicity by the total number of microstates?
3. Why do typical values dominate in a large collection of independent binary variables?
4. Explain why Boltzmann entropy uses a logarithm.
5. What role do conservation laws and other constraints play in statistical mechanics?
6. Why can a system be in equilibrium while its particles continue to move?
7. How does multiplicity help explain the observed direction of macroscopic processes?
8. What is the difference between a possible event and a typical event?

## 12. Short recap

Statistical mechanics connects microscopic configurations to macroscopic behaviour by counting or weighting the microscopic states compatible with macroscopic constraints. When microstates are equally likely, multiplicity determines macrostate probability; for large systems, the multiplicity distribution often makes a narrow range of macroscopic outcomes overwhelmingly typical. Boltzmann's entropy, \(S=k_{\mathrm B}\ln\Omega\), expresses this counting in a form compatible with additive thermodynamic entropy. These ideas provide a statistical framework for understanding equilibrium and the usual direction of macroscopic processes.

---

## How to make these notes lecture-faithful

On YouTube, open the video's description and choose **Show transcript**, if available. Copy the transcript into a text file or upload it here. I can then revise these notes to match the actual lecture, preserve the order of the arguments, include the lecturer's examples, and add timestamps where useful.

# Temperature from the Viewpoint of Statistical Mechanics

Temperature is often introduced as a thermometer reading or as a measure of how hot something feels. Statistical mechanics gives a deeper definition: **temperature describes how entropy changes when energy is added to a system**. Entropy, in turn, is determined by the microscopic states compatible with the system's macroscopic constraints. Temperature is therefore not an extra microscopic ingredient; it emerges from counting states and assigning probabilities.

This original supplementary chapter develops that idea using microstates, entropy, energy exchange, and the canonical ensemble. It is not a transcript of any particular lecture.

## 1. Microstates, macrostates, and multiplicity

A **microstate** specifies a system's microscopic configuration at the level of detail used by a model. A **macrostate** specifies coarser properties—such as energy, volume, or particle number—and can be realized by many microstates.

Let \(\Omega(E)\) be the number of accessible microstates in a narrow energy range around \(E\), with the other macroscopic constraints held fixed. This is the **multiplicity** of the macrostate. For a classical system, a suitably measured phase-space volume plays the analogous role.

For an isolated system whose accessible microstates are treated equally, a macrostate with greater multiplicity is more probable: there are more microscopic arrangements that realize it. This observation motivates the statistical definition of entropy.

## 2. Entropy counts microscopic possibilities

For a macrostate with multiplicity \(\Omega\), Boltzmann's entropy is

$$
S = k_B \ln \Omega,
$$

where \(k_B\) is Boltzmann's constant. The logarithm makes entropy additive for independent systems: when their multiplicities multiply, their entropies add.

More generally, if microstate \(i\) has probability \(p_i\), the Gibbs entropy is

$$
S = -k_B \sum_i p_i \ln p_i.
$$

For a uniform distribution over \(\Omega\) accessible states, the Gibbs expression reduces to the Boltzmann expression. Both quantify the spread of probability over microscopic possibilities.

Temperature depends not on the absolute size of entropy, but on **how entropy changes with energy**.

## 3. The statistical definition of temperature

For a system whose entropy can be expressed as \(S(E)\), define inverse temperature \(\beta\) by

$$
\beta \equiv \frac{1}{k_B T}
= \left(\frac{\partial S}{\partial E}\right)_{V,N,\ldots}.
$$

Equivalently,

$$
T = \left[k_B\left(\frac{\partial S}{\partial E}\right)_{V,N,\ldots}\right]^{-1}.
$$

The derivative is taken while holding the other relevant constraints fixed. For a discrete system, it can be understood as an appropriate finite difference, or as a smooth approximation for a sufficiently large system.

This relation is the central result:

- If adding a little energy makes many additional microscopic states accessible, entropy rises rapidly with energy.
- If entropy rises more slowly with energy, its slope is smaller.
- If entropy is locally maximal as a function of energy, its slope is zero: \(\beta=0\), corresponding formally to infinite temperature.
- If entropy decreases as energy increases, the slope is negative and the system has negative temperature under this definition.

For ordinary positive-temperature systems, a steeper entropy-versus-energy curve means a lower temperature, while a shallower curve means a higher temperature. Temperature is not simply the total energy, nor is it proportional to the number of states. It is related to the **logarithmic rate at which the number of states grows with energy**.

Using \(S=k_B\ln\Omega\), one can write

$$
\frac{1}{T}
= k_B\frac{\partial\ln\Omega}{\partial E}
= \frac{k_B}{\Omega}\frac{\partial\Omega}{\partial E}.
$$

Thus temperature is controlled by the fractional growth of multiplicity per unit energy. A system may have an enormous number of states and still have a high or low temperature depending on how that number changes when energy is added.

## 4. Why systems in thermal equilibrium have equal temperatures

Consider two weakly coupled systems \(A\) and \(B\) that can exchange energy, while their total energy remains fixed:

$$
E_A+E_B=E_{\mathrm{tot}}.
$$

If their multiplicities approximately multiply, the multiplicity for a particular energy split is

$$
\Omega_{\mathrm{tot}}(E_A)
= \Omega_A(E_A)\,\Omega_B(E_{\mathrm{tot}}-E_A).
$$

The most probable energy split maximizes the combined entropy,

$$
S_{\mathrm{tot}}=S_A(E_A)+S_B(E_B).
$$

At an interior maximum, changing the energy split slightly cannot increase the total entropy. Differentiating with respect to \(E_A\), while keeping \(E_{\mathrm{tot}}\) fixed, gives

$$
\frac{\partial S_{\mathrm{tot}}}{\partial E_A}
= \frac{\partial S_A}{\partial E_A}
- \frac{\partial S_B}{\partial E_B}=0.
$$

Therefore,

$$
\left(\frac{\partial S_A}{\partial E_A}\right)
=\left(\frac{\partial S_B}{\partial E_B}\right),
\qquad T_A=T_B,
$$

provided both systems have well-defined temperatures under the same convention.

**Equal temperature is the condition that makes total entropy stationary under a small exchange of energy.** Temperature is the quantity that becomes equal when systems reach thermal equilibrium. It follows from state counting and the most-probable energy split rather than being assumed at the outset.

For stable equilibrium, the stationary point must also be a maximum of total entropy. Equality of temperatures is the first-derivative condition; stability depends on the curvature as well.

## 5. Temperature in the canonical distribution

Now consider a small system in contact with a much larger reservoir. If the small system occupies microstate \(i\) with energy \(E_i\), the probability of that microstate is proportional to the number of reservoir states compatible with the remaining total energy:

$$
p_i \propto \Omega_R(E_{\mathrm{tot}}-E_i).
$$

Since \(S_R=k_B\ln\Omega_R\), expanding the reservoir entropy for a small change in its energy gives

$$
\ln\Omega_R(E_{\mathrm{tot}}-E_i)
\approx \text{constant}
-\frac{E_i}{k_B}\left(\frac{\partial S_R}{\partial E_R}\right).
$$

Using \(\partial S_R/\partial E_R=1/T\), the probability becomes

$$
p_i \propto e^{-\beta E_i},
\qquad \beta=\frac{1}{k_B T}.
$$

After normalization, this is the canonical distribution:

$$
p_i=\frac{e^{-\beta E_i}}{Z},
\qquad Z=\sum_i e^{-\beta E_i}.
$$

The quantity \(Z\) is the **partition function**. In this ensemble, temperature controls how strongly high-energy states are suppressed relative to low-energy states:

- At lower positive temperatures, probability is more concentrated on low-energy states.
- At higher positive temperatures, the distribution over energies is more spread out.
- The relative probabilities of two states depend on their energy difference:
  \(p_i/p_j=e^{-\beta(E_i-E_j)}\).

This is the same concept in a different form. In the microcanonical viewpoint, temperature is the slope of entropy with energy. In the canonical viewpoint, that same slope sets the exponential weighting of microstates.

## 6. Example: a system of two-level units

Imagine \(N\) independent units, each with energy either \(0\) or \(\epsilon\). If exactly \(n\) units are excited, then \(E=n\epsilon\), and the multiplicity is

$$
\Omega(E)=\binom{N}{n}.
$$

For large \(N\), Stirling's approximation gives

$$
S \approx -Nk_B\left[x\ln x+(1-x)\ln(1-x)\right],
\qquad x=\frac{n}{N}=\frac{E}{N\epsilon}.
$$

Differentiating with respect to energy yields

$$
\frac{1}{T}=\frac{k_B}{\epsilon}\ln\left(\frac{1-x}{x}\right).
$$

If fewer than half the units are excited, \(x<1/2\), the derivative is positive and the temperature is positive. At half excitation, \(x=1/2\), entropy is maximal and inverse temperature is zero. If more than half are excited, \(x>1/2\), the derivative is negative: increasing the energy now reduces the number of compatible configurations, so the entropy-defined temperature is negative.

Negative temperatures require a system with an upper bound on its energy (or other conditions that allow entropy to decrease as energy rises). They are **not colder than absolute zero**. Where both positive- and negative-temperature states are possible, negative-temperature states favor higher energies and are hotter than positive-temperature states in the statistical ordering. Most familiar systems, whose energies are not bounded above, cannot reach negative absolute temperatures in equilibrium.

## 7. What temperature is—and is not

From the statistical-mechanical viewpoint:

1. **Temperature is not total energy.** Systems with different sizes and energies can have the same temperature.
2. **Temperature is not entropy itself.** It is related to the derivative of entropy with respect to energy under specified constraints.
3. **Temperature is not fundamentally a sensation.** It is a parameter inferred from microscopic state counts or equilibrium probabilities.
4. **Temperature is an equilibrium parameter.** For weakly coupled systems in stable thermal equilibrium, their entropy slopes are equal.
5. **Temperature depends on the model and constraints.** A calculation requires specifying the available states and which macroscopic quantities are held fixed.

For small systems, energy fluctuations can be appreciable, so one should be careful about treating temperature as a perfectly sharp descriptor. Away from equilibrium, a single temperature may not be defined without additional assumptions. The entropy-derivative definition is fundamentally an equilibrium one.

## 8. A practical method for calculating temperature

For a new model:

1. Specify the microstates and constraints.
2. Count accessible states at each energy, or calculate the relevant probability distribution.
3. Obtain the entropy, for example \(S(E)=k_B\ln\Omega(E)\) for a uniform microcanonical description.
4. Differentiate with respect to energy while holding the other specified constraints fixed.
5. Apply \(1/T=(\partial S/\partial E)_{V,N,\ldots}\), checking the sign and the range in which the approximation is valid.

If using the canonical ensemble, calculate the partition function and use \(\beta=1/(k_BT)\). The microcanonical and canonical approaches give consistent descriptions of temperature in appropriate equilibrium and large-system limits, though finite systems and phase transitions require care.

## Summary

Temperature emerges from the statistical structure of microscopic states. Entropy measures the logarithm of the number of possibilities; temperature measures the slope of entropy with energy:

$$
\boxed{\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_{V,N,\ldots}}
\qquad
\boxed{\beta=\frac{1}{k_B T}}.
$$

When two systems exchange energy, their most probable equilibrium split maximizes combined entropy. The condition for that maximum is equality of their entropy slopes—and hence equality of temperature. In the canonical ensemble, the same inverse temperature determines Boltzmann probabilities. Temperature is therefore a compact description of how microscopic possibilities are distributed and how their number changes with energy.

## Review questions

1. Why is multiplicity relevant to the probability of a macrostate in an isolated system?
2. Why is temperature related to the derivative of entropy rather than to entropy itself?
3. Derive \(T_A=T_B\) by maximizing the combined entropy of two systems at fixed total energy.
4. How does \(\beta\) appear in the canonical probability distribution?
5. Why does the temperature of the two-level model become infinite at half excitation and negative above half excitation?
6. What assumptions should be checked before assigning one temperature to a small or non-equilibrium system?

---

*This is an original supplementary chapter written for this repository. It is not a transcript of, or a claim about the contents of, any particular lecture. Check conventions and derivations against a standard statistical-mechanics text when using it for formal study.*

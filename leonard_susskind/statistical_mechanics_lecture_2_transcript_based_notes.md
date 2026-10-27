# Statistical Mechanics — Lecture 2

## Temperature, entropy, and thermal equilibrium

**Lecturer:** Leonard Susskind\
**Course:** Stanford University — Statistical Mechanics\
**Video:** https://www.youtube.com/watch?v=MCRHXHskWnE\
**Basis:** Notes prepared from the transcript supplied by the user.

***

## 1. Why discuss units first?

The lecture begins by discussing physical constants as conversion factors. The speed of light, for example, converts between units of distance and time. The Boltzmann constant $k\_{\mathrm B}$ plays a similar role: it converts between the familiar thermometer scale of temperature and energy.

The main idea is that, in statistical mechanics, **temperature naturally has the dimensions of energy**. The Kelvin scale is convenient for everyday measurement, but the microscopic physics involves energy.

## 2. Thermometer temperature versus energy

### 2.1 Human-scale temperature units

The Celsius scale is defined using familiar properties of water: the freezing and boiling points at atmospheric pressure are separated into 100 degrees. This is a convenient convention, not a fundamental microscopic definition.

The Kelvin scale is measured from absolute zero. A temperature difference of one kelvin has the same size as a difference of one degree Celsius.

### 2.2 Temperature and molecular kinetic energy

For a dilute, monatomic ideal gas in three spatial dimensions, the mean translational kinetic energy per molecule is

$$
\langle K\rangle=\frac{3}{2}k_{\mathrm B}T_{\mathrm K},
$$

where $T\_{\mathrm K}$ is the temperature in kelvin.

Why the factor $3/2$?

* There are three independent translational directions: $x$, $y$, and $z$.
* Each quadratic translational degree of freedom contributes $\tfrac12 k\_{\mathrm B}T\_{\mathrm K}$ to the mean energy.
* Adding the three contributions gives $\tfrac32 k\_{\mathrm B}T\_{\mathrm K}$.

This formula applies to the translational kinetic energy of a classical dilute monatomic gas. It should not be read as saying that every particle in every system has exactly the same instantaneous kinetic energy.

The lecturer uses the example of a helium–oxygen gas mixture and even a macroscopic object such as a bowling ball to illustrate the counterintuitive point that, in thermal equilibrium, the mean kinetic energy associated with a translational degree of freedom is not determined by the particle's mass. The speeds differ because the masses differ.

## 3. The Boltzmann constant

In SI units,

$$
k_{\mathrm B}\approx 1.38\times10^{-23}\ \mathrm{J\,K^{-1}}.
$$

Thus $k\_{\mathrm B}T\_{\mathrm K}$ has units of energy. At room temperature, $T\_{\mathrm K}\approx300\ \mathrm K$, the energy scale $k\_{\mathrm B}T\_{\mathrm K}$ is very small when expressed in joules.

The Boltzmann constant is the conversion factor between the Kelvin scale and the microscopic energy scale.

### 3.1 Natural energy units for temperature

The lecturer introduces a new temperature variable, written here as $T$, defined by

$$
\boxed{T=k_{\mathrm B}T_{\mathrm K}}.
$$

Here:

* $T\_{\mathrm K}$ is thermometer temperature in kelvin.
* $T$ is temperature expressed in energy units.

With this convention, temperature has energy units and $k\_{\mathrm B}$ no longer appears explicitly in many equations. To return to kelvin, use $T\_{\mathrm K}=T/k\_{\mathrm B}$.

**Notation warning:** In standard textbooks, the symbol $T$ often means kelvin temperature and $k\_{\mathrm B}$ is retained. In these notes, $T$ without the subscript denotes the lecturer's energy-unit temperature when discussing the convention above.

## 4. Two conventions for entropy

The lecture next makes a parallel distinction between thermodynamic entropy and the dimensionless entropy used in statistical mechanics.

### 4.1 Entropy of a probability distribution

For a discrete set of states $i$ with probabilities $p\_i$, statistical entropy is

$$
\boxed{S=-\sum_i p_i\ln p_i}.
$$

This quantity is dimensionless. It measures, roughly, the logarithmic effective number of states represented by the probability distribution.

For a uniform distribution over $\Omega$ states, $p\_i=1/\Omega$, so

$$
S=-\sum_{i=1}^{\Omega}\frac1\Omega\ln\frac1\Omega
=\ln\Omega.
$$

### 4.2 Thermodynamic entropy

The conventional thermodynamic entropy, denoted here by $S\_{\mathrm{th\}}$, has SI units of joules per kelvin. The relation between the two conventions is

$$
\boxed{S_{\mathrm{th}}=k_{\mathrm B}S}.
$$

Equivalently, the dimensionless statistical entropy is $S=S\_{\mathrm{th\}}/k\_{\mathrm B}$.

This is another conversion factor: the thermodynamic entropy has units, while the statistical entropy in the lecture's convention is dimensionless. The lecture connects the historical thermodynamic quantity associated with Carnot-era heat-engine analysis to the statistical-mechanical quantity associated with Boltzmann.

## 5. Defining temperature from entropy and energy

This is the conceptual centre of the lecture.

Suppose a system has microscopic states labelled by $i$, with energies $E\_i$, and a probability distribution $p\_i$.

The probabilities obey the normalization condition

$$
\sum_i p_i=1.
$$

The average energy is

$$
\boxed{\langle E\rangle=\sum_i p_iE_i}.
$$

When the system exchanges energy with an environment (a heat bath), its energy can fluctuate. A measurement at one moment may give a different value from a measurement later, so the average energy is useful.

The lecture considers a family of equilibrium probability distributions indexed by their average energy. For each distribution, the statistical entropy is

$$
S=-\sum_i p_i\ln p_i.
$$

Consequently, within this family, entropy can be treated as a function of average energy, $S=S(E)$, or energy as a function of entropy, $E=E(S)$, where the relationship is single-valued and differentiable.

### 5.1 Small changes

For small changes in the family of equilibrium states,

$$
dE=\frac{dE}{dS}\,dS.
$$

The lecturer **defines temperature** (in energy units) as

$$
\boxed{T=\frac{dE}{dS}}.
$$

Therefore,

$$
\boxed{dE=T\,dS}
\qquad\text{or}\qquad
\boxed{dS=\frac{1}{T}\,dE}.
$$

This is not yet a derivation of the detailed equilibrium probability distribution. The lecture says that the form of the Boltzmann distribution will be developed later. At this point, the family of distributions is treated as an established feature of equilibrium systems.

### 5.2 Interpretation

Temperature measures how much the average energy must change to produce a given small change in entropy.

* A large $dE/dS$ means a relatively large energy change per unit change in entropy.
* A small $dE/dS$ means a smaller energy change per unit change in entropy.

The lecturer briefly assumes that, for ordinary systems under consideration, energy and entropy increase together. Under this assumption $dE/dS>0$, so temperature is positive. The transcript notes that this monotonicity is not universal and that unusual exceptions can exist.

## 6. Returning to conventional units

Using the lecture's notation,

$$
T=k_{\mathrm B}T_{\mathrm K},
\qquad
S=\frac{S_{\mathrm{th}}}{k_{\mathrm B}}.
$$

Substitute these into $dE=T,dS$:

$$
dE=(k_{\mathrm B}T_{\mathrm K})
\left(\frac{dS_{\mathrm{th}}}{k_{\mathrm B}}\right).
$$

The Boltzmann constants cancel:

$$
\boxed{dE=T_{\mathrm K}\,dS_{\mathrm{th}}}.
$$

This explains why conventional thermodynamics often writes the energy–entropy relation using Kelvin temperature and thermodynamic entropy without an explicit $k\_{\mathrm B}$.

## 7. Temperature as the direction of heat flow

The lecturer now connects the abstract definition to familiar experience.

Consider two systems, $A$ and $B$, each initially in equilibrium at temperatures $T\_A$ and $T\_B$. Connect them so that they can exchange energy weakly.

The basic empirical principle is that net heat flow is from the system at higher temperature to the system at lower temperature. If $T\_B>T\_A$, energy tends to flow from $B$ to $A$. If the temperatures are equal, there is no net energy flow in equilibrium.

The lecture then sets up a statistical argument for this direction using the second law.

## 8. Entropy additivity and energy conservation

### 8.1 Total entropy

For the combined systems,

$$
S_{\mathrm{total}}=S_A+S_B.
$$

Why does entropy add? For independent systems, joint probabilities multiply. Since entropy is built from logarithms of probabilities, the logarithms turn products into sums.

### 8.2 Total energy

If $A$ and $B$ exchange energy but the combined pair is isolated, total energy is conserved:

$$
dE_A+dE_B=0,
$$

so

$$
\boxed{dE_B=-dE_A}.
$$

### 8.3 The second law

The lecture takes the second law as a postulate at this stage:

$$
\boxed{dS_A+dS_B\geq 0}
$$

for the spontaneous equilibration of the combined system. The lecturer's transcript first states entropy increase as a strict inequality for a process that moves toward equilibrium; equality applies at equilibrium or for an ideal reversible limiting change.

For each subsystem, use the temperature definition:

$$
dE_A=T_A\,dS_A,
\qquad
dE_B=T_B\,dS_B.
$$

Equivalently,

$$
dS_A=\frac{dE_A}{T_A},
\qquad
dS_B=\frac{dE_B}{T_B}.
$$

Combining these with energy conservation gives

$$
dS_{\mathrm{total}}
=\frac{dE_A}{T_A}+\frac{dE_B}{T_B}
=dE_A\left(\frac1{T_A}-\frac1{T_B}\right).
$$

If $T\_B>T\_A$, then

$$
\frac1{T_A}-\frac1{T_B}>0.
$$

For the total entropy to increase, the spontaneous energy transfer must have $dE\_A>0$: system $A$ gains energy and system $B$ loses it. Thus energy flows from the hotter system $B$ to the colder system $A$.

This is the statistical-mechanical logic connecting the definition $T=dE/dS$ to the familiar direction of heat flow.

At equilibrium, there is no net tendency for energy to transfer in either direction. The equilibrium condition is

$$
\boxed{T_A=T_B}.
$$

**Scope note:** This derivation assumes that the two systems can exchange energy, that their total energy is conserved, that their entropies add, and that the second law applies to the combined isolated system.

## 9. Key equations at a glance

| Concept                                     | Equation                                                 | Meaning                                                 |
| ------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------- |
| Ideal-gas mean translational kinetic energy | $\langle K\rangle=\tfrac32 k\_{\mathrm B}T\_{\mathrm K}$ | Three translational quadratic degrees of freedom        |
| Energy-unit temperature                     | $T=k\_{\mathrm B}T\_{\mathrm K}$                         | Converts kelvin temperature to an energy scale          |
| Statistical entropy                         | $S=-\sum\_i p\_i\ln p\_i$                                | Dimensionless entropy of a probability distribution     |
| Thermodynamic entropy                       | $S\_{\mathrm{th\}}=k\_{\mathrm B}S$                      | Entropy in joules per kelvin                            |
| Average energy                              | $\langle E\rangle=\sum\_i p\_iE\_i$                      | Expected energy under the distribution                  |
| Temperature definition                      | $T=dE/dS$                                                | Energy change per unit change in dimensionless entropy  |
| Energy–entropy relation                     | $dE=T,dS$                                                | Differential definition of temperature                  |
| Energy conservation                         | $dE\_A+dE\_B=0$                                          | Energy exchanged between two isolated-together systems  |
| Total entropy                               | $S\_{\mathrm{total\}}=S\_A+S\_B$                         | Additivity for independent subsystems                   |
| Heat-flow argument                          | $dS\_{\mathrm{total\}}=dE\_A(1/T\_A-1/T\_B)$             | Determines the spontaneous direction of energy transfer |

## 10. Important distinctions and cautions

1. **Two meanings of temperature symbol:** the lecturer uses a rescaled temperature in energy units. Always check whether a formula uses kelvin temperature or energy-unit temperature.
2. **Two entropy conventions:** statistical entropy $S=-\sum p\_i\ln p\_i$ is dimensionless; thermodynamic entropy includes a factor of $k\_{\mathrm B}$.
3. **Average energy is not instantaneous energy:** a system coupled to a heat bath can fluctuate between energies.
4. **The temperature definition comes first:** in this lecture, temperature is defined as $dE/dS$ before deriving the detailed equilibrium distribution.
5. **Positive temperature is an assumption here:** the lecturer assumes ordinary systems for which energy and entropy increase together, while acknowledging that this is not universally true.
6. **The second law is assumed at this stage:** the lecture uses entropy increase to establish the direction of heat flow; it does not yet derive the second law from microscopic dynamics.

## 11. Review questions

1. Why is the Boltzmann constant described as a conversion factor?
2. Why does a dilute monatomic ideal gas have $\langle K\rangle=\tfrac32 k\_{\mathrm B}T\_{\mathrm K}$?
3. What is the difference between kelvin temperature and temperature expressed in energy units?
4. What is the difference between statistical entropy and thermodynamic entropy?
5. Why is average energy used for a system exchanging energy with a heat bath?
6. Starting from $S=-\sum\_i p\_i\ln p\_i$, what does the lecture assume in treating entropy as a function of average energy?
7. Explain the definition $T=dE/dS$ in words.
8. Why do the Boltzmann constants cancel in $dE=T\_{\mathrm K},dS\_{\mathrm{th\}}$?
9. Use energy conservation and entropy increase to show why energy flows from hot to cold.
10. What condition characterizes thermal equilibrium between two systems that can exchange energy?

## 12. Short recap

The lecture reframes temperature as a derived quantity rather than merely a thermometer reading. With dimensionless statistical entropy $S=-\sum\_i p\_i\ln p\_i$ and average energy $E$, temperature in energy units is defined by $T=dE/dS$. The Boltzmann constant converts this convention to the familiar Kelvin scale and converts dimensionless statistical entropy to thermodynamic entropy. For two systems that exchange energy, conservation of total energy and the second law imply that energy flows spontaneously from higher temperature to lower temperature, reaching thermal equilibrium when their temperatures are equal.

***

## Transcript note

These notes follow the supplied transcript. The lecture ends while setting up the equations for two systems exchanging energy; the heat-flow argument above completes the algebra directly implied by those equations. The detailed derivation of the Boltzmann equilibrium distribution is explicitly deferred by the lecturer to a later part of the course.

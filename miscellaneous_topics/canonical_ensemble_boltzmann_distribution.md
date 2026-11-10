# The Canonical Ensemble and the Boltzmann Distribution

## 1. The physical situation

The microcanonical ensemble describes an isolated system with fixed energy. Many systems of interest instead exchange energy with a much larger environment while their own volume and particle number remain fixed. Examples include a gas in thermal contact with a reservoir and a small magnetic system coupled to a thermal bath.

The **canonical ensemble** describes such a subsystem when the reservoir fixes its temperature $T$. The subsystem's energy can fluctuate, but its equilibrium probability distribution is determined by the reservoir.

## 2. Deriving the Boltzmann weight from a reservoir

Consider a small system and a much larger reservoir forming an isolated whole. If the small system is in microstate $r$ with energy $E_r$, the reservoir energy is

$$
E_R=E_{\mathrm{tot}}-E_r.
$$

The probability of finding the small system in microstate $r$ is proportional to the number of reservoir microstates compatible with the remaining energy:

$$
P_r\propto W_R(E_{\mathrm{tot}}-E_r)
=\exp\left[\frac{S_R(E_{\mathrm{tot}}-E_r)}{k_B}\right].
$$

Assume the reservoir is sufficiently large that its entropy is smooth over the range of energy exchanged. A Taylor expansion about $E_{\mathrm{tot}}$ gives

$$
S_R(E_{\mathrm{tot}}-E_r)
=S_R(E_{\mathrm{tot}})
-E_r\left(\frac{\partial S_R}{\partial E_R}\right)_{V_R,N_R}
+\frac{E_r^2}{2}\left(\frac{\partial^2S_R}{\partial E_R^2}\right)_{V_R,N_R}
+\cdots.
$$

For a macroscopic reservoir, the second derivative is small on the scale of a finite subsystem energy. More explicitly, if $S_R=N_Rs(E_R/N_R)$, then $\partial^2S_R/\partial E_R^2$ scales as $1/N_R$. In the large-reservoir limit, the quadratic and higher corrections can therefore be neglected, provided the subsystem energy remains small compared with the reservoir's thermodynamic scale.

Using the thermodynamic definition

$$
\left(\frac{\partial S_R}{\partial E_R}\right)_{V_R,N_R}
=\frac{1}{T},
$$

the reservoir entropy becomes, to first order,

$$
S_R(E_{\mathrm{tot}}-E_r)
\simeq S_R(E_{\mathrm{tot}})-\frac{E_r}{T}.
$$

Consequently,

$$
P_r\propto e^{-E_r/(k_BT)}.
$$

Defining

$$
\boxed{\beta=\frac{1}{k_BT}},
$$

we obtain the **Boltzmann weight** $e^{-\beta E_r}$.

This derivation assumes weak enough coupling that the subsystem energy is well defined, a reservoir much larger than the subsystem, and negligible higher-order terms in the reservoir entropy expansion. If the coupling is strong or the reservoir is finite, the simple canonical weight may require corrections.

## 3. Normalization and the partition function

Probabilities must sum to one. The normalization factor is therefore the sum of all Boltzmann weights:

$$
Z(T,V,N)=\sum_r e^{-\beta E_r}.
$$

This is the **canonical partition function**. The probability of microstate $r$ is

$$
\boxed{P_r=\frac{e^{-\beta E_r}}{Z}.}
$$

The sum is over all accessible microstates, including degeneracies. If several distinct microstates have the same energy, each contributes its own Boltzmann weight.

For two states $r$ and $s$,

$$
\frac{P_r}{P_s}=e^{-\beta(E_r-E_s)}.
$$

Thus temperature controls the relative suppression of higher-energy states. At low positive temperature, low-energy states dominate; as temperature rises, higher-energy states become more probable.

## 4. Meaning and dimensions of $\beta$

The exponent $\beta E_r$ must be dimensionless, so $\beta$ has units of inverse energy. Since $k_BT$ has units of energy, $\beta=1/(k_BT)$.

The parameter $\beta$ is often more convenient than $T$ in calculations because the statistical weights are simple exponentials in $\beta E$. For systems with a bounded spectrum, negative temperatures correspond to negative $\beta$ and favor higher-energy states; the physical conditions for such states are discussed in [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md).

## 5. A two-level illustration

For a system with two non-degenerate levels, $E_0=0$ and $E_1=\Delta$, the partition function is

$
Z=1+e^{-\beta\Delta}.
$

This simple sum illustrates how the partition function normalizes the Boltzmann weights. The relative probability of the two levels follows from the general ratio derived above. The population interpretation, including negative temperature, is discussed in [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md); the internal energy, heat capacity, and Schottky anomaly are treated in [Two-Level Systems and the Schottky Anomaly](two_level_system_schottky_anomaly.md).

## Summary

- A canonical subsystem exchanges energy with a large heat reservoir while $V$ and $N$ remain fixed.
- The reservoir's entropy change gives the weight $e^{-\beta E_r}$.
- $\beta=1/(k_BT)$, and normalization gives $P_r=e^{-\beta E_r}/Z$.
- The derivation relies on weak coupling and a reservoir large enough that higher-order entropy terms are negligible.

## Review questions

1. Starting from the reservoir multiplicity, derive the canonical probability weight.
2. Why is the reservoir entropy expanded in powers of the subsystem energy?
3. Explain why the quadratic correction becomes negligible for a macroscopic reservoir.
4. Why must the Boltzmann weights be divided by the partition function?
5. What is the physical meaning and dimension of $\beta$?
6. For a two-level system with energies $0$ and $\Delta$, derive the ratio of excited- to ground-state probabilities.

# Grand Canonical Ensemble and Chemical Potential

## 1. The physical question

The canonical ensemble describes a system in thermal equilibrium with a heat bath while its particle number remains fixed. Many physical systems, however, can exchange both energy and particles with their surroundings. Examples include particles adsorbing onto a surface, atoms moving between phases, and electrons occupying available states.

The **grand canonical ensemble** describes a subsystem held at fixed temperature $T$, volume $V$, and chemical potential $\mu$, while its energy and particle number may fluctuate.

Its central object is the **grand partition function**. It packages the statistical weights of states with every allowed particle number into one function.

## 2. Why chemical potential appears

For a closed system, equilibrium between accessible states is governed by energy and entropy. When particles can also move between a system and a reservoir, the reservoir's entropy changes when it supplies or accepts particles. The thermodynamic quantity controlling this exchange is the chemical potential.

Define chemical potential in the entropy representation by

$$
\boxed{\mu=-T\left(\frac{\partial S}{\partial N}\right)_{U,V}}.
$$

Equivalently, $dU=T\,dS-p\,dV+\mu\,dN$. Thus $\mu$ is the reversible energy cost of adding a particle at fixed entropy and volume, and the free-energy cost at fixed temperature and volume. When two regions can exchange particles, net flow is from higher chemical potential to lower chemical potential until equilibrium.

The statistical weight follows from a reservoir expansion, as in the canonical derivation. If the subsystem has energy $E$ and particle number $N$, the reservoir has $E_R=E_{R,0}-E$ and $N_R=N_{R,0}-N$. To first order,

$$
S_R(E_R,N_R)\simeq S_{R,0}-\frac{E}{T}+\frac{\mu N}{T},
$$

because $(\partial S_R/\partial E_R)_{N_R,V_R}=1/T$ and $(\partial S_R/\partial N_R)_{E_R,V_R}=-\mu/T$. The reservoir's number of accessible states is proportional to $e^{S_R/k_B}$, so the subsystem probability is proportional to $e^{-\beta(E-\mu N)}$, where $\beta=1/(k_BT)$.

For a reservoir at temperature $T$ and chemical potential $\mu$, the probability of a system microstate with energy $E_{N,r}$, particle number $N$, and state label $r$ is proportional to

$$
\exp\!\left[-\beta(E_{N,r}-\mu N)\right],
\qquad \beta=\frac{1}{k_B T}.
$$

The combination $E-\mu N$ plays the role of an effective energy for this ensemble. A state is favored by low energy, but the chemical-potential term also accounts for the exchange of particles with the reservoir.

## 3. Deriving the grand partition function

Let $Z_N(T,V)$ be the canonical partition function for exactly $N$ particles:

$$
Z_N(T,V)=\sum_r e^{-\beta E_{N,r}}.
$$

In the grand canonical ensemble, states with different particle numbers are all accessible. Summing their statistical weights gives

$$
\begin{aligned}
\Xi(T,V,\mu)
&=\sum_{N=0}^{\infty}\sum_r
e^{-\beta(E_{N,r}-\mu N)}\\
&=\sum_{N=0}^{\infty}e^{\beta\mu N}
\sum_r e^{-\beta E_{N,r}}.
\end{aligned}
$$

Therefore,

$$
\boxed{
\Xi(T,V,\mu)=\sum_{N=0}^{\infty}
e^{\beta\mu N}Z_N(T,V)
}
$$

Define the **fugacity**

$$
\boxed{z=e^{\beta\mu}}.
$$

Then the same expression is often written as

$$
\Xi(T,V,z)=\sum_{N=0}^{\infty}z^N Z_N(T,V).
$$

The grand partition function is a normalization factor: it ensures that the probabilities of all microstates sum to one.

The probability of a particular microstate $(N,r)$ is

$$
\boxed{
P_{N,r}=\frac{e^{-\beta(E_{N,r}-\mu N)}}{\Xi}
}
$$

and the probability of finding exactly $N$ particles is

$$
\boxed{
P(N)=\frac{e^{\beta\mu N}Z_N}{\Xi}
=\frac{z^N Z_N}{\Xi}.
}
$$

## 4. Thermodynamic information from $\Xi$

The logarithm of the grand partition function generates useful equilibrium averages.

### Average particle number

Differentiate with respect to chemical potential at fixed $T$ and $V$:

$$
\boxed{
\langle N\rangle
=\frac{1}{\beta}
\left(\frac{\partial\ln\Xi}{\partial\mu}\right)_{T,V}
=k_BT\left(\frac{\partial\ln\Xi}{\partial\mu}\right)_{T,V}
}
$$

Equivalently, using fugacity,

$$
\boxed{
\langle N\rangle
=z\left(\frac{\partial\ln\Xi}{\partial z}\right)_{T,V}.
}
$$

### Average energy

At fixed fugacity $z$, differentiating with respect to $\beta$ gives

$$
\boxed{
\langle E\rangle
=-\left(\frac{\partial\ln\Xi}{\partial\beta}\right)_{z,V}.
}
$$

The condition that $z$ is held fixed matters: it keeps the particle-number weight $z^N$ constant during this derivative.

### Grand potential

The thermodynamic potential naturally associated with this ensemble is the **grand potential**:

$$
\boxed{\Omega_G=-k_BT\ln\Xi.}
$$

For a system whose thermodynamic variables are $T,V,\mu$,

$$
\Omega_G=U-TS-\mu\langle N\rangle.
$$

For a homogeneous bulk system in the thermodynamic limit, the grand potential is related to pressure by

$$
\boxed{\Omega_G=-pV.}
$$

Thus,

$$
pV=k_BT\ln\Xi.
$$

This gives a direct route from the grand partition function to the equation of state.

## 5. Particle-number fluctuations

Unlike the canonical ensemble, the grand canonical ensemble allows $N$ to fluctuate. Its variance is

$$
\operatorname{Var}(N)
=\langle N^2\rangle-\langle N\rangle^2.
$$

Differentiating the mean particle number with respect to chemical potential gives

$$
\boxed{
\operatorname{Var}(N)
=k_BT\left(\frac{\partial\langle N\rangle}
{\partial\mu}\right)_{T,V}.
}
$$

The response of the mean particle number to a change in chemical potential is therefore tied directly to the size of particle-number fluctuations. A system that responds strongly to changes in $\mu$ generally exhibits larger fluctuations in $N$.

## 6. Worked example: a classical ideal gas

For a classical ideal gas of indistinguishable particles, the canonical partition function is

$$
Z_N(T,V)=\frac{1}{N!}
\left(\frac{V}{\lambda_T^3}\right)^N,
\qquad
\lambda_T=\frac{h}{\sqrt{2\pi m k_BT}},
$$

where $\lambda_T$ is the thermal de Broglie wavelength.

Substitute this into the grand partition function:

$$
\begin{aligned}
\Xi
&=\sum_{N=0}^{\infty}
\frac{1}{N!}
\left(\frac{zV}{\lambda_T^3}\right)^N\\
&=\exp\!\left(\frac{zV}{\lambda_T^3}\right).
\end{aligned}
$$

Hence,

$$
\ln\Xi=\frac{zV}{\lambda_T^3}.
$$

Using the derivative formula for the mean particle number,

$$
\boxed{
\langle N\rangle=\frac{zV}{\lambda_T^3}.
}
$$

Using the pressure relation,

$$
pV=k_BT\ln\Xi
=\frac{zVk_BT}{\lambda_T^3}.
$$

Since $\langle N\rangle=zV/\lambda_T^3$, we recover the ideal-gas equation of state:

$$
\boxed{pV=\langle N\rangle k_BT.}
$$

In this classical ideal-gas example, the probability distribution of $N$ is Poissonian, so

$$
\boxed{\operatorname{Var}(N)=\langle N\rangle.}
$$

This result is a useful illustration of how the grand canonical ensemble describes both the average thermodynamics and fluctuations in particle number.

For a dilute classical ideal gas, $z=n\lambda_T^3$, so

$$
\boxed{\mu=k_BT\ln(n\lambda_T^3)}.
$$

Here $n=\langle N\rangle/V$ and $\lambda_T=h/\sqrt{2\pi m k_BT}$. The dilute-gas criterion $n\lambda_T^3\ll1$ makes the logarithm negative. The chemical potential includes the entropic effect of adding a particle, not just its bare energy.

The $1/N!$ in the ideal-gas canonical partition function corrects for overcounting permutations of identical particles. Without it, the entropy contains a spurious $k_B\ln N!$ term and is not extensive in the thermodynamic limit (the Gibbs paradox).

For the classical ideal gas, $P(N)$ is Poissonian and $\operatorname{Var}(N)=\langle N\rangle$. Its relative root-mean-square fluctuation is therefore

$$
\frac{\sqrt{\operatorname{Var}(N)}}{\langle N\rangle}=\frac{1}{\sqrt{\langle N\rangle}}.
$$

Relative fluctuations become negligible for large systems, explaining why ensembles often agree on bulk observables in the thermodynamic limit, except near critical points or other regimes with anomalously large fluctuations.

## 7. An independent site that can be empty or occupied

Consider one site that can either be empty, with energy zero and particle number zero, or occupied by one particle of energy $\epsilon$. The two statistical weights are $1$ and $e^{-\beta(\epsilon-\mu)}$. Therefore,

$$
\boxed{
\Xi_1=1+e^{-\beta(\epsilon-\mu)}.
}
$$

The mean occupation of the site is

$$
\boxed{
\langle n\rangle
=\frac{1}{e^{\beta(\epsilon-\mu)}+1}.
}
$$

For $M$ independent equivalent sites, the grand partition function factorizes:

$$
\Xi_M=\left[1+e^{-\beta(\epsilon-\mu)}\right]^M,
$$

and the mean number of occupied sites is

$$
\boxed{
\langle N\rangle
=\frac{M}{e^{\beta(\epsilon-\mu)}+1}.
}
$$

This has the same mathematical form as the Fermi–Dirac occupation factor. The example illustrates how the chemical potential controls the likelihood that a state is occupied. The model assumes at most one particle per site and does not, by itself, describe interactions between sites.

The single-state grand-partition method also leads directly to the Bose–Einstein and Fermi–Dirac occupation laws: sum the allowed particle-number weights for each state, then calculate its mean occupation. See [Bose–Einstein Statistics](bose_einstein_statistics_derivation.md) and [Fermi–Dirac Statistics](fermi_dirac_statistics_derivation.md).

### Bosonic orbital

For a bosonic orbital of energy $\epsilon$, any occupation $n=0,1,2,\ldots$ is allowed. Writing $q=e^{-\beta(\epsilon-\mu)}$, its grand-partition sum is a geometric series:
$
\Xi_1=\sum_{n=0}^{\infty}q^n
=\frac{1}{1-e^{-\beta(\epsilon-\mu)}}.
$
The series converges only when $q<1$, or $\mu<\epsilon$. Differentiating the logarithm of this single-orbital partition function, or summing $nq^n$, gives
$
\boxed{\langle n\rangle
=\frac{1}{e^{\beta(\epsilon-\mu)}-1}.}
$
This is the Bose–Einstein mean occupation factor. In contrast to a fermionic orbital, a bosonic orbital can hold arbitrarily many particles, subject to the convergence condition.

### Langmuir adsorption isotherm

Now consider $M$ independent adsorption sites that can each be empty or occupied. If the occupied site's energy is $\epsilon$, its mean occupancy is
$
\theta=\frac{1}{e^{\beta(\epsilon-\mu)}+1}.
$
For a dilute classical gas above the surface, $n=p/(k_BT)$ and $z=e^{\beta\mu}=n\lambda_T^3$, so $z=p\lambda_T^3/(k_BT)$. Substitution gives
$
\boxed{\theta=\frac{p}{p+p_0(T)},\qquad
p_0(T)=\frac{k_BT}{\lambda_T^3}e^{\beta\epsilon}.}
$
This is the Langmuir form: occupancy rises with gas pressure and approaches one at high pressure. The expression assumes independent sites, no lateral interactions, and equilibrium between the gas and adsorbed particles.

## 8. Comparing ensembles

| Ensemble | Fixed variables | Quantities that may fluctuate | Natural potential |
|---|---|---|---|
| Microcanonical | $E,V,N$ | None of these macroscopic constraints | Entropy $S$ |
| Canonical | $T,V,N$ | Energy | Helmholtz free energy $F$ |
| Grand canonical | $T,V,\mu$ | Energy and particle number | Grand potential $\Omega_G$ |

For a sufficiently large system away from unusual critical regimes, different ensembles often give the same thermodynamic predictions for bulk observables. Their fluctuation properties and convenience for particular calculations can nevertheless differ.

## 9. Assumptions and limits

- The system is in equilibrium with a large reservoir that fixes $T$ and $\mu$.
- The volume is fixed; particle exchange is allowed.
- The allowed particle numbers and states must make $\Xi$ converge.
- The ideal-gas example assumes a dilute classical gas, while the independent-site example assumes at most one particle per site.
- For small systems or near critical points, fluctuations can be important, and ensemble equivalence should not be assumed without checking the conditions.

## 10. Summary

- The grand canonical ensemble describes a system that exchanges energy and particles with a reservoir.
- The chemical potential $\mu$ controls particle exchange, and the fugacity is $z=e^{\beta\mu}$.
- The grand partition function is $\Xi=\sum_N e^{\beta\mu N}Z_N$.
- Its derivatives give the mean particle number and energy.
- The grand potential is $\Omega_G=-k_BT\ln\Xi$, and for homogeneous bulk matter $\Omega_G=-pV$.
- Particle-number fluctuations are connected to the response of the mean number to chemical potential.

## Review questions

1. Why does the grand canonical probability weight contain $E-\mu N$ rather than energy alone?
2. Starting from the microstate probabilities, derive the grand partition function in terms of the canonical partition functions $Z_N$.
3. Show that $\langle N\rangle=(1/\beta)(\partial\ln\Xi/\partial\mu)_{T,V}$.
4. For a classical ideal gas, derive $\Xi=\exp(zV/\lambda_T^3)$ and recover $pV=\langle N\rangle k_BT$.
5. What is the physical meaning of the relation between particle-number fluctuations and the derivative of $\langle N\rangle$ with respect to $\mu$?
6. Explain when the grand canonical ensemble is more convenient than the canonical ensemble.

# The Grand Canonical Ensemble and Chemical Potential

## 1. The physical question

The canonical ensemble describes a system in thermal equilibrium with a heat bath while its particle number remains fixed. Many physical systems, however, can exchange both energy and particles with their surroundings. Examples include particles adsorbing onto a surface, atoms moving between phases, and electrons occupying available states.

The **grand canonical ensemble** describes a subsystem held at fixed temperature \(T\), volume \(V\), and chemical potential \(\mu\), while its energy and particle number may fluctuate.

Its central object is the **grand partition function**. It packages the statistical weights of states with every allowed particle number into one function.

## 2. Why chemical potential appears

For a closed system, equilibrium between accessible states is governed by energy and entropy. When particles can also move between a system and a reservoir, the reservoir's entropy changes when it supplies or accepts particles. The thermodynamic quantity controlling this exchange is the chemical potential.

For a reservoir at temperature \(T\) and chemical potential \(\mu\), the probability of a system microstate with energy \(E_{N,r}\), particle number \(N\), and state label \(r\) is proportional to

\[
\exp\!\left[-\beta(E_{N,r}-\mu N)\right],
\qquad \beta=\frac{1}{k_B T}.
\]

The combination \(E-\mu N\) plays the role of an effective energy for this ensemble. A state is favored by low energy, but the chemical-potential term also accounts for the exchange of particles with the reservoir.

## 3. Deriving the grand partition function

Let \(Z_N(T,V)\) be the canonical partition function for exactly \(N\) particles:

\[
Z_N(T,V)=\sum_r e^{-\beta E_{N,r}}.
\]

In the grand canonical ensemble, states with different particle numbers are all accessible. Summing their statistical weights gives

\[
\begin{aligned}
\Xi(T,V,\mu)
&=\sum_{N=0}^{\infty}\sum_r
e^{-\beta(E_{N,r}-\mu N)}\\
&=\sum_{N=0}^{\infty}e^{\beta\mu N}
\sum_r e^{-\beta E_{N,r}}.
\end{aligned}
\]

Therefore,

\[
\boxed{
\Xi(T,V,\mu)=\sum_{N=0}^{\infty}
e^{\beta\mu N}Z_N(T,V)
}
\]

Define the **fugacity**

\[
\boxed{z=e^{\beta\mu}}.
\]

Then the same expression is often written as

\[
\Xi(T,V,z)=\sum_{N=0}^{\infty}z^N Z_N(T,V).
\]

The grand partition function is a normalization factor: it ensures that the probabilities of all microstates sum to one.

The probability of a particular microstate \((N,r)\) is

\[
\boxed{
P_{N,r}=\frac{e^{-\beta(E_{N,r}-\mu N)}}{\Xi}
}
\]

and the probability of finding exactly \(N\) particles is

\[
\boxed{
P(N)=\frac{e^{\beta\mu N}Z_N}{\Xi}
=\frac{z^N Z_N}{\Xi}.
}
\]

## 4. Thermodynamic information from \(\Xi\)

The logarithm of the grand partition function generates useful equilibrium averages.

### Average particle number

Differentiate with respect to chemical potential at fixed \(T\) and \(V\):

\[
\boxed{
\langle N\rangle
=\frac{1}{\beta}
\left(\frac{\partial\ln\Xi}{\partial\mu}\right)_{T,V}
=k_BT\left(\frac{\partial\ln\Xi}{\partial\mu}\right)_{T,V}
}
\]

Equivalently, using fugacity,

\[
\boxed{
\langle N\rangle
=z\left(\frac{\partial\ln\Xi}{\partial z}\right)_{T,V}.
}
\]

### Average energy

At fixed fugacity \(z\), differentiating with respect to \(\beta\) gives

\[
\boxed{
\langle E\rangle
=-\left(\frac{\partial\ln\Xi}{\partial\beta}\right)_{z,V}.
}
\]

The condition that \(z\) is held fixed matters: it keeps the particle-number weight \(z^N\) constant during this derivative.

### Grand potential

The thermodynamic potential naturally associated with this ensemble is the **grand potential**:

\[
\boxed{\Omega_G=-k_BT\ln\Xi.}
\]

For a system whose thermodynamic variables are \(T,V,\mu\),

\[
\Omega_G=U-TS-\mu\langle N\rangle.
\]

For a homogeneous bulk system in the thermodynamic limit, the grand potential is related to pressure by

\[
\boxed{\Omega_G=-pV.}
\]

Thus,

\[
pV=k_BT\ln\Xi.
\]

This gives a direct route from the grand partition function to the equation of state.

## 5. Particle-number fluctuations

Unlike the canonical ensemble, the grand canonical ensemble allows \(N\) to fluctuate. Its variance is

\[
\operatorname{Var}(N)
=\langle N^2\rangle-\langle N\rangle^2.
\]

Differentiating the mean particle number with respect to chemical potential gives

\[
\boxed{
\operatorname{Var}(N)
=k_BT\left(\frac{\partial\langle N\rangle}
{\partial\mu}\right)_{T,V}.
}
\]

The response of the mean particle number to a change in chemical potential is therefore tied directly to the size of particle-number fluctuations. A system that responds strongly to changes in \(\mu\) generally exhibits larger fluctuations in \(N\).

## 6. Worked example: a classical ideal gas

For a classical ideal gas of indistinguishable particles, the canonical partition function is

\[
Z_N(T,V)=\frac{1}{N!}
\left(\frac{V}{\lambda_T^3}\right)^N,
\qquad
\lambda_T=\frac{h}{\sqrt{2\pi m k_BT}},
\]

where \(\lambda_T\) is the thermal de Broglie wavelength.

Substitute this into the grand partition function:

\[
\begin{aligned}
\Xi
&=\sum_{N=0}^{\infty}
\frac{1}{N!}
\left(\frac{zV}{\lambda_T^3}\right)^N\\
&=\exp\!\left(\frac{zV}{\lambda_T^3}\right).
\end{aligned}
\]

Hence,

\[
\ln\Xi=\frac{zV}{\lambda_T^3}.
\]

Using the derivative formula for the mean particle number,

\[
\boxed{
\langle N\rangle=\frac{zV}{\lambda_T^3}.
}
\]

Using the pressure relation,

\[
pV=k_BT\ln\Xi
=\frac{zVk_BT}{\lambda_T^3}.
\]

Since \(\langle N\rangle=zV/\lambda_T^3\), we recover the ideal-gas equation of state:

\[
\boxed{pV=\langle N\rangle k_BT.}
\]

In this classical ideal-gas example, the probability distribution of \(N\) is Poissonian, so

\[
\boxed{\operatorname{Var}(N)=\langle N\rangle.}
\]

This result is a useful illustration of how the grand canonical ensemble describes both the average thermodynamics and fluctuations in particle number.

## 7. An independent site that can be empty or occupied

Consider one site that can either be empty, with energy zero and particle number zero, or occupied by one particle of energy \(\epsilon\). The two statistical weights are \(1\) and \(e^{-\beta(\epsilon-\mu)}\). Therefore,

\[
\boxed{
\Xi_1=1+e^{-\beta(\epsilon-\mu)}.
}
\]

The mean occupation of the site is

\[
\boxed{
\langle n\rangle
=\frac{1}{e^{\beta(\epsilon-\mu)}+1}.
}
\]

For \(M\) independent equivalent sites, the grand partition function factorizes:

\[
\Xi_M=\left[1+e^{-\beta(\epsilon-\mu)}\right]^M,
\]

and the mean number of occupied sites is

\[
\boxed{
\langle N\rangle
=\frac{M}{e^{\beta(\epsilon-\mu)}+1}.
}
\]

This has the same mathematical form as the Fermi–Dirac occupation factor. The example illustrates how the chemical potential controls the likelihood that a state is occupied. The model assumes at most one particle per site and does not, by itself, describe interactions between sites.

## 8. Comparing ensembles

| Ensemble | Fixed variables | Quantities that may fluctuate | Natural potential |
|---|---|---|---|
| Microcanonical | \(E,V,N\) | None of these macroscopic constraints | Entropy \(S\) |
| Canonical | \(T,V,N\) | Energy | Helmholtz free energy \(F\) |
| Grand canonical | \(T,V,\mu\) | Energy and particle number | Grand potential \(\Omega_G\) |

For a sufficiently large system away from unusual critical regimes, different ensembles often give the same thermodynamic predictions for bulk observables. Their fluctuation properties and convenience for particular calculations can nevertheless differ.

## 9. Assumptions and limits

- The system is in equilibrium with a large reservoir that fixes \(T\) and \(\mu\).
- The volume is fixed; particle exchange is allowed.
- The allowed particle numbers and states must make \(\Xi\) converge.
- The ideal-gas example assumes a dilute classical gas, while the independent-site example assumes at most one particle per site.
- For small systems or near critical points, fluctuations can be important, and ensemble equivalence should not be assumed without checking the conditions.

## 10. Summary

- The grand canonical ensemble describes a system that exchanges energy and particles with a reservoir.
- The chemical potential \(\mu\) controls particle exchange, and the fugacity is \(z=e^{\beta\mu}\).
- The grand partition function is \(\Xi=\sum_N e^{\beta\mu N}Z_N\).
- Its derivatives give the mean particle number and energy.
- The grand potential is \(\Omega_G=-k_BT\ln\Xi\), and for homogeneous bulk matter \(\Omega_G=-pV\).
- Particle-number fluctuations are connected to the response of the mean number to chemical potential.

## Review questions

1. Why does the grand canonical probability weight contain \(E-\mu N\) rather than energy alone?
2. Starting from the microstate probabilities, derive the grand partition function in terms of the canonical partition functions \(Z_N\).
3. Show that \(\langle N\rangle=(1/\beta)(\partial\ln\Xi/\partial\mu)_{T,V}\).
4. For a classical ideal gas, derive \(\Xi=\exp(zV/\lambda_T^3)\) and recover \(pV=\langle N\rangle k_BT\).
5. What is the physical meaning of the relation between particle-number fluctuations and the derivative of \(\langle N\rangle\) with respect to \(\mu\)?
6. Explain when the grand canonical ensemble is more convenient than the canonical ensemble.

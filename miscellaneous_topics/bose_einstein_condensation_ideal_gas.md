# Bose–Einstein Condensation in the Uniform Ideal Gas

## 1. What condenses?

Bose–Einstein statistics allows any number of identical bosons to occupy the same one-particle state. At sufficiently low temperature and high density, a three-dimensional uniform ideal Bose gas cannot accommodate all its particles in excited states. The excess particles accumulate in the lowest-energy state, producing Bose–Einstein condensation (BEC).

This is distinct from ordinary vapour–liquid condensation. Liquid–gas condensation is driven by intermolecular interactions and a free-energy competition between dilute and dense phases. The ideal-gas BEC discussed here occurs even without interactions, because of quantum statistics and the finite capacity of the excited states at a given temperature.

We consider non-interacting bosons of mass $m$ in a three-dimensional box of volume $V$, in the thermodynamic limit. The gas is uniform and the total particle number $N$ is fixed, although the grand canonical ensemble is a convenient way to calculate occupations.

## 2. Grand-canonical occupation of one-particle states

For a one-particle state of energy $\epsilon$, the Bose–Einstein mean occupation is

$$
\bar n(\epsilon)=\frac{1}{e^{\beta(\epsilon-\mu)}-1},
\qquad \beta=\frac{1}{k_BT}.
$$

The grand-partition sum for one bosonic state is geometric:

$$
\Xi_\epsilon=\sum_{n=0}^{\infty}e^{-\beta n(\epsilon-\mu)}
=\frac{1}{1-e^{-\beta(\epsilon-\mu)}}.
$$

Convergence requires $\mu<\epsilon$ for every state with finite mean occupation. If the ground-state energy is chosen as zero, the chemical potential therefore satisfies $\mu<0$ for a finite system, and can approach zero from below in the thermodynamic limit. It cannot exceed the ground-state energy.

For a free particle in a box, the ground state has zero momentum and energy zero. The excited states have positive kinetic energy. The mean total particle number is the sum of the ground-state occupation and all excited-state occupations:

$$
N=N_0+N_{\rm ex}.
$$

The key question is whether the excited states can hold all $N$ particles at the chosen temperature.

## 3. Density of one-particle states in three dimensions

For a large box with periodic boundary conditions, allowed wave vectors occupy $k$-space with one state per volume $(2\pi)^3/V$. The number of one-particle states with wave number less than $k$ is

$$
\mathcal N(k)=\frac{V}{(2\pi)^3}\frac{4\pi k^3}{3}
=\frac{Vk^3}{6\pi^2}.
$$

For a free particle, $\epsilon=\hbar^2k^2/(2m)$, so

$$
\mathcal N(\epsilon)
=\frac{V}{6\pi^2}
\left(\frac{2m}{\hbar^2}\right)^{3/2}\epsilon^{3/2}.
$$

Differentiating gives the density of one-particle states per unit energy:

$$
\boxed{
g(\epsilon)=\frac{V}{4\pi^2}
\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{\epsilon},
\qquad \epsilon>0.}
$$

There is no spin factor in this expression: it describes a single internal state per momentum state. If the bosons have an internal degeneracy, that factor must be included explicitly.

## 4. Maximum population of the excited states

Define the fugacity $z=e^{\beta\mu}$. With the ground-state energy set to zero, $0<z<1$ for a finite system. In the continuum approximation for the excited states,

$$
N_{\rm ex}
=\int_0^{\infty}
\frac{g(\epsilon)}
{z^{-1}e^{\beta\epsilon}-1}\,d\epsilon.
$$

Substitute $x=\beta\epsilon$ and use the density of states above:

$$
N_{\rm ex}
=\frac{V}{4\pi^2}
\left(\frac{2m k_BT}{\hbar^2}\right)^{3/2}
\int_0^{\infty}\frac{x^{1/2}}{z^{-1}e^x-1}\,dx.
$$

The Bose function is defined by

$$
g_s(z)=\frac{1}{\Gamma(s)}
\int_0^{\infty}\frac{x^{s-1}}{z^{-1}e^x-1}\,dx
=\sum_{\ell=1}^{\infty}\frac{z^\ell}{\ell^s},
\qquad 0<z\leq1.
$$

Using $\Gamma(3/2)=\sqrt\pi/2$ and the thermal de Broglie wavelength

$$
\lambda_T=\frac{h}{\sqrt{2\pi m k_BT}}
=\sqrt{\frac{2\pi\hbar^2}{m k_BT}},
$$

the excited-state population becomes

$$
\boxed{N_{\rm ex}=\frac{V}{\lambda_T^3}g_{3/2}(z).}
$$

As the temperature is lowered at fixed density, the chemical potential rises toward zero and $z$ approaches one. The Bose function increases monotonically and reaches

$$
g_{3/2}(1)=\sum_{\ell=1}^{\infty}\frac{1}{\ell^{3/2}}
=\zeta(3/2)\simeq2.612.
$$

Thus, at a given temperature, the continuum of excited states has a maximum population:

$$
\boxed{N_{\rm ex}^{\rm max}
=\frac{V}{\lambda_T^3}\zeta(3/2).}
$$

The convergence of this integral at $z=1$ is crucial. It is possible in three dimensions because the low-energy density of states is proportional to $\sqrt\epsilon$.

## 5. Critical temperature

The critical temperature is reached when the excited states just hold all the particles, so that $N_0$ is negligible and $N=N_{\rm ex}^{\rm max}$. Writing $n=N/V$,

$$
n=\frac{1}{\lambda_{T_c}^3}\zeta(3/2).
$$

Substitute $\lambda_{T_c}^2=2\pi\hbar^2/(m k_BT_c)$ and solve for $T_c$:

$$
\boxed{
T_c=\frac{2\pi\hbar^2}{m k_B}
\left[\frac{n}{\zeta(3/2)}\right]^{2/3}.}
$$

This critical temperature depends on particle mass and number density. It is not a universal temperature; it is the point at which the excited-state capacity equals the total particle number for the ideal, uniform three-dimensional gas.

## 6. Condensate fraction below the transition

For $T<T_c$, the chemical potential approaches the ground-state energy, which has been set to zero. In the thermodynamic limit, $z\to1$ for the excited states, and therefore

$$
N_{\rm ex}=\frac{V}{\lambda_T^3}\zeta(3/2).
$$

Since $\lambda_T^{-3}\propto T^{3/2}$, compare this with the defining equation at $T_c$:

$$
\frac{N_{\rm ex}}{N}
=\left(\frac{T}{T_c}\right)^{3/2}.
$$

The remaining particles occupy the ground state:

$$
\boxed{
\frac{N_0}{N}
=1-\left(\frac{T}{T_c}\right)^{3/2},
\qquad T<T_c.}
$$

At $T=0$, all particles occupy the ground state in the ideal model. At $T=T_c$, the condensate fraction vanishes continuously. Above $T_c$, the chemical potential is below the ground-state energy and there is no macroscopic ground-state population.

The result is a thermodynamic-limit statement. In a finite box, the chemical potential remains strictly below the ground-state energy and the onset is rounded rather than a mathematically sharp phase transition.

## 7. Why the ground state must be separated

The continuum density of states is a good approximation for the excited spectrum in a large volume, but it does not correctly represent a single state that contains a macroscopic fraction of all particles. The ground state is one state, not a continuum of states near zero energy.

Near and below $T_c$, the excited-state integral saturates at $z\to1$. The ground-state occupation is

$$
N_0=\frac{1}{z^{-1}-1}
=\frac{z}{1-z}.
$$

For a finite system, $z<1$ and this is finite. In the thermodynamic limit below $T_c$, $N_0$ is of order $N$, while the excited-state population is described by the continuum integral. One must therefore write $N=N_0+N_{\rm ex}$ and treat these contributions separately. Replacing the ground state by a continuum contribution can hide the macroscopic occupation and lead to an incorrect particle count.

## 8. Dimensionality, finite size, and traps

The existence of ideal-gas BEC depends on the low-energy density of states. In a uniform ideal gas in $d$ dimensions, the density of states scales as $g(\epsilon)\propto\epsilon^{d/2-1}$. At $z=1$, the excited-particle integral near zero energy behaves as

$$
\int_0 \frac{\epsilon^{d/2-1}}{e^{\beta\epsilon}-1}\,d\epsilon
\sim \int_0 \epsilon^{d/2-2}\,d\epsilon.
$$

This integral converges at its lower limit only for $d>2$. Consequently, a homogeneous ideal Bose gas has no finite-temperature condensation in the thermodynamic limit in one or two dimensions. This statement concerns the uniform ideal gas; interactions, finite size, and external confinement can change the physics.

Experiments often use harmonic traps rather than uniform boxes. A trap changes the density of states and the relation between total particle number and temperature. For example, an ideal gas in a three-dimensional harmonic trap has a different critical-temperature formula and can exhibit a finite-temperature condensation transition. The uniform-box formula above must not be applied unchanged to a trapped cloud.

Finite systems also have a rounded crossover rather than a sharp thermodynamic singularity. The thermodynamic-limit formulas are accurate when the number of particles and the number of thermally occupied excited states are large.

## 9. Why liquid helium is not an ideal Bose gas

Helium-4 atoms are bosons, and liquid helium-4 becomes superfluid at low temperature. However, liquid helium is dense and strongly interacting. The ideal-gas formula for $T_c$ and the ideal condensate fraction do not quantitatively describe it. Interactions alter the excitation spectrum and the relationship between condensate fraction and superfluid density; these are distinct quantities.

Dilute ultracold atomic gases are much closer to the weakly interacting ideal-gas limit, although interactions and trapping still matter in precision comparisons. The ideal homogeneous gas is best understood as a controlled baseline model that isolates the statistical mechanism.

## 10. BEC compared with liquid–gas condensation

| Feature | Ideal-gas Bose–Einstein condensation | Classical vapour–liquid condensation |
|---|---|---|
| Essential mechanism | Bosonic quantum statistics and saturation of excited states | Intermolecular attractions, repulsion, and free-energy competition |
| Interactions required? | No; occurs in the ideal model | Yes, interactions are essential |
| Condensed state | Macroscopic occupation of one quantum state | Dense liquid phase coexisting with a dilute gas |
| Main control | Temperature and number density (plus mass and dimensionality) | Temperature, pressure, and intermolecular potential |
| Equilibrium signature | Ground-state occupation becomes macroscopic | Equality of temperature, pressure, and chemical potential in two phases |

The shared word “condensation” refers to different phenomena. The ideal-gas BEC is not a liquid droplet forming in a vapour, and the liquid–gas transition is not explained by ideal-gas Bose statistics.

## 11. Assumptions and scope

The formulas for $T_c$ and $N_0/N$ assume:

- a uniform three-dimensional gas in a box;
- non-interacting bosons of mass $m$;
- a single internal state per momentum state;
- the thermodynamic limit;
- the ground-state energy chosen as zero;
- equilibrium at fixed total number density.

For finite systems, trapped gases, lower dimensions, or interacting fluids, the density of states and/or the equation of state must be changed. The ideal-gas condensate fraction should not be interpreted as the superfluid fraction.

## 12. Summary

- The Bose occupation of a one-particle state is $[e^{\beta(\epsilon-\mu)}-1]^{-1}$, with $\mu$ below the ground-state energy.
- In a uniform three-dimensional box, $g(\epsilon)=V(2m/\hbar^2)^{3/2}\sqrt\epsilon/(4\pi^2)$.
- The excited states hold $N_{\rm ex}=Vg_{3/2}(z)/\lambda_T^3$ particles.
- At $z\to1$, their maximum population is $V\zeta(3/2)/\lambda_T^3$.
- The critical temperature is $T_c=(2\pi\hbar^2/mk_B)[n/\zeta(3/2)]^{2/3}$.
- Below $T_c$, the ideal-gas condensate fraction is $N_0/N=1-(T/T_c)^{3/2}$.
- The ground state must be separated from the continuum of excited states once it is macroscopically occupied.
- The homogeneous ideal-gas transition is specific to three dimensions in the thermodynamic limit; traps, finite size, and interactions change the analysis.

## Review questions

1. Why must the chemical potential of an ideal Bose gas remain below its ground-state energy?
2. Derive the three-dimensional density of states from the number of wave vectors inside a sphere in $k$-space.
3. Show how the integral for $N_{\rm ex}$ reduces to $Vg_{3/2}(z)/\lambda_T^3$.
4. Why does the excited-state population saturate at $z=1$ in three dimensions?
5. Derive the critical temperature and condensate fraction.
6. Why must the ground state be treated separately below the transition?
7. Why does the homogeneous ideal gas not undergo finite-temperature BEC in one or two dimensions?
8. Why is the ideal-gas condensate fraction not the same as the superfluid fraction in helium-4?
9. Contrast the microscopic mechanism of ideal-gas BEC with ordinary liquid–gas condensation.

## Further reading

- K. Huang, *Statistical Mechanics*, 2nd edition — ideal Bose gas and quantum statistics.
- R. K. Pathria and P. D. Beale, *Statistical Mechanics*, 3rd edition — Bose–Einstein condensation and the thermodynamic limit.
- L. Pitaevskii and S. Stringari, *Bose–Einstein Condensation and Superfluidity* — trapped and interacting Bose gases.
- C. J. Pethick and H. Smith, *Bose–Einstein Condensation in Dilute Gases* — dilute-gas theory and experiments.

---

*This chapter treats the uniform, non-interacting three-dimensional gas as a baseline model. It is not a quantitative model of liquid helium or a substitute for the trapped, interacting-gas theory used in experiments.*

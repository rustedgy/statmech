# Liquid–Gas Phase Transitions and Condensation

## 1. Physical picture

A gas can condense into a liquid when temperature and pressure place it in a region where a dense phase has lower thermodynamic free energy than a dilute phase. Statistical mechanics explains this transition by connecting the microscopic interactions between molecules to macroscopic thermodynamic potentials.

The essential competition is between **energy and entropy**:

- Attractive intermolecular interactions lower the energy when molecules are near one another, favouring dense configurations.
- Translational entropy favours molecules spreading through the available volume, favouring a dilute gas.
- At high temperature, thermal motion makes the entropic advantage of the gas important. At lower temperature, attraction can make a dense liquid phase favourable.

This chapter develops the classical liquid–gas transition using the canonical partition function, the van der Waals model, and equilibrium conditions for phase coexistence. It also distinguishes an equilibrium phase transition from the kinetics of nucleation.

## 2. Interacting particles in the canonical ensemble

For $N$ classical particles of mass $m$ in volume $V$, with positions $\mathbf r_i$ and momenta $\mathbf p_i$, take a Hamiltonian

$$
H=\sum_{i=1}^{N}\frac{\mathbf p_i^2}{2m}
+U(\mathbf r_1,\ldots,\mathbf r_N),
$$

where $U$ is the intermolecular potential energy. The canonical partition function is

$$
Z_N(T,V)=\frac{1}{N!h^{3N}}\int
e^{-\beta H}\,d^{3N}p\,d^{3N}r,
\qquad \beta=\frac{1}{k_BT}.
$$

The momentum integrals are Gaussian. Performing them gives

$$
\boxed{
Z_N(T,V)=\frac{1}{N!\Lambda^{3N}}
\int_V e^{-\beta U(\mathbf r_1,\ldots,\mathbf r_N)}
\,d^{3N}r,
}
$$

where $\Lambda=h/\sqrt{2\pi m k_BT}$ is the thermal de Broglie wavelength. The factor $1/N!$ accounts for indistinguishability in the classical regime.

For an ideal gas, $U=0$ and the configurational integral is simply $V^N$. Interactions change this integral by weighting each configuration according to its potential energy. Configurations with strongly repulsive overlaps receive very small weight; configurations in which attractive neighbours are close receive enhanced weight. The equation of state and free energy follow from this weighted sum over configurations.

The Helmholtz free energy is $F=-k_BT\ln Z_N$, and the pressure is

$$
p=-\left(\frac{\partial F}{\partial V}\right)_{T,N}
=k_BT\left(\frac{\partial\ln Z_N}{\partial V}\right)_{T,N}.
$$

A liquid–gas transition is therefore encoded in how the configurational integral, and hence $F$, changes with volume and temperature.

## 3. The van der Waals model

A useful first model separates two effects of molecular interactions:

1. **Repulsive cores** make part of the volume unavailable for molecular motion. If $b$ is the excluded-volume parameter per particle, the free volume is approximated by $V-Nb$.
2. **Attractions** reduce the pressure exerted on the container walls, because a molecule near the boundary is pulled back toward the fluid. In a uniform-density approximation this pressure correction is proportional to the square of the number density.

These assumptions lead to the van der Waals equation

$$
\boxed{
p=\frac{Nk_BT}{V-Nb}-a\frac{N^2}{V^2},
}
$$

where $a>0$ measures the strength of attraction and $b>0$ measures excluded volume. In terms of the molar volume $v=V/n_{\!\mathrm{mol}}$ and molar constants $a_m,b_m$, the same equation is commonly written $p=RT/(v-b_m)-a_m/v^2$. Here we use the per-particle form.

The first term is the ideal-gas pressure with $V$ replaced by the free volume. The second term is the attractive correction. When $a\to0$ and $b\to0$, the ideal-gas equation $pV=Nk_BT$ is recovered.

The model is phenomenological: it captures the qualitative competition between repulsion and attraction, but it does not calculate $a$ and $b$ exactly from an arbitrary molecular potential. A more microscopic route starts with the configurational integral above and uses approximations such as a virial expansion or a mean-field treatment of attractive interactions.

## 4. Critical point of the van der Waals fluid

At sufficiently high temperature, the van der Waals isotherm is monotonic. Below a particular temperature, it develops a region in which the pressure first decreases, then increases, and then decreases with volume. The critical point is where the two extrema merge into a horizontal inflection point:

$$
\left(\frac{\partial p}{\partial V}\right)_{T,N}=0,
\qquad
\left(\frac{\partial^2p}{\partial V^2}\right)_{T,N}=0.
$$

Writing the equation in terms of number density $n=N/V$,

$$
p=\frac{n k_BT}{1-bn}-a n^2,
$$

The derivatives are

$$
\left(\frac{\partial p}{\partial n}\right)_T
=\frac{k_BT}{(1-bn)^2}-2an,
\qquad
\left(\frac{\partial^2p}{\partial n^2}\right)_T
=\frac{2bk_BT}{(1-bn)^3}-2a.
$$

Setting both to zero, the second equation gives $k_BT=a(1-bn)^3/b$. Substituting into the first gives $a(1-bn)/b=2an$, hence $bn=1/3$. Therefore,

$$
\boxed{
n_c=\frac{1}{3b},\qquad
k_BT_c=\frac{8a}{27b},\qquad
p_c=\frac{a}{27b^2}.
}
$$

Equivalently, the critical volume per particle is $v_c=3b$. The critical compressibility factor is

$$
\boxed{\frac{p_c}{n_c k_BT_c}=\frac{3}{8}.}
$$

This value is a prediction of the van der Waals model, not a universal constant for real fluids. Real substances have different critical compressibility factors because their intermolecular potentials and correlations are more complicated.

For $T>T_c$, there is no distinct gas–liquid coexistence in this model: the fluid changes continuously from gas-like to liquid-like as it is compressed. At $T=T_c$, the distinction between the two phases disappears at the critical point. For $T<T_c$, gas and liquid can coexist at a particular pressure.

## 5. Phase coexistence: equality of chemical potential

Consider two macroscopic portions of the same substance, one gas and one liquid, able to exchange particles and volume while total particle number and total volume are fixed. At equilibrium, the temperature, pressure, and chemical potential must be equal in the two phases:

$$
\boxed{
T_g=T_l,\qquad p_g=p_l,\qquad \mu_g=\mu_l.
}
$$

The equality of temperature follows from maximizing entropy with respect to energy transfer. Equality of pressure follows from mechanical equilibrium under volume transfer. Equality of chemical potential follows from equilibrium under particle transfer.

At fixed temperature, the stable phase is the one with the lower appropriate thermodynamic potential. In the isothermal–isobaric description, the Gibbs free energy per particle is the chemical potential for a one-component fluid. At coexistence, the gas and liquid have equal chemical potentials, so neither phase can lower the total free energy by transferring particles to the other.

This is the equilibrium meaning of condensation. It is not enough for a dense arrangement to have lower interaction energy: the full free energy, including entropy, must be lower.

## 6. The van der Waals loop and Maxwell construction

For $T<T_c$, the van der Waals equation produces an S-shaped isotherm. Part of this curve has

$$
\left(\frac{\partial p}{\partial V}\right)_T>0,
$$

which corresponds to negative isothermal compressibility and mechanical instability. A homogeneous equilibrium fluid cannot occupy this portion of the isotherm.

The actual equilibrium transition occurs at a single coexistence pressure $p_{\mathrm{coex}}$. The gas and liquid coexist at two different volumes per particle, $v_g$ and $v_l$, with the same pressure and chemical potential. In the van der Waals model, the coexistence pressure is found by the **Maxwell equal-area construction**:

$$
\boxed{
\int_{v_l}^{v_g}
\big[p(v,T)-p_{\mathrm{coex}}\big],dv=0.
}
$$

### Deriving the equal-area condition from chemical-potential equality

Let $f(v,T)$ be the Helmholtz free energy per particle of a homogeneous phase, with $v=V/N$. Its differential at fixed particle number is

$$
df=-s\,dT-p\,dv,
$$

so along an isotherm, $(\partial f/\partial v)_T=-p(v,T)$. For a one-component phase, the chemical potential is the Gibbs free energy per particle,

$$
\mu=f+pv.
$$

At coexistence, the two phases have the same temperature, pressure, and chemical potential. Thus

$$
f(v_g,T)+p_{\rm coex}v_g
=f(v_l,T)+p_{\rm coex}v_l.
$$

Rearrange and use the isothermal free-energy difference:

$$
\begin{aligned}
f(v_g,T)-f(v_l,T)
&=-\int_{v_l}^{v_g}p(v,T)\,dv,\\
0&=f(v_g,T)-f(v_l,T)+p_{\rm coex}(v_g-v_l),
\end{aligned}
$$

which gives

$$
\boxed{\int_{v_l}^{v_g}[p(v,T)-p_{\rm coex}]\,dv=0.}
$$

The integrand has units of pressure and $dv$ has units of volume per particle, so the integral has units of energy per particle, as it must to compare free energies. The two signed areas between the isotherm and the coexistence-pressure line are equal.

The same result has a geometric interpretation. The straight line

$$
f_{\rm tan}(v)=\mu_{\rm coex}-p_{\rm coex}v
$$

is tangent to the homogeneous Helmholtz free-energy curve at both $v_l$ and $v_g$. Its slope is $-p_{\rm coex}$ and its intercept is the common chemical potential. This **common tangent** is the convex-envelope construction: for average volumes between $v_l$ and $v_g$, a mixture of the two phases has lower free energy than a homogeneous state on the non-convex portion of the model curve.

The equal-area condition therefore follows from equality of the chemical potentials, not from an independent geometric rule. It replaces the unphysical loop by a horizontal coexistence segment in the equilibrium pressure–volume isotherm.

The construction is a thermodynamic prescription, not a claim that a real fluid passes through every intermediate homogeneous state on the loop. In a two-phase sample, changing the total volume can change the relative amounts of liquid and gas while the pressure remains at the coexistence value.

## 7. Stability, metastability, and nucleation

It is useful to distinguish three regions below the critical temperature:

- **Stable region:** the phase has the lowest free energy. Between the coexistence volumes, the equilibrium state is a mixture of gas and liquid.
- **Metastable region:** a homogeneous gas or liquid is locally stable against small fluctuations but is not the globally stable equilibrium state. For example, a vapour can persist above its equilibrium condensation pressure as a supersaturated vapour.
- **Unstable region:** small density fluctuations grow spontaneously. In the van der Waals picture this is the region where the isothermal compressibility becomes negative.

The boundary of local stability is the **spinodal**, defined by

$$
\left(\frac{\partial p}{\partial V}\right)_T=0.
$$

The coexistence curve (the binodal) and the spinodal are not the same. Between them lies a metastable region.

A metastable vapour may condense only after a sufficiently large liquid-like droplet forms. Creating a droplet costs surface free energy, because molecules at the interface have fewer favourable neighbours. Increasing the droplet size gains bulk free energy when the liquid is the stable phase. For a spherical droplet of radius $R$, classical nucleation theory writes the free-energy change schematically as

$$
\Delta G(R)=4\pi R^2\gamma
-\frac{4\pi}{3}R^3\Delta p,
$$

where $\gamma$ is the liquid–vapour surface tension and $\Delta p>0$ represents the bulk free-energy driving force per unit volume in this simplified description. The surface term scales as $R^2$ and opposes small droplets; the bulk term scales as $R^3$ and favours growth. The critical radius is

$$
R_* = \frac{2\gamma}{\Delta p}.
$$

Droplets smaller than $R_*$ tend to shrink, while droplets larger than $R_*$ tend to grow. This explains why condensation can be delayed even when the liquid is thermodynamically favoured. The formula assumes a spherical droplet, a sharp interface with radius-independent surface tension (the capillarity approximation), a bulk driving force proportional to droplet volume, and a droplet large enough for continuum thermodynamics to apply. It neglects curvature dependence of surface tension, molecular-scale structure, and detailed interfacial profiles. Real nucleation rates also depend on fluctuations, impurities, heat transfer, and kinetic barriers; the equilibrium van der Waals equation alone does not determine the rate.

## 8. Critical behaviour and limitations of mean-field theory

As the critical point is approached, the density difference between coexisting liquid and gas tends to zero, and the distinction between the phases disappears. Density fluctuations become large and correlated over long distances. This is why the critical region cannot be described accurately by treating molecules as independent or by assuming that every region experiences only the average density.

The van der Waals model is a mean-field theory. It predicts, for example, a critical exponent $1/2$ for the order parameter (the difference between liquid and gas densities) near the critical point. Real fluids in three dimensions exhibit critical behaviour in the Ising universality class, with different exponents. The Ising model chapter provides a complementary example of how local interactions can generate collective phase transitions, while also showing why fluctuations beyond mean-field theory matter.

The van der Waals model remains valuable because it displays the central thermodynamic structure: a critical point, a coexistence curve, metastability, and the need to compare free energies. Quantitative predictions close to a real fluid's critical point require more sophisticated treatments of correlations and fluctuations.

## 9. Worked checks

### 9.1 Ideal-gas limit

Set $a=b=0$ in the van der Waals equation:

$$
p=\frac{Nk_BT}{V},
$$

which is the ideal-gas equation. This check confirms the interpretation of $a$ and $b$ as corrections due to attraction and excluded volume.

### 9.2 Critical compressibility factor

Using the critical values,

$$
\frac{p_cV_c}{Nk_BT_c}
=\frac{p_c}{n_ck_BT_c}
=\frac{a/(27b^2)}{(1/3b)(8a/27b)}
=\frac{3}{8}.
$$

The result is dimensionless and independent of $a$ and $b$ within this model.

### 9.3 Why attraction matters more at low temperature

The ratio of the attractive pressure correction to the repulsive/free-volume term is

$$
\frac{a n^2}{n k_BT/(1-bn)}
=\frac{a n(1-bn)}{k_BT}.
$$

At fixed density, this ratio grows as temperature decreases. Thus the attractive contribution becomes more important relative to thermal pressure, helping explain why cooling favours condensation. This ratio is only a qualitative guide; the actual transition is determined by equality of the full thermodynamic potentials.

## 10. Summary

- The classical canonical partition function weights configurations by their intermolecular potential energy. Attractive interactions and repulsive cores both affect the equation of state.
- The van der Waals equation models excluded volume and attraction through parameters $b$ and $a$.
- Its critical point satisfies $n_c=1/(3b)$, $k_BT_c=8a/(27b)$, and $p_c=a/(27b^2)$.
- Gas and liquid coexist when temperature, pressure, and chemical potential are equal.
- The Maxwell construction replaces the unstable van der Waals loop by a constant-pressure coexistence segment.
- Metastability and nucleation explain why condensation can be delayed even when the liquid is the equilibrium phase.
- Mean-field theory captures the qualitative transition but not the full critical fluctuations of real fluids.

## Review questions

1. Starting from the classical Hamiltonian, show how integrating over momenta gives the configurational partition function.
2. What physical effects are represented by the van der Waals parameters $a$ and $b$?
3. Derive the critical constants by applying the first- and second-derivative conditions to the van der Waals equation.
4. Why must the chemical potentials of coexisting liquid and gas be equal?
5. Explain why the van der Waals loop contains a mechanically unstable region.
6. What does the Maxwell equal-area construction enforce, and why is it equivalent to equality of chemical potentials?
7. Distinguish the binodal, spinodal, and metastable regions.
8. Why can a supersaturated vapour persist before condensation begins? Explain the role of the critical droplet.
9. What is the limitation of mean-field theory near the critical point?

## References and further reading

- R. K. Pathria and P. D. Beale, *Statistical Mechanics*, 3rd edition — classical fluids, virial expansions, and phase transitions.
- K. Huang, *Statistical Mechanics*, 2nd edition — interacting classical systems and the van der Waals theory.
- T. L. Hill, *An Introduction to Statistical Thermodynamics* — thermodynamic potentials and phase equilibrium.
- J. P. Hansen and I. R. McDonald, *Theory of Simple Liquids* — microscopic liquid-state statistical mechanics and intermolecular correlations.
- J. S. Rowlinson and B. Widom, *Molecular Theory of Capillarity* — interfaces and surface tension.
- P. G. Debenedetti, *Metastable Liquids: Concepts and Principles* — metastability, nucleation, and supercooled or supersaturated states.
- J. M. Yeomans, *Statistical Mechanics of Phase Transitions* — mean-field theory, critical phenomena, and universality.

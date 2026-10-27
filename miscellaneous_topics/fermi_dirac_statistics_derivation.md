# Fermi–Dirac Statistics: A Statistical-Mechanical Derivation

This chapter derives the Fermi–Dirac occupation law by counting allowed many-particle microstates and maximizing entropy under fixed energy and particle number. The exclusion principle enters through the allowed occupancy of one-particle states; the distribution then follows from statistical mechanics.

## 1. States, occupations, and constraints

Consider identical, non-interacting fermions in equilibrium. Let energy level \\(\epsilon_i\\) have degeneracy \\(g_i\\), meaning there are \\(g_i\\) distinct one-particle states at that energy. Let \\(n_i\\) denote the number of fermions occupying the level.

The Pauli exclusion principle permits at most one fermion in each one-particle state. Therefore,

$$
0\\leq n_i\\leq g_i.
$$

For fixed total particle number and energy,

$$
\\sum_i n_i=N, \\qquad \\sum_i n_i\\epsilon_i=E,
$$

we seek the occupation distribution corresponding to the most numerous allowed macrostate.

## 2. Count the allowed arrangements

For a level with degeneracy \\(g_i\\), choosing \\(n_i\\) occupied states from the \\(g_i\\) available states determines the arrangement. The number of choices is

$$
W_i=\\binom{g_i}{n_i}
=\\frac{g_i!}{n_i!(g_i-n_i)!}.
$$

Unlike the bosonic count, each one-particle state can be selected at most once. For a complete occupation list, independent state counting gives

$$
W(\\{n_i\\})=\\prod_i\\frac{g_i!}{n_i!(g_i-n_i)!}.
$$

This combinatorial factor is where the exclusion constraint enters the calculation.

## 3. Entropy from multiplicity

Using Boltzmann's relation \\(S=k_B\\ln W\\) and Stirling's approximation for large factorial arguments,

$$
\\begin{aligned}
\\ln W\\approx\\sum_i\\big[&
g_i\\ln g_i-n_i\\ln n_i\\\\
&-(g_i-n_i)\\ln(g_i-n_i)\\big].
\\end{aligned}
$$

Thus

$$
S\\approx k_B\\sum_i\\big[g_i\\ln g_i-n_i\\ln n_i
-(g_i-n_i)\\ln(g_i-n_i)\\big].
$$

For fixed \\(g_i\\), differentiating with respect to \\(n_i\\) gives

$$
\\frac{1}{k_B}\\frac{\\partial S}{\\partial n_i}
=\\ln\\left(\\frac{g_i-n_i}{n_i}\\right).
$$

The factor \\(g_i-n_i\\) counts the unoccupied one-particle states. Its appearance is the statistical signature of exclusion.

## 4. Maximize entropy at fixed energy and particle number

The equilibrium occupation maximizes entropy subject to the two macroscopic constraints. Introduce Lagrange multipliers \\(\\alpha\\) and \\(\\beta\\):

$$
\\Phi=S-k_B\\alpha\\sum_i n_i-k_B\\beta\\sum_i n_i\\epsilon_i.
$$

Stationarity with respect to every \\(n_i\\) requires

$$
\\frac{1}{k_B}\\frac{\\partial S}{\\partial n_i}
=\\alpha+\\beta\\epsilon_i.
$$

Substituting the entropy derivative yields

$$
\\ln\\left(\\frac{g_i-n_i}{n_i}\\right)
=\\alpha+\\beta\\epsilon_i.
$$

Exponentiating,

$$
\\frac{g_i-n_i}{n_i}=e^{\\alpha+\\beta\\epsilon_i}.
$$

Rearranging,

$$
g_i=n_i\\left(1+e^{\\alpha+\\beta\\epsilon_i}\\right),
$$

and hence

$$
n_i=\\frac{g_i}{e^{\\alpha+\\beta\\epsilon_i}+1}.
$$

At equilibrium, \\(\\beta=1/(k_BT)\\) and \\(\\alpha=-\\mu/(k_BT)\\), where \\(T\\) is temperature and \\(\\mu\\) is chemical potential. Therefore,

$$
\\boxed{n_i=\\frac{g_i}{e^{(\\epsilon_i-\\mu)/(k_BT)}+1}}.
$$

The mean occupation of an individual one-particle state is

$$
\\boxed{\\bar n(\\epsilon)=\\frac{1}{e^{(\\epsilon-\\mu)/(k_BT)}+1}}.
$$

This is the Fermi–Dirac distribution. The plus one is a direct consequence of counting only arrangements with no more than one fermion in each one-particle state.

## 5. Interpreting the result

The mean occupation per one-particle state lies between zero and one, as required by exclusion:

$$
0\\leq\\bar n(\\epsilon)\\leq1.
$$

At \\(\\epsilon=\\mu\\), the occupation is one half. For positive temperature, states far below the chemical potential are likely to be occupied, while states far above it are unlikely to be occupied.

In the zero-temperature limit for a system with a conventional ground-state filling, the distribution approaches a step:

$$
\\bar n(\\epsilon)\\longrightarrow
\\begin{cases}
1,&\\epsilon<\\mu,\\\\
0,&\\epsilon>\\mu.
\\end{cases}
$$

At zero temperature, \\(\\mu\\) approaches the Fermi energy for the usual ground state. The value exactly at the step depends on how the limiting case is represented and does not change bulk counting.

## 6. Consequences of Fermi–Dirac statistics

The distribution is more than a formula for average occupation. It predicts how fermions fill states, how temperature changes that filling, and which states can respond to a perturbation. The consequences below are especially useful when applying the distribution to electrons in solids.

### 6.1 A filled Fermi sea at zero temperature

At \\(T=0\\), the Fermi–Dirac distribution becomes a step function: every available one-particle state below the Fermi energy \\(E_F\\) is occupied, and every state above it is empty, apart from possible details of degeneracy exactly at the boundary. The filled states are often called the **Fermi sea**. This sharp boundary is a consequence of exclusion: electrons cannot gain a small amount of energy by moving into a nearby state if that state is already occupied.

### 6.2 Finite temperature smears the Fermi edge

At \\(T>0\\), the step becomes a smooth crossover. Some electrons near the Fermi energy are thermally excited into states above the chemical potential, leaving holes in states below it. The main changes occur over an energy range of order \\(k_BT\\); states many \\(k_BT\\) below or above \\(\\mu\\) remain nearly full or nearly empty, respectively.

A more precise measure comes from the peak in \\(-\\partial f/\\partial E\\), which describes how strongly occupation changes with energy. The full width at half maximum of this peak is approximately \\(3.53,k_BT\\). Thus the width of the thermally active energy window grows linearly with temperature.

### 6.3 The chemical potential is the half-occupation energy

For any positive temperature, setting \\(E=\\mu\\) in the distribution gives

$$
f(\\mu,T)=\\frac{1}{e^0+1}=\\frac12.
$$

The chemical potential is therefore the energy at which a one-particle state has occupation probability one half. It is not generally identical to the zero-temperature Fermi energy at finite temperature, although the two are close in a strongly degenerate electron gas at low temperature.

### 6.4 Electron–hole symmetry around the chemical potential

Writing the distribution as \\(f(E)=[e^{(E-\\mu)/(k_BT)}+1]^{-1}\\), direct substitution shows

$$
f(\\mu-\\Delta)+f(\\mu+\\Delta)=1.
$$

A state \\(\\Delta\\) below \\(\\mu\\) is occupied with exactly the same probability that a state \\(\\Delta\\) above \\(\\mu\\) is empty. This is a symmetry of the **occupation function**. It does not by itself imply equal total numbers of electrons and holes, because that also depends on how many states are available at each energy (the density of states).

### 6.5 The occupation changes most steeply at the chemical potential

Differentiating the distribution gives

$$
\\frac{df}{dE}=-\\frac{1}{k_BT}f(1-f).
$$

The magnitude of this slope is largest when \\(f=1/2\\), namely at \\(E=\\mu\\):

$$
\\left.\\frac{df}{dE}\\right|_{E=\\mu}
=-\\frac{1}{4k_BT}.
$$

At low temperature the edge is very sharp; increasing temperature makes it more gradual. This derivative is also important in transport and response calculations, because it identifies the energies whose occupations respond most strongly to a small change in energy.

### 6.6 Occupation fluctuations are largest at half filling

For a single fermionic state whose occupation is either zero or one, the occupation-number variance is

$$
\\operatorname{Var}(n)=\\langle n^2\\rangle-\\langle n\\rangle^2=f(1-f).
$$

This is largest at \\(f=1/2\\), where it equals \\(1/4\\). States far below \\(\\mu\\) are almost certainly occupied, and states far above it are almost certainly empty, so their occupation fluctuations are small. The largest fluctuations occur near the Fermi edge.

### 6.7 The chemical potential shifts with temperature

For a system whose total particle number is fixed, \\(\\mu\\) generally has to change as temperature smears the occupation distribution. The particle number is determined by

$$
N=\\int g(E)f(E,\\mu,T)\\,dE,
$$

where \\(g(E)\\) is the density of one-particle states. The direction and size of the shift depend on the shape of \\(g(E)\\), not just on the Fermi–Dirac function.

For a smooth density of states in the low-temperature, degenerate regime, the Sommerfeld expansion gives the leading estimate

$$
\\mu(T)\\approx E_F-\\frac{\\pi^2}{6}(k_BT)^2
\\frac{g'(E_F)}{g(E_F)}.
$$

Here \\(E_F=\\mu(0)\\). If the density of states rises with energy at \\(E_F\\), this correction is negative; if it falls, the correction is positive. This approximation assumes the density of states is sufficiently smooth near the Fermi energy and is not valid at arbitrary high temperatures.

### 6.8 Only a small fraction of electrons contribute to low-temperature heat capacity

In a metal with \\(k_BT\\ll E_F\\), most electrons lie far below the Fermi energy and cannot be thermally promoted because nearby states are occupied. Only electrons within an energy window of order \\(k_BT\\) of the Fermi surface can be rearranged thermally. Consequently, the electronic heat capacity of a simple degenerate Fermi gas is proportional to temperature at low temperatures, rather than having the classical temperature-independent value expected for a gas with all particles thermally active.

These results explain why the Fermi surface—the boundary between mostly occupied and mostly empty states—plays such a central role in the low-temperature properties of metals.

## 7. Classical limit

When \\(e^{(\\epsilon-\\mu)/(k_BT)}\\gg1\\), the plus one is negligible, giving

$$
\\bar n(\\epsilon)\\approx e^{-(\\epsilon-\\mu)/(k_BT)}.
$$

This is the Maxwell–Boltzmann limit. It applies when the occupation per one-particle state is small, so the distinction caused by exclusion is negligible for the distribution.

## 8. Comparison with Bose–Einstein counting

The derivations for bosons and fermions have the same statistical structure:

- Count microstates compatible with a proposed set of level occupations.
- Take \\(S=k_B\\ln W\\).
- Maximize entropy while enforcing fixed total energy and particle number.
- Interpret the Lagrange multipliers as inverse temperature and chemical potential.

The difference lies in the allowed occupancy and therefore the combinatorics:

$$
\\begin{array}{ll}
\\text{Bosons:}&W_i=\\dfrac{(n_i+g_i-1)!}{n_i!(g_i-1)!},\\\\[6pt]
\\text{Fermions:}&W_i=\\dfrac{g_i!}{n_i!(g_i-n_i)!}.
\\end{array}
$$

The resulting distributions differ only by the sign in the denominator:

$$
\\bar n_{\\mathrm{BE}}(\\epsilon)
=\\frac{1}{e^{(\\epsilon-\\mu)/(k_BT)}-1},
\\qquad
\\bar n_{\\mathrm{FD}}(\\epsilon)
=\\frac{1}{e^{(\\epsilon-\\mu)/(k_BT)}+1}.
$$

These signs are not arbitrary algebraic choices. They encode the different ways identical bosons and fermions may populate one-particle states.

## Summary

Fermi–Dirac statistics follows from the finite occupancy of fermionic one-particle states. For a level with degeneracy \\(g_i\\), there are \\(\\binom{g_i}{n_i}\\) ways to choose its occupied states. Maximizing the entropy derived from this multiplicity, subject to fixed energy and particle number, gives

$$
\\boxed{\\bar n_i=\\frac{1}{e^{(\\epsilon_i-\\mu)/(k_BT)}+1}}
$$

per one-particle state. The result is statistical-mechanical: it follows from allowed microstates and equilibrium constraints.

The distribution also explains the zero-temperature Fermi sea, thermal smearing and electron–hole excitations near the Fermi energy, the half-occupation property at the chemical potential, occupation fluctuations, and the temperature dependence of the chemical potential and electronic heat capacity.

## Review questions

1. How does the Pauli exclusion principle change the multiplicity for a level?
2. Why does the entropy derivative contain \\(g_i-n_i\\)?
3. Derive the Fermi–Dirac denominator by maximizing entropy with two constraints.
4. Why is the occupation one half at \\(\\epsilon=\\mu\\)?
5. Why does the occupation change most rapidly near the chemical potential?
6. What is meant by thermal smearing, and why are only states near the Fermi energy strongly affected at low temperature?
7. Why does the temperature dependence of the chemical potential depend on the density of states?
8. Under what conditions does the Fermi–Dirac distribution reduce to the Maxwell–Boltzmann form?

## Further reading

These consequences are discussed in the Bohrium Scipedia articles on the [Fermi–Dirac distribution function](https://scipedia.bohrium.com/en/sciencepedia/feynman/solid_state_physics_undergraduate-the_Fermi-Dirac_distribution_function), [Fermi–Dirac statistics and electronic density of states](https://scipedia.bohrium.com/en/sciencepedia/feynman/materials_physics_graduate-fermi_dirac_statistics_and_electronic_density_of_states), and the [Sommerfeld expansion](https://scipedia.bohrium.com/en/sciencepedia/feynman/keyword/sommerfeld_expansion). The explanations in this chapter are independently written; consult those pages for further discussion and context.

---

*This is an original supplementary derivation from statistical-mechanical state counting. It is not a transcript of any particular lecture. The Stirling approximation is appropriate for large occupation groups; exact finite systems require discrete counting.*

# Maxwell–Boltzmann Statistics

## 1. Aim and assumptions

Maxwell–Boltzmann (MB) statistics describes the distribution of particles among available single-particle energy states in the classical, dilute regime. We will derive it using only statistical-mechanical ideas: counting compatible microstates, defining entropy, and maximizing entropy subject to fixed particle number and energy.

Consider \(N\) identical classical particles in contact with a system whose accessible single-particle energy levels are grouped into energy classes. Let

- \(\epsilon_i\) be the energy of class \(i\);
- \(g_i\) be the number of distinct single-particle states in that class (its degeneracy);
- \(n_i\) be the number of particles occupying states in that class.

The constraints are

\[
\sum_i n_i=N,\qquad \sum_i n_i\epsilon_i=E.
\]

In the classical regime, the occupation of any particular single-particle state is typically small, so quantum restrictions on state occupancy do not control the distribution.

## 2. Count the compatible arrangements

For a specified set of occupation numbers \(\{n_i\}\), first imagine assigning \(N\) distinguishable particle labels to the available single-particle states. The number of assignments that produce the occupations \(\{n_i\}\) is proportional to

\[
W(\{n_i\})=\frac{N!}{\prod_i n_i!}\prod_i g_i^{n_i}.
\]

The factor \(N!/\prod_i n_i!\) counts how the particle labels are partitioned among the energy classes. Each of the \(n_i\) particles assigned to class \(i\) has \(g_i\) choices of state, giving the factor \(g_i^{n_i}\).

For identical classical particles, the common overall factor associated with relabelling particles does not affect the most probable occupation numbers. Thus this counting expression is sufficient for finding the equilibrium distribution.

The equilibrium macrostate is the one compatible with the largest number of microscopic arrangements, equivalently the one with the greatest Boltzmann entropy,

\[
S=k_B\ln W.
\]

## 3. Write the entropy

Taking the logarithm gives

\[
\ln W=\ln N!+\sum_i n_i\ln g_i-\sum_i\ln(n_i!).
\]

For large occupation numbers, Stirling's approximation is useful:

\[
\ln n!\simeq n\ln n-n.
\]

Since \(N\) is fixed, \(\ln N!\) is constant during the maximization. Therefore, apart from constants independent of the \(\{n_i\}\),

\[
\frac{S}{k_B}\simeq
\sum_i\left[n_i\ln g_i-n_i\ln n_i+n_i\right]+\text{constant}.
\]

## 4. Maximize entropy with fixed particle number and energy

We maximize \(S\) while keeping both \(N\) and \(E\) fixed. Introduce Lagrange multipliers \(\alpha\) and \(\beta\) and define

\[
\Phi=\frac{S}{k_B}
-\alpha\left(\sum_i n_i-N\right)
-\beta\left(\sum_i n_i\epsilon_i-E\right).
\]

At the maximum, the derivative with respect to each \(n_i\) vanishes. Using the entropy expression above,

\[
\frac{\partial\Phi}{\partial n_i}
=\ln g_i-\ln n_i-\alpha-\beta\epsilon_i=0.
\]

Rearranging,

\[
\ln\left(\frac{n_i}{g_i}\right)
=-\alpha-\beta\epsilon_i,
\]

so

\[
\boxed{n_i=g_i e^{-\alpha}e^{-\beta\epsilon_i}}.
\]

The number of particles in an energy class is therefore proportional to its degeneracy and decreases exponentially with energy.

The multiplier \(\beta\) is identified thermodynamically as

\[
\beta=\frac{1}{k_BT},
\]

while \(\alpha\) is related to the chemical potential by \(\alpha=-\mu/(k_BT)\). Thus the mean occupation of class \(i\) can also be written as

\[
\boxed{n_i=g_i\exp\left[-\frac{\epsilon_i-\mu}{k_BT}\right]}.
\]

This is the Maxwell–Boltzmann occupation law.

## 5. Normalize the distribution

Define the single-particle partition sum

\[
Z_1=\sum_i g_i e^{-\beta\epsilon_i}.
\]

Summing the occupation law over all energy classes and requiring \(\sum_i n_i=N\) gives

\[
N=e^{-\alpha}\sum_i g_i e^{-\beta\epsilon_i}
=e^{-\alpha}Z_1.
\]

Hence \(e^{-\alpha}=N/Z_1\), and

\[
\boxed{n_i=N\frac{g_i e^{-\beta\epsilon_i}}{Z_1}}.
\]

The probability that a particle selected from the ensemble belongs to energy class \(i\) is consequently

\[
\boxed{P_i=\frac{n_i}{N}
=\frac{g_i e^{-\beta\epsilon_i}}{Z_1}}.
\]

If individual states are indexed separately rather than grouped into energy classes, the probability of a particular single-particle state \(a\) with energy \(\epsilon_a\) is

\[
p_a=\frac{e^{-\beta\epsilon_a}}{Z_1}.
\]

Degeneracy appears in the class probability because a class with more states offers more ways for a particle to occupy that energy.

## 6. Physical interpretation

The distribution reflects two competing effects:

- **State availability:** a class with larger \(g_i\) has more states and therefore tends to contain more particles.
- **Energy cost:** at positive temperature, the factor \(e^{-\beta\epsilon_i}\) suppresses high-energy classes.

At higher temperature, \(\beta=1/(k_BT)\) is smaller, so the exponential penalty for high energies is weaker. The distribution spreads more broadly across energy levels.

The MB law is appropriate when the gas is sufficiently dilute and quantum occupation effects are negligible. It can be obtained as the low-occupation limit of both Bose–Einstein and Fermi–Dirac distributions, but the counting-and-entropy argument above derives it directly in the classical regime.

## 7. Example: equally spaced energy levels

Suppose non-degenerate levels have energies \(\epsilon_n=n\Delta\), where \(n=0,1,2,\ldots\) and \(\Delta>0\). Then \(g_n=1\) and

\[
P_n=\frac{e^{-\beta n\Delta}}{\sum_{m=0}^{\infty}e^{-\beta m\Delta}}.
\]

For \(\beta>0\), the geometric series gives

\[
Z_1=\frac{1}{1-e^{-\beta\Delta}},
\]

so

\[
\boxed{P_n=(1-e^{-\beta\Delta})e^{-\beta n\Delta}}.
\]

The ratio of probabilities for successive levels is constant:

\[
\frac{P_{n+1}}{P_n}=e^{-\beta\Delta}.
\]

As temperature increases, this ratio approaches one and higher levels become relatively more populated.

## 8. Summary

The statistical-mechanical derivation follows a short chain:

1. Specify the occupation numbers and the particle-number and energy constraints.
2. Count the microscopic arrangements compatible with those occupations.
3. Use \(S=k_B\ln W\) and Stirling's approximation.
4. Maximize entropy while enforcing fixed \(N\) and \(E\).
5. Obtain an exponential occupation law and normalize it using the partition sum.

The result is

\[
\boxed{P_i=\frac{g_i e^{-\epsilon_i/(k_BT)}}{\sum_j g_j e^{-\epsilon_j/(k_BT)}}},
\]

the Maxwell–Boltzmann distribution over energy classes.

## Review questions

1. What does the degeneracy \(g_i\) count, and why does it multiply the exponential factor?
2. Why is entropy maximized subject to both particle-number and energy constraints?
3. Where does Stirling's approximation enter the derivation?
4. How does the distribution change as temperature increases?
5. Under what physical conditions is the Maxwell–Boltzmann description appropriate?

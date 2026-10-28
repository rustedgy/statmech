# The Two-Level System and the Schottky Anomaly

## 1. Why study a two-level system?

The two-level system is one of the simplest models in statistical mechanics. Each particle can occupy one of two energy levels, making the partition function easy to calculate while still producing non-trivial temperature dependence.

Two-level approximations are useful for understanding magnetic moments in a field, atoms with two relevant states, and localized excitations in solids. A collection of two-level systems can also exhibit a characteristic heat-capacity peak known as the **Schottky anomaly**.

We begin with a single non-interacting particle with energies

\[
E_0=0,\qquad E_1=\Delta,
\]

where \(\Delta>0\) is the energy gap. For now, assume both levels are non-degenerate.

## 2. Partition function and level probabilities

The canonical partition function is the sum of the Boltzmann weights:

\[
\boxed{Z=1+e^{-\beta\Delta}},
\qquad \beta=\frac{1}{k_BT}.
\]

The probability of occupying the ground state is

\[
\boxed{P_0=\frac{1}{1+e^{-\beta\Delta}}}
\]

and the probability of occupying the excited state is

\[
\boxed{P_1=\frac{e^{-\beta\Delta}}{1+e^{-\beta\Delta}}
=\frac{1}{e^{\beta\Delta}+1}.}
\]

These probabilities sum to one. Their ratio is

\[
\frac{P_1}{P_0}=e^{-\beta\Delta},
\]

so the excited state is exponentially suppressed when \(k_BT\ll\Delta\), while both levels become equally likely when \(k_BT\gg\Delta\).

## 3. Internal energy

Taking the ground-state energy to be zero, the mean energy is the energy gap multiplied by the excited-state probability:

\[
U=E_0P_0+E_1P_1=\Delta P_1.
\]

Therefore,

\[
\boxed{
U(T)=\frac{\Delta}{e^{\Delta/(k_BT)}+1}.
}
\]

At low temperature, the system mostly occupies the ground state and \(U\to0\). At high temperature, the two levels approach equal probability and \(U\to\Delta/2\).

For \(N\) independent identical systems, the total partition function is \(Z_N=Z^N\) and the mean total energy is

\[
\boxed{
U_N=\frac{N\Delta}{e^{\Delta/(k_BT)}+1}.
}
\]

Here the particles are treated as independent distinguishable units, or equivalently as independent local two-state degrees of freedom. Interactions between them are neglected.

## 4. Heat capacity

The heat capacity at fixed external conditions is the temperature derivative of the internal energy. Introduce the dimensionless variable

\[
x=\frac{\Delta}{k_BT}.
\]

For one two-level unit,

\[
U=\frac{\Delta}{e^x+1},
\qquad
\frac{dx}{dT}=-\frac{x}{T}.
\]

Differentiate:

\[
\begin{aligned}
C_V
&=\frac{dU}{dT}\\
&=\frac{\Delta e^x}{(1+e^x)^2}\frac{x}{T}.
\end{aligned}
\]

Since \(\Delta/T=k_Bx\),

\[
\boxed{
C_V=k_Bx^2\frac{e^x}{(1+e^x)^2},
\qquad x=\frac{\Delta}{k_BT}.
}
\]

For \(N\) independent two-level units, the heat capacity is \(N\) times this result.

## 5. The Schottky anomaly

The heat capacity approaches zero at both temperature extremes, so it must have a maximum at an intermediate temperature.

### Low-temperature limit

When \(T\to0\), we have \(x\gg1\). Then

\[
e^x+1\simeq e^x
\]

and

\[
\boxed{
C_V\simeq k_Bx^2e^{-x}
=k_B\left(\frac{\Delta}{k_BT}\right)^2
e^{-\Delta/(k_BT)}.
}
\]

The exponential factor makes the heat capacity vanish rapidly: there are very few thermally excited particles available to absorb additional energy.

### High-temperature limit

When \(T\to\infty\), we have \(x\ll1\). Using \(e^x/(1+e^x)^2\to1/4\),

\[
\boxed{
C_V\simeq\frac{k_B}{4}
\left(\frac{\Delta}{k_BT}\right)^2.
}
\]

The heat capacity again tends to zero, now algebraically. At high temperature the two levels are nearly equally populated, so raising the temperature changes their probabilities only slightly.

### Temperature of the peak

Write the dimensionless heat capacity as

\[
\frac{C_V}{k_B}=x^2\frac{e^x}{(1+e^x)^2}.
\]

Setting its derivative with respect to \(x\) equal to zero gives

\[
\frac{2}{x}+1-\frac{2e^x}{1+e^x}=0,
\]

or

\[
\boxed{x\tanh\left(\frac{x}{2}\right)=2.}
\]

The positive solution is approximately \(x\approx2.40\). Consequently,

\[
\boxed{T_{\mathrm{peak}}\approx
\frac{\Delta}{2.40\,k_B}.}
\]

The maximum heat capacity per two-level unit is approximately

\[
\boxed{C_{V,\max}\approx0.439\,k_B.}
\]

This finite peak is called the **Schottky anomaly**. It occurs because the excited-state population changes most rapidly over a temperature range comparable to the energy gap.

## 6. Magnetic two-level systems

A magnetic moment in an applied magnetic field provides a physical realization of the model. For a spin-\(1/2\) magnetic moment with two field-dependent energies separated by \(\Delta\), the partition function has the same two-term form after choosing the lower energy as the zero.

The energy and heat capacity therefore follow the expressions above, with the gap determined by the field. In a simple Zeeman model, the splitting is proportional to the field magnitude, so the location of the heat-capacity peak shifts with field strength.

The same framework also explains why a collection of independent magnetic moments can have a heat capacity distinct from the lattice contribution. In real materials, interactions, distributions of energy gaps, and coupling to other degrees of freedom may broaden or alter the ideal two-level peak.

## 7. If the levels are degenerate

If the ground and excited levels have degeneracies \(g_0\) and \(g_1\), respectively, the partition function becomes

\[
\boxed{Z=g_0+g_1e^{-\beta\Delta}.}
\]

The excited-level probability is then

\[
\boxed{
P_1=\frac{g_1e^{-\beta\Delta}}
{g_0+g_1e^{-\beta\Delta}}.
}
\]

The mean energy is \(U=\Delta P_1\). The degeneracy ratio changes the temperature at which the levels have comparable total probabilities, and hence shifts the heat-capacity peak. The simple numerical peak values above apply only to the non-degenerate case \(g_0=g_1=1\).

## 8. Assumptions and limitations

- The two energy levels are treated as fixed and separated by a positive gap \(\Delta\).
- The system is in canonical thermal equilibrium.
- For many units, interactions between units are neglected.
- The basic derivation assumes non-degenerate levels; degeneracy can be included through multiplicity factors.
- The Schottky peak is a finite-level population effect, not by itself evidence of a thermodynamic phase transition.

## 9. Summary

- The non-degenerate two-level partition function is \(Z=1+e^{-\beta\Delta}\).
- The excited-state probability is \(P_1=1/(e^{\beta\Delta}+1)\).
- The mean energy is \(U=\Delta/(e^{\beta\Delta}+1)\).
- The heat capacity is \(C_V=k_Bx^2e^x/(1+e^x)^2\), with \(x=\Delta/(k_BT)\).
- The heat capacity vanishes at low and high temperatures and has a peak near \(T=\Delta/(2.40k_B)\).
- The peak is the Schottky anomaly and reflects thermal redistribution between the two energy levels.

## Review questions

1. Derive the partition function and the probabilities of the two energy levels.
2. Show that the mean energy is \(U=\Delta/(e^{\beta\Delta}+1)\).
3. Derive the heat-capacity formula in terms of \(x=\Delta/(k_BT)\).
4. Explain physically why the heat capacity tends to zero at both low and high temperatures.
5. Derive the condition \(x\tanh(x/2)=2\) for the heat-capacity maximum.
6. How does degeneracy of the two levels change the partition function and occupation probabilities?

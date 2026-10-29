# Partition Function as a Generator of Thermodynamics

## 1. The central idea

Statistical mechanics connects microscopic states to macroscopic thermodynamic properties. For a system in the canonical ensemble, the **partition function** contains the statistical weights of all accessible microstates. Once it is known, many thermodynamic quantities can be obtained by differentiating its logarithm.

For a system with microstate energies $E_r$, at temperature $T$, define

$$
\beta=\frac{1}{k_BT},
\qquad
Z(T,V,N)=\sum_r e^{-\beta E_r}.
$$

The sum includes every accessible microstate, including degeneracies. The probability of microstate $r$ is

$$
P_r=\frac{e^{-\beta E_r}}{Z}.
$$

The partition function is therefore both a normalization constant for probabilities and a compact generator of equilibrium thermodynamics.

For two independent subsystems $A$ and $B$, the joint energy is $E_{ab}=E_a+E_b$. Their partition function factorizes:
$$
Z_{AB}=\sum_{a,b}e^{-\beta(E_a+E_b)}
=\left(\sum_a e^{-\beta E_a}\right)
\left(\sum_b e^{-\beta E_b}\right)
=Z_AZ_B.
$$
Consequently, $\ln Z_{AB}=\ln Z_A+\ln Z_B$. This multiplicative rule is the reason partition functions of independent particles or independent local degrees of freedom often take a power such as $Z^N$. For identical classical particles, the additional factor $1/N!$ corrects for indistinguishability; it is not a replacement for the independence factorization.

## 2. Internal energy from the partition function

The average internal energy is the probability-weighted mean of the microstate energies:

$$
U=\langle E\rangle
=\sum_r E_r P_r
=\frac{1}{Z}\sum_r E_r e^{-\beta E_r}.
$$

Differentiate $Z$ with respect to $\beta$, holding the energy levels and other fixed external parameters constant:

$$
\frac{\partial Z}{\partial\beta}
=-\sum_r E_r e^{-\beta E_r}.
$$

Divide by $Z$ to obtain

$$
\frac{\partial\ln Z}{\partial\beta}
=\frac{1}{Z}\frac{\partial Z}{\partial\beta}
=-\langle E\rangle.
$$

Thus,

$$
\boxed{
U=-\left(\frac{\partial\ln Z}{\partial\beta}\right)_{V,N}
}
$$

This is often the fastest way to find the internal energy once $Z$ has been calculated.

## 3. Helmholtz free energy and entropy

The Helmholtz free energy is
$$
F=U-TS.
$$

We can derive its connection to $Z$ from the canonical probabilities rather than assume the result. Since
$$
P_r=\frac{e^{-\beta E_r}}{Z},
$$
taking logarithms gives
$$
\ln P_r=-\beta E_r-\ln Z.
$$
Insert this into the Gibbs entropy:
$$
\begin{aligned}
S&=-k_B\sum_r P_r\ln P_r\\
&=k_B\sum_r P_r(\beta E_r+\ln Z)\\
&=k_B(\beta U+\ln Z),
\end{aligned}
$$
where $\sum_rP_r=1$ and $U=\sum_rP_rE_r$. Then
$$
F=U-TS
=U-k_BT(\beta U+\ln Z)
=-k_BT\ln Z,
$$
because $k_BT\beta=1$. Hence
$$
\boxed{F=-k_BT\ln Z,\qquad
S=k_B(\ln Z+\beta U).}
$$

Using $U=-\partial_\beta\ln Z$, the entropy can equivalently be written
$$
\boxed{S=k_B\left(\ln Z-\beta
\frac{\partial\ln Z}{\partial\beta}\right).}
$$

So a single function, $Z$, gives the internal energy, Helmholtz free energy, and entropy.

## 4. Pressure and generalized forces

If the energy levels depend on volume, the thermodynamic pressure follows from the Helmholtz free energy:

$$
p=-\left(\frac{\partial F}{\partial V}\right)_{T,N}.
$$

Since $F=-k_BT\ln Z$,

$$
\boxed{
p=k_BT\left(\frac{\partial\ln Z}{\partial V}\right)_{T,N}.
}
$$

The same idea applies to a generalized external parameter $\lambda$. If the Hamiltonian depends on $\lambda$, the conjugate generalized force is

$$
\boxed{
X=-\left(\frac{\partial F}{\partial\lambda}\right)_T
=k_BT\left(\frac{\partial\ln Z}{\partial\lambda}\right)_T.
}
$$

For example, a magnetic field is conjugate to magnetization (with the sign and units determined by the chosen magnetic Hamiltonian). This gives a general route from a microscopic model to a macroscopic response.

## 5. Heat capacity and energy fluctuations

At fixed volume and particle number, the heat capacity is

$$
C_V=\left(\frac{\partial U}{\partial T}\right)_{V,N}.
$$

Because $\beta=1/(k_BT)$, the chain rule gives

$$
C_V=-k_B\beta^2\frac{\partial U}{\partial\beta}.
$$

Differentiate the canonical mean energy. Since
$$
\frac{\partial\ln Z}{\partial\beta}=-\langle E\rangle,
$$
a second derivative gives
$$
\begin{aligned}
\frac{\partial^2\ln Z}{\partial\beta^2}
&= -\frac{\partial\langle E\rangle}{\partial\beta}\\
&=\langle E^2\rangle-\langle E\rangle^2
=\operatorname{Var}(E).
\end{aligned}
$$
Thus $\partial U/\partial\beta=-\operatorname{Var}(E)$. Because a variance cannot be negative, this canonical relation also shows that $C_V\geq0$ when the energy levels are independent of temperature and the derivative is taken at fixed $V,N$.

Therefore,

$$
\boxed{
C_V=\frac{\langle E^2\rangle-\langle E\rangle^2}
{k_BT^2}
=\frac{\operatorname{Var}(E)}{k_BT^2}.
}
$$

This is an important physical connection: **heat capacity measures equilibrium energy fluctuations**. A system with larger energy fluctuations has a larger heat capacity, under the conditions of this canonical relation.

## 6. Worked example: a classical ideal gas

For a monatomic classical ideal gas of $N$ indistinguishable particles,

$$
Z_N(T,V)=\frac{1}{N!}
\left(\frac{V}{\lambda_T^3}\right)^N,
\qquad
\lambda_T=\frac{h}{\sqrt{2\pi m k_BT}}.
$$

Taking the logarithm gives

$$
\ln Z_N
=-\ln N!+N\ln V-3N\ln\lambda_T.
$$

Since $\lambda_T\propto T^{-1/2}$, the temperature-dependent part of $\ln Z_N$ is $(3N/2)\ln T$, up to constants independent of temperature. Differentiating with respect to $\beta$ gives

$$
\boxed{U=\frac{3}{2}Nk_BT.}
$$

The heat capacity follows immediately:

$$
\boxed{C_V=\frac{3}{2}Nk_B.}
$$

Differentiating with respect to volume gives

$$
p=k_BT\left(\frac{\partial\ln Z_N}{\partial V}\right)_{T,N}
=\frac{Nk_BT}{V},
$$

so

$$
\boxed{pV=Nk_BT.}
$$

The partition function has reproduced the ideal-gas equation of state, internal energy, and heat capacity without separately calculating each observable from the microstate probabilities.

## 7. A two-level preview

Consider a particle with two non-degenerate energy levels, $0$ and $\Delta$. Its partition function is

$$
Z=1+e^{-\beta\Delta}.
$$

The general formula $U=-\partial_\beta\ln Z$ gives

$$
U=\frac{\Delta}{e^{\beta\Delta}+1}.
$$

Differentiating with respect to temperature yields

$$
C_V=k_B(\beta\Delta)^2
\frac{e^{\beta\Delta}}{(1+e^{\beta\Delta})^2}.
$$

The heat capacity is small at very low temperatures because the excited level is rarely occupied, and small at very high temperatures because the two levels approach equal occupation and the mean energy changes only weakly with temperature. It therefore has a peak at an intermediate temperature, called the **Schottky anomaly**. The next chapter develops this example in detail.

## 8. What the partition function does—and does not—tell us

The partition function determines equilibrium properties when the energy spectrum and ensemble are specified. It does not, by itself, determine the time taken to reach equilibrium or the kinetics of a transition. Those questions require dynamical information in addition to equilibrium statistical weights.

The formulas also assume that the partition function converges and that derivatives are taken while holding the appropriate thermodynamic variables fixed. If energy levels depend on volume, field, or another parameter, that dependence must be included when differentiating.

## 9. Summary

- The canonical partition function is $Z=\sum_r e^{-\beta E_r}$.
- Internal energy: $U=-\partial_\beta\ln Z$, at fixed external parameters.
- Helmholtz free energy: $F=-k_BT\ln Z$.
- Entropy: $S=k_B(\ln Z+\beta U)$.
- Pressure: $p=k_BT\,\partial_V\ln Z$, at fixed $T,N$.
- Heat capacity: $C_V=\operatorname{Var}(E)/(k_BT^2)$.
- The partition function connects microscopic energy levels to macroscopic thermodynamics, but equilibrium information alone does not specify dynamics.

## Review questions

1. Starting from $Z=\sum_r e^{-\beta E_r}$, derive the expression for the average internal energy.
2. Explain why the Helmholtz free energy is related to $\ln Z$.
3. Derive the entropy formula $S=k_B(\ln Z+\beta U)$.
4. Show how differentiating $\ln Z$ with respect to volume gives the pressure.
5. Derive the connection between heat capacity and the variance of energy.
6. For the classical monatomic ideal gas, use the partition function to recover $U=3Nk_BT/2$ and $pV=Nk_BT$.

# Paramagnetism from the Canonical Ensemble

## 1. Aim and physical model

A paramagnet contains microscopic magnetic moments that tend to align with an applied magnetic field. Thermal agitation opposes alignment, so the magnetization depends on both the field strength and temperature.

We will derive the magnetization, magnetic susceptibility, internal energy, and heat capacity from the canonical partition function. The model is deliberately simple: it shows how familiar magnetic behaviour follows from statistical mechanics without requiring a phenomenological equation of state.

Consider \(N\) independent, identical, localized moments in a uniform magnetic field \(B\). Each moment has magnitude \(\mu\) and can point either parallel or antiparallel to the field. We neglect interactions between moments and assume that the field is externally fixed.

For one moment, the two possible energies are
\[
\epsilon_{+}=-\mu B, \qquad \epsilon_{-}=+\mu B.
\]
The label \(+\) denotes alignment with the field. We use \(B\) for the magnetic field and \(\mu\) for the moment magnitude; in SI units, the magnetic moment has units of joules per tesla.

## 2. Single-moment partition function

In the canonical ensemble, a state of energy \(E_r\) has Boltzmann weight \(e^{-\beta E_r}\), where
\[
\beta=\frac{1}{k_B T}.
\]
The partition function of one moment is therefore
\[
z=\sum_r e^{-\beta\epsilon_r}
=e^{\beta\mu B}+e^{-\beta\mu B}
=2\cosh(\beta\mu B).
\]

It is convenient to define the dimensionless field
\[
x=\beta\mu B=\frac{\mu B}{k_B T}.
\]
Then \(z=2\cosh x\).

Because the moments are independent, the partition function for \(N\) distinguishable, localized moments factorizes:
\[
Z_N=z^N=[2\cosh x]^N.
\]
The assumption of localized moments matters here: we are counting independent magnetic sites, not treating the moments as a gas of freely translating particles.

## 3. Helmholtz free energy and magnetization

The canonical Helmholtz free energy is
\[
F=-k_B T\ln Z_N
=-Nk_B T\ln[2\cosh x].
\]

The total magnetic moment along the field, or magnetization in the sense of total moment, is obtained by differentiating the free energy with respect to the field:
\[
M=-\left(\frac{\partial F}{\partial B}\right)_{T,N}.
\]
Since \(\partial x/\partial B=\beta\mu\), this gives
\[
\boxed{M=N\mu\tanh\left(\frac{\mu B}{k_B T}\right).}
\]

If magnetization is defined per unit volume, write \(m=M/V\), where \(V\) is the sample volume. The equation above is the response of the ideal, noninteracting two-state paramagnet.

The same result follows directly from probabilities. The probability that one moment is aligned is
\[
p_+=\frac{e^x}{2\cosh x},
\]
and the probability that it is anti-aligned is
\[
p_-=\frac{e^{-x}}{2\cosh x}.
\]
Thus the mean moment of one site is
\[
\langle\mu_z\rangle=\mu(p_+-p_-)=\mu\tanh x,
\]
and multiplying by \(N\) reproduces \(M\).

## 4. Weak-field limit: Curie's law

When \(x\ll1\), the expansion \(\tanh x\simeq x\) gives
\[
M\simeq N\mu\frac{\mu B}{k_B T}
=\frac{N\mu^2}{k_B T}B.
\]
The response is linear in field in this limit. Define the susceptibility with respect to \(B\) as
\[
\chi_B=\left(\frac{\partial M}{\partial B}\right)_{T,B\to0}.
\]
Then
\[
\boxed{\chi_B=\frac{N\mu^2}{k_B T}.}
\]
For a fixed number of independent moments, this is Curie's law: the weak-field susceptibility is inversely proportional to absolute temperature.

Conventions for magnetic susceptibility vary between total moment, moment per unit volume, and SI susceptibility defined relative to \(H\). The expression above uses total moment \(M\) and field \(B\); converting to a volume susceptibility or to an \(H\)-based convention introduces the corresponding volume and electromagnetic-unit factors.

The physical reason for the \(1/T\) dependence is visible in \(x=\frac{\mu B}{k_B T}\). At higher temperature, the field energy difference is smaller relative to thermal energy, so the two orientations are more nearly equally populated.

## 5. Strong-field and high-temperature limits

For \(x\gg1\), \(\tanh x\to1\), so
\[
M\to N\mu.
\]
The moments become almost completely aligned and the magnetization approaches its saturation value. It cannot grow without bound because each moment has only the two allowed orientations in this model.

At fixed field and high temperature, \(x\to0\), and
\[
M\simeq\frac{N\mu^2B}{k_BT}\to0.
\]
Thermal agitation makes the two orientations nearly equally likely. At zero field, the two states are equally populated and the net equilibrium magnetization is zero.

## 6. Internal energy

The mean energy is related to the partition function by
\[
U=-\frac{\partial\ln Z_N}{\partial\beta}\bigg|_{B,N}.
\]
At fixed \(B\), differentiating \(\ln Z_N=N\ln[2\cosh(\beta\mu B)]\) yields
\[
\boxed{U=-N\mu B\tanh x=-MB.}
\]
The energy is negative when the moments have a net alignment with the field, using the zero of energy chosen in Section 1. As the field aligns the moments, the system's energy decreases.

This derivative is taken at fixed field. If the field itself changes while the system is manipulated, work is exchanged with the source that produces the field; that is a different thermodynamic process.

## 7. Heat capacity

The heat capacity at fixed field is
\[
C_B=\left(\frac{\partial U}{\partial T}\right)_{B,N}.
\]
With \(U=-N\mu B\tanh x\) and \(x=\frac{\mu B}{k_B T}\), we have
\[
\frac{\partial x}{\partial T}=-\frac{x}{T}.
\]
Therefore
\[
\boxed{C_B=Nk_B x^2\operatorname{sech}^2 x.}
\]
This quantity is nonnegative. It tends to zero both as \(T\to\infty\) (where \(x\to0\)) and as \(T\to0^+\) at fixed nonzero field (where \(x\to\infty\)). Between these limits it has a maximum: the field-split two-level system absorbs heat most effectively when thermal energy is comparable to the level splitting. This is the two-level Schottky heat-capacity peak.

## 8. Entropy and the role of disorder

The canonical entropy is
\[
S=\frac{U-F}{T}.
\]
Substituting the expressions above gives
\[
\boxed{S=Nk_B\left[\ln(2\cosh x)-x\tanh x\right].}
\]

At zero field, \(x=0\), so \(S=Nk_B\ln2\): each independent moment has two equally probable states. At fixed nonzero field as \(T\to0^+\), the lower-energy orientation dominates, and the entropy tends to zero in this ideal model. As temperature rises, the excited orientation becomes more populated and the entropy increases.

The competition is between energy and entropy. Alignment lowers the magnetic energy, while a disordered mixture of orientations has more statistical weight. The canonical probabilities balance these effects according to the Boltzmann factor.

## 9. Assumptions and limitations

The result
\[
M=N\mu\tanh\left(\frac{\mu B}{k_BT}\right)
\]
is exact for the stated independent two-state model, but it is not a universal equation for all magnetic materials. Important limitations are:

- **Interactions:** dipole-dipole or exchange interactions between moments can produce collective behaviour, including ferromagnetic ordering, which this model cannot describe.
- **More than two orientations:** moments with larger angular momentum or quantum spin can have multiple allowed magnetic projections and lead to a Brillouin function rather than this simple hyperbolic tangent.
- **Mobile carriers and orbital effects:** the model treats localized moments only; it does not include orbital magnetic response or the translational motion of carriers.
- **Very low temperatures:** real materials may have interactions, degeneracies, or other physics absent from the ideal model.

The derivation is useful precisely because its assumptions are explicit: the partition function gives the thermodynamic response once the allowed energy levels are specified.

## 10. Summary

Starting from the canonical partition function of \(N\) independent two-state magnetic moments, we obtained
\[
Z_N=[2\cosh(\beta\mu B)]^N,
\]
\[
M=N\mu\tanh\left(\frac{\mu B}{k_BT}\right),
\qquad
\chi_B=\frac{N\mu^2}{k_BT}\quad(B\to0),
\]
\[
U=-MB,\qquad
C_B=Nk_Bx^2\operatorname{sech}^2x.
\]
Thus saturation, Curie's law, and the two-level heat-capacity peak all follow from canonical statistical mechanics.

## Review questions

1. Why does the partition function factorize as \(Z_N=z^N\) in this model?
2. Derive the magnetization both from the free energy and from the probabilities of the two orientations.
3. What approximation leads to Curie's law, and when does it fail?
4. Why does the magnetization saturate at \(N\mu\)?
5. Explain why the heat capacity vanishes in both the high-temperature and low-temperature limits.
6. Which assumption would have to be changed to describe a ferromagnetic phase transition?

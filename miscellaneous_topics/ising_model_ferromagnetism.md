# From Independent Spins to the Ising Model

## 1. Physical question

An ideal paramagnet made of independent two-state moments has a smooth magnetization response, but it cannot explain spontaneous magnetic order caused by interactions between moments. How can local interactions produce a collective phase transition?

The Ising model is a minimal statistical-mechanical model of this phenomenon. It replaces each magnetic moment with a two-valued spin and allows neighbouring spins to interact.

## 2. The microscopic model

Place spins \(s_i=\pm1\) on the sites of a lattice. The Hamiltonian is

\[
\boxed{H=-J\sum_{\langle i,j\rangle}s_is_j-h\sum_i s_i.}
\]

The first sum runs over neighbouring pairs, \(J\) is the interaction strength, and \(h\) is an external field measured in energy units. For \(J>0\), neighbouring parallel spins lower the interaction energy, so the interaction favours alignment. The field term favours spins aligned with \(h\).

For \(N\) spins, the canonical partition function is

\[
Z_N=\sum_{\{s_i=\pm1\}}e^{-\beta H(\{s_i\})},
\qquad \beta=\frac{1}{k_BT}.
\]

There are \(2^N\) possible spin configurations. Unlike the independent-spin paramagnet, the energy of a spin depends on its neighbours, so the sum generally does not factor into \(N\) identical one-spin partition functions.

## 3. Energy versus entropy

At high temperature, thermal fluctuations make many configurations accessible, and the average magnetization tends to vanish when \(h=0\). At low temperature with \(J>0\), aligned configurations have lower energy and can dominate. The central question is how this competition changes with temperature.

Define the magnetization per spin as

\[
m=\frac{1}{N}\sum_i\langle s_i\rangle.
\]

With no external field, the Hamiltonian is unchanged when every spin is reversed. Therefore a finite system in exact equilibrium has zero average magnetization at \(h=0\), unless a symmetry-breaking convention is introduced. Spontaneous magnetization refers to the thermodynamic limit in which the system can select one of two symmetry-related ordered states as the field is taken to zero.

## 4. Mean-field approximation

An exact solution is not available for every lattice. Mean-field theory approximates the influence of neighbouring spins by an average magnetization \(m\).

Suppose each site has \(q\) nearest neighbours. In a mean-field treatment, the interaction energy experienced by one spin is approximated by an effective field \(h_{\mathrm{eff}}=h+qJm\). The probability of spin \(s=\pm1\) is then proportional to \(e^{\beta s h_{\mathrm{eff}}}\). The mean spin is

\[
\langle s\rangle
=\frac{e^{\beta h_{\mathrm{eff}}}-e^{-\beta h_{\mathrm{eff}}}}
{e^{\beta h_{\mathrm{eff}}}+e^{-\beta h_{\mathrm{eff}}}}
=\tanh(\beta h_{\mathrm{eff}}).
\]

Self-consistency requires the mean of a spin to equal the magnetization used to construct the effective field:

\[
\boxed{m=\tanh\!\left(\frac{h+qJm}{k_BT}\right).}
\]

This nonlinear equation captures the possibility of a nonzero magnetization even when \(h=0\).

## 5. Critical temperature in mean-field theory

Set \(h=0\). The self-consistency equation becomes

\[
m=\tanh\!\left(\frac{qJm}{k_BT}\right).
\]

For small \(m\), use \(\tanh x\approx x-x^3/3+\cdots\). To leading order,

\[
m\approx\frac{qJ}{k_BT}m.
\]

A nonzero small-\(m\) solution can emerge when the coefficient reaches one. Mean-field theory therefore predicts

\[
\boxed{k_BT_c^{\mathrm{MF}}=qJ.}
\]

Above this temperature the only stable zero-field solution is \(m=0\). Below it, two symmetry-related nonzero solutions appear, corresponding to positive or negative spontaneous magnetization. The predicted critical temperature is an approximation; its accuracy depends on lattice dimension and fluctuations ignored by mean-field theory.

## 6. What the model teaches us

The Ising model demonstrates that collective behaviour can emerge from simple local interactions. Its key ingredients are a large number of degrees of freedom, a coupling that favours alignment, and thermal fluctuations that compete with that tendency.

It also clarifies the difference between an independent paramagnet and an interacting magnet. Independent spins respond to an external field but do not spontaneously order in this model. Interactions make the response of one spin depend on its surroundings and allow a collective ordered phase.

Mean-field theory is useful but not exact in general. In low dimensions, spatial correlations and fluctuations can be decisive; in particular, the one-dimensional nearest-neighbour Ising model with finite-range interactions has no finite-temperature spontaneous magnetization at zero field. A quantitative description of a specific material also requires more realistic microscopic interactions and degrees of freedom.

## Summary

The Ising Hamiltonian couples neighbouring two-state spins. Mean-field theory replaces neighbouring spins by their average magnetization and produces the self-consistency equation \(m=\tanh[(h+qJm)/(k_BT)]\). At zero field, it predicts a critical temperature \(k_BT_c^{\mathrm{MF}}=qJ\), illustrating how microscopic interactions can produce collective order.

## Review questions

1. What is the physical meaning of each term in the Ising Hamiltonian?
2. Why does the partition function generally fail to factorize into independent single-spin terms?
3. Derive the mean-field self-consistency equation for \(m\).
4. Use the small-\(m\) expansion of \(\tanh x\) to obtain the mean-field critical temperature.
5. Why can a finite zero-field system have zero average magnetization even when the thermodynamic system exhibits spontaneous order?
6. What physical effects are neglected by mean-field theory?

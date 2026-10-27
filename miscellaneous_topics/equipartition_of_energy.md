# Equipartition of Energy

The equipartition theorem connects temperature to the average energy stored in the microscopic degrees of freedom of a classical system. Its familiar form says that each independent quadratic term in the Hamiltonian contributes an average energy of \(k_B T/2\). The more general result applies even when the energy is **not quadratic**: a term that is homogeneous of degree \(p\) in one independent continuous variable contributes \(k_B T/p\), under the assumptions described below.

## 1. The familiar quadratic result

For a classical system in thermal equilibrium at temperature \(T\), the canonical probability density in phase space is proportional to

\[
\rho(q,p)=\frac{1}{Z}e^{-\beta H(q,p)},
\qquad \beta=\frac{1}{k_B T},
\]

where \(H\) is the Hamiltonian and \(Z\) is the classical partition function.

A standard quadratic contribution to the energy has the form

\[
H_x=\frac{a x^2}{2}, \qquad a>0.
\]

Equipartition gives

\[
\boxed{\langle H_x\rangle=\frac{1}{2}k_B T}.
\]

For example, each Cartesian momentum component of a nonrelativistic particle contributes

\[
\left\langle\frac{p_x^2}{2m}\right\rangle
=\left\langle\frac{p_y^2}{2m}\right\rangle
=\left\langle\frac{p_z^2}{2m}\right\rangle
=\frac{1}{2}k_B T.
\]

Thus the mean translational kinetic energy in three dimensions is \(3k_B T/2\). A harmonic potential \(\tfrac12 kx^2\) contributes another \(k_B T/2\) for its one quadratic coordinate. The counting is by independent quadratic terms, not simply by the number of particles.

## 2. The general equipartition identity

The canonical distribution lets us derive a more general result. Let \(x\) be one continuous phase-space variable, and suppose the partition integral converges and the probability density vanishes sufficiently rapidly at the integration boundaries. Integrating a total derivative gives

\[
0=\int \frac{\partial}{\partial x}
\left(x e^{-\beta H}\right)\,d\Gamma,
\]

where \(d\Gamma\) denotes integration over all phase-space variables. Expanding the derivative,

\[
0=\int \left(1-\beta x\frac{\partial H}{\partial x}\right)
e^{-\beta H}\,d\Gamma.
\]

Dividing by the partition function yields

\[
1-\beta\left\langle x\frac{\partial H}{\partial x}\right\rangle=0.
\]

Therefore,

\[
\boxed{\left\langle x\frac{\partial H}{\partial x}\right\rangle=k_B T.}
\]

This is the general classical equipartition identity. It does not require the Hamiltonian to be quadratic or even separable. However, for a complicated Hamiltonian it constrains the average of \(x\,\partial H/\partial x\), which need not equal the average of a simple energy term. To turn it into a statement about a particular contribution to the energy, we use the form of that contribution.

## 3. When the energy is a power rather than a quadratic

Suppose the Hamiltonian depends on one variable through a confining power-law term

\[
H_x=a|x|^p,\qquad a>0,\quad p>0.
\]

Away from \(x=0\),

\[
x\frac{\partial H_x}{\partial x}=p\,a|x|^p=pH_x.
\]

If this is the only \(x\)-dependent contribution to \(H\), the general identity gives

\[
p\langle H_x\rangle=k_B T,
\]

or

\[
\boxed{\langle H_x\rangle=\frac{1}{p}k_B T.}
\]

The exponent \(p\), rather than a universal factor of two, determines the average energy for this one-variable term.

- **Quadratic term** \(H_x=ax^2\): \(p=2\), so \(\langle H_x\rangle=k_B T/2\).
- **Quartic term** \(H_x=ax^4\): \(p=4\), so \(\langle H_x\rangle=k_B T/4\).
- **Sixth-power term** \(H_x=ax^6\): \(p=6\), so \(\langle H_x\rangle=k_B T/6\).

More generally, if a contribution \(H_j\) is homogeneous of degree \(p\) in \(d\) independent coordinates, Euler's theorem gives \(\sum_{a=1}^{d}x_a\,\partial H_j/\partial x_a=pH_j\). Applying the identity to each coordinate and summing gives

\[
\boxed{\langle H_j\rangle=\frac{d}{p}k_B T,}
\]

provided the contribution is homogeneous in those coordinates and the stated canonical boundary conditions hold.

## 4. Example: a quartic oscillator

Consider a one-dimensional classical particle with Hamiltonian

\[
H(x,p)=\frac{p^2}{2m}+\lambda x^4,
\qquad \lambda>0.
\]

There are two energy contributions, but they have different powers:

- The kinetic energy is quadratic in momentum, so \(\left\langle p^2/(2m)\right\rangle=k_B T/2\).
- The potential energy is quartic in position, so \(\langle\lambda x^4\rangle=k_B T/4\).

Consequently, the mean total energy is

\[
\boxed{\langle H\rangle=\frac{3}{4}k_B T.}
\]

If the classical model remains valid and \(m\) and \(\lambda\) are temperature-independent, its mean energy has heat capacity

\[
\boxed{C_V=\frac{\partial\langle H\rangle}{\partial T}
=\frac{3}{4}k_B.}
\]

Compare this with the ordinary harmonic oscillator, whose kinetic and quadratic potential terms each contribute \(k_B T/2\), giving \(\langle H\rangle=k_B T\) and \(C_V=k_B\). The difference arises because the potential energy in the quartic oscillator grows as the fourth power of displacement, not the second.

## 5. A broader result for homogeneous Hamiltonians

Suppose a classical Hamiltonian is a sum of independent contributions, each homogeneous in its own set of variables:

\[
H=\sum_j H_j,\qquad H_j(\lambda x_1,\ldots,\lambda x_{d_j})
=\lambda^{p_j}H_j(x_1,\ldots,x_{d_j}).
\]

Under the canonical assumptions above, each contribution satisfies

\[
\boxed{\langle H_j\rangle=\frac{d_j}{p_j}k_B T.}
\]

Here \(d_j\) is the number of independent continuous variables in that homogeneous group and \(p_j\) is its degree. The familiar theorem follows by setting every \(p_j=2\). Summing the contributions gives

\[
\boxed{\langle H\rangle=k_B T\sum_j\frac{d_j}{p_j}.}
\]

This formula is useful when the energy contains several different powers. It also shows why one should not assign \(k_B T/2\) to every variable automatically: the power-law degree matters.

## 6. Assumptions and limitations

Equipartition is a classical equilibrium result, not a universal rule for every physical system.

1. **Classical continuous variables:** The derivation integrates over continuous phase space. Quantum energy levels can invalidate classical equipartition, especially when level spacings are large compared with \(k_B T\).
2. **A canonical equilibrium distribution:** The system is described by a Boltzmann weight at a well-defined temperature.
3. **Convergent integrals and suitable boundaries:** The integration-by-parts boundary term must vanish. A non-confining power law or a restricted domain may require a more careful treatment.
4. **Constraints:** Constraints can reduce the number of independent degrees of freedom or couple them. Count only independent variables and verify that the relevant boundary and constraint terms are handled correctly.
5. **Energy dependence:** The simple formula \(\langle H_j\rangle=d_j k_B T/p_j\) requires a homogeneous contribution of degree \(p_j\) in the stated variables. For a general nonseparable Hamiltonian, the robust statement is \(\langle x\,\partial H/\partial x\rangle=k_B T\), not necessarily an average energy for each term.

## 7. Summary

The classical equipartition theorem has a familiar quadratic form and a broader power-law form:

\[
\boxed{\text{one quadratic term}\ \longrightarrow\ \frac12 k_B T}
\]

\[
\boxed{H_x=a|x|^p\ \longrightarrow\ \langle H_x\rangle=\frac{1}{p}k_B T}
\]

The underlying identity is

\[
\boxed{\left\langle x\frac{\partial H}{\partial x}\right\rangle=k_B T.}
\]

For a homogeneous contribution of degree \(p\) in \(d\) independent variables, this becomes \(\langle H_j\rangle=d k_B T/p\). Thus the factor \(1/2\) is a special consequence of quadratic energy, not the most general result.

## Review questions

1. What assumptions are needed to derive the general equipartition identity by integration by parts?
2. Why does a quartic potential contribute \(k_B T/4\), rather than \(k_B T/2\), for one coordinate?
3. Derive the mean energy and heat capacity of the classical quartic oscillator.
4. How does the result change for a homogeneous energy contribution of degree \(p\) in \(d\) independent variables?
5. Give two reasons why the classical equipartition theorem may fail in a real physical system.

---

*This is an original supplementary chapter written for this repository. It presents the classical canonical result; consult a standard statistical-mechanics text for treatments of constraints, quantum corrections, and noncanonical ensembles.*

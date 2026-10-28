# Debye Model of a Solid

## 1. The physical question

Why does the heat capacity of a crystalline solid fall far below the classical Dulong–Petit value at low temperature, and why does it approach a value proportional to (T^3) as (T\to 0)?

The Einstein model treats every atom as an independent quantum harmonic oscillator with the same frequency. It correctly predicts a strong low-temperature suppression of heat capacity, but its single-frequency spectrum gives an exponentially small heat capacity at low (T). Experiments on many insulating crystals instead show an approximate cubic law, (C_V\propto T^3), over a low-temperature range.

The Debye model improves the description by treating vibrations as collective normal modes (phonons) and approximating their low-frequency spectrum by that of sound waves in a continuum.

## 2. Assumptions and model

Consider a three-dimensional solid containing (N) atoms. In the harmonic approximation, the vibrational modes are independent quantum oscillators. Each mode of angular frequency \(\omega\) has energies

\[
E_n=\hbar\omega\left(n+\frac12\right),\qquad n=0,1,2,\ldots
\]

The zero-point contribution does not depend on temperature, so it does not contribute to the heat capacity. The thermal energy of one mode is therefore

\[
\bar E(\omega)=\frac{\hbar\omega}{e^{\beta\hbar\omega}-1},
\qquad \beta=\frac{1}{k_BT}.
\]

The Debye approximation makes two central assumptions:

1. At sufficiently low frequencies, the dispersion relation is approximately linear, \(\omega=v_s k\), as for sound waves.
2. The continuum spectrum is cut off at a maximum Debye frequency \(\omega_D\), chosen so that the total number of vibrational modes is exactly \(3N\) for a three-dimensional solid.

Real crystals have multiple branches, anisotropy, and deviations from linear dispersion at large wave number. The Debye model compresses these details into an effective sound speed and a cutoff.

## 3. Counting vibrational modes

For a single acoustic branch in a large three-dimensional volume \(V\), the number of wave vectors with magnitude less than \(k\) is approximately

\[
\mathcal N(k)=\frac{V}{(2\pi)^3}\frac{4\pi k^3}{3}
=\frac{Vk^3}{6\pi^2}.
\]

If we use an effective sound speed \(v_s\) and count the three acoustic polarizations together, the number of modes with angular frequency below \(\omega\) is

\[
\mathcal N(\omega)=\frac{V\omega^3}{2\pi^2v_s^3}.
\]

Differentiating gives the Debye density of states,

\[
g(\omega)=\frac{d\mathcal N}{d\omega}
=\frac{3V\omega^2}{2\pi^2v_s^3},
\qquad 0\leq\omega\leq\omega_D.
\]

Here the effective sound speed represents an average over longitudinal and transverse sound speeds. More generally, the prefactor can be written using a polarization-averaged speed.

The cutoff is fixed by requiring \(3N\) modes in total:

\[
\int_0^{\omega_D}g(\omega)\,d\omega=3N.
\]

With the effective-speed form above, this gives

\[
\omega_D^3=\frac{6\pi^2N}{V}v_s^3.
\]

The associated Debye temperature is defined by

\[
\Theta_D=\frac{\hbar\omega_D}{k_B}.
\]

It is a material-dependent energy scale expressed as a temperature. It marks the crossover between the low-temperature regime, where only low-frequency modes are excited, and the high-temperature regime, where nearly all modes are thermally populated.

## 4. Internal energy and heat capacity

Summing the thermal energy over all modes gives

\[
U(T)=\int_0^{\omega_D}g(\omega)
\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\,d\omega.
\]

Substitute \(x=\hbar\omega/(k_BT)\). Since \(\omega_D\hbar/(k_BT)=\Theta_D/T\), the internal energy becomes

\[
U(T)=9Nk_BT\left(\frac{T}{\Theta_D}\right)^3
\int_0^{\Theta_D/T}\frac{x^3}{e^x-1}\,dx.
\]

This expression describes the thermal vibrational energy in the Debye approximation; the temperature-independent zero-point energy has been omitted.

At constant volume, the heat capacity is \(C_V=(\partial U/\partial T)_V\). Differentiating the integral expression yields

\[
C_V=9Nk_B\left(\frac{T}{\Theta_D}\right)^3
\int_0^{\Theta_D/T}
\frac{x^4e^x}{(e^x-1)^2}\,dx.
\]

This is the Debye heat-capacity formula. In general, the integral is evaluated numerically. Its limiting forms show the main physics.

## 5. Low-temperature limit: the cubic law

When \(T\ll\Theta_D\), the upper integration limit \(\Theta_D/T\) is large. The integral can be extended to infinity with exponentially small error:

\[
\int_0^{\infty}\frac{x^4e^x}{(e^x-1)^2}\,dx
=\frac{4\pi^4}{15}.
\]

Consequently,

\[
\boxed{C_V\simeq\frac{12\pi^4}{5}Nk_B
\left(\frac{T}{\Theta_D}\right)^3},
\qquad T\ll\Theta_D.
\]

Thus the Debye model predicts \(C_V\propto T^3\). The physical reason is that only long-wavelength, low-frequency acoustic modes can be appreciably excited at low temperatures. In three dimensions, their density of states scales as \(g(\omega)\propto\omega^2\), which leads to the cubic temperature dependence.

This result applies to the phonon contribution in an insulating crystal over the regime where the continuum and harmonic approximations are good. In metals, an electronic contribution proportional to \(T\) can also be important at sufficiently low temperatures.

## 6. High-temperature limit: Dulong–Petit law

When \(T\gg\Theta_D\), the thermally relevant values of \(x=\hbar\omega/(k_BT)\) are small. For a single oscillator,

\[
\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}
\simeq k_BT.
\]

There are \(3N\) vibrational modes, so

\[
U\simeq 3Nk_BT,
\qquad
\boxed{C_V\longrightarrow 3Nk_B}.
\]

This is the Dulong–Petit law, also obtained from classical equipartition: each of the \(3N\) harmonic modes contributes \(k_B\) to the heat capacity. The approach to this limit is gradual, and the quantum formula is needed when temperature is not large compared with \(\Theta_D\).

## 7. Comparison with the Einstein model

| Feature | Einstein model | Debye model |
|---|---|---|
| Vibrational spectrum | All modes have one frequency | Continuum of frequencies up to \(\omega_D\) |
| Low-temperature heat capacity | Exponentially suppressed | \(C_V\propto T^3\) |
| High-temperature limit | \(3Nk_B\) | \(3Nk_B\) |
| Main strength | Simple quantum model; useful for optical modes | Captures low-frequency acoustic modes in crystals |
| Main limitation | Misses the acoustic spectrum and cubic low-(T\) law | Approximate continuum spectrum and cutoff; not a full crystal-dynamics calculation |

The models are complementary approximations rather than mutually exclusive theories. Einstein-like oscillators can be useful for localized or optical vibrations, while Debye physics is especially important for low-frequency acoustic modes.

## 8. Assumptions and limitations

- The crystal is treated in the harmonic approximation, so phonon–phonon interactions and thermal expansion are neglected.
- The low-frequency dispersion is approximated as linear and the density of states as proportional to \(\omega^2\).
- A sharp cutoff is imposed to obtain exactly \(3N\) modes.
- A single effective sound speed simplifies the different longitudinal and transverse branches.
- The model predicts the lattice heat capacity at constant volume. Measured heat capacity at constant pressure can differ, particularly when thermal expansion is significant.
- At very low temperatures, defects, boundaries, electrons in metals, and other excitations may add contributions not included in the basic model.

## 9. Summary

The Debye model treats a solid's vibrations as phonon modes with a continuum density of states. Linear acoustic dispersion in three dimensions gives \(g(\omega)\propto\omega^2\); imposing a cutoff ensures there are \(3N\) modes. Integrating the Bose occupation energy over this spectrum produces the Debye heat capacity. It recovers the Dulong–Petit limit at high temperature and predicts the experimentally important cubic law \(C_V\propto T^3\) at low temperature.

## 10. Review questions

1. Why does the Einstein model fail to predict the observed cubic low-temperature heat capacity of many insulating solids?
2. How does linear dispersion in three dimensions lead to a density of states proportional to \(\omega^2\)?
3. Why is the Debye cutoff chosen so that the total number of modes is \(3N\)?
4. Derive the low-temperature scaling of the Debye heat capacity and identify where the numerical coefficient comes from.
5. How does the high-temperature limit recover the Dulong–Petit law?
6. Name two assumptions of the Debye model that can limit its accuracy for a real crystal.

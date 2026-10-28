# Blackbody Radiation from Quantum Statistics

## 1. Physical question

A blackbody absorbs incident radiation and, in thermal equilibrium, emits a spectrum determined only by its temperature. Classical physics predicts too much energy at high frequencies. Quantum statistical mechanics resolves this problem by treating electromagnetic modes as quantized excitations.

This chapter derives Planck's radiation law by combining the density of electromagnetic modes with the Bose–Einstein mean occupation of each mode.

## 2. Electromagnetic modes in a cavity

Consider electromagnetic radiation in a large cavity of volume \(V\) at temperature \(T\). A mode of frequency \(\nu\) can contain \(n=0,1,2,\ldots\) photons, with energy \(E_n=nh\nu\), ignoring the temperature-independent zero-point contribution.

Photons are bosons, and their number is not conserved in thermal equilibrium. Their chemical potential is therefore zero. The partition function for one mode is the geometric series

\[
z_\nu=\sum_{n=0}^{\infty}e^{-\beta nh\nu}
=\frac{1}{1-e^{-\beta h\nu}},
\qquad \beta=\frac{1}{k_BT}.
\]

The mean number of photons in a mode follows from the geometric distribution:

\[
\bar n_\nu
=\frac{\sum_{n=0}^{\infty}n e^{-\beta nh\nu}}
{\sum_{n=0}^{\infty}e^{-\beta nh\nu}}
=\frac{1}{e^{\beta h\nu}-1}.
\]

This is the Bose–Einstein occupation factor for photons.

## 3. Count the modes

For a large three-dimensional cavity, counting wave vectors in reciprocal space gives a density of electromagnetic modes per unit volume per unit frequency,

\[
g(\nu)=\frac{8\pi\nu^2}{c^3}.
\]

The factor includes the two independent polarizations of electromagnetic waves. Thus \(g(\nu)\,d\nu\) is the number of modes per unit volume with frequencies between \(\nu\) and \(\nu+d\nu\), in the large-cavity limit.

Each mode has mean thermal energy \(h\nu\bar n_\nu\). Multiplying the number of modes by the mean energy per mode yields the spectral energy density:

\[
u(\nu,T)=g(\nu)\,h\nu\,\bar n_\nu.
\]

Substituting the expressions above gives Planck's law per unit frequency:

\[
\boxed{
u(\nu,T)=\frac{8\pi h\nu^3}{c^3}
\frac{1}{e^{h\nu/(k_BT)}-1}.
}
\]

Here \(u(\nu,T)\,d\nu\) is the radiation energy per unit volume in the frequency interval \(d\nu\).

## 4. Classical and high-frequency limits

Define the dimensionless ratio \(y=h\nu/(k_BT)\).

### Low-frequency limit: Rayleigh–Jeans law

When \(y\ll1\), \(e^y-1\approx y\). Planck's law becomes

\[
u(\nu,T)\approx\frac{8\pi\nu^2}{c^3}k_BT.
\]

This is the Rayleigh–Jeans result. It agrees with classical equipartition at low frequency, where the quantum \(h\nu\) is small compared with thermal energy.

### High-frequency limit: Wien form

When \(y\gg1\), the denominator is approximately \(e^y\), giving

\[
u(\nu,T)\approx\frac{8\pi h\nu^3}{c^3}e^{-h\nu/(k_BT)}.
\]

The exponential suppression makes the total energy finite. By contrast, extending the Rayleigh–Jeans expression to arbitrarily high frequency gives an infinite integral, the classical ultraviolet catastrophe.

## 5. Total energy and temperature scaling

The total radiation energy density is obtained by integrating over all frequencies:

\[
u_{\mathrm{tot}}(T)=\int_0^\infty u(\nu,T)\,d\nu.
\]

With the substitution \(x=h\nu/(k_BT)\),

\[
u_{\mathrm{tot}}(T)=
\frac{8\pi k_B^4T^4}{h^3c^3}
\int_0^\infty\frac{x^3}{e^x-1}\,dx.
\]

The integral equals \(\pi^4/15\), so

\[
\boxed{u_{\mathrm{tot}}(T)=aT^4,\qquad
a=\frac{8\pi^5k_B^4}{15h^3c^3}.}
\]

The fourth-power dependence is the basis of the Stefan–Boltzmann law for thermal radiation. The spectrum's peak also shifts to higher frequency as temperature rises; differentiating Planck's spectrum gives Wien's displacement law \(\nu_{\max}\propto T\) for the peak when plotted per unit frequency.

## 6. Why quantization matters

The result comes from two ingredients: the number of available electromagnetic modes and the mean quantum occupation of each mode. Mode counting alone does not determine the spectrum; the Bose–Einstein factor supplies the high-frequency suppression that classical equipartition lacks.

The formula \(u(\nu,T)\) is a spectral density per unit frequency. A spectrum expressed per unit wavelength has a different functional form because changing variables requires the Jacobian \(|d\nu/d\lambda|=c/\lambda^2\). Peaks in the frequency and wavelength representations therefore do not transform by simply replacing \(\nu\) with \(c/\lambda\).

## Summary

Quantized electromagnetic modes have mean photon occupation \(1/(e^{h\nu/(k_BT)}-1)\). Multiplying this by the mode density and photon energy gives Planck's law. Its low-frequency limit reproduces classical radiation, while its high-frequency exponential cutoff resolves the ultraviolet catastrophe. Integrating the spectrum yields the \(T^4\) law for total radiation energy density.

## Review questions

1. Why is the photon chemical potential zero in thermal equilibrium?
2. Derive the mean occupation of a single electromagnetic mode.
3. Where does the factor \(8\pi\nu^2/c^3\) enter the derivation?
4. Recover the Rayleigh–Jeans law from Planck's formula.
5. Why does the classical ultraviolet catastrophe disappear?
6. Why must a spectrum per unit wavelength include a Jacobian when converting from frequency?

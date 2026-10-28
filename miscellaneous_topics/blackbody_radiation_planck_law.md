# Blackbody Radiation and Planck's Law

## 1. Physical question

A blackbody absorbs incident radiation and, in thermal equilibrium, emits a spectrum determined only by its temperature. Classical physics predicts too much energy at high frequencies. Quantum statistical mechanics resolves this problem by treating electromagnetic modes as quantized excitations.

This chapter derives Planck's radiation law by combining the density of electromagnetic modes with the Bose–Einstein mean occupation of each mode.

## 2. Electromagnetic modes in a cavity

Consider electromagnetic radiation in a large cavity of volume $V$ at temperature $T$. A mode of frequency $\nu$ can contain $n=0,1,2,\ldots$ photons, with energy $E_n=nh\nu$, ignoring the temperature-independent zero-point contribution.

Photons are bosons, and their number is not conserved in thermal equilibrium. Their chemical potential is therefore zero. The partition function for one mode is the geometric series

$$
z_\nu=\sum_{n=0}^{\infty}e^{-\beta nh\nu}
=\frac{1}{1-e^{-\beta h\nu}},
\qquad \beta=\frac{1}{k_BT}.
$$

The mean number of photons in a mode follows from the geometric distribution:

$$
\bar n_\nu
=\frac{\sum_{n=0}^{\infty}n e^{-\beta nh\nu}}
{\sum_{n=0}^{\infty}e^{-\beta nh\nu}}
=\frac{1}{e^{\beta h\nu}-1}.
$$

This is the Bose–Einstein occupation factor for photons.

## 3. Count the modes

For a large cavity, count standing-wave modes in a cube of volume $V=L^3$. The allowed wave-vector components are approximately $k_x=n_x\pi/L$, $k_y=n_y\pi/L$, and $k_z=n_z\pi/L$, with positive integers. Each mode is a lattice point in the positive octant of $k$-space. For one polarization, the number of modes in a thin shell is the octant shell volume divided by the volume per lattice point:
$
d\mathcal N_{\text{one pol.}}\simeq \frac18(4\pi k^2\,dk)\frac{V}{\pi^3}=\frac{Vk^2}{2\pi^2}\,dk.
$
Electromagnetic waves have two independent transverse polarizations, so
$
d\mathcal N=\frac{Vk^2}{\pi^2}\,dk.
$
Using $k=2\pi\nu/c$ and $dk=(2\pi/c)d\nu$, then dividing by $V$, gives
$
\boxed{g(\nu)=\frac1V\frac{d\mathcal N}{d\nu}=\frac{8\pi\nu^2}{c^3}.}
$
Thus $g(\nu)\,d\nu$ counts both polarizations in the frequency interval $[\nu,\nu+d\nu]$. Finite-cavity boundary corrections are negligible in the large-volume limit.

Each mode has mean thermal energy $h\nu\bar n_\nu$. Multiplying the number of modes by the mean energy per mode yields the spectral energy density:

$$
u(\nu,T)=g(\nu)\,h\nu\,\bar n_\nu.
$$

Substituting the expressions above gives Planck's law per unit frequency:

$$
\boxed{
u(\nu,T)=\frac{8\pi h\nu^3}{c^3}
\frac{1}{e^{h\nu/(k_BT)}-1}.
}
$$

Here $u(\nu,T)\,d\nu$ is the radiation energy per unit volume in the frequency interval $d\nu$.

## 4. Classical and high-frequency limits

Define the dimensionless ratio $y=h\nu/(k_BT)$.

### Low-frequency limit: Rayleigh–Jeans law

When $y\ll1$, $e^y-1\approx y$. Planck's law becomes

$$
u(\nu,T)\approx\frac{8\pi\nu^2}{c^3}k_BT.
$$

This is the Rayleigh–Jeans result. It agrees with classical equipartition at low frequency, where the quantum $h\nu$ is small compared with thermal energy.

### High-frequency limit: Wien form

When $y\gg1$, the denominator is approximately $e^y$, giving

$$
u(\nu,T)\approx\frac{8\pi h\nu^3}{c^3}e^{-h\nu/(k_BT)}.
$$

The exponential suppression makes the total energy finite. By contrast, extending the Rayleigh–Jeans expression to arbitrarily high frequency gives an infinite integral, the classical ultraviolet catastrophe.

## 5. Total energy and temperature scaling

The total radiation energy density is obtained by integrating over all frequencies:

$$
u_{\mathrm{tot}}(T)=\int_0^\infty u(\nu,T)\,d\nu.
$$

With the substitution $x=h\nu/(k_BT)$,

$$
u_{\mathrm{tot}}(T)=
\frac{8\pi k_B^4T^4}{h^3c^3}
\int_0^\infty\frac{x^3}{e^x-1}\,dx.
$$

The integral equals $\pi^4/15$, so

$$
\boxed{u_{\mathrm{tot}}(T)=aT^4,\qquad
a=\frac{8\pi^5k_B^4}{15h^3c^3}.}
$$

The energy density is not itself the emitted power per unit area. For isotropic radiation, angular averaging over the outgoing hemisphere gives the flux $F=cu_{\mathrm{tot}}/4$. Therefore
$
F=\frac{c}{4}aT^4=\sigma T^4,\qquad
\boxed{\sigma=\frac{ca}{4}=\frac{2\pi^5k_B^4}{15h^3c^2}=5.670\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}.}
$
This is the Stefan–Boltzmann law. The frequency spectrum peaks where $x=h\nu/(k_BT)$ solves $3(1-e^{-x})=x$, with positive solution $x\simeq2.82144$. Thus
$
\boxed{h\nu_{\max}=2.821\,k_BT.}
$
This Wien peak constant applies to a spectrum plotted per unit frequency. A spectrum per unit wavelength has a different peak because changing variables introduces a Jacobian.

## 6. Why quantization matters

The result comes from two ingredients: the number of available electromagnetic modes and the mean quantum occupation of each mode. Mode counting alone does not determine the spectrum; the Bose–Einstein factor supplies the high-frequency suppression that classical equipartition lacks.

The formula $u(\nu,T)$ is a spectral density per unit frequency. A spectrum expressed per unit wavelength has a different functional form because changing variables requires the Jacobian $|d\nu/d\lambda|=c/\lambda^2$. Peaks in the frequency and wavelength representations therefore do not transform by simply replacing $\nu$ with $c/\lambda$.

## Summary

Quantized electromagnetic modes have mean photon occupation $1/(e^{h\nu/(k_BT)}-1)$. Multiplying this by the mode density and photon energy gives Planck's law. Its low-frequency limit reproduces classical radiation, while its high-frequency exponential cutoff resolves the ultraviolet catastrophe. Integrating the spectrum yields the $T^4$ law for total radiation energy density.

## Review questions

1. Why is the photon chemical potential zero in thermal equilibrium?
2. Derive the mean occupation of a single electromagnetic mode.
3. Where does the factor $8\pi\nu^2/c^3$ enter the derivation?
4. Recover the Rayleigh–Jeans law from Planck's formula.
5. Why does the classical ultraviolet catastrophe disappear?
6. Why must a spectrum per unit wavelength include a Jacobian when converting from frequency?

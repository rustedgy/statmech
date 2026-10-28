# Maxwell–Boltzmann Speed Distribution

## 1. Physical question

A gas at equilibrium has a well-defined temperature, but its molecules do not all move at the same speed. Why is there a distribution of speeds, and how does temperature determine its shape?

This chapter derives the distribution of molecular speeds for a dilute, classical ideal gas in thermal equilibrium. It complements the chapter on Maxwell–Boltzmann **occupation statistics**: here the focus is the distribution of molecular velocities and speeds.

## 2. Microscopic model

Consider a molecule of mass $m$ whose translational kinetic energy is

$$
E=\frac{1}{2}m(v_x^2+v_y^2+v_z^2).
$$

In the canonical ensemble, the probability density in velocity space is proportional to the Boltzmann factor $e^{-\beta E}$, where $\beta=1/(k_BT)$. Normalizing the three independent velocity components gives

$$
p(v_x,v_y,v_z)=
\left(\frac{m}{2\pi k_BT}\right)^{3/2}
\exp\left[-\frac{m(v_x^2+v_y^2+v_z^2)}{2k_BT}\right].
$$

This is a probability density per unit volume in velocity space. The components are independent Gaussian random variables, each with mean zero and variance $k_BT/m$.

## 3. From velocity to speed

The speed is $v=\sqrt{v_x^2+v_y^2+v_z^2}$, so it is nonnegative. All velocity vectors whose endpoints lie between radii $v$ and $v+dv$ occupy a spherical shell in velocity space with volume $4\pi v^2\,dv$.

Because the velocity density depends only on $v$, the probability that the speed lies in this interval is the density at radius $v$ multiplied by the shell volume:

$$
f(v)\,dv=4\pi v^2p(v)\,dv.
$$

Therefore the Maxwell–Boltzmann speed distribution is

$$
\boxed{
f(v)=4\pi\left(\frac{m}{2\pi k_BT}\right)^{3/2}
v^2e^{-mv^2/(2k_BT)},\qquad v\geq0.
}
$$

The factor $v^2$ is essential: even though the probability density of each velocity component is largest at zero, there are many more velocity-space directions in a shell at a larger radius. The exponential eventually wins, so the speed distribution rises from zero, reaches a maximum, and then decays.

The distribution is normalized:

$$
\int_0^\infty f(v)\,dv=1.
$$

Thus $f(v)\,dv$ is the fraction of molecules with speeds between $v$ and $v+dv$. The density $f(v)$ itself has units of inverse speed.

## 4. Characteristic speeds

Different averages answer different questions.

### Most probable speed

The most probable speed maximizes $f(v)$. Differentiating its logarithm for $v>0$,

$$
\frac{d}{dv}\ln f(v)=\frac{2}{v}-\frac{mv}{k_BT}=0,
$$

so

$$
\boxed{v_{\mathrm{mp}}=\sqrt{\frac{2k_BT}{m}}.}
$$

### Mean speed

The mean is obtained by integrating the speed against its probability density:

$$
\langle v\rangle=\int_0^\infty vf(v)\,dv.
$$

Using the Gaussian integral gives

$$
\boxed{\langle v\rangle=\sqrt{\frac{8k_BT}{\pi m}}.}
$$

### Root-mean-square speed

The root-mean-square speed is $\sqrt{\langle v^2\rangle}$. Equipartition assigns mean energy $k_BT/2$ to each of the three translational quadratic degrees of freedom:

$$
\frac12m\langle v^2\rangle=\frac32k_BT.
$$

Therefore

$$
\boxed{v_{\mathrm{rms}}=\sqrt{\frac{3k_BT}{m}}.}
$$

These are not interchangeable quantities. They obey $v_{\mathrm{mp}}<\langle v\rangle<v_{\mathrm{rms}}$.

## 5. Temperature and molecular mass

All three characteristic speeds scale as $\sqrt{T/m}$. Raising the temperature broadens the distribution and shifts it towards higher speeds. At the same temperature, lighter molecules have higher characteristic speeds than heavier molecules.

If the horizontal axis is rescaled by the thermal speed $\sqrt{k_BT/m}$, the distribution has the same dimensionless shape for every ideal classical gas. The mass and temperature set the speed scale, not the shape in rescaled coordinates.

## 6. Assumptions and limits

The derivation assumes a dilute classical gas in thermal equilibrium, with nonrelativistic translational kinetic energy. Quantum degeneracy becomes important when the phase-space density is high; strong interactions can also change the simple ideal-gas description. The distribution describes equilibrium speeds, not the time-dependent relaxation towards equilibrium.

## Summary

The canonical Boltzmann factor gives a Gaussian distribution for each velocity component. Counting the spherical shell of velocity states introduces the $4\pi v^2$ factor and produces the Maxwell–Boltzmann speed distribution. Its characteristic speeds scale as $\sqrt{k_BT/m}$, connecting microscopic motion directly to temperature and molecular mass.

## Review questions

1. Why is each velocity component Gaussian in the canonical ensemble?
2. Why does the speed distribution contain a factor $v^2$?
3. Derive the most probable speed by maximizing $f(v)$.
4. Use equipartition to derive the root-mean-square speed.
5. How would the speed distribution change if the molecular mass doubled at fixed temperature?
6. Explain why the most probable, mean, and root-mean-square speeds are different.

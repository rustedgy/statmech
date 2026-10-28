# Newton's Law of Cooling: Equilibrium, Direction, and Linear Response

Newton's law of cooling states that, under suitable conditions, the temperature of a body approaches the temperature of its surroundings exponentially:

$$
\boxed{\frac{dT}{dt}=-\gamma\,(T-T_{\mathrm{bath}})}
$$

Here $T$ is the body's temperature, $T_{\mathrm{bath}}$ is the temperature of a large environment that remains effectively constant, and $\gamma>0$ is a relaxation rate. Statistical mechanics does **not** determine this rate from equilibrium probabilities alone. It identifies the equilibrium fixed point, explains the statistically preferred direction of net energy transfer, and shows why a smooth response is linear to leading order near equilibrium. Exponential cooling additionally requires one relaxation mode to dominate, or a suitable one-mode dynamical model to apply.

This chapter separates these equilibrium and near-equilibrium conclusions from the dynamical assumptions needed for a quantitative cooling law. An exactly solvable two-level model illustrates when exponential energy relaxation holds, while lumped-body and radiation examples show how to estimate a rate in practice.

## 1. The system and its thermal environment

Consider a body that can exchange energy with a much larger thermal reservoir. Let the body's energy be $E$, its temperature be $T$, and the reservoir temperature be $T_{\mathrm{bath}}$. Assume:

1. The body is internally close enough to equilibrium that it can be assigned a single temperature at each time.
2. The body and reservoir are weakly coupled, so each has a meaningful approximate equilibrium state between energy-transfer events.
3. The reservoir is large enough that its temperature changes negligibly.
4. The energy-transfer dynamics are sufficiently rapid and memoryless on the timescale of the body's macroscopic relaxation.
5. We study a regime close enough to equilibrium that the response can be linearized.

The first two assumptions allow us to use equilibrium statistical mechanics to describe the states of the body and reservoir. The later assumptions are dynamical: equilibrium state counting alone does not specify how quickly the system approaches equilibrium.

For a body in equilibrium at fixed volume and particle number, its canonical probabilities are

$$
P_i(T)=\frac{e^{-\beta E_i}}{Z(T)},
\qquad
\beta=\frac{1}{k_B T},
\qquad
Z(T)=\sum_i e^{-\beta E_i}.
$$

Its mean energy is

$$
U(T)=\langle E\rangle
=\sum_i P_i(T)E_i.
$$

The heat capacity at fixed volume is

$$
C_V=\left(\frac{\partial U}{\partial T}\right)_{V,N}.
$$

If the temperature difference is small and the heat capacity varies little over the range of interest, a small change in mean energy and temperature are related by

$$
\delta U \simeq C_V\,\delta T.
$$

This relation will convert an energy-relaxation law into a temperature-relaxation law.

## 2. Why equilibrium is the final state

Statistical mechanics identifies the equilibrium state by its probability distribution, not by a preferred direction of individual microscopic motions. A body warmer than its surroundings does not transfer energy only from hot to cold at the microscopic level: individual exchanges can occur in either direction. What differs is the statistical balance between the two directions.

For a body and a reservoir exchanging a small amount of energy, the total entropy change associated with energy $\delta Q$ flowing from the body to the reservoir is, to first order,

$$
\delta S_{\mathrm{tot}}
\simeq -\frac{\delta Q}{T}
+\frac{\delta Q}{T_{\mathrm{bath}}}
=\delta Q\left(\frac{1}{T_{\mathrm{bath}}}-\frac{1}{T}\right).
$$

If $T>T_{\mathrm{bath}}$, this expression is positive for net energy transfer from the body to the reservoir. If $T<T_{\mathrm{bath}}$, the statistically favored net transfer is in the opposite direction. At equilibrium, $T=T_{\mathrm{bath}}$, the first-order entropy change vanishes and the net heat current is zero.

This argument explains the direction of net relaxation near equilibrium. It does **not** by itself determine the rate or prove that the temperature difference decays exponentially. For that, we need a model of the microscopic dynamics.

## 3. Microscopic transition rates and detailed balance

Let the body's possible energy eigenstates be labelled by $i$, with energies $E_i$. Coupling to the reservoir allows transitions $i\to j$. In a Markov description, the probabilities obey a master equation,

$$
\frac{dP_i}{dt}
=\sum_j\left[W_{j\to i}P_j-W_{i\to j}P_i\right],
$$

where $W_{i\to j}$ is the transition rate from state $i$ to state $j$.

When the reservoir is at temperature $T_{\mathrm{bath}}$, microscopic reversibility leads, under the usual equilibrium assumptions, to the detailed-balance relation

$$
W_{i\to j}P_i^{\mathrm{eq}}
=W_{j\to i}P_j^{\mathrm{eq}},
\qquad
P_i^{\mathrm{eq}}
=\frac{e^{-\beta_{\mathrm{bath}}E_i}}{Z_{\mathrm{bath}}},
\qquad
\beta_{\mathrm{bath}}=\frac{1}{k_B T_{\mathrm{bath}}}.
$$

Detailed balance says that at equilibrium each transition is balanced by its reverse. It does not mean that microscopic transitions stop; rather, their probability currents cancel in the equilibrium distribution.

After a small perturbation away from equilibrium, write

$$
P_i(t)=P_i^{\mathrm{eq}}+\delta P_i(t).
$$

Linearizing the master equation around equilibrium gives a linear system for the perturbations. Its solutions can be expressed as sums of decaying modes, schematically,

$$
\delta P_i(t)=\sum_\alpha c_\alpha v_i^{(\alpha)}e^{-t/\tau_\alpha},
$$

where the relaxation times $\tau_\alpha$ depend on the transition rates and on the coupling to the reservoir. The equilibrium mode does not decay; the other modes decay when the dynamics are relaxing and ergodic over the relevant states.

The mean-energy deviation is a weighted sum of these modes:

$$
\delta U(t)=\sum_i E_i\,\delta P_i(t).
$$

In general, this is a sum of exponentials, not necessarily a single exponential. **Newton's law follows when one slow mode dominates the energy relaxation**, or when the dynamics reduce effectively to a single relaxation time:

$$
\boxed{\frac{d\,\delta U}{dt}=-\frac{\delta U}{\tau_R}.}
$$

Here $\tau_R$ is an effective energy-relaxation time. Its value is set by microscopic transition rates, which depend on the interaction between the body and its environment.

## 4. From energy relaxation to Newton's law

Close to equilibrium, let

$$
\delta T(t)=T(t)-T_{\mathrm{bath}},
\qquad
\delta U(t)=U(t)-U(T_{\mathrm{bath}}).
$$

For nearly constant heat capacity,

$$
\delta U(t)\simeq C\,\delta T(t).
$$

If the energy deviation obeys the single-mode relaxation law

$$
\frac{d\,\delta U}{dt}=-\frac{\delta U}{\tau_R},
$$

then

$$
C\frac{d\,\delta T}{dt}
=-\frac{C\,\delta T}{\tau_R}.
$$

For $C\ne0$, this gives

$$
\boxed{\frac{dT}{dt}
=-\gamma(T-T_{\mathrm{bath}}),\qquad
\gamma=\frac{1}{\tau_R}.}
$$

Solving the differential equation,

$$
\boxed{T(t)-T_{\mathrm{bath}}
=\big[T(0)-T_{\mathrm{bath}}\big]e^{-\gamma t}.}
$$

This is Newton's law of cooling. The exponential is not a universal consequence of entropy alone. It results from a near-equilibrium linearization together with effectively single-time-scale relaxation.

The same result can be expressed in terms of heat current. Define $\dot Q_{\mathrm{out}}$ as the net rate at which energy leaves the body. A linear-response description gives

$$
\dot Q_{\mathrm{out}}\simeq G(T-T_{\mathrm{bath}}),
$$

where $G>0$ is the thermal conductance for the specified body–reservoir contact. Energy balance gives

$$
\frac{dU}{dt}=-\dot Q_{\mathrm{out}}.
$$

Using $dU/dt\simeq C\,dT/dt$,

$$
C\frac{dT}{dt}=-G(T-T_{\mathrm{bath}}),
$$

so

$$
\boxed{\gamma=\frac{G}{C},
\qquad \tau_R=\frac{C}{G}.}
$$

This form makes the physical parameters transparent. A larger heat capacity means more energy must be transferred to change the temperature by a given amount, so cooling is slower. A larger conductance means energy is exchanged more readily, so cooling is faster.

Statistical mechanics determines equilibrium distributions and constrains the allowed transition rates. A microscopic interaction model is needed to calculate $G$ or $\tau_R$ quantitatively.

## 5. Timescale separation and an exactly solvable model

A single temperature for the whole body is justified when internal equilibration is much faster than energy exchange with the surroundings. Let $\tau_{\mathrm{int}}$ be a characteristic time for internal temperature gradients to relax, and let $\tau_{\mathrm{bath}}$ be the time over which the body exchanges an appreciable fraction of its thermal energy with the environment. The lumped-temperature approximation requires

$$
\tau_{\mathrm{int}}\ll \tau_{\mathrm{bath}}.
$$

If this separation fails, different parts of the body can have different temperatures and multiple thermal modes contribute. Even when internal equilibration is fast, a single exponential is not automatic: it also requires one slow mode to dominate or a dynamical model with one relevant relaxation time.

### An exact two-level example

Consider $N$ independent two-level units, each with ground-state energy $0$ and excited-state energy $\epsilon$. Each unit exchanges energy with a bath at fixed temperature $T_{\mathrm{bath}}$. Let $p(t)$ be the probability that one unit is excited. Suppose the bath induces upward and downward transitions with constant rates $w_+$ and $w_-$, respectively. The rate equation is

$$
\frac{dp}{dt}=w_+(1-p)-w_-p=-(w_++w_-)(p-p_{\mathrm{eq}}),
$$

where $p_{\mathrm{eq}}=w_+/(w_++w_-)$. Detailed balance requires

$$
\frac{w_+}{w_-}=e^{-\epsilon/(k_BT_{\mathrm{bath}})},
$$

so $p_{\mathrm{eq}}=[1+e^{\epsilon/(k_BT_{\mathrm{bath}})}]^{-1}$, the canonical excited-state probability. The mean energy is $U(t)=N\epsilon p(t)$, and therefore

$$
\boxed{\frac{dU}{dt}=-\frac{U-U_{\mathrm{bath}}}{\tau}},
\qquad
\tau=\frac{1}{w_++w_-},
$$

with $U_{\mathrm{bath}}=N\epsilon p_{\mathrm{eq}}$. This exponential is exact for this Markov model, not merely a near-equilibrium approximation. The rate depends on the transition rates; detailed balance fixes their ratio but not their overall scale. More complicated systems generally have several relaxation modes.

### Why a linear heat current is plausible

Near equilibrium, a small temperature difference is a small thermodynamic driving force. If the heat current is a smooth function of the two temperatures and vanishes when they are equal, its leading expansion has the form $J=G(T-T_{\mathrm{bath}})$, with $G>0$ for passive heat transfer. Higher-order terms matter farther from equilibrium. This is a linear-response statement; it is not justified by assuming that carrier arrival rates are temperature-independent. In kinetic transport, both the energy distribution of carriers and their arrival rates can vary with temperature, and both contribute to the conductance $G.

## 6. Entropy production and the sign of the heat current

The linear heat-current law is consistent with the second law. Let

$$
J=\dot Q_{\mathrm{out}}=G(T-T_{\mathrm{bath}}).
$$

The entropy change rate of the body due to this heat loss is approximately $-J/T$, while that of the reservoir is $J/T_{\mathrm{bath}}$. Thus the total entropy production rate is

$$
\dot S_{\mathrm{tot}}
=J\left(\frac{1}{T_{\mathrm{bath}}}-\frac{1}{T}\right).
$$

Substituting the linear-response current,

$$
\dot S_{\mathrm{tot}}
=G(T-T_{\mathrm{bath}})
\left(\frac{1}{T_{\mathrm{bath}}}-\frac{1}{T}\right)
=\frac{G(T-T_{\mathrm{bath}})^2}{TT_{\mathrm{bath}}}
\ge 0,
$$

for positive temperatures and $G\ge0$. The net transfer therefore moves the combined system toward equilibrium while producing nonnegative entropy.

Near equilibrium, write $T=T_{\mathrm{bath}}+\Delta T$, with $|\Delta T|\ll T_{\mathrm{bath}}$. Then

$$
\dot S_{\mathrm{tot}}
\simeq \frac{G}{T_{\mathrm{bath}}^2}(\Delta T)^2\ge0.
$$

The entropy production is second order in the small temperature difference, while the heat current is first order. This is the usual structure of near-equilibrium irreversible thermodynamics.

## 7. When Newton's law is expected to work—and when it fails

The simple exponential law is a useful approximation when:

- the body has a well-defined, nearly uniform internal temperature;
- the reservoir temperature is effectively constant;
- the temperature difference is small enough for linear response;
- the heat capacity and effective thermal conductance vary little during relaxation;
- one relaxation time dominates the observable energy or temperature deviation.

It may fail or need modification when:

- the temperature difference is large, so the current is nonlinear in $T-T_{\mathrm{bath}}$;
- internal temperature gradients are important, so the body cannot be treated as a single uniform-temperature lump. For a solid with thermal conductivity $k$, surface heat-transfer coefficient $h$, and characteristic length $L_c=V/A$, a common criterion is the Biot number $\mathrm{Bi}=hL_c/k\ll1$ (often taken as $\mathrm{Bi}<0.1$). This means internal conduction is fast compared with heat transfer at the surface;
- radiation dominates. Unlike a phenomenological cooling coefficient, the ideal-blackbody $T^4$ law has a statistical-mechanical derivation: the Planck spectrum in [Blackbody Radiation and Planck's Law](blackbody_radiation_planck_law.md) follows from Bose statistics for photons (with $\mu=0$) and electromagnetic mode counting. Integrating that spectrum gives

  $$
  u_{\mathrm{rad}}(T)=aT^4,
  \qquad
  a=\frac{8\pi^5 k_B^4}{15h^3c^3},
  $$

  and isotropic angular averaging gives the outward flux $F=cu_{\mathrm{rad}}/4=\sigma T^4$, where $\sigma=ac/4$. For a blackbody exchanging radiation with a large blackbody environment, the net power is therefore $P_{\mathrm{net}}=\sigma A(T^4-T_{\mathrm{bath}}^4)$. A grey-body approximation introduces the additional material factor $\varepsilon$:

  $$
  P_{\mathrm{net}}\simeq\varepsilon\sigma A(T^4-T_{\mathrm{bath}}^4).
  $$

  Near $T_{\mathrm{bath}}$, write $T=T_{\mathrm{bath}}+\Delta T$ and linearize:

  $$
  T^4-T_{\mathrm{bath}}^4\simeq4T_{\mathrm{bath}}^3\Delta T.
  $$

  Energy balance, $C\,dT/dt=-P_{\mathrm{net}}$, then gives

  $$
  \boxed{\gamma_{\mathrm{rad}}=\frac{4\varepsilon\sigma A T_{\mathrm{bath}}^3}{C}}.
  $$

  Thus the $T^4$ dependence is derived from photon statistics and mode counting; the emissivity factor and the applicability of a single-temperature cooling model are additional physical assumptions.
- the body's interior is not in local equilibrium and different regions have different temperatures;
- several slow modes contribute, producing a sum of exponentials;
- the environment itself warms or cools appreciably;
- the microscopic dynamics have memory or are far from equilibrium.

For example, consider $250\,\mathrm{mL}$ of coffee, approximated as $0.25\,\mathrm{kg}$ of water. Its heat capacity is about $C=mc_p\simeq1.05\times10^3\,\mathrm{J/K}$. If convection, conduction through the cup, radiation, and other losses together give an illustrative effective conductance $G_{\mathrm{eff}}\simeq1\,\mathrm{W/K}$ near room temperature, then

$
\tau\simeq\frac{C}{G_{\mathrm{eff}}}\simeq1.05\times10^3\,\mathrm{s}\approx17\,\mathrm{min}.
$

This is an order-of-magnitude illustration, not a universal coffee-cooling time: the effective conductance depends strongly on cup geometry, lid, airflow, evaporation, and temperature. If $C$ or the conductance depends strongly on temperature, the energy-balance equation is instead

$
C(T)\frac{dT}{dt}=-\dot Q(T,T_{\mathrm{bath}}),
$

which need not have an exponential solution.

## 8. Summary

From a statistical-mechanical viewpoint, the strongest general conclusions are the **equilibrium fixed point**, the preferred direction of net energy transfer, and the linear leading response near equilibrium. Detailed balance makes the bath's equilibrium distribution stationary, but it does not determine the relaxation rate. Exponential cooling follows when a single relaxation mode dominates; the two-level model above demonstrates one exact case. With approximately constant heat capacity, this gives

$$
\boxed{\frac{dT}{dt}
=-\gamma(T-T_{\mathrm{bath}})}
$$

and

$$
\boxed{T(t)-T_{\mathrm{bath}}
=[T(0)-T_{\mathrm{bath}}]e^{-\gamma t}.}
$$

Equivalently, a linear-response heat current $J=G(T-T_{\mathrm{bath}})$ combined with energy balance gives $\gamma=G/C$. The microscopic interaction determines the relaxation rate; statistical mechanics explains the equilibrium state, the preferred direction of net transfer, and why linear relaxation is natural close to equilibrium. The law is therefore well motivated, but conditional—not a universal exact law for every cooling process.

## Review questions

1. Why does the entropy change favor net energy flow from a warmer body to a cooler reservoir?
2. What does detailed balance mean, and why does it not imply that microscopic transitions stop at equilibrium?
3. Why does a general master equation produce a sum of decaying modes rather than necessarily one exponential?
4. Derive Newton's cooling equation from $J=G(T-T_{\mathrm{bath}})$ and $dU/dt=-J$.
5. Explain why a larger heat capacity slows cooling if the conductance stays fixed.
6. Why must internal equilibration be faster than bath exchange for the lumped-body model to apply, and how does the Biot number express this condition?
7. Derive the exact relaxation time of the two-level model and explain why detailed balance does not fix its numerical value.
8. Linearize $T^4-T_{\mathrm{bath}}^4$ near the bath temperature and obtain the radiative relaxation rate.
9. Give two physical situations in which Newton's simple exponential law is not expected to hold.

---

*This is an original supplementary chapter written for this repository. The derivation uses equilibrium statistical mechanics and near-equilibrium relaxation theory; the numerical cooling rate requires a microscopic model of the body's coupling to its environment.*
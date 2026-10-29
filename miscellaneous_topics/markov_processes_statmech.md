# Markov Processes in Statistical Mechanics

Markov processes describe systems whose future evolution depends on their present state, rather than on the full history that led there. They are useful for modeling stochastic dynamics such as molecular transitions, spin flips, diffusion between coarse-grained states, and relaxation toward thermal equilibrium.

A Markov model is a dynamical description, not an equilibrium ensemble by itself. Its transition rates specify how the system moves between states; equilibrium statistical mechanics can constrain those rates, for example through detailed balance.

## 1. The Markov property

Let (X_t) denote the state of a system at time (t). The Markov property says that, conditioned on the current state, the future is independent of the earlier history:

$$
\Pr(X_{t+\Delta t}=j\mid X_t=i,X_{t_1},\ldots)
=\Pr(X_{t+\Delta t}=j\mid X_t=i),
$$

where all earlier times (t_1,\ldots<t). The state must contain enough information for this property to be a good model. If important hidden variables or memory effects are omitted, the reduced process may not be Markovian.

Two common types are:

- **Discrete-time Markov chain:** the state changes at steps (n=0,1,2,\ldots), described by transition probabilities.
- **Continuous-time Markov process:** transitions can occur at any time, described by rates per unit time.

## 2. Discrete-time chains and transition matrices

For a discrete-time process, define

$$
P_{ij}=\Pr(X_{n+1}=j\mid X_n=i).
$$

Each row is a probability distribution:

$$
P_{ij}\geq 0,\qquad \sum_j P_{ij}=1.
$$

Using a row vector (p_i(n)=\Pr(X_n=i)), the probability distribution evolves as

$$
p_j(n+1)=\sum_i p_i(n)P_{ij},
\qquad \boldsymbol p(n+1)=\boldsymbol p(n)P.
$$

A stationary distribution \(\boldsymbol\pi\) obeys

$$
\boldsymbol\pi=\boldsymbol\pi P.
$$

If the chain is finite and irreducible and aperiodic, its distribution converges to a unique stationary distribution from any initial distribution. Without such conditions, convergence or uniqueness need not hold.

## 3. Continuous-time processes and the master equation

For a continuous-time process, let (w_{i\to j}\) be the transition rate from state (i) to state (j), with units of inverse time. For (i\ne j), the probability of a transition (i\to j) during a sufficiently short interval (dt) is approximately (w_{i\to j}dt).

The master equation is

$$
\frac{dp_i}{dt}
=\sum_{j\ne i}\left[p_jw_{j\to i}-p_iw_{i\to j}\right].
$$

The first term counts probability flowing into state (i); the second counts probability flowing out. Summing over all states gives (d(\sum_i p_i)/dt=0), so total probability is conserved.

It is often convenient to define a generator (Q), using the row-vector convention above, by

$$
Q_{ij}=w_{i\to j}\quad(i\ne j),\qquad
Q_{ii}=-\sum_{j\ne i}w_{i\to j}.
$$

Then (\dot{\boldsymbol p}=\boldsymbol p Q). The off-diagonal entries are nonnegative, and every row of (Q) sums to zero. Other texts use column probability vectors and transpose this convention; always check the chosen convention.

## 4. Stationarity and detailed balance

A stationary distribution (\pi_i) satisfies

$$
\sum_{j\ne i}\left[\pi_jw_{j\to i}-\pi_iw_{i\to j}\right]=0
$$

for every state (i). This condition says that total probability inflow balances total outflow. A stronger condition, **detailed balance**, requires balance for each pair:

$$
\pi_iw_{i\to j}=\pi_jw_{j\to i}.
$$

Detailed balance implies stationarity, but stationarity does not always imply detailed balance: a system can have steady probability currents around cycles.

For a system coupled to a heat bath at temperature (T), equilibrium state probabilities are often canonical,

$$
\pi_i=\frac{e^{-\beta E_i}}{Z},\qquad
\beta=\frac{1}{k_BT}.
$$

Detailed balance then requires

$$
\frac{w_{i\to j}}{w_{j\to i}}
=\frac{\pi_j}{\pi_i}
=e^{-\beta(E_j-E_i)}.
$$

Thus detailed balance fixes the ratio of forward and reverse rates, not their common overall scale. Many different dynamical models can share the same equilibrium distribution while relaxing at different speeds.

## 5. Worked example: a thermally activated two-state system

Consider a system with a ground state of energy (0) and an excited state of energy \(\epsilon>0\). Let (p(t)) be the probability of being excited. Write (w_+\) for the rate from ground to excited and (w_-\) for the reverse rate.

The master equation is

$$
\frac{dp}{dt}=w_+(1-p)-w_-p.
$$

Rearranging,

$$
\frac{dp}{dt}=w_+-(w_++w_-)p.
$$

At stationarity,

$$
p_{\mathrm{eq}}=\frac{w_+}{w_++w_-}.
$$

If the rates obey detailed balance with a bath at temperature (T),

$$
\frac{w_+}{w_-}=e^{-\beta\epsilon},
\qquad
p_{\mathrm{eq}}=\frac{1}{1+e^{\beta\epsilon}}.
$$

The solution at time (t), starting from (p(0)), is

$$
p(t)=p_{\mathrm{eq}}+
[p(0)-p_{\mathrm{eq}}]e^{-(w_++w_-)t}.
$$

The relaxation time is therefore

$$
\tau=\frac{1}{w_++w_-}.
$$

The equilibrium occupation is determined by the ratio of the rates, while the relaxation time depends on their sum. This is a simple exact example of exponential relaxation arising from a Markov process.

For (N) independent copies with excitation energy \(\epsilon\), the mean energy is (U(t)=N\epsilon p(t)). If the bath temperature is fixed, then

$$
\frac{dU}{dt}=-\frac{U-U_{\mathrm{eq}}}{\tau}.
$$

This is the same mathematical form as a one-mode cooling law. The result follows exactly for this two-state Markov model; it is not a universal law for every many-body system.

## 6. Connecting Markov processes to statistical mechanics

The equilibrium ensemble tells us the probability of each state under specified constraints. A Markov process supplies a possible rule for how those probabilities evolve in time. The two descriptions connect when the transition rates are chosen so that the desired equilibrium distribution is stationary.

Common applications include:

- **Spin-flip dynamics:** a spin in an Ising model flips with a rate depending on the energy change.
- **Kinetic Monte Carlo:** stochastic transitions are sampled using specified rates to simulate time-dependent processes.
- **Chemical reactions:** states represent molecular populations or reaction configurations, and rates describe transitions.
- **Diffusion and hopping:** states represent sites or coarse-grained positions, with transitions between neighboring sites.
- **Thermal relaxation:** energy levels exchange energy with a bath, and detailed balance sets the equilibrium occupations.

A Markov description is only as good as its states and rates. It may fail when transitions have memory, when hidden variables matter, or when a coarse-grained state does not have well-defined transition rates independent of history. Equilibrium detailed balance alone also does not determine the absolute rates or the time scale.

## Summary

A Markov process models stochastic evolution with no dependence on the earlier past once the current state is specified. Discrete-time chains use transition probabilities; continuous-time processes use rates and obey a master equation. Stationary distributions describe long-time balance, and detailed balance is a sufficient pairwise condition for equilibrium. In statistical mechanics, detailed balance connects stochastic dynamics to Boltzmann probabilities, while the rates determine how quickly equilibrium is approached.

# Statistical Mechanics: Principles and Applications

This is a developing book of self-contained chapters on the concepts, methods, and applications of statistical mechanics. The organization is thematic rather than tied to a particular lecture series. Part and chapter numbers are intentionally omitted so the structure can evolve as the book grows.

## How the book is organized

### Part I — Foundations and Ensembles

- [Notation and Symbols](notation_and_symbols.md) — a reference for common symbols, ensemble conventions, and sign choices.
- [Indicator Functions](indicator_functions_statmech.md) — use zero-or-one functions to express events, count objects, restrict partition sums, and compute probabilities.
- [Temperature and Thermal Equilibrium](temperature_from_statistical_mechanics.md) — define temperature through entropy, energy exchange, and equilibrium; connect the microcanonical and canonical descriptions.
- [Partition Function and Thermodynamic Potentials](partition_function_thermodynamics_generator.md) — derive energy, free energy, entropy, pressure, and heat capacity from the partition function.
- [Grand Canonical Ensemble and Chemical Potential](grand_canonical_ensemble_chemical_potential.md) — derive the grand partition function and connect chemical potential, thermodynamic potentials, and particle-number fluctuations.
- [Two-Level Systems and the Schottky Anomaly](two_level_system_schottky_anomaly.md) — derive level occupations, internal energy, and the characteristic heat-capacity peak.

### Part II — Classical and Quantum Statistics

- [Equipartition of Energy](equipartition_of_energy.md) — derive the classical quadratic theorem and its generalization to power-law energy terms.
- [Maxwell–Boltzmann Statistics](maxwell_boltzmann_statistics.md) — derive the classical occupation distribution from state counting and entropy maximization.
- [Maxwell–Boltzmann Speed Distribution](maxwell_boltzmann_speed_distribution.md) — derive molecular speed distributions and characteristic speeds from the thermal velocity distribution.
- [Bose–Einstein Statistics](bose_einstein_statistics_derivation.md) — derive the occupation distribution for bosons from state counting and entropy maximization.
- [Fermi–Dirac Statistics](fermi_dirac_statistics_derivation.md) — derive the occupation distribution for fermions from state counting and entropy maximization.

### Part III — Applications to Matter and Radiation

- [Blackbody Radiation and Planck's Law](blackbody_radiation_planck_law.md) — derive the thermal radiation spectrum from electromagnetic mode counting and Bose–Einstein occupation.
- [Paramagnetism](paramagnetism_canonical_ensemble.md) — derive magnetization, Curie's law, internal energy, and heat capacity for independent magnetic moments.
- [Ising Model and Ferromagnetism](ising_model_ferromagnetism.md) — extend independent spins to interacting spins, mean-field theory, and spontaneous magnetic order.
- [Einstein Model of a Solid](einstein_model_of_a_solid.md) — derive vibrational thermodynamics and quantum heat capacity; identify the low-temperature limitation.
- [Debye Model of a Solid](debye_model_of_a_solid.md) — derive the phonon density of states and heat capacity, including the low-temperature cubic law.

### Part IV — Stochastic Processes and Relaxation

- [Markov Processes](markov_processes_statmech.md) — introduce Markov chains, transition rates, the master equation, stationary distributions, detailed balance, and thermal relaxation.
- [Newton's Law of Cooling](newtons_law_of_cooling_statmech.md) — connect near-equilibrium energy relaxation, detailed balance, linear response, and the cooling law.

## Sources and limitations

These chapters are original study notes, not transcripts of a particular textbook or lecture. Their derivations aim to make assumptions and intermediate steps explicit, but they are not a substitute for checking a result against a standard reference or the conventions used in a particular course.

Useful references for cross-checking include:

- R. K. Pathria and Paul D. Beale, *Statistical Mechanics*, 3rd edition — ensembles, partition functions, and quantum statistics.
- F. Reif, *Fundamentals of Statistical and Thermal Physics* — entropy, equilibrium, statistical ensembles, and thermodynamic relations.
- C. Kittel and H. Kroemer, *Thermal Physics*, 2nd edition — ensembles, paramagnetism, and quantum statistics.
- K. Huang, *Statistical Mechanics*, 2nd edition — statistical distributions and interacting systems.
- C. Kittel, *Introduction to Solid State Physics* — lattice vibrations and the Einstein and Debye models.
- N. W. Ashcroft and N. D. Mermin, *Solid State Physics* — phonons and low-temperature heat capacity.

Model limitations matter: the Ising mean-field treatment is an approximation; the Einstein and Debye models idealize the vibrational spectrum; the classical equipartition theorem does not capture quantum freeze-out; and Newton's law of cooling assumes a suitable near-equilibrium regime with an approximately constant effective heat-transfer coefficient. Results may also depend on dimensionality, boundary conditions, whether energy is measured with or without zero-point contributions, and the definitions of intensive variables. Where a chapter adopts a simplified model, read its assumptions before applying its formula to a real material or experiment.

The references above are suggested verification sources, not a claim that every equation in these notes has been independently checked against every edition. Corrections and source-specific caveats are welcome through issues or pull requests.

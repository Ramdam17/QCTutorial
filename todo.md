# TODO - Quantum Computing Workshop

## Project Setup

### Repository & Environment
- [ ] Configure Git repository
  - [ ] Review `.gitignore` (Python, Jupyter, Poetry)
  - [ ] Verify GitLab remote connection
  - [ ] Create initial commit structure
- [ ] Setup Poetry environment
  - [ ] Review `pyproject.toml` structure
  - [ ] Add core dependencies (Qiskit, matplotlib, seaborn, numpy, jupyter)
  - [ ] Add dev dependencies (black, ruff)
  - [ ] Run `poetry install` to verify environment
- [ ] Create project structure
  - [ ] Create `notebooks/` directory
  - [ ] Create `utils/` directory with `__init__.py`
  - [ ] Create `README.md`
  - [ ] Create `.gitignore`

### Utility Files
- [ ] Create `utils/plotting.py`
  - [ ] Beautiful plotting configuration (seaborn + matplotlib)
  - [ ] Color palette definitions (sparkly/unicorn theme 🦄✨)
  - [ ] Reusable plotting functions:
    - [ ] `plot_histogram_comparison()` - Classical vs quantum side-by-side
    - [ ] `plot_bloch_sphere()` - Styled Bloch sphere
    - [ ] `plot_circuit()` - Beautiful circuit diagrams
    - [ ] `plot_correlation_matrix()` - Heatmap for correlations
    - [ ] `plot_statevector()` - State visualization
- [ ] Create `utils/monarch_config.py`
  - [ ] Placeholder Compute Canada configuration
  - [ ] Backend selection helpers
  - [ ] Job submission utilities
  - [ ] Results comparison functions (simulator vs hardware)

---

## Notebook 1: Superposition (`01_superposition.ipynb`)

### Cell Structure
- [ ] **Cell 1** [Markdown] - Introduction
  - [ ] What is superposition?
  - [ ] Why it matters for quantum computing
  - [ ] Classical analogy vs quantum reality
  - [ ] Overview of what we'll demonstrate
  - [ ] Key equation: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$

- [ ] **Cell 2** [Code] - Imports & Setup
  - [ ] Import Qiskit components
  - [ ] Import matplotlib, seaborn, numpy
  - [ ] Import custom plotting utilities
  - [ ] Configure plotting style (beautiful mode)
  - [ ] Set random seeds for reproducibility

- [ ] **Cell 3** [Markdown] - Classical Probability Explanation
  - [ ] What: Monte Carlo simulation of fair coin
  - [ ] Why: Establish classical baseline
  - [ ] How: Random number generation, 1000 trials
  - [ ] Expected: ~50/50 distribution

- [ ] **Cell 4** [Code] - Classical Coin Simulation
  - [ ] Implement Monte Carlo simulation
  - [ ] Generate 1000 coin flips
  - [ ] Count outcomes
  - [ ] Create beautiful histogram

- [ ] **Cell 5** [Markdown] - Classical Results Interpretation
  - [ ] Analyze distribution
  - [ ] Explain classical randomness
  - [ ] Set up comparison with quantum case

- [ ] **Cell 6** [Markdown] - Quantum Superposition Explanation
  - [ ] What: Hadamard gate on |0⟩ state
  - [ ] Why: Creates genuine quantum superposition
  - [ ] How: Single-qubit circuit with H gate
  - [ ] Expected: 50/50 measurement outcomes (but fundamentally different!)
  - [ ] Circuit diagram visualization
  - [ ] Equation: $H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$

- [ ] **Cell 7** [Code] - Quantum Superposition Circuit
  - [ ] Create 1-qubit circuit
  - [ ] Apply Hadamard gate
  - [ ] Add measurement
  - [ ] Draw circuit (beautiful style)
  - [ ] Run on AerSimulator (1000 shots)
  - [ ] Extract and plot counts

- [ ] **Cell 8** [Markdown] - Quantum Results Interpretation
  - [ ] Compare to classical results
  - [ ] Explain superposition vs probability
  - [ ] Key insight: State exists in superposition until measured
  - [ ] Measurement collapses superposition

- [ ] **Cell 9** [Markdown] - Bloch Sphere Explanation
  - [ ] What: Geometric representation of single-qubit state
  - [ ] Why: Visualize quantum states intuitively
  - [ ] How: Show |0⟩ → after H gate
  - [ ] Expected: |0⟩ at north pole, superposition at equator

- [ ] **Cell 10** [Code] - Bloch Sphere Visualization
  - [ ] Create circuit without measurement
  - [ ] Extract statevector
  - [ ] Plot on Bloch sphere (initial state)
  - [ ] Plot on Bloch sphere (after H gate)
  - [ ] Side-by-side visualization

- [ ] **Cell 11** [Markdown] - Comparison Overview
  - [ ] Explain side-by-side comparison
  - [ ] Why distributions look similar but are fundamentally different
  - [ ] Key differences to highlight

- [ ] **Cell 12** [Code] - Beautiful Side-by-Side Comparison
  - [ ] Create 1x2 subplot figure (large, high DPI)
  - [ ] Classical histogram (left)
  - [ ] Quantum histogram (right)
  - [ ] Matching styling, clear labels
  - [ ] Annotations highlighting key differences

- [ ] **Cell 13** [Markdown] - Monarch Hardware Execution Intro
  - [ ] What: Run same circuit on real quantum hardware
  - [ ] Why: Compare ideal simulation vs noisy reality
  - [ ] How: Submit job to Compute Canada Monarch
  - [ ] Expected: Similar distribution but with hardware noise

- [ ] **Cell 14** [Code] - Monarch Execution
  - [ ] Load Monarch configuration (placeholder)
  - [ ] Submit circuit to hardware backend
  - [ ] Monitor job status
  - [ ] Retrieve results
  - [ ] Compare: simulator vs hardware (3-way plot)

- [ ] **Cell 15** [Markdown] - Hardware Results Analysis
  - [ ] Interpret noise patterns
  - [ ] Discuss decoherence effects
  - [ ] Readout errors
  - [ ] Conclusion: Real quantum computers are noisy!

---

## Notebook 2: Interference (`02_interference.ipynb`)

### Cell Structure
- [ ] **Cell 1** [Markdown] - Introduction to Quantum Interference
  - [ ] What is interference?
  - [ ] Classical vs quantum interference
  - [ ] Why interference is powerful for algorithms
  - [ ] Overview of demonstrations

- [ ] **Cell 2** [Code] - Imports & Setup
  - [ ] Standard imports (Qiskit, plotting, numpy)
  - [ ] Configure beautiful plotting

- [ ] **Cell 3** [Markdown] - Classical Wave Interference
  - [ ] What: Simulate interfering waves
  - [ ] Why: Establish classical analogy
  - [ ] How: Add sine waves, show constructive/destructive interference
  - [ ] Expected: Visual patterns of interference

- [ ] **Cell 4** [Code] - Classical Wave Simulation
  - [ ] Generate two sine waves
  - [ ] Show constructive interference (same phase)
  - [ ] Show destructive interference (opposite phase)
  - [ ] Beautiful 2x2 subplot visualization

- [ ] **Cell 5** [Markdown] - Classical Interference Interpretation
  - [ ] Waves can add or cancel
  - [ ] But amplitudes are always positive (classical)
  - [ ] Set up quantum case

- [ ] **Cell 6** [Markdown] - Quantum Interference Explanation
  - [ ] What: Two different circuits (H-X-H and H-H)
  - [ ] Why: Demonstrate amplitude interference
  - [ ] How: Build circuits, compare outcomes
  - [ ] Expected: H-X-H gives |1⟩ with certainty (destructive interference on |0⟩)
  - [ ] Expected: H-H gives |0⟩ with certainty (constructive on |0⟩)
  - [ ] Key: Negative amplitudes exist in quantum mechanics!

- [ ] **Cell 7** [Code] - Quantum Interference Circuits
  - [ ] Create circuit 1: H-X-H
  - [ ] Create circuit 2: H-H
  - [ ] Draw both circuits
  - [ ] Run both on simulator (1000 shots)
  - [ ] Side-by-side histogram comparison

- [ ] **Cell 8** [Markdown] - Quantum Interference Results
  - [ ] Analyze outcomes
  - [ ] Explain why H-X-H → |1⟩ (amplitude math)
  - [ ] Explain why H-H → |0⟩ (amplitude math)
  - [ ] Key insight: Amplitudes interfere, then square to get probabilities

- [ ] **Cell 9** [Markdown] - Amplitude Visualization Intro
  - [ ] What: Show amplitudes before measurement
  - [ ] Why: See negative values that classical probabilities can't have
  - [ ] How: Extract statevector, plot real/imaginary parts
  - [ ] Expected: See cancellation patterns

- [ ] **Cell 10** [Code] - Amplitude Bar Plots
  - [ ] For each circuit, extract statevector before measurement
  - [ ] Plot amplitude bars (can be negative!)
  - [ ] Show real and imaginary parts
  - [ ] Beautiful visualization with annotations

- [ ] **Cell 11** [Markdown] - Deutsch Algorithm Introduction
  - [ ] What: Simplest quantum algorithm
  - [ ] Why: Demonstrates quantum advantage via interference
  - [ ] How: Determine if function is constant or balanced in 1 query
  - [ ] Classical: Requires 2 queries
  - [ ] Quantum: Uses superposition + interference for 1 query
  - [ ] Circuit explanation

- [ ] **Cell 12** [Code] - Deutsch Algorithm Implementation
  - [ ] Implement constant function oracle
  - [ ] Implement balanced function oracle
  - [ ] Build Deutsch circuit for each
  - [ ] Run both
  - [ ] Beautiful comparison showing different outcomes
  - [ ] Annotate: "Constant" vs "Balanced" detection

- [ ] **Cell 13** [Markdown] - Deutsch Results Interpretation
  - [ ] How interference solves the problem
  - [ ] Why this is quantum advantage
  - [ ] Limitation: Toy problem, but principle extends

- [ ] **Cell 14** [Markdown] - Monarch Execution Intro
  - [ ] Real hardware test of interference
  - [ ] Expected: Noise may reduce contrast

- [ ] **Cell 15** [Code] - Run on Monarch
  - [ ] Submit interference circuits to hardware
  - [ ] Retrieve results
  - [ ] Compare simulator vs hardware

- [ ] **Cell 16** [Markdown] - Hardware Impact on Interference
  - [ ] Analyze how noise affects interference
  - [ ] Discuss error mitigation strategies
  - [ ] Conclusion

---

## Notebook 3: Entanglement (`03_entanglement.ipynb`)

### Cell Structure
- [ ] **Cell 1** [Markdown] - Introduction to Entanglement
  - [ ] What is entanglement?
  - [ ] "Spooky action at a distance"
  - [ ] Why it's fundamental to quantum computing
  - [ ] Classical correlations vs quantum correlations

- [ ] **Cell 2** [Code] - Imports & Setup
  - [ ] Standard imports
  - [ ] Beautiful plotting configuration

- [ ] **Cell 3** [Markdown] - Classical Correlations Explanation
  - [ ] What: Pre-arranged random bits scenario
  - [ ] Why: Establish maximum classical correlation
  - [ ] How: Simulate correlated coin flips
  - [ ] Expected: Perfect correlation in outcomes
  - [ ] But: No mystery - predetermined results

- [ ] **Cell 4** [Code] - Classical Correlation Simulation
  - [ ] Generate pairs of correlated random bits
  - [ ] 1000 pairs
  - [ ] Calculate correlation matrix
  - [ ] Beautiful heatmap visualization
  - [ ] Show individual measurements too

- [ ] **Cell 5** [Markdown] - Classical Correlation Interpretation
  - [ ] Correlation = 1.0
  - [ ] But explainable by local hidden variables
  - [ ] Set up quantum case

- [ ] **Cell 6** [Markdown] - Bell State Creation Explanation
  - [ ] What: Create Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
  - [ ] Why: Demonstrate true quantum entanglement
  - [ ] How: H gate on qubit 0, CNOT(0,1)
  - [ ] Expected: Only |00⟩ and |11⟩ outcomes (never |01⟩ or |10⟩)
  - [ ] Circuit diagram with explanation

- [ ] **Cell 7** [Code] - Bell State Circuit
  - [ ] Create 2-qubit circuit
  - [ ] Apply H to qubit 0
  - [ ] Apply CNOT(0,1)
  - [ ] Measure both qubits
  - [ ] Draw circuit
  - [ ] Run on simulator (1000 shots)

- [ ] **Cell 8** [Markdown] - Bell State Results Explanation
  - [ ] Analyze measurement outcomes
  - [ ] Only |00⟩ and |11⟩ appear (50% each)
  - [ ] Never |01⟩ or |10⟩
  - [ ] This is entanglement!
  - [ ] Measuring qubit 0 instantly determines qubit 1

- [ ] **Cell 9** [Code] - Beautiful Bar Chart
  - [ ] Plot measurement outcomes
  - [ ] Highlight |00⟩ and |11⟩
  - [ ] Annotate zero probability for |01⟩ and |10⟩
  - [ ] Beautiful, clear visualization

- [ ] **Cell 10** [Markdown] - Correlation Analysis Intro
  - [ ] What: Compare classical vs quantum correlations
  - [ ] Why: Show quantum correlations are stronger
  - [ ] How: Calculate correlation matrices for both
  - [ ] Expected: Both show correlation, but quantum is non-local

- [ ] **Cell 11** [Code] - Correlation Matrix Comparison
  - [ ] Classical correlation matrix (from earlier)
  - [ ] Quantum correlation matrix (from Bell state measurements)
  - [ ] Side-by-side heatmaps
  - [ ] Beautiful visualization with annotations

- [ ] **Cell 12** [Markdown] - Correlation Interpretation
  - [ ] Both show correlation
  - [ ] Classical: Local hidden variables possible
  - [ ] Quantum: Violates Bell inequality (mention but don't prove)
  - [ ] Key: Quantum correlations are fundamentally different

- [ ] **Cell 13** [Markdown] - 2-Qubit State Visualization Intro
  - [ ] What: Visualize the entangled state itself
  - [ ] Why: See non-separability
  - [ ] How: Statevector or density matrix heatmap
  - [ ] Expected: See superposition structure

- [ ] **Cell 14** [Code] - Statevector/Density Matrix Visualization
  - [ ] Extract statevector before measurement
  - [ ] Plot as city plot or matrix heatmap
  - [ ] Beautiful visualization showing |00⟩ and |11⟩ amplitudes
  - [ ] Annotations

- [ ] **Cell 15** [Markdown] - All Four Bell States
  - [ ] What: There are 4 maximally entangled states
  - [ ] $|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle$
  - [ ] Why: Different correlations and anti-correlations
  - [ ] How: Different gate combinations
  - [ ] Show circuit modifications for each

- [ ] **Cell 16** [Code] - Create All 4 Bell States
  - [ ] Create 4 circuits (one for each Bell state)
  - [ ] Run all 4
  - [ ] 2x2 grid visualization
  - [ ] Beautiful comparison showing different correlation patterns

- [ ] **Cell 17** [Markdown] - Monarch Execution Intro
  - [ ] Test entanglement on real hardware
  - [ ] Expected: Fidelity < 1.0 due to decoherence

- [ ] **Cell 18** [Code] - Run on Monarch
  - [ ] Submit Bell state circuit to hardware
  - [ ] Retrieve results
  - [ ] Compare simulator vs hardware
  - [ ] Calculate entanglement fidelity

- [ ] **Cell 19** [Markdown] - Hardware Entanglement Analysis
  - [ ] Interpret fidelity
  - [ ] Discuss decoherence effects on entanglement
  - [ ] Two-qubit gates are noisier than single-qubit gates
  - [ ] Conclusion

---

## Notebook 4: Teleportation (`04_teleportation.ipynb`)

### Cell Structure
- [ ] **Cell 1** [Markdown] - Introduction to Quantum Teleportation
  - [ ] What is quantum teleportation?
  - [ ] NOT Star Trek! (information, not matter)
  - [ ] Why it's important (quantum communication)
  - [ ] Overview of protocol

- [ ] **Cell 2** [Code] - Imports & Setup
  - [ ] Standard imports
  - [ ] Beautiful plotting configuration

- [ ] **Cell 3** [Markdown] - The Classical Problem
  - [ ] What: No-cloning theorem
  - [ ] Why: Can't copy unknown quantum state
  - [ ] Equation: No operation can do $|\psi\rangle \rightarrow |\psi\rangle \otimes |\psi\rangle$
  - [ ] But can TRANSFER (destroy original)
  - [ ] Set up teleportation as solution

- [ ] **Cell 4** [Markdown] - Teleportation Protocol Overview
  - [ ] Three qubits: Alice's unknown state, shared entangled pair
  - [ ] Alice has: qubit in state $|\psi\rangle$ (unknown to her)
  - [ ] Alice & Bob share: Bell pair
  - [ ] Steps:
    1. Create Bell pair, distribute
    2. Alice performs Bell measurement on her qubits
    3. Alice sends 2 classical bits to Bob
    4. Bob applies gates based on classical bits
    5. Bob now has $|\psi\rangle$, Alice's is destroyed
  - [ ] Diagram of protocol

- [ ] **Cell 5** [Markdown] - Implementation Plan
  - [ ] What we'll do step-by-step:
  - [ ] Create arbitrary initial state $|\psi\rangle$
  - [ ] Create Bell pair between qubits 1 & 2
  - [ ] Alice's Bell measurement (qubits 0 & 1)
  - [ ] Classical communication (simulated with conditional gates)
  - [ ] Verify Bob has original state
  - [ ] Expected: Perfect fidelity in simulation

- [ ] **Cell 6** [Code] - Complete Teleportation Circuit
  - [ ] Create 3-qubit circuit, 2 classical bits
  - [ ] Initialize qubit 0 with arbitrary state (parameterized)
  - [ ] Create Bell pair on qubits 1 & 2
  - [ ] Alice's Bell measurement (CNOT, H, measure qubits 0 & 1)
  - [ ] Bob's conditional gates (controlled on classical bits)
  - [ ] Measure qubit 2 (Bob's qubit) for verification
  - [ ] Draw beautiful circuit diagram

- [ ] **Cell 7** [Markdown] - Circuit Explanation
  - [ ] Which qubit is which (Alice's, shared 1, Bob's)
  - [ ] Purpose of each gate
  - [ ] Why measurements are necessary
  - [ ] Classical communication role

- [ ] **Cell 8** [Code] - Run Teleportation
  - [ ] Run with several different initial states
  - [ ] For each: verify Bob's qubit matches Alice's initial state
  - [ ] Calculate fidelity
  - [ ] Beautiful results table or plot

- [ ] **Cell 9** [Markdown] - Results Interpretation
  - [ ] Fidelity = 1.0 (perfect in simulation)
  - [ ] Alice's qubit is now decorrelated (no-cloning preserved)
  - [ ] Bob has exact copy of original unknown state
  - [ ] Emphasize: Information transferred, not matter

- [ ] **Cell 10** [Markdown] - Protocol Step Visualization Intro
  - [ ] What: Animate protocol step-by-step
  - [ ] Why: Understand how state evolves
  - [ ] How: Show statevector at each stage
  - [ ] Expected: See entanglement build, then transfer

- [ ] **Cell 11** [Code] - Step-by-Step Animation
  - [ ] Create circuit in stages
  - [ ] After initialization: show state
  - [ ] After Bell pair creation: show state
  - [ ] After Alice's measurement: show state
  - [ ] After Bob's corrections: show state
  - [ ] Multi-panel beautiful figure

- [ ] **Cell 12** [Markdown] - Protocol Animation Interpretation
  - [ ] Explain state at each step
  - [ ] How entanglement is used
  - [ ] Role of measurement and classical communication

- [ ] **Cell 13** [Markdown] - Fidelity Benchmark Intro
  - [ ] What: Test many random initial states
  - [ ] Why: Verify protocol works for any state
  - [ ] How: Generate random states, teleport, measure fidelity
  - [ ] Expected: All fidelities ≈ 1.0

- [ ] **Cell 14** [Code] - Fidelity Benchmark
  - [ ] Generate 100 random single-qubit states
  - [ ] Teleport each
  - [ ] Calculate fidelity for each
  - [ ] Beautiful histogram of fidelities
  - [ ] Should cluster near 1.0

- [ ] **Cell 15** [Markdown] - Fidelity Results
  - [ ] Interpret distribution
  - [ ] Confirm protocol works universally
  - [ ] Minor variations due to finite shots

- [ ] **Cell 16** [Markdown] - Monarch Execution Intro
  - [ ] Real quantum teleportation!
  - [ ] Expected: Lower fidelity due to noise
  - [ ] Decoherence during protocol
  - [ ] But should still work

- [ ] **Cell 17** [Code] - Run on Monarch
  - [ ] Submit teleportation circuit to hardware
  - [ ] Multiple trials
  - [ ] Calculate fidelity distribution
  - [ ] Compare simulator vs hardware

- [ ] **Cell 18** [Markdown] - Hardware Teleportation Results
  - [ ] Interpret fidelity (likely 0.7-0.9 range)
  - [ ] Impact of decoherence during multi-step protocol
  - [ ] Error sources: gate errors, measurement errors, decoherence
  - [ ] Still demonstrates quantum teleportation!

- [ ] **Cell 19** [Markdown] - Conclusion & Next Steps
  - [ ] Recap of 4 fundamental concepts:
    - Superposition: Qubits in multiple states
    - Interference: Amplitudes interfere to solve problems
    - Entanglement: Non-local correlations
    - Teleportation: Transfer quantum information
  - [ ] How they build on each other
  - [ ] Concepts form foundation of quantum computing
  - [ ] Next steps for learning:
    - Quantum algorithms (Grover, Shor)
    - Error correction
    - Quantum machine learning
  - [ ] Resources for further study

---

## Documentation

- [ ] Create comprehensive `README.md`
  - [ ] Project overview
  - [ ] Learning objectives
  - [ ] Prerequisites
  - [ ] Setup instructions
    - [ ] Clone repository
    - [ ] Install Poetry
    - [ ] Run `poetry install`
    - [ ] Configure Monarch (optional)
  - [ ] Notebook descriptions
  - [ ] Usage guidelines
  - [ ] Hardware requirements
  - [ ] Credits and references
  - [ ] License information

- [ ] Review and finalize `copilot-instructions.md`
  - [ ] Ensure all guidelines are clear
  - [ ] Add any missing patterns
  - [ ] Proofread

---

## Testing & Validation

- [ ] Test Notebook 1
  - [ ] Run all cells sequentially
  - [ ] Verify plots render correctly
  - [ ] Check for typos in markdown
  - [ ] Validate quantum results match theory
  - [ ] Ensure timing (~10 minutes)

- [ ] Test Notebook 2
  - [ ] Full run-through
  - [ ] Verify interference patterns
  - [ ] Check Deutsch algorithm results
  - [ ] Validate visualizations

- [ ] Test Notebook 3
  - [ ] Full run-through
  - [ ] Verify Bell state correlations
  - [ ] Check all 4 Bell states
  - [ ] Validate entanglement metrics

- [ ] Test Notebook 4
  - [ ] Full run-through
  - [ ] Verify teleportation fidelity
  - [ ] Check protocol visualization
  - [ ] Validate random state tests

- [ ] Integration testing
  - [ ] Run all 4 notebooks in sequence
  - [ ] Verify total time ≈ 40 minutes
  - [ ] Check narrative flow between notebooks
  - [ ] Ensure consistent styling

---

## Final Polish

- [ ] Code review
  - [ ] Consistent naming conventions
  - [ ] All functions documented
  - [ ] No unused imports
  - [ ] Clean, readable code

- [ ] Visual polish
  - [ ] All plots use beautiful style
  - [ ] Consistent color scheme across notebooks
  - [ ] High-quality figures (DPI ≥ 150)
  - [ ] Clear labels and titles

- [ ] Content review
  - [ ] Accurate physics/math
  - [ ] Clear explanations
  - [ ] No jargon without definition
  - [ ] Logical flow

- [ ] Accessibility
  - [ ] Alt text for key concepts (in markdown)
  - [ ] Color-blind friendly palettes
  - [ ] Clear font sizes

---

## Optional Enhancements (Post-Workshop)

- [ ] Add bonus notebook: Error correction basics
- [ ] Add bonus notebook: Variational quantum algorithms
- [ ] Create slides for live presentation
- [ ] Record video walkthrough
- [ ] Add interactive widgets (ipywidgets)
- [ ] Create Binder/Colab links for easy access
- [ ] Translate to French (maybe!)

---

## Notes

- Remember: Always ask before creating/modifying/deleting files
- Commit messages should be descriptive
- Git workflow: Create meaningful commits after each major milestone
- Poetry: Keep dependencies minimal and well-organized
- Make it beautiful! 🦄✨ This is as much art as science

---

**Priority Order:**
1. Project setup (environment, structure)
2. Utility files (plotting, config)
3. Notebook 1 (foundation)
4. Notebook 2 (builds on 1)
5. Notebook 3 (builds on 1+2)
6. Notebook 4 (synthesis)
7. Documentation
8. Testing & polish

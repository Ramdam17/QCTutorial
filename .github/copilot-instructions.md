# Copilot Instructions - Quantum Computing Workshop

## Project Overview

This project contains 7 Jupyter notebooks for a comprehensive introduction to quantum computing fundamentals. Each notebook is designed to run in 12-20 minutes and demonstrates core concepts through beautiful visualizations and progressive exercises.

**Target audience**: Team with no quantum computing background
**Total Duration**: ~100 minutes (1h40 with breaks)
**Style**: 4-part structure - Intuition → Concept → Implementation → Visualization

## Core Concepts Covered

0. **My First Qubit** - Circuit creation, X gate, measurement basics
1. **Superposition** - Classical probability vs quantum superposition
2. **Rotations & Interference** - Pauli gates, arbitrary rotations, phase, interference
3. **Two Qubits & CNOT** - Multi-qubit systems, CNOT gate, Bell states
4. **Entanglement** - Quantum correlations, CHSH inequality
5. **Deutsch's Algorithm** - First quantum algorithm, quantum advantage
6. **Teleportation** - Complete quantum state transfer protocol

## Technical Stack

- **Language**: Python 3.10+
- **Package Manager**: Poetry
- **Quantum Framework**: Qiskit (pure, no PennyLane)
- **Visualization**: Matplotlib + Seaborn (beautiful/sparkly style 🦄✨)
- **Version Control**: Git with remote on GitLab
- **Hardware Access**: Compute Canada Monarch quantum computer

## Project Structure

```
quantum-workshop/
├── .github/
│   └── copilot-instructions.md      # This file
├── NOTEBOOK_WRITING_PLAN_EN.md      # Detailed pedagogical structure
├── pyproject.toml                    # Poetry dependencies
├── README.md                         # Project overview
├── notebooks/
│   ├── 00_first_qubit.ipynb
│   ├── 01_superposition.ipynb
│   ├── 02_rotations_interference.ipynb
│   ├── 03_two_qubits_cnot.ipynb
│   ├── 04_entanglement.ipynb
│   ├── 05_deutsch_algorithm.ipynb
│   ├── 06_teleportation.ipynb
│   └── legacy/                       # Previous version notebooks
├── utils/
│   ├── __init__.py
│   ├── monarch_config.py            # Compute Canada configuration
│   ├── plotting.py                  # Shared beautiful plotting functions
│   └── legacy/                       # Previous version utilities
└── .gitignore
```

## Strict Workflow Rules

### 🚨 CRITICAL: Never Act Without Permission

**NEVER** perform these actions without explicit user approval:
- Create new files
- Delete files
- Modify existing files
- Git commit
- Git push
- Git merge
- Git branch operations

**Always ask first**: "May I create/modify/delete [filename]?" or "Should I commit these changes?"

### Git Workflow

1. **Check status** before suggesting changes: `git status`
2. **Ask before committing**: "Ready to commit [description]?"
3. **Ask before pushing**: "Should I push to remote?"
4. **Never force push**
5. Remote is already configured on GitLab (credentials available)

### Poetry Workflow

- Use `poetry add` for new dependencies
- Use `poetry install` for setup
- Keep `pyproject.toml` clean and organized
- Group dependencies logically (main, dev, visualization)

## Code Style Guidelines

### Language & Comments

- **Everything in English**: code, comments, docstrings, markdown cells
- **Readable code**: Prefer clarity over cleverness
- **Comprehensive comments**: Explain WHY, not just WHAT
- **Type hints**: Use them for function signatures

### Python Style

```python
# Good: Clear, commented, typed
def create_bell_state(circuit: QuantumCircuit, qubits: list[int]) -> None:
    """
    Create a Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
    
    Args:
        circuit: Quantum circuit to modify
        qubits: List of two qubit indices [control, target]
    """
    # Apply Hadamard to create superposition on first qubit
    circuit.h(qubits[0])
    
    # Entangle qubits with CNOT gate
    circuit.cx(qubits[0], qubits[1])
```

### Jupyter Notebook Structure

Each notebook follows this strict 4-part pattern:

```
Cell 1:  [Markdown] Header with progress bar, duration, learning objectives
Cell 2:  [Code] Imports & setup

--- Repeating pattern (4-part structure) ---
Section Start: [Markdown] 🤔 INTUITION - Classical analogy or conceptual diagram
Cell N:        [Markdown] 💡 CONCEPT - Progressive explanation of quantum concept
Cell N+1:      [Code] 💻 IMPLEMENTATION - Step-by-step commented code
Cell N+2:      [Markdown] 📊 VISUALIZATION - Interpreted results
--- End pattern ---

Checkpoints:   [Code] Regular checkpoints with □ checklists
Exercises:     [Markdown] 3 levels - 🟢 Predict, 🟡 Modify, 🔴 Create
Quiz:          [Markdown] End-of-notebook quiz with correct answers marked
Summary:       [Markdown] Progress bar, next notebook teaser

Optional:      Monarch hardware execution
```

### Markdown Cell Guidelines

Each explanatory markdown cell should include:

1. **What**: Clear description of the upcoming step
2. **Why**: Scientific/pedagogical motivation
3. **How**: Brief methodology overview
4. **Expected**: What results we anticipate
5. **Equations**: Use LaTeX for math (inline `$...$` or display `$$...$$`)

**Required Elements for Each Notebook:**

**Header format:**
```markdown
# Notebook X: Title

📘 **Notebook X/7**: Title  
⏱️  **Estimated Duration**: XX min  
🎯 **What You'll Learn**:
   • Concept 1
   • Concept 2
   • Concept 3

**Progress**: ⬛⬛⬛⬜⬜⬜⬜ (X/7)
```

**Checkpoint format:**
```python
# 🎯 CHECKPOINT: Can you...
# □ Action 1?
# □ Action 2?
# □ Action 3?
```

**Exercise format:**
```markdown
## 🎯 Exercise: Title

**Question**: ...

🤔 **Predict the result**:
- [ ] Option A
- [ ] Option B
- [ ] Option C

<details>
<summary>👉 Click for the answer</summary>

**Answer**: ...

**Explanation**: ...

</details>
```

**Quiz format:**
```markdown
## 🎯 Quick Quiz

**1. Question?**
- [ ] Wrong answer
- [x] Correct answer
- [ ] Wrong answer
```

Example section:
```markdown
## Creating Quantum Superposition

**What we'll do**: Apply a Hadamard gate to the |0⟩ state to create superposition

**Why**: Superposition is the foundation of quantum computing, allowing qubits to explore multiple states simultaneously

**How**: We'll use Qiskit's `h()` gate on a single qubit, then measure 1000 times

**Expected**: Equal probability of measuring |0⟩ and |1⟩ (≈50% each)

The Hadamard gate transforms our state:
$$H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$
```

## Visualization Guidelines

### General Plotting Style

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Beautiful style setup (sparkly/unicorn mode 🦄✨)
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Color palettes - use vibrant, beautiful colors
COLORS = {
    'primary': '#FF69B4',      # Hot pink
    'secondary': '#9370DB',    # Medium purple
    'accent': '#00CED1',       # Dark turquoise
    'highlight': '#FFD700',    # Gold
    'quantum': '#8A2BE2'       # Blue violet
}

# Use gradients and beautiful palettes
palette = sns.color_palette("husl", 8)  # Or "rocket", "mako", "flare"
```

### Figure Requirements

- **High DPI**: Always use `dpi=150` minimum
- **Large figures**: Generous sizing for readability
- **Labels**: Clear axis labels, titles, legends
- **Grid**: Use seaborn grids for clarity
- **Colors**: Vibrant, professional, accessible
- **Annotations**: Highlight key results

### Specific Visualizations

1. **Histograms**: Use seaborn `barplot` with beautiful colors
2. **Bloch spheres**: Qiskit's built-in, with custom colors if possible
3. **Circuit diagrams**: Use `circuit.draw('mpl')` with styling
4. **Heatmaps**: Seaborn heatmaps with annotated values
5. **Comparison plots**: Side-by-side subplots with shared scales

Example:
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=150)

# Classical results
sns.barplot(x=['0', '1'], y=classical_counts, ax=ax1, 
            palette=['#FF69B4', '#9370DB'])
ax1.set_title('Classical Probability', fontsize=16, fontweight='bold')
ax1.set_ylabel('Counts', fontsize=12)

# Quantum results  
sns.barplot(x=['0', '1'], y=quantum_counts, ax=ax2,
            palette=['#00CED1', '#8A2BE2'])
ax2.set_title('Quantum Superposition', fontsize=16, fontweight='bold')
ax2.set_ylabel('Counts', fontsize=12)

plt.tight_layout()
plt.show()
```

## Monarch (Compute Canada) Integration

### Configuration Template

Each notebook should include a Monarch execution cell with this structure:

```python
# Monarch Configuration (Compute Canada)
from qiskit_ibm_runtime import QiskitRuntimeService

# TODO: Configure with actual Compute Canada credentials
# This is a placeholder for the Monarch backend configuration

"""
Expected configuration:
1. Load account credentials from environment or config file
2. Select Monarch backend from available quantum computers
3. Submit job with appropriate queue settings
4. Monitor job status
5. Retrieve and compare results with simulator
"""

# Placeholder code
# service = QiskitRuntimeService(channel="ibm_quantum")
# backend = service.backend("monarch")  # Replace with actual backend name
# job = backend.run(circuit, shots=1000)
# result = job.result()

print("⚠️ Monarch execution placeholder - configure with actual credentials")
print("Expected: Results will show hardware noise compared to simulator")
```

### Hardware Comparison

Always compare:
- Simulator results (ideal)
- Hardware results (with noise)
- Discuss decoherence, gate fidelity, readout errors

## Dependencies (Poetry)

### Main Dependencies
```toml
[tool.poetry.dependencies]
python = "^3.10"
qiskit = "^1.0.0"
qiskit-aer = "^0.13.0"
qiskit-ibm-runtime = "^0.20.0"
matplotlib = "^3.8.0"
seaborn = "^0.13.0"
numpy = "^1.26.0"
jupyter = "^1.0.0"
ipykernel = "^6.27.0"
```

### Dev Dependencies
```toml
[tool.poetry.group.dev.dependencies]
black = "^23.12.0"
ruff = "^0.1.0"
```

## Common Patterns

### Circuit Creation Pattern
```python
from qiskit import QuantumCircuit

# Create circuit with appropriate qubits and classical bits
qc = QuantumCircuit(n_qubits, n_classical_bits)

# Build circuit
# ... gates ...

# Measure (if needed)
qc.measure_all()  # or specific measurements

# Visualize
qc.draw('mpl', style='iqp')  # Beautiful circuit diagram
```

### Simulation Pattern
```python
from qiskit_aer import AerSimulator

# Create simulator
simulator = AerSimulator()

# Run circuit
job = simulator.run(circuit, shots=1000)
result = job.result()
counts = result.get_counts()

# Visualize results
# ... beautiful plots ...
```

### State Visualization Pattern
```python
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city

# Get statevector (before measurement)
state = Statevector(circuit)

# Visualize
plot_bloch_multivector(state)
plot_state_city(state)
```

## Error Handling

- Use try-except for hardware connections
- Provide informative error messages
- Always include fallback to simulator
- Never let notebooks crash - graceful degradation

## Documentation Standards

### Docstrings
Use Google-style docstrings:

```python
def calculate_fidelity(state1: Statevector, state2: Statevector) -> float:
    """
    Calculate fidelity between two quantum states.
    
    Fidelity measures how close two quantum states are, with 1.0 being
    identical and 0.0 being orthogonal.
    
    Args:
        state1: First quantum state
        state2: Second quantum state
        
    Returns:
        Fidelity value between 0 and 1
        
    Example:
        >>> state1 = Statevector([1, 0])
        >>> state2 = Statevector([1, 0])
        >>> calculate_fidelity(state1, state2)
        1.0
    """
    return state1.inner(state2).conjugate() * state1.inner(state2)
```

### README Structure
- Project overview
- Setup instructions (Poetry)
- Notebook descriptions
- Hardware requirements
- Contributing guidelines

## Testing Approach

For this workshop, we prioritize:
- **Visual verification**: Do plots look correct?
- **Sanity checks**: Do probabilities sum to 1?
- **Conceptual accuracy**: Do results match theory?

No formal unit tests needed for workshop notebooks.

## Tips for Copilot

1. **Think pedagogically**: These are teaching materials for complete beginners
2. **Prioritize clarity**: Someone with no quantum background should understand from the code
3. **Make it beautiful**: Visualizations are as important as correct results
4. **Follow the 4-part structure**: Intuition → Concept → Implementation → Visualization
5. **Include checkpoints**: Regular verification points with checkbox lists
6. **Progressive exercises**: 🟢 Predict → 🟡 Modify → 🔴 Create from scratch
7. **Add quizzes**: End each notebook with a quick quiz (mark correct answers)
8. **Ask questions**: If unsure about a design choice, ask the user
9. **Reference theory**: Include equations and explanations
10. **Compare classical**: Always show classical analog first
11. **Show progress**: Use progress bars (⬛⬛⬛⬜⬜⬜⬜) consistently

## Additional Notes

- **Progressive exercises**: Each notebook includes 3-level exercises (predict, modify, create)
- **Interactive quizzes**: End-of-notebook quizzes to verify understanding
- **Checkpoints**: Regular verification points throughout notebooks
- **No neuroscience parallels**: Keep focus on quantum concepts
- **Linear progression**: Each notebook builds on previous ones (0→1→2→3→4→5→6)
- **Reproducible**: Set random seeds where applicable
- **Accessible**: Assume no prior quantum mechanics knowledge
- **Detailed plan**: Follow NOTEBOOK_WRITING_PLAN_EN.md for exact structure

## Questions to Ask User

Before implementing, consider asking:
- "Should I create the utility functions in `plotting.py` first?"
- "Which notebook should we start with?"
- "Do you want a `requirements.txt` alongside Poetry for compatibility?"
- "Should I add a `.gitignore` for Python/Jupyter?"

---

**Remember**: Never create, modify, delete, commit, or push without explicit approval! 🚨

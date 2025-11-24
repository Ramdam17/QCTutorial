# Quantum Computing Workshop 🦄✨
## From Zero to Quantum Hero

A comprehensive introduction to quantum computing fundamentals through beautiful visualizations, progressive exercises, and hands-on demonstrations.

## 🎯 Overview

This workshop consists of 7 Jupyter notebooks, each designed to run in 12-20 minutes. Through clear explanations, stunning visualizations, checkpoints, and interactive quizzes, you'll build a solid intuition of fundamental quantum concepts.

**Target Audience**: Anyone with basic Python knowledge - no quantum background required!  
**Prerequisites**: Basic Python knowledge, no prior quantum mechanics or physics required  
**Total Duration**: ~100 minutes (1h40 with breaks)  
**Pedagogical Approach**: 4-part structure (Intuition → Concept → Implementation → Visualization)

## 📚 Notebooks

| # | Title | Duration | Difficulty | Key Concepts |
|---|-------|----------|------------|-------------|
| 0 | My First Qubit | 12 min | ⭐ | Circuit, X gate, Measurement, Bloch sphere |
| 1 | Superposition | 12 min | ⭐ | Hadamard, Probabilities, H·H = I |
| 2 | Rotations & Interference | 20 min | ⭐⭐ | Pauli gates, RX/RY/RZ, Phase, H-Z-H |
| 3 | Two Qubits & CNOT | 15 min | ⭐⭐ | CNOT, Bell states, Correlations |
| 4 | Entanglement | 15 min | ⭐⭐⭐ | Quantum correlations, CHSH inequality |
| 5 | Deutsch's Algorithm | 12 min | ⭐⭐ | Oracle, Quantum advantage, First algorithm |
| 6 | Teleportation | 15 min | ⭐⭐⭐ | Complete protocol, No-cloning, Fidelity |

### 0. My First Qubit (`00_first_qubit.ipynb`) ⭐
Demystify quantum computing and manipulate your first qubit.
- Create a quantum circuit
- Apply the X gate (quantum NOT)
- Measure and interpret results
- Visualize on the Bloch sphere

**Key Concept**: Quantum circuits are like programs with qubits, gates, and measurements.

### 1. Superposition (`01_superposition.ipynb`) ⭐
Explore the fundamental difference between classical probability and quantum superposition.
- Classical random bits vs quantum superposition
- The Hadamard gate: creating (|0⟩+|1⟩)/√2
- The "spinning coin" analogy
- Understanding measurement collapse

**Key Concept**: A qubit can exist in multiple states simultaneously (0 AND 1), not just be unknown.

### 2. Rotations & Interference (`02_rotations_interference.ipynb`) ⭐⭐
Master quantum gates as rotations and understand interference.
- Pauli gates (X, Y, Z) as 180° rotations
- Arbitrary rotations (RX, RY, RZ) with any angle
- The concept of phase (negative amplitudes)
- Interference: H-H cancellation, H-Z-H to |1⟩

**Key Concept**: Gates rotate qubits on the Bloch sphere; amplitudes interfere constructively/destructively.

### 3. Two Qubits & CNOT (`03_two_qubits_cnot.ipynb`) ⭐⭐
Work with multiple qubits and create quantum correlations.
- 2-qubit systems: 4 basis states |00⟩, |01⟩, |10⟩, |11⟩
- The CNOT gate (Controlled-NOT)
- Creating the 4 Bell states
- First quantum correlations

**Key Concept**: CNOT creates correlations between qubits that are the foundation of entanglement.

### 4. Entanglement (`04_entanglement.ipynb`) ⭐⭐⭐
Understand quantum correlations that Einstein called "spooky action at a distance."
- Classical correlations vs quantum entanglement
- Measuring correlations in different bases
- CHSH inequality violation
- Why entanglement is non-classical

**Key Concept**: Entangled qubits have correlations stronger than any classical system can achieve.

### 5. Deutsch's Algorithm (`05_deutsch_algorithm.ipynb`) ⭐⭐
Implement your first quantum algorithm and see quantum advantage.
- The oracle concept (black box function)
- Deutsch's problem: constant vs balanced
- Quantum solution with 1 query (vs 2 classical)
- How interference gives the answer

**Key Concept**: Quantum interference can solve certain problems with exponentially fewer queries.

### 6. Teleportation (`06_teleportation.ipynb`) ⭐⭐⭐
See the complete quantum teleportation protocol in action.
- The no-cloning theorem
- Complete teleportation protocol (Bell state + measurements)
- Step-by-step state evolution
- Fidelity analysis across random states

**Key Concept**: Quantum information can be transferred using entanglement and classical communication.

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-gitlab-url>
   cd QCTutorial
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

4. **Launch Jupyter**
   ```bash
   jupyter notebook
   ```

5. **Open the first notebook** (`notebooks/01_superposition.ipynb`) and start learning!

## 🛠️ Technology Stack

- **Quantum Framework**: [Qiskit](https://qiskit.org/) - IBM's open-source quantum computing SDK
- **Visualization**: Matplotlib + Seaborn with custom "sparkly/unicorn" theme 🦄✨
- **Numerical Computing**: NumPy
- **Development**: Poetry for dependency management, Black & Ruff for code quality

## 📊 What Makes This Workshop Special

### 🎨 Beautiful Visualizations
Every concept is illustrated with high-quality, colorful plots (🦄✨ sparkly/unicorn theme) designed to make quantum mechanics intuitive and engaging.

### 📚 Progressive Structure
Each notebook follows a strict 4-part structure:
1. 🤔 **Intuition**: Classical analogy or conceptual diagram
2. 💡 **Concept**: Progressive explanation of quantum concept
3. 💻 **Implementation**: Step-by-step commented code
4. 📊 **Visualization**: Interpreted results

### ✅ Regular Checkpoints
Verify your understanding with checkpoint lists throughout each notebook.

### 🎯 Interactive Exercises
Three difficulty levels:
- 🟢 **Level 1**: Predict the result
- 🟡 **Level 2**: Modify a parameter
- 🔴 **Level 3**: Create from scratch

### 🧠 End-of-Notebook Quizzes
Test your understanding with quick quizzes (answers provided).

### 📈 Visual Progress Tracking
See your progress through the workshop with ⬛⬛⬛⬜⬜⬜⬜ progress bars.

### 🎓 Complete Beginner Friendly
No prior quantum mechanics or physics knowledge required. Start from absolute zero!

### Real Hardware Ready
Includes placeholder configuration for running circuits on Compute Canada's Monarch quantum computer (requires separate setup).

## 🌟 Learning Path

```
First Qubit → Superposition → Rotations → Two Qubits → Entanglement → Deutsch → Teleportation
     ↓             ↓              ↓            ↓             ↓            ↓           ↓
  Basics      Foundation    Interference    CNOT Gate   Correlations  Algorithm   Protocol
   (⭐)          (⭐)          (⭐⭐)          (⭐⭐)        (⭐⭐⭐)       (⭐⭐)      (⭐⭐⭐)
```

**Progress tracking**: Each notebook shows your progress with ⬛⬛⬛⬜⬜⬜⬜ bars

## 📁 Project Structure

```
QCTutorial/
├── README.md                              # This file
├── NOTEBOOK_WRITING_PLAN_EN.md            # Detailed pedagogical structure
├── pyproject.toml                         # Poetry dependencies
├── .github/
│   └── copilot-instructions.md            # Development guidelines
├── notebooks/
│   ├── 00_first_qubit.ipynb              # Notebook 0: My First Qubit
│   ├── 01_superposition.ipynb            # Notebook 1: Superposition
│   ├── 02_rotations_interference.ipynb   # Notebook 2: Rotations & Interference
│   ├── 03_two_qubits_cnot.ipynb          # Notebook 3: Two Qubits & CNOT
│   ├── 04_entanglement.ipynb             # Notebook 4: Entanglement
│   ├── 05_deutsch_algorithm.ipynb        # Notebook 5: Deutsch's Algorithm
│   ├── 06_teleportation.ipynb            # Notebook 6: Teleportation
│   └── legacy/                            # Previous version (4 notebooks)
└── utils/
    ├── __init__.py
    ├── plotting.py                        # Beautiful visualization utilities
    ├── monarch_config.py                  # Quantum hardware configuration
    └── legacy/                            # Previous version utilities
```

## 🔬 Hardware Execution (Optional)

The notebooks include placeholder cells for executing circuits on real quantum hardware via Compute Canada's Monarch quantum computer. This requires:

1. Compute Canada account with quantum computing access
2. IBM Quantum credentials
3. Configuration of `utils/monarch_config.py` with your credentials

**Note**: All notebooks work perfectly with the included quantum simulator. Hardware execution is optional and demonstrates the difference between ideal simulation and noisy real-world quantum computers.

## 🎨 Visualization Theme

All plots use a custom "sparkly/unicorn" color palette 🦄✨:
- **Hot Pink** (#FF69B4) - Primary quantum states
- **Medium Purple** (#9370DB) - Secondary states
- **Dark Turquoise** (#00CED1) - Accent colors
- **Gold** (#FFD700) - Highlights
- **Blue Violet** (#8A2BE2) - Quantum operations

High DPI (150+), clean styling, and careful annotations ensure every visualization is publication-quality.

## 📖 Additional Resources

After completing this workshop, continue your quantum journey with:

- **Qiskit Textbook**: [learn.qiskit.org](https://learn.qiskit.org/)
- **Quantum Algorithms**: Grover's search, Shor's factoring
- **Quantum Error Correction**: Protecting quantum information from noise
- **Variational Quantum Algorithms**: QAOA, VQE for near-term quantum computers
- **Quantum Machine Learning**: QML with PennyLane or Qiskit ML

## 🤝 Contributing

This is an educational project. Feedback, suggestions, and improvements are welcome!

## 📄 License

MIT License - Feel free to use this workshop for learning and teaching.

## 🙏 Acknowledgments

- **IBM Qiskit Team** for the excellent quantum computing framework
- **Compute Canada** for quantum hardware access (Monarch)
- The quantum computing community for educational resources

## ⚡ Quick Tips

1. **Start from Notebook 0**: Begin with `00_first_qubit.ipynb` - even if you have some quantum knowledge
2. **Run cells sequentially**: Each notebook is designed to be run from top to bottom
3. **Use checkpoints**: Verify your understanding at each 🎯 CHECKPOINT before continuing
4. **Try exercises**: Do the 🟢 exercises at minimum, challenge yourself with 🟡 and 🔴
5. **Take quizzes**: Test yourself with end-of-notebook quizzes
6. **Take your time**: Estimated times are guidelines - explore at your own pace!
7. **Modify and experiment**: Change parameters, try different gates, see what happens!
8. **Visual learner?**: Focus on the plots - they tell the story
9. **Math curious?**: Read the equations and explanations for deeper understanding
10. **Track progress**: Watch your ⬛⬛⬛⬜⬜⬜⬜ progress bar fill up!

---

**Ready to explore the quantum world?** Start with `notebooks/00_first_qubit.ipynb` and enjoy the journey from zero to quantum hero! 🚀✨

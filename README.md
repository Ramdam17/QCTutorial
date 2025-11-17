# Quantum Computing Workshop 🦄✨

A lightning-fast introduction to quantum computing fundamentals through beautiful visualizations and hands-on demonstrations.

## 🎯 Overview

This workshop consists of 4 Jupyter notebooks, each designed to run in approximately 10 minutes. Through clear explanations and stunning visualizations, you'll learn the core concepts that make quantum computing powerful.

**Target Audience**: Experienced Python developers interested in quantum computing  
**Prerequisites**: Basic Python knowledge, no prior quantum mechanics required  
**Total Duration**: ~40 minutes (10 minutes per notebook)

## 📚 Notebooks

### 1. Superposition (`01_superposition.ipynb`)
Explore the fundamental difference between classical probability and quantum superposition.
- Classical coin flips vs quantum superposition
- Hadamard gate and state preparation
- Bloch sphere visualization
- First quantum circuit

**Key Concept**: A qubit can exist in multiple states simultaneously until measured.

### 2. Interference (`02_interference.ipynb`)
Discover how quantum amplitudes interfere to solve computational problems.
- Classical wave interference vs quantum amplitude interference
- Negative amplitudes in quantum mechanics
- The Deutsch algorithm (first quantum algorithm)
- Quantum advantage demonstration

**Key Concept**: Quantum amplitudes can interfere constructively or destructively, enabling new computational approaches.

### 3. Entanglement (`03_entanglement.ipynb`)
Understand quantum correlations that Einstein called "spooky action at a distance."
- Classical correlations vs quantum entanglement
- Bell states creation and measurement
- Correlation analysis and visualization
- All four maximally entangled states

**Key Concept**: Entangled qubits share correlations that cannot be explained by classical physics.

### 4. Teleportation (`04_teleportation.ipynb`)
See how quantum information can be transferred without physically moving the qubit.
- No-cloning theorem
- Complete quantum teleportation protocol
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

### Beautiful Visualizations
Every concept is illustrated with high-quality, colorful plots designed to make quantum mechanics intuitive and engaging.

### Show, Don't Tell
Minimal code, maximum impact. See quantum phenomena in action rather than reading about abstract theory.

### Progressive Learning
Each notebook builds on previous concepts, creating a coherent narrative from basic superposition to quantum teleportation.

### Real Hardware Ready
Includes placeholder configuration for running circuits on Compute Canada's Monarch quantum computer (requires separate setup).

## 🌟 Learning Path

```
Superposition → Interference → Entanglement → Teleportation
     ↓              ↓               ↓              ↓
  Foundation   Quantum Algo    Correlations   Full Protocol
```

## 📁 Project Structure

```
quantum-workshop/
├── README.md                         # This file
├── pyproject.toml                    # Poetry dependencies
├── copilot-instructions.md           # Development guidelines
├── todo.md                           # Project roadmap
├── notebooks/
│   ├── 01_superposition.ipynb       # Notebook 1: Superposition
│   ├── 02_interference.ipynb        # Notebook 2: Interference
│   ├── 03_entanglement.ipynb        # Notebook 3: Entanglement
│   └── 04_teleportation.ipynb       # Notebook 4: Teleportation
└── utils/
    ├── __init__.py
    ├── plotting.py                  # Beautiful visualization utilities
    └── monarch_config.py            # Quantum hardware configuration
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

1. **Run cells sequentially**: Each notebook is designed to be run from top to bottom
2. **Take your time**: Even though each notebook is ~10 minutes, feel free to explore and experiment
3. **Modify and experiment**: Change parameters, try different gates, see what happens!
4. **Visual learner?**: Focus on the plots - they tell the story
5. **Math curious?**: Read the equations and explanations for deeper understanding

---

**Ready to explore the quantum world?** Start with `notebooks/01_superposition.ipynb` and enjoy the journey! 🚀✨

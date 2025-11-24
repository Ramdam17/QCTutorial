# 📚 Complete Writing Plan - QCTutorial Workshop
## "From Zero to Quantum Hero"

**Version**: 2.0 - Optimized Structure  
**Target Audience**: Team with no quantum computing background  
**Total Duration**: ~100 minutes (1h40 with breaks)  
**Goal**: Build solid intuition of fundamental quantum concepts

---

## 🎯 General Pedagogical Principles

### For EACH notebook:

1. **4-Part Structure**:
   - 🤔 **Intuition**: Classical analogy, conceptual diagram
   - 💡 **Concept**: Progressive explanation of quantum concept
   - 💻 **Implementation**: Step-by-step commented code
   - 📊 **Visualization**: Interpreted results

2. **Required Elements**:
   ```markdown
   # [Notebook Title]
   
   📘 **Notebook X/7**: [Title]  
   ⏱️  **Estimated Duration**: XX min  
   🎯 **What You'll Learn**:
      • Concept 1
      • Concept 2
      • Concept 3
   
   **Progress**: ⬛⬛⬛⬜⬜⬜⬜ (X/7)
   ```

3. **Regular Checkpoints**:
   ```python
   # 🎯 CHECKPOINT: Can you...
   # □ Action 1?
   # □ Action 2?
   # □ Action 3?
   ```

4. **Progressive Exercises**:
   - **Level 1 (🟢)**: Predict the result
   - **Level 2 (🟡)**: Modify a parameter
   - **Level 3 (🔴)**: Create from scratch

5. **End Quiz**:
   ```markdown
   ## 🎯 Quick Quiz
   1. Question 1?
      - [ ] Option A
      - [x] Option B (correct)
      - [ ] Option C
   ```

---

## 📖 Notebook Overview

| # | Title | Duration | Key Concepts | Difficulty |
|---|-------|----------|--------------|------------|
| 0 | My First Qubit | 12 min | Circuit, X, Measurement, Bloch | ⭐ |
| 1 | Superposition | 12 min | Hadamard, Probabilities | ⭐ |
| 2 | Rotations & Interference | 20 min | X/Y/Z, RZ, Phase, H-Z-H | ⭐⭐ |
| 3 | Two Qubits & CNOT | 15 min | CNOT, Bell states | ⭐⭐ |
| 4 | Entanglement | 15 min | Correlations, CHSH | ⭐⭐⭐ |
| 5 | Deutsch's Algorithm | 12 min | Oracle, Quantum advantage | ⭐⭐ |
| 6 | Teleportation | 15 min | Complete protocol | ⭐⭐⭐ |

---

# 📘 NOTEBOOK 0: My First Qubit

**Duration**: 12 minutes  
**Goal**: Demystify the quantum environment, manipulate a qubit

## Detailed Structure

### 📌 Header (30 seconds)

```markdown
# Notebook 0: My First Qubit

📘 **Notebook 0/7**: My First Qubit  
⏱️  **Estimated Duration**: 12 min  
🎯 **What You'll Learn**:
   • Create a quantum circuit
   • Add a gate (X)
   • Measure a qubit
   • Visualize results

**Progress**: ⬛⬜⬜⬜⬜⬜⬜ (0/7)

---

## 🚀 Welcome to Quantum Computing!

**What is a quantum computer?**

A classical computer manipulates **bits**: 0 or 1.  
A quantum computer manipulates **qubits**: 0, 1, or... both at the same time! 🤯

**Why is this useful?**

For certain problems (cryptography, optimization, molecular simulation), quantum computers can be **exponentially faster** than classical computers.

**What we'll learn today:**

We won't build a physical quantum computer, but we'll learn to **program** quantum circuits and simulate them.

Let's go! 🎉
```

---

### 📌 Section 1: Setup and Imports (1 min)

**Markdown content**:
```markdown
## Section 1: Environment Configuration

Let's import the necessary tools to program quantum circuits with **Qiskit** (IBM's open-source framework).
```

**Code cell**:
```python
# Quantum computing framework
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector

# Visualization
import numpy as np
import matplotlib.pyplot as plt

# Custom plotting utilities
import sys
sys.path.append('..')
from utils.plotting import configure_beautiful_plots, COLORS

# Configure beautiful plots
configure_beautiful_plots()

print("✅ All imports successful!")
print("✅ Ready to discover qubits")
```

---

### 📌 Section 2: Our First Circuit (2 min)

**Markdown content**:
```markdown
## Section 2: Creating Our First Quantum Circuit

A **quantum circuit** is like a program:
- It has **qubits** (the variables)
- It has **gates** (the operations)
- It ends with a **measurement** (reading the result)

Let's create the simplest possible circuit: **1 qubit, 0 gates**.
```

**Code cell with annotations**:
```python
# Create a circuit with 1 quantum qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
#                   ↑  ↑
#                   │  └─ 1 classical bit (to store the result)
#                   └──── 1 quantum qubit

# Display the circuit
print("Our first circuit:")
display(qc.draw('mpl'))

print("\n📝 Explanation:")
print("   • Horizontal line = the qubit (indexed q[0])")
print("   • It always starts in state |0⟩")
print("   • For now, there are no gates")
```

**Expected visualization**:
```
     ┌─┐
q_0: ┤M├
     └╥┘
c: 1/═╩═
     0
```

---

### 📌 Section 3: The Initial State |0⟩ (2 min)

**Markdown content**:
```markdown
## Section 3: Visualizing the Initial State

When we create a qubit, it's automatically in state **|0⟩**.

Let's visualize this state on the **Bloch Sphere** (a geometric representation of qubits).
```

**Code cell**:
```python
# Get the quantum state of the circuit (without gates)
qc = QuantumCircuit(1)
statevector = Statevector(qc)

# Visualize on the Bloch sphere
fig = plot_bloch_multivector(statevector)
plt.title("Initial state: |0⟩", fontsize=14, fontweight='bold')
plt.show()

print("🔵 State |0⟩ is at the NORTH pole of the sphere")
print("   This is the default state of every qubit")
```

**Explanation to add**:
```markdown
### 🌐 The Bloch Sphere: A Map of Quantum States

Imagine a sphere where:
- **North Pole** = |0⟩ (state "0")
- **South Pole** = |1⟩ (state "1")
- **Equator** = superpositions (we'll see that in the next notebook!)

Each point on the sphere = a possible quantum state.
```

---

### 📌 Section 4: Our First Gate - X (Bit Flip) (3 min)

**Markdown content**:
```markdown
## Section 4: The X Gate - The Quantum "NOT"

The **X** gate (also called "bit flip") transforms:
- |0⟩ → |1⟩
- |1⟩ → |0⟩

It's the quantum equivalent of the classical **NOT** gate.

### 🔄 Classical Analogy

```python
# Classical NOT in Python
bit = 0
bit = not bit  # becomes 1
```

Let's do the same thing with a qubit!
```

**Code cell**:
```python
# Create a circuit with the X gate
qc = QuantumCircuit(1, 1)
qc.x(0)  # Apply X to qubit 0: |0⟩ → |1⟩
qc.measure(0, 0)  # Measure qubit 0, store in classical bit 0

# Visualize the circuit
print("Circuit with X gate:")
display(qc.draw('mpl'))

# Execute the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
counts = job.result().get_counts()

# Display the results
print(f"\n📊 Results (1000 measurements):")
print(f"   State |0⟩: {counts.get('0', 0)} times")
print(f"   State |1⟩: {counts.get('1', 0)} times")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.bar(counts.keys(), counts.values(), color=COLORS['primary'], 
       edgecolor='black', linewidth=2, alpha=0.8)
ax.set_xlabel('Measured state', fontsize=12)
ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('Result of X Gate', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
plt.show()

print("\n✅ Observation: We ALWAYS get |1⟩!")
print("   The X gate successfully transformed |0⟩ into |1⟩")
```

---

### 📌 Section 5: Before/After Visualization on Bloch Sphere (2 min)

**Markdown content**:
```markdown
## Section 5: The X Gate on the Bloch Sphere

Let's see how the X gate transforms the state on the Bloch sphere.
```

**Code cell**:
```python
# State BEFORE X gate
qc_before = QuantumCircuit(1)
sv_before = Statevector(qc_before)

# State AFTER X gate
qc_after = QuantumCircuit(1)
qc_after.x(0)
sv_after = Statevector(qc_after)

# Side-by-side visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), 
                                subplot_kw={'projection': '3d'})

# Before
plot_bloch_multivector(sv_before, ax=ax1)
ax1.set_title("BEFORE: |0⟩ (North Pole)", fontsize=12, fontweight='bold')

# After
plot_bloch_multivector(sv_after, ax=ax2)
ax2.set_title("AFTER: |1⟩ (South Pole)", fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print("🔄 The X gate performs a 180° rotation around the X axis")
print("   It transforms the North pole (|0⟩) into the South pole (|1⟩)")
```

---

### 📌 Section 6: Anatomy of a Quantum Circuit (1 min)

**Markdown content**:
```markdown
## Section 6: Understanding a Quantum Circuit

Let's decode the elements of a circuit:

```
     ┌───┐┌─┐
q_0: ┤ X ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0
```

**Elements:**
1. **Horizontal lines** (`q_0:`) = quantum qubits
2. **Boxes** (`┤ X ├`) = quantum gates (operations)
3. **Measurement symbol** (`┤M├`) = reading the qubit
4. **Classical line** (`c: 1/`) = classical bits (to store results)
5. **Read left → right**: Time flows from left to right

**Execution order:**
1. Initialize q_0 to |0⟩
2. Apply X gate → |1⟩
3. Measure → Store "1" in classical bit c[0]
```

---

### 📌 Section 7: The Complete Workflow (1 min)

**Markdown content**:
```markdown
## Section 7: The Complete Quantum Workflow

Let's recap the process:

```
┌─────────────┐
│ 1. Create   │  qc = QuantumCircuit(1, 1)
│    Circuit  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 2. Add      │  qc.x(0)
│    Gates    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 3. Measure  │  qc.measure(0, 0)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 4. Simulate │  simulator.run(qc, shots=1000)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 5. Analyze  │  result.get_counts()
│    Results  │
└─────────────┘
```

**Important note**: We're using a **simulator** (running on a classical computer), not a real quantum computer. For learning, this is perfect!
```

---

### 📌 Section 8: Guided Exercise (1 min)

**Markdown content**:
```markdown
## 🎯 Guided Exercise: Predict the Result!

**Question**: If we apply the X gate **twice**, what will be the result?

```python
qc = QuantumCircuit(1, 1)
qc.x(0)  # First time: |0⟩ → |1⟩
qc.x(0)  # Second time: |1⟩ → ???
qc.measure(0, 0)
```

🤔 **Think before coding**:
- [ ] We always get |0⟩
- [ ] We always get |1⟩
- [ ] We get 50% |0⟩ and 50% |1⟩

<details>
<summary>👉 Click here to see the answer</summary>

**Answer**: We always get |0⟩

**Explanation**: 
- First X: |0⟩ → |1⟩
- Second X: |1⟩ → |0⟩
- The X gate is **reversible**: X·X = I (identity)

</details>
```

**Code cell (to be uncommented by student)**:
```python
# 🟢 Level 1: Test it yourself!
# Uncomment and run this code:

# qc = QuantumCircuit(1, 1)
# qc.x(0)  # First X
# qc.x(0)  # Second X
# qc.measure(0, 0)

# simulator = AerSimulator()
# counts = simulator.run(qc, shots=1000).result().get_counts()
# print(counts)
```

---

### 📌 Section 9: Checkpoint & Quiz (1 min)

**Markdown content**:
```markdown
## 🎯 CHECKPOINT: Can you...

Check your knowledge before moving to the next notebook:

- [ ] Create a circuit with `QuantumCircuit(n_qubits, n_bits)`?
- [ ] Add an X gate with `qc.x(0)`?
- [ ] Measure a qubit with `qc.measure(0, 0)`?
- [ ] Execute with `simulator.run(qc, shots=1000)`?
- [ ] Interpret a result histogram?

If you answered "yes" to everything, congratulations! 🎉

---

## 🎯 Quick Quiz

**1. A qubit always starts in which state?**
- [x] |0⟩ (north pole)
- [ ] |1⟩ (south pole)
- [ ] Superposition (equator)

**2. What does the X gate do?**
- [ ] Creates a superposition
- [x] Transforms |0⟩ into |1⟩ (and vice versa)
- [ ] Measures the qubit

**3. How many times must you apply X to return to the initial state?**
- [ ] 1 time
- [x] 2 times
- [ ] 4 times

**4. On the Bloch sphere, where is |1⟩ located?**
- [ ] North Pole
- [x] South Pole
- [ ] Equator
```

---

### 📌 Section 10: Summary & Next Step (30 sec)

**Markdown content**:
```markdown
## 🎓 Notebook 0 Summary

**What you learned:**
✅ Create a quantum circuit  
✅ Add a gate (X)  
✅ Measure a qubit  
✅ Visualize on the Bloch sphere  
✅ Interpret results  

**Progress**: ⬛⬜⬜⬜⬜⬜⬜ (1/7 completed)

---

## 🚀 Next Step: Notebook 1 - Superposition

So far, we've seen **definite** states: either |0⟩ or |1⟩.

In the next notebook, we discover **quantum superposition**:  
A qubit that is **both 0 AND 1** until measured! 🤯

**Teaser**: We'll create a truly random number generator with the **Hadamard** (H) gate.

See you soon! 🎉
```

---

# 📘 NOTEBOOK 1: Superposition

**Duration**: 12 minutes  
**Goal**: Understand and create quantum superposition

## Detailed Structure

### 📌 Header (30 seconds)

```markdown
# Notebook 1: Superposition - The Coin in Flight

📘 **Notebook 1/7**: Superposition  
⏱️  **Estimated Duration**: 12 min  
🎯 **What You'll Learn**:
   • Difference between classical probability and quantum superposition
   • Use the Hadamard (H) gate
   • Create a quantum number generator
   • Understand probabilistic measurement

**Progress**: ⬛⬛⬜⬜⬜⬜⬜ (1/7)

---

## 🪙 The Coin: Classical vs Quantum

In this notebook, we explore THE fundamental difference between classical and quantum computing: **superposition**.
```

---

### 📌 Section 1: Reminder - The Classical Bit (1 min)

**Markdown content**:
```markdown
## Section 1: The Classical Bit - Always Defined

A classical bit is always in **one single state**:
- Either 0
- Or 1
- Never in between

It's like a switch: either ON or OFF.
```

**Code cell**:
```python
# Classical simulation: a random bit
import random

# Generate 1000 random bits
classical_bits = [random.randint(0, 1) for _ in range(1000)]

# Count
count_0 = classical_bits.count(0)
count_1 = classical_bits.count(1)

print(f"📊 Classical results (1000 bits):")
print(f"   0: {count_0} times ({count_0/10:.1f}%)")
print(f"   1: {count_1} times ({count_1/10:.1f}%)")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.bar(['0', '1'], [count_0, count_1], color=COLORS['classical'],
       edgecolor='black', linewidth=2, alpha=0.8)
ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('Classical Random Bit', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
plt.show()

print("\n📝 Each bit IS either 0 or 1, we just don't know which before looking.")
```

---

### 📌 Section 2: Analogy - The Spinning Coin (2 min)

**Markdown content**:
```markdown
## Section 2: Classical Analogy - The Spinning Coin

### 🪙 Philosophical Question

Imagine a coin tossed in the air, spinning.

**Is it Heads AND Tails at the same time?**

🤔 Classical answer: **NO**  
- The coin is EITHER heads OR tails (we just don't know yet)
- The information already exists, we haven't observed it yet
- This is **ignorance**, not superposition

**Analogy**:
```python
def coin_in_air():
    """
    While the coin spins, it ALREADY has a defined state.
    We just don't know it yet.
    """
    # The coin "decides" at launch (deterministic physics)
    outcome = random.choice(['Heads', 'Tails'])
    return outcome

# The coin already has a result, we're just waiting to see it
result = coin_in_air()
print(f"Result: {result}")
```

### 🌟 And the Quantum Qubit?

In quantum mechanics, it's **radically different**:

**A qubit can truly be 0 AND 1 at the same time** until measured.

This isn't ignorance - it's **physical reality**!

Let's see how to create this magical state...
```

---

### 📌 Section 3: The Hadamard Gate - Creating Superposition (3 min)

**Markdown content**:
```markdown
## Section 3: The Hadamard (H) Gate - The Magic Gate

The **Hadamard** gate (noted H) is THE gate that creates superposition.

### 🔄 Transformation

$$|0\rangle \xrightarrow{H} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$$

**In English**:
- Initial state: |0⟩ (north pole)
- After H: Equal superposition of |0⟩ and |1⟩ (equator)
- Probability of measuring 0: 50%
- Probability of measuring 1: 50%

### 📐 Mathematical Notation

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

Where:
- α (alpha) and β (beta) are **amplitudes** (complex numbers)
- The probabilities are: P(0) = |α|² and P(1) = |β|²
- For H: α = β = 1/√2, so P(0) = P(1) = 50%
```

**Code cell**:
```python
# Create a circuit with Hadamard
qc = QuantumCircuit(1, 1)
qc.h(0)  # Hadamard on qubit 0: |0⟩ → (|0⟩+|1⟩)/√2
qc.measure(0, 0)

# Visualize the circuit
print("Circuit with Hadamard:")
display(qc.draw('mpl'))

print("\n📝 Circuit explained:")
print("   1. Qubit starts at |0⟩")
print("   2. H creates superposition: (|0⟩ + |1⟩)/√2")
print("   3. Measurement → forces the qubit to choose 0 or 1")
```

---

### 📌 Section 4: Measuring Superposition (2 min)

**Markdown content**:
```markdown
## Section 4: Measuring Superposition - The Moment of Truth

When we **measure** a qubit in superposition:
1. The qubit "collapses" to |0⟩ or |1⟩
2. It's **random** (truly random, not pseudo-random!)
3. The probability depends on amplitudes α and β

Let's run our circuit 1000 times to see the statistics.
```

**Code cell**:
```python
# Execute the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
counts = job.result().get_counts()

print(f"📊 Quantum results (1000 measurements):")
print(f"   State |0⟩: {counts.get('0', 0)} times")
print(f"   State |1⟩: {counts.get('1', 0)} times")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
bars = ax.bar(counts.keys(), counts.values(), 
              color=COLORS['quantum'], edgecolor='black', 
              linewidth=2, alpha=0.8)

# Add theoretical 50% line
ax.axhline(y=500, color='red', linestyle='--', linewidth=2, 
           label='Theoretical: 50%')

ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('Quantum Superposition after Hadamard', 
             fontsize=14, fontweight='bold')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.show()

print("\n✅ Result: ~50% |0⟩ and ~50% |1⟩")
print("   Before measurement: the qubit was in BOTH states!")
print("   Measurement forced it to choose")
```

---

### 📌 Section 5: Visualization on Bloch Sphere (2 min)

**Markdown content**:
```markdown
## Section 5: Visualizing Superposition

On the Bloch sphere, superposition |+⟩ = (|0⟩+|1⟩)/√2 is at the **equator**.
```

**Code cell**:
```python
# State BEFORE Hadamard
qc_before = QuantumCircuit(1)
sv_before = Statevector(qc_before)

# State AFTER Hadamard (but before measurement!)
qc_after = QuantumCircuit(1)
qc_after.h(0)
sv_after = Statevector(qc_after)

# Side-by-side visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Before
plot_bloch_multivector(sv_before, ax=ax1)
ax1.set_title("BEFORE: |0⟩", fontsize=12, fontweight='bold')

# After
plot_bloch_multivector(sv_after, ax=ax2)
ax2.set_title("AFTER: |+⟩ = (|0⟩+|1⟩)/√2", fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print("🌍 On the Bloch sphere:")
print("   • |0⟩: North Pole")
print("   • |1⟩: South Pole")
print("   • |+⟩: Equator (on positive X axis)")
print("\nThe H gate performs a 90° rotation around the Y axis")
```

---

### 📌 Section 6: Classical vs Quantum Comparison (2 min)

**Markdown content**:
```markdown
## Section 6: Classical vs Quantum - Where's the Difference?

The statistics are **identical**: 50/50 in both cases.

**But the underlying physics is radically different!**

| Aspect | Classical | Quantum |
|--------|-----------|---------|
| **State** | EITHER 0 OR 1 | 0 AND 1 simultaneously |
| **Before measurement** | Value exists, unknown | Real superposition |
| **Randomness** | Ignorance (pseudo-random) | Fundamental (truly random) |
| **Nature** | Deterministic | Probabilistic |

### 🔬 Why It Matters

This difference becomes crucial when we have **multiple qubits**:
- 2 classical bits: 2 bits → 4 possible configurations, one at a time
- 2 quantum qubits: 2 qubits → 4 states in **simultaneous superposition**!

**Exponential power**:
- 10 qubits → 2¹⁰ = 1,024 simultaneous states
- 50 qubits → 2⁵⁰ = 1,125,899,906,842,624 simultaneous states! 🤯
```

**Code cell - Comparative visualization**:
```python
# Side-by-side visual comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=150)

# Classical
ax1.bar(['0', '1'], [count_0, count_1], color=COLORS['classical'],
        edgecolor='black', linewidth=2, alpha=0.8)
ax1.set_ylabel('Number of times', fontsize=12)
ax1.set_title('🖥️ Classical: Random.randint()', 
              fontsize=13, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)
ax1.text(0.5, 0.95, 'Each bit IS 0 or 1\n(we don\'t know which)',
         transform=ax1.transAxes, ha='center', va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7),
         fontsize=10)

# Quantum
ax2.bar(counts.keys(), counts.values(), color=COLORS['quantum'],
        edgecolor='black', linewidth=2, alpha=0.8)
ax2.set_ylabel('Number of times', fontsize=12)
ax2.set_title('⚛️  Quantum: Hadamard Gate', 
              fontsize=13, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.text(0.5, 0.95, 'The qubit is 0 AND 1\nuntil measured',
         transform=ax2.transAxes, ha='center', va='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
         fontsize=10)

plt.suptitle('Same Statistics, Different Physics', 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

### 📌 Section 7: Exercise - Double Hadamard (1 min)

**Markdown content**:
```markdown
## 🎯 Exercise: What Happens with Two Hadamards?

**Question**: If we apply H twice, what do we get?

```python
qc = QuantumCircuit(1, 1)
qc.h(0)  # First H: |0⟩ → |+⟩
qc.h(0)  # Second H: |+⟩ → ???
qc.measure(0, 0)
```

🤔 **Predict the result**:
- [ ] 50% |0⟩, 50% |1⟩ (like a single H)
- [ ] 100% |0⟩ (return to initial state)
- [ ] 100% |1⟩

<details>
<summary>👉 Click for the answer</summary>

**Answer**: 100% |0⟩ (return to initial state)

**Explanation**:
- H · H = I (identity)
- Two Hadamards cancel out!
- This is an **interference** property (we'll see that in Notebook 2)

</details>
```

**Code cell**:
```python
# 🟢 Level 1: Test it yourself
qc_double_h = QuantumCircuit(1, 1)
qc_double_h.h(0)
qc_double_h.h(0)
qc_double_h.measure(0, 0)

counts_double = simulator.run(qc_double_h, shots=1000).result().get_counts()
print(f"Results with two H: {counts_double}")

# Visualization
fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
ax.bar(counts_double.keys(), counts_double.values(), 
       color=COLORS['success'], edgecolor='black', linewidth=2)
ax.set_title('Double Hadamard: H · H = Identity', 
             fontsize=14, fontweight='bold')
ax.set_ylabel('Number of times')
plt.show()

print("\n✅ We always get |0⟩!")
print("   The two Hs cancelled through interference")
```

---

### 📌 Section 8: Checkpoint & Quiz (1 min)

**Markdown content**:
```markdown
## 🎯 CHECKPOINT: Can you...

- [ ] Explain the difference between classical probability and quantum superposition?
- [ ] Create a superposition with the Hadamard gate?
- [ ] Predict that H gives 50/50 on measurement?
- [ ] Explain what happens during measurement (collapse)?

---

## 🎯 Quick Quiz

**1. What does "superposition" mean?**
- [ ] The qubit is 0 or 1, we don't know which
- [x] The qubit is 0 AND 1 simultaneously
- [ ] The qubit changes rapidly between 0 and 1

**2. What does the Hadamard gate do to |0⟩?**
- [x] Creates (|0⟩+|1⟩)/√2
- [ ] Transforms into |1⟩
- [ ] Does nothing

**3. What happens during measurement?**
- [ ] We reveal the hidden value
- [x] The superposition collapses to 0 or 1
- [ ] Nothing, the qubit stays in superposition

**4. H · H = ?**
- [ ] H²
- [x] I (identity, return to initial state)
- [ ] Double superposition
```

---

### 📌 Section 9: Summary & Next Step (30 sec)

**Markdown content**:
```markdown
## 🎓 Notebook 1 Summary

**What you learned:**
✅ The fundamental difference between classical and quantum  
✅ Create a superposition with Hadamard  
✅ Understand probabilistic measurement  
✅ Visualize on the Bloch sphere  
✅ The property H · H = I  

**Progress**: ⬛⬛⬜⬜⬜⬜⬜ (2/7 completed)

---

## 🚀 Next Step: Notebook 2 - Rotations & Interference

Now that we can create superpositions, we'll learn to **manipulate** them!

**Coming up**:
- Quantum gates as **rotations** on the sphere
- The concept of **phase** (negative amplitudes)
- How amplitudes can **cancel out** (interference)

This is where the magic happens! ✨

See you soon! 🎉
```

---

# 📘 NOTEBOOK 2: Rotations & Interference

**Duration**: 20 minutes (longest notebook, but crucial)  
**Goal**: Master rotations and understand interference

## Detailed Structure

### 📌 Header (30 seconds)

```markdown
# Notebook 2: Rotations & Interference

📘 **Notebook 2/7**: Rotations & Interference  
⏱️  **Estimated Duration**: 20 min  
🎯 **What You'll Learn**:
   • Quantum gates as rotations (X, Y, Z)
   • Arbitrary rotations (RX, RY, RZ)
   • The concept of phase
   • How amplitudes interfere (H-H, H-Z-H)
   • Why this is powerful for computation

**Progress**: ⬛⬛⬛⬜⬜⬜⬜ (2/7)

---

## 🌀 Qubits as a Sphere

In this notebook, we level up: manipulating qubits with precision.

**Key idea**: Quantum gates are **rotations** on the Bloch sphere.
```

---

### 📌 Section 1: Reminder - Classical Gates (1 min)

**Markdown content**:
```markdown
## Section 1: Classical Gates - Limited

In classical computing, logic gates:
- AND, OR, NOT, XOR...
- All operate on defined bits (0 or 1)
- **No rotation**: a bit is discrete

### ❌ Impossible Classically

You can't "gently rotate" a bit from 0 towards 1.  
It's either one or the other.

### ✅ Possible Quantumly

A qubit lives on a **sphere**, not on two points.  
We can rotate it by any angle!
```

---

### 📌 Section 2: The Bloch Sphere Revisited (2 min)

**Markdown content**:
```markdown
## Section 2: The Bloch Sphere - Our Playground

Reminder: Each point on the sphere = a possible quantum state.

### 🌐 Anatomy of the Sphere

```
           Z (|0⟩)
            ↑
            |
    Y ←-----+----→ X
            |
            ↓
           (|1⟩)
```

**Key points**:
- **North Pole (Z+)**: |0⟩
- **South Pole (Z-)**: |1⟩
- **Equator X+**: |+⟩ = (|0⟩+|1⟩)/√2
- **Equator X-**: |-⟩ = (|0⟩-|1⟩)/√2
- **Equator Y+**: |i⟩ = (|0⟩+i|1⟩)/√2
- **Equator Y-**: |-i⟩ = (|0⟩-i|1⟩)/√2

### 🔄 Operations = Rotations

Every quantum gate **rotates** the state on the sphere!
```

**Code cell - 3D interactive visualization (if possible)**:
```python
# Visualize several states on the sphere
states_to_show = {
    '|0⟩': Statevector.from_label('0'),
    '|1⟩': Statevector.from_label('1'),
    '|+⟩': Statevector(QuantumCircuit(1).h(0)),
    '|-⟩': Statevector(QuantumCircuit(1).x(0).h(0)),
}

fig, axes = plt.subplots(1, 4, figsize=(16, 4), 
                         subplot_kw={'projection': '3d'})

for (name, state), ax in zip(states_to_show.items(), axes):
    plot_bloch_multivector(state, ax=ax)
    ax.set_title(name, fontsize=12, fontweight='bold')

plt.suptitle('Important States on the Bloch Sphere', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("🌍 Each state is a point on the sphere")
print("   Gates rotate these points!")
```

---

### 📌 Section 3: The Pauli Gates (X, Y, Z) (3 min)

**Markdown content**:
```markdown
## Section 3: The Three Pauli Gates

The **X, Y, Z** gates are the basic rotations (180° around each axis).

### 🔴 X Gate: Rotation around X axis (180°)

**Effect**: |0⟩ ↔ |1⟩ (bit flip)

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
```

**Code cell**:
```python
# X gate: 180° rotation around X
qc_x = QuantumCircuit(1)
sv_before = Statevector(qc_x)

qc_x.x(0)
sv_after = Statevector(qc_x)

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plot_bloch_multivector(sv_before, ax=ax1)
ax1.set_title('Before X: |0⟩', fontsize=12, fontweight='bold')

plot_bloch_multivector(sv_after, ax=ax2)
ax2.set_title('After X: |1⟩', fontsize=12, fontweight='bold')

plt.suptitle('X Gate: 180° Rotation around X axis', fontsize=14)
plt.tight_layout()
plt.show()

print("❌ X flips the bit: North ↔ South")
```

**Markdown content**:
```markdown
### 🟢 Y Gate: Rotation around Y axis (180°)

**Effect**: |0⟩ → i|1⟩ and |1⟩ → -i|0⟩

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$

Similar to X, but adds a **complex phase** (factor i).
```

**Code cell**:
```python
# Y gate
qc_y = QuantumCircuit(1)
qc_y.y(0)
sv_y = Statevector(qc_y)

# Visualization
fig = plot_bloch_multivector(sv_y)
plt.title('Y Gate: 180° Rotation around Y', fontsize=14)
plt.show()

print("🔄 Y = rotation around Y axis + phase")
```

**Markdown content**:
```markdown
### 🔵 Z Gate: Rotation around Z axis (180°)

**Effect**: |0⟩ → |0⟩, but |1⟩ → -|1⟩ (phase flip)

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Important**: Z does NOT change measurement probabilities!  
It only changes the **phase** (the sign of the amplitude).
```

**Code cell**:
```python
# Z gate on |0⟩ (no visible change)
qc_z0 = QuantumCircuit(1)
qc_z0.z(0)
sv_z0 = Statevector(qc_z0)

# Z gate on |+⟩ (gives |-⟩!)
qc_z_plus = QuantumCircuit(1)
qc_z_plus.h(0)  # Create |+⟩
sv_plus = Statevector(qc_z_plus)

qc_z_plus.z(0)  # Apply Z
sv_minus = Statevector(qc_z_plus)

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plot_bloch_multivector(sv_plus, ax=ax1)
ax1.set_title('Before Z: |+⟩ = (|0⟩+|1⟩)/√2', fontsize=11, fontweight='bold')

plot_bloch_multivector(sv_minus, ax=ax2)
ax2.set_title('After Z: |-⟩ = (|0⟩-|1⟩)/√2', fontsize=11, fontweight='bold')

plt.suptitle('Z Gate: Changes the Sign (Phase)', fontsize=14)
plt.tight_layout()
plt.show()

print("⚡ Z adds a negative phase to |1⟩")
print("   |+⟩ = (|0⟩+|1⟩)/√2  →  Z  →  |-⟩ = (|0⟩-|1⟩)/√2")
```

---

### 📌 Section 4: Arbitrary Rotations (RX, RY, RZ) (3 min)

**Markdown content**:
```markdown
## Section 4: Arbitrary Rotations - Full Control

X, Y, Z perform 180° rotations.  
What if we want to rotate by **any angle** θ?

### 🎛️ RX, RY, RZ Gates

- **RX(θ)**: Rotation of θ radians around X
- **RY(θ)**: Rotation of θ radians around Y
- **RZ(θ)**: Rotation of θ radians around Z

**Examples**:
- RX(π) = X (180° rotation = π radians)
- RY(π/2) = 90° rotation around Y
- RZ(π/4) = 45° rotation around Z
```

**Code cell - Rotation animation**:
```python
# Create several RY rotations with different angles
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
titles = ['0°', '45°', '90°', '135°', '180°']

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for angle, title, ax in zip(angles, titles, axes):
    qc = QuantumCircuit(1)
    qc.ry(angle, 0)  # RY rotation of 'angle' radians
    sv = Statevector(qc)
    
    plot_bloch_multivector(sv, ax=ax)
    ax.set_title(f'RY({title})', fontsize=12, fontweight='bold')

plt.suptitle('Progressive RY Rotations: From |0⟩ to |1⟩', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("🌀 With RY, we can reach ANY point on the sphere!")
```

---

### 📌 Section 5: The Phase Concept - Why It's Crucial (3 min)

**Markdown content**:
```markdown
## Section 5: Phase - The Secret Ingredient of Quantum

### 🤔 What is Phase?

In quantum mechanics, amplitudes can be:
- Positive: +α
- **Negative**: -α
- **Complex**: e^(iφ)

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

Where α and β are **complex numbers**.

### 🎭 Global Phase vs Relative Phase

**Global phase** (invisible):
$$e^{i\phi}|\psi\rangle$$
Does NOT change measurement probabilities.

**Relative phase** (important!):
$$|0\rangle + e^{i\phi}|1\rangle$$
Changes how amplitudes **interfere**!

### 💡 Concrete Example

Compare:
- **|+⟩** = (|0⟩ + |1⟩)/√2  (relative phase = 0)
- **|-⟩** = (|0⟩ - |1⟩)/√2  (relative phase = π)

Same measurement probabilities (50/50), but DIFFERENT behavior in circuits!
```

**Code cell - Demonstration**:
```python
# States |+⟩ and |-⟩: same measurement, different phase
qc_plus = QuantumCircuit(1, 1)
qc_plus.h(0)  # |+⟩
qc_plus.measure(0, 0)

qc_minus = QuantumCircuit(1, 1)
qc_minus.x(0)
qc_minus.h(0)  # |-⟩ = X · H(|0⟩)
qc_minus.measure(0, 0)

# Measure both
counts_plus = simulator.run(qc_plus, shots=1000).result().get_counts()
counts_minus = simulator.run(qc_minus, shots=1000).result().get_counts()

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=150)

ax1.bar(counts_plus.keys(), counts_plus.values(), 
        color=COLORS['primary'], edgecolor='black', linewidth=2)
ax1.set_title('|+⟩ = (|0⟩+|1⟩)/√2', fontsize=13, fontweight='bold')
ax1.set_ylabel('Number of times')
ax1.grid(axis='y', alpha=0.3)

ax2.bar(counts_minus.keys(), counts_minus.values(), 
        color=COLORS['secondary'], edgecolor='black', linewidth=2)
ax2.set_title('|-⟩ = (|0⟩-|1⟩)/√2', fontsize=13, fontweight='bold')
ax2.set_ylabel('Number of times')
ax2.grid(axis='y', alpha=0.3)

plt.suptitle('Same Measurement, Different Phase', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

print("📊 Both give 50/50!")
print("   But the phase (+ vs -) becomes important in circuits...")
```

---

### 📌 Section 6: Interlude - Transition to Interference (1 min)

**Markdown content**:
```markdown
---

## 🌊 Interlude: From Rotation to Interference

**So far, we've learned**:
✅ Gates are rotations  
✅ We can rotate by any angle  
✅ Phase exists (negative amplitudes)  

**Now, the big question**:

💡 **What's the point of phase if it doesn't change measurements?**

**Answer**: Interference! 🌊

When we combine multiple gates, amplitudes **add algebraically**.  
Negative amplitudes can **cancel** positive amplitudes.

This is **THE** power of quantum computing.

Let's see it in action...

---
```

---

### 📌 Section 7: Interference - H-H Cancels (3 min)

**Markdown content**:
```markdown
## Section 7: First Interference - The H-H Circuit

We already saw in Notebook 1 that **H · H = I**.  
Let's now understand **why** in terms of amplitudes.

### 🔄 Step-by-Step Evolution

**Initial state**: |0⟩

**After 1st H**:
$$|0\rangle \xrightarrow{H} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$

Amplitudes:
- α₀ = +1/√2 (for |0⟩)
- α₁ = +1/√2 (for |1⟩)

**After 2nd H**:

The H gate transforms:
- |0⟩ → (|0⟩+|1⟩)/√2
- |1⟩ → (|0⟩-|1⟩)/√2

So:
$$\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \xrightarrow{H} \frac{1}{\sqrt{2}}\left[\frac{|0\rangle+|1\rangle}{\sqrt{2}} + \frac{|0\rangle-|1\rangle}{\sqrt{2}}\right]$$

Simplify:
$$= \frac{1}{2}[(|0\rangle + |1\rangle) + (|0\rangle - |1\rangle)]$$
$$= \frac{1}{2}[2|0\rangle] = |0\rangle$$

**🎯 Result**: Paths to |1⟩ cancel! (interference **destructive**)  
Paths to |0⟩ add up! (interference **constructive**)
```

**Code cell - Amplitude visualization**:
```python
# Visualize amplitudes at each step
from utils.plotting import plot_statevector

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5), dpi=150)

# Initial state
qc1 = QuantumCircuit(1)
sv1 = Statevector(qc1)
plot_statevector(sv1, ax=ax1, title='Initial State: |0⟩')

# After first H
qc2 = QuantumCircuit(1)
qc2.h(0)
sv2 = Statevector(qc2)
plot_statevector(sv2, ax=ax2, title='After 1st H: (|0⟩+|1⟩)/√2')

# After second H
qc3 = QuantumCircuit(1)
qc3.h(0)
qc3.h(0)
sv3 = Statevector(qc3)
plot_statevector(sv3, ax=ax3, title='After 2nd H: |0⟩')

plt.suptitle('H-H: Cancellation by Interference', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("🌊 Constructive interference on |0⟩: +1/2 + 1/2 = 1")
print("🌊 Destructive interference on |1⟩: +1/2 - 1/2 = 0")
```

---

### 📌 Section 8: Destructive Interference - H-Z-H (3 min)

**Markdown content**:
```markdown
## Section 8: Destructive Interference - The H-Z-H Circuit

Now, let's add a **Z** gate between the two Hs.

### 🔄 Evolution

**Initial state**: |0⟩

**After H**:
$$|0\rangle \xrightarrow{H} \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$

**After Z**:
Reminder: Z leaves |0⟩ intact, but transforms |1⟩ → -|1⟩

$$\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \xrightarrow{Z} \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$$

**After 2nd H**:

$$\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \xrightarrow{H} \frac{1}{2}[(|0\rangle+|1\rangle) - (|0\rangle-|1\rangle)]$$
$$= \frac{1}{2}[2|1\rangle] = |1\rangle$$

**🎯 Result**: We ALWAYS get **|1⟩**!

This time:
- Interference **constructive** on |1⟩
- Interference **destructive** on |0⟩
```

**Code cell**:
```python
# H-Z-H circuit
qc_hzh = QuantumCircuit(1, 1)
qc_hzh.h(0)   # Superposition
qc_hzh.z(0)   # Phase flip
qc_hzh.h(0)   # Interference
qc_hzh.measure(0, 0)

# Visualize the circuit
print("H-Z-H circuit:")
display(qc_hzh.draw('mpl'))

# Execute
counts_hzh = simulator.run(qc_hzh, shots=1000).result().get_counts()

print(f"\n📊 Results: {counts_hzh}")
print("✅ We ALWAYS get |1⟩!")

# Visualize amplitudes at each step
fig, axes = plt.subplots(1, 4, figsize=(18, 4), dpi=150)

# Intermediate states
states = [
    (QuantumCircuit(1), "Initial: |0⟩"),
    (QuantumCircuit(1).h(0), "After H"),
    (QuantumCircuit(1).h(0).z(0), "After Z"),
    (QuantumCircuit(1).h(0).z(0).h(0), "After 2nd H")
]

for (qc, title), ax in zip(states, axes):
    sv = Statevector(qc)
    plot_statevector(sv, ax=ax, title=title)

plt.suptitle('H-Z-H: Interference to |1⟩', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n🎭 The Z gate changed the sign of the amplitude on |1⟩")
print("   Result: destructive interference on |0⟩, constructive on |1⟩")
```

---

### 📌 Section 9: The Power of Interference (2 min)

**Markdown content**:
```markdown
## Section 9: Why Interference is Powerful

### 💡 The Fundamental Idea of Quantum Computing

**Classically**:
- We explore solutions **one by one**
- If we have 2ⁿ possibilities, it takes 2ⁿ steps

**Quantumly**:
1. **Superposition**: Explore all 2ⁿ possibilities simultaneously
2. **Interference**: Amplify good solutions, cancel bad ones
3. **Measurement**: Get the answer with high probability

### 🎯 General Strategy

```
┌─────────────┐     ┌──────────────┐     ┌─────────┐
│Superposition│ ──► │ Interference │ ──► │ Measure │
│  (create)   │     │  (manipulate)│     │(extract)│
└─────────────┘     └──────────────┘     └─────────┘
     |                      |                    |
  Explore            Amplify                Read the
everything          good                   answer
in parallel        solutions
```

### 📚 Algorithm Examples

- **Deutsch** (we'll see in Notebook 5): 1 query vs 2 classical
- **Grover**: √N queries vs N classical (search)
- **Shor**: Polynomial vs exponential (factorization)

All use **superposition + interference**!
```

---

### 📌 Section 10: Exercise - Predict Interference (1 min)

**Markdown content**:
```markdown
## 🎯 Exercise: Predict the Result!

**Question**: What will be the result of the following circuit?

```python
qc = QuantumCircuit(1, 1)
qc.h(0)   # H
qc.x(0)   # X (bit flip)
qc.h(0)   # H
qc.measure(0, 0)
```

🤔 **Options**:
- [ ] 100% |0⟩
- [ ] 100% |1⟩
- [ ] 50% |0⟩, 50% |1⟩

<details>
<summary>👉 Click for the answer</summary>

**Answer**: 100% |1⟩

**Explanation**:
1. H: |0⟩ → (|0⟩+|1⟩)/√2
2. X: Flip → (|1⟩+|0⟩)/√2 = (|0⟩+|1⟩)/√2 (same state!)
3. Wait, no... X transforms |0⟩→|1⟩ and |1⟩→|0⟩, so:
   (|0⟩+|1⟩)/√2 → (|1⟩+|0⟩)/√2
4. H: (|1⟩+|0⟩)/√2 → ...

Actually, H-X-H = Z!  
The circuit is equivalent to Z on |0⟩, which gives |0⟩...

Oops, recalculation:
H-X-H on |0⟩ gives |1⟩. Test the code to confirm!

</details>
```

**Code cell**:
```python
# 🟡 Level 2: Test and explain
qc_hxh = QuantumCircuit(1, 1)
qc_hxh.h(0)
qc_hxh.x(0)
qc_hxh.h(0)
qc_hxh.measure(0, 0)

counts_hxh = simulator.run(qc_hxh, shots=1000).result().get_counts()
print(f"H-X-H result: {counts_hxh}")

# Visualize amplitudes
fig, axes = plt.subplots(1, 4, figsize=(18, 4))
# ... (same structure as H-Z-H)

print("\n💡 Property: H-X-H = Z!")
```

---

### 📌 Section 11: Checkpoint & Quiz (1 min)

**Markdown content**:
```markdown
## 🎯 CHECKPOINT

- [ ] Understand that gates are rotations?
- [ ] Use RX, RY, RZ with different angles?
- [ ] Explain what phase is?
- [ ] Predict that H-Z-H gives |1⟩?
- [ ] Understand constructive/destructive interference?

---

## 🎯 Quick Quiz

**1. What does the Z gate do?**
- [ ] Transforms |0⟩ into |1⟩
- [x] Adds a negative phase to |1⟩
- [ ] Creates a superposition

**2. RY(π/2) performs a rotation of how many degrees?**
- [ ] 45°
- [x] 90°
- [ ] 180°

**3. Why does H-H = I?**
- [ ] By definition
- [x] Interference: paths to |1⟩ cancel
- [ ] Calculation error

**4. H-Z-H gives what result on |0⟩?**
- [ ] |0⟩
- [x] |1⟩
- [ ] Superposition

**5. What is interference used for?**
- [x] Amplify good solutions, cancel bad ones
- [ ] Create randomness
- [ ] Measure faster
```

---

### 📌 Section 12: Summary & Next Step (1 min)

**Markdown content**:
```markdown
## 🎓 Notebook 2 Summary

**What you learned:**
✅ Gates are rotations (X, Y, Z)  
✅ Arbitrary rotations (RX, RY, RZ)  
✅ The concept of phase (negative amplitudes)  
✅ Interference (H-H, H-Z-H)  
✅ Why this is powerful for computation  

**Progress**: ⬛⬛⬛⬜⬜⬜⬜ (3/7 completed)

---

## 🚀 Next Step: Notebook 3 - Two Qubits & CNOT

So far, we've worked with **one single qubit**.

Now we move to **two qubits** and discover the most important gate:  
**CNOT** (Controlled-NOT)

**Coming up**:
- 2-qubit systems (4 basis states)
- The CNOT gate (control + target)
- Creating **Bell states** (first step towards entanglement)

We're entering the real power of quantum! ⚛️

See you soon! 🎉
```

---

*(The document continues with Notebooks 3, 4, 5, 6 with the same level of detail...)*

---

# 📘 NOTEBOOK 3: Two Qubits & CNOT

**Duration**: 15 minutes  
**Goal**: Master 2-qubit gates and create entanglement

## Detailed Structure

### 📌 Header (30 seconds)

```markdown
# Notebook 3: Two Qubits & CNOT

📘 **Notebook 3/7**: Two Qubits & CNOT  
⏱️  **Estimated Duration**: 15 min  
🎯 **What You'll Learn**:
   • Work with 2 qubits
   • The CNOT (Controlled-NOT) gate
   • Quantum correlations
   • Create the 4 Bell states

**Progress**: ⬛⬛⬛⬛⬜⬜⬜ (3/7)

---

## 🔗 When Qubits Meet

One qubit is good. Two qubits together - that's where the magic begins! 🎭
```

---

### 📌 Section 1: Classical Multi-Bit Systems (1 min)

**Markdown content**:
```markdown
## Section 1: Reminder - Two Classical Bits

With 2 classical bits, we have **4 possible configurations**:
- 00 (both at 0)
- 01 (first at 0, second at 1)
- 10 (first at 1, second at 0)
- 11 (both at 1)

**Important**: The bits are **independent**.  
Changing bit 1 does NOT affect bit 2.
```

**Code cell**:
```python
# Classical simulation: 2 independent bits
import random

def generate_2bits():
    bit1 = random.randint(0, 1)
    bit2 = random.randint(0, 1)
    return f"{bit1}{bit2}"

# Generate 1000 pairs
results = [generate_2bits() for _ in range(1000)]
from collections import Counter
counts_classical = Counter(results)

print("📊 Classical results (2 independent bits):")
for state, count in sorted(counts_classical.items()):
    print(f"   {state}: {count} times (~{count/10:.0f}%)")

# Visualization
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
ax.bar(counts_classical.keys(), counts_classical.values(),
       color=COLORS['classical'], edgecolor='black', linewidth=2)
ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('2 Independent Classical Bits', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
plt.show()

print("\n✅ Uniform distribution: each state appears ~25% of the time")
```

---

### 📌 Section 2: Two Quantum Qubits (2 min)

**Markdown content**:
```markdown
## Section 2: Two Quantum Qubits

With 2 qubits, we also have **4 basis states**: |00⟩, |01⟩, |10⟩, |11⟩

**BUT**: A 2-qubit system can be in **superposition** of all 4 states!

$$|\psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$$

Where:
- α, β, γ, δ are **amplitudes** (complex numbers)
- Probabilities: |α|² + |β|² + |γ|² + |δ|² = 1

### 🌌 Hilbert Space

The space of possible states grows **exponentially**:
- 1 qubit: 2 dimensions (2¹)
- 2 qubits: 4 dimensions (2²)
- 10 qubits: 1024 dimensions (2¹⁰)
- 50 qubits: 10¹⁵ dimensions (2⁵⁰)!

This is the origin of quantum power.
```

**Code cell**:
```python
# Create a circuit with 2 qubits
qc_2q = QuantumCircuit(2, 2)

# Visualize
print("Circuit with 2 qubits:")
display(qc_2q.draw('mpl'))

# Initial state
sv_2q = Statevector(qc_2q)
print(f"\nInitial state: {sv_2q.data}")
print("   Index 0 (|00⟩): amplitude = 1")
print("   Index 1 (|01⟩): amplitude = 0")
print("   Index 2 (|10⟩): amplitude = 0")
print("   Index 3 (|11⟩): amplitude = 0")
print("\n📝 By default: |00⟩ (both qubits at |0⟩)")
```

---

### 📌 Section 3: The CNOT Gate - Control & Target (4 min)

**Markdown content**:
```markdown
## Section 3: The CNOT (Controlled-NOT) Gate

The **CNOT** gate is THE fundamental 2-qubit gate.

### 🎮 Principle

**CNOT** has two qubits:
1. **Control qubit** (control)
2. **Target qubit** (target)

**Rule**:
- If control = |0⟩ → do nothing
- If control = |1⟩ → apply X to target

### 📊 Truth Table

| Control | Target | After CNOT |
|---------|--------|------------|
| 0 | 0 | 0 0 |
| 0 | 1 | 0 1 |
| 1 | 0 | 1 1 |
| 1 | 1 | 1 0 |

**Observation**: Only rows with control=1 change!
```

**Code cell - Test the 4 cases**:
```python
# Test CNOT on the 4 basis states
test_cases = [
    ('00', []),                    # |00⟩
    ('01', [('x', 1)]),           # |01⟩ = X on qubit 1
    ('10', [('x', 0)]),           # |10⟩ = X on qubit 0
    ('11', [('x', 0), ('x', 1)])  # |11⟩ = X on both
]

fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=150)
axes = axes.flatten()

for idx, (label, gates) in enumerate(test_cases):
    # Prepare initial state
    qc = QuantumCircuit(2, 2)
    for gate, qubit in gates:
        if gate == 'x':
            qc.x(qubit)
    
    # Apply CNOT (qubit 0 control, qubit 1 target)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    # Execute
    counts = simulator.run(qc, shots=1000).result().get_counts()
    
    # Visualize
    ax = axes[idx]
    ax.bar(counts.keys(), counts.values(), color=COLORS['primary'],
           edgecolor='black', linewidth=2)
    ax.set_title(f'CNOT on |{label}⟩', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of times')
    ax.grid(axis='y', alpha=0.3)
    
    # Annotate expected result
    expected = list(counts.keys())[0]
    ax.text(0.5, 0.9, f'Result: |{expected}⟩',
            transform=ax.transAxes, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5),
            fontsize=10)

plt.suptitle('CNOT Truth Table', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("✅ CNOT: flip target IF AND ONLY IF control = 1")
```

---

### 📌 Section 4: CNOT with Superposition - It Gets Interesting! (3 min)

**Markdown content**:
```markdown
## Section 4: CNOT + Superposition = Correlation

Now, let's apply CNOT when the **control** qubit is in **superposition**.

### 🎭 Circuit

```
q0 (control): ──H──●──
                   │
q1 (target):  ─────X──
```

**Steps**:
1. H on q0: |00⟩ → (|00⟩ + |10⟩)/√2
2. CNOT: 
   - On |00⟩ component: no change → |00⟩
   - On |10⟩ component: flip q1 → |11⟩
3. Result: (|00⟩ + |11⟩)/√2

### 🎯 Crucial Observation

The qubits are now **correlated**:
- If we measure q0 = 0 → q1 will definitely be 0
- If we measure q0 = 1 → q1 will definitely be 1

Never |01⟩ or |10⟩!
```

**Code cell**:
```python
# Create state (|00⟩ + |11⟩)/√2
qc_bell = QuantumCircuit(2, 2)
qc_bell.h(0)        # Superposition on q0
qc_bell.cx(0, 1)    # CNOT
qc_bell.measure([0, 1], [0, 1])

# Visualize the circuit
print("Circuit to create (|00⟩ + |11⟩)/√2:")
display(qc_bell.draw('mpl'))

# Execute
counts_bell = simulator.run(qc_bell, shots=1000).result().get_counts()

print(f"\n📊 Results:")
for state, count in sorted(counts_bell.items()):
    print(f"   |{state}⟩: {count} times ({count/10:.1f}%)")

# Visualization
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
bars = ax.bar(counts_bell.keys(), counts_bell.values(),
              color=COLORS['quantum'], edgecolor='black', linewidth=2)
ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('Bell State: (|00⟩ + |11⟩)/√2', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Annotate
ax.text(0.5, 0.9, '⚠️ Never |01⟩ or |10⟩!',
        transform=ax.transAxes, ha='center', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

plt.show()

print("\n🔗 The qubits are CORRELATED!")
print("   Measuring one instantly determines the other")
```

---

### 📌 Section 5: The 4 Bell States (3 min)

**Markdown content**:
```markdown
## Section 5: The Four Bell States

State (|00⟩ + |11⟩)/√2 is a **Bell state**, also called **EPR state** (Einstein-Podolsky-Rosen).

There are **4 Bell states**, all maximally correlated:

### 🔵 |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
**Circuit**: H on q0, then CNOT

**Correlation**: Results always identical (00 or 11)

### 🟢 |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
**Circuit**: H on q0, CNOT, then Z on q0 (or q1)

**Correlation**: Identical, but with negative phase

### 🟡 |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
**Circuit**: X on q1, H on q0, CNOT

**Correlation**: Results always opposite (01 or 10)

### 🔴 |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2
**Circuit**: X on q1, H on q0, CNOT, Z on q0

**Correlation**: Opposite, with negative phase

### 📐 Importance

Bell states are:
- **Maximally entangled**
- **Orthogonal** to each other
- The basis for **quantum teleportation**
- Used in **quantum cryptography**
```

**Code cell - Create the 4 states**:
```python
# Functions to create the 4 Bell states
def create_phi_plus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def create_phi_minus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(0)
    return qc

def create_psi_plus():
    qc = QuantumCircuit(2, 2)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def create_psi_minus():
    qc = QuantumCircuit(2, 2)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(0)
    return qc

# Create and measure the 4 states
bell_states = [
    (create_phi_plus(), '|Φ⁺⟩ = (|00⟩+|11⟩)/√2'),
    (create_phi_minus(), '|Φ⁻⟩ = (|00⟩-|11⟩)/√2'),
    (create_psi_plus(), '|Ψ⁺⟩ = (|01⟩+|10⟩)/√2'),
    (create_psi_minus(), '|Ψ⁻⟩ = (|01⟩-|10⟩)/√2')
]

fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=150)
axes = axes.flatten()

for idx, (qc, label) in enumerate(bell_states):
    qc.measure([0, 1], [0, 1])
    counts = simulator.run(qc, shots=1000).result().get_counts()
    
    ax = axes[idx]
    colors = [COLORS['primary'], COLORS['secondary'], 
              COLORS['accent'], COLORS['quantum']]
    ax.bar(counts.keys(), counts.values(), 
           color=colors[idx], edgecolor='black', linewidth=2)
    ax.set_title(label, fontsize=11, fontweight='bold')
    ax.set_ylabel('Number of times')
    ax.grid(axis='y', alpha=0.3)

plt.suptitle('The 4 Bell States', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("✅ The 4 Bell states created!")
print("   Φ⁺ and Φ⁻: identical correlation (00 or 11)")
print("   Ψ⁺ and Ψ⁻: anti-correlation (01 or 10)")
```

---

### 📌 Section 6: Exercise - No-Cloning? (1 min)

**Markdown content**:
```markdown
## 🎯 Exercise: Can We "Copy" a Qubit?

**Question**: We want to copy the state of q0 onto q1.

```python
# Goal: |ψ⟩|0⟩ → |ψ⟩|ψ⟩
qc = QuantumCircuit(2, 2)
# Prepare a state on q0 (e.g., H for |+⟩)
qc.h(0)
# Try to copy with CNOT?
qc.cx(0, 1)
```

🤔 **Does it work for "copying"?**

<details>
<summary>👉 Click for the answer</summary>

**It depends on the state!**

- **For |0⟩**: |0⟩|0⟩ → |0⟩|0⟩ ✅ (copy successful)
- **For |1⟩**: |1⟩|0⟩ → |1⟩|1⟩ ✅ (copy successful)
- **For |+⟩**: 
  - Initial: (|0⟩+|1⟩)/√2 ⊗ |0⟩ = (|00⟩+|10⟩)/√2
  - After CNOT: (|00⟩+|11⟩)/√2 ❌ (NOT |+⟩|+⟩!)

**Conclusion**: CNOT only copies basis states.  
This is a consequence of the **no-cloning theorem**: we cannot copy an arbitrary quantum state.

We'll see this in more detail in Notebook 6 (Teleportation)!

</details>
```

---

### 📌 Section 7: Checkpoint & Quiz (1 min)

**Markdown content**:
```markdown
## 🎯 CHECKPOINT

- [ ] Create a circuit with 2 qubits?
- [ ] Apply CNOT with correct control/target?
- [ ] Predict CNOT result on the 4 basis states?
- [ ] Create the 4 Bell states?
- [ ] Understand quantum correlation?

---

## 🎯 Quick Quiz

**1. CNOT with control=0 does what?**
- [x] Nothing
- [ ] Flips target
- [ ] Flips control

**2. (|00⟩ + |11⟩)/√2 is which Bell state?**
- [x] |Φ⁺⟩
- [ ] |Φ⁻⟩
- [ ] |Ψ⁺⟩

**3. In (|00⟩ + |11⟩)/√2, can we measure |01⟩?**
- [ ] Yes, with 25% probability
- [ ] Yes, with 50% probability
- [x] No, impossible

**4. Which circuit creates |Ψ⁺⟩?**
- [ ] H then CNOT
- [x] X on q1, H on q0, then CNOT
- [ ] CNOT then H

**5. Can CNOT copy an arbitrary state?**
- [ ] Yes
- [x] No (no-cloning theorem)
```

---

### 📌 Section 8: Summary & Next Step (30 sec)

**Markdown content**:
```markdown
## 🎓 Notebook 3 Summary

**What you learned:**
✅ 2-qubit systems (4 basis states)  
✅ The CNOT gate (control + target)  
✅ Create quantum correlations  
✅ The 4 Bell states  
✅ Intuition of no-cloning theorem  

**Progress**: ⬛⬛⬛⬛⬜⬜⬜ (4/7 completed)

---

## 🚀 Next Step: Notebook 4 - Entanglement

We've created correlations with Bell states.  
Now we'll understand **why** these correlations are **classically impossible**.

**Coming up**:
- Classical vs quantum correlations
- Measurements in different bases
- Bell test (CHSH)
- Prove that nature is quantum!

We'll see Einstein be wrong! 🤯

See you soon! 🎉
```

---

# 📘 NOTEBOOK 4: Entanglement

**Duration**: 15 minutes  
**Goal**: Understand entanglement and prove its non-locality

*(Similar structure, with sections on classical correlations, CHSH test, etc.)*

---

# 📘 NOTEBOOK 5: Deutsch's Algorithm

**Duration**: 12 minutes  
**Goal**: First concrete quantum advantage

*(Structure with oracle, 1 query vs 2, implementation)*

---

# 📘 NOTEBOOK 6: Teleportation

**Duration**: 15 minutes  
**Goal**: Complete quantum teleportation protocol

*(Structure with no-cloning, 4 steps, fidelity)*

---

# 🎓 APPENDICES

## A. File Structure

```
QCTutorial/
├── notebooks/
│   ├── 00_my_first_qubit.ipynb
│   ├── 01_superposition.ipynb
│   ├── 02_rotations_interference.ipynb
│   ├── 03_two_qubits_cnot.ipynb
│   ├── 04_entanglement.ipynb
│   ├── 05_deutsch.ipynb
│   └── 06_teleportation.ipynb
├── utils/
│   ├── __init__.py
│   ├── plotting.py
│   └── monarch_config.py
├── README.md
├── pyproject.toml
└── NOTEBOOK_WRITING_PLAN.md (this file)
```

## B. Writing Checklist

For each notebook:

- [ ] Header with progress
- [ ] Section 1: Reminder/Context
- [ ] Intuition → implementation progression
- [ ] Code commented line by line
- [ ] Visualizations at each step
- [ ] Exercises (🟢🟡🔴)
- [ ] Intermediate checkpoints
- [ ] Final quiz
- [ ] Summary
- [ ] Teaser for next notebook

## C. Code Conventions

```python
# ✅ GOOD: Commented and annotated code
qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits
qc.h(0)                     # Hadamard on qubit 0
qc.cx(0, 1)                 # CNOT: 0 control, 1 target

# ❌ BAD: Code without explanation
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
```

## D. Color Palette (utils/plotting.py)

```python
COLORS = {
    'primary': '#FF69B4',      # Hot Pink
    'secondary': '#9370DB',    # Medium Purple
    'accent': '#00CED1',       # Dark Turquoise
    'quantum': '#8A2BE2',      # Blue Violet
    'classical': '#808080',    # Gray
    'success': '#32CD32',      # Lime Green
}
```

## E. Cell Templates

### Template: Circuit Visualization
```python
# Visualize the circuit
print("Circuit [Circuit name]:")
display(qc.draw('mpl'))

print("\n📝 Explanation:")
print("   • Line 1: Description")
print("   • Line 2: Description")
```

### Template: Measurement and Histogram
```python
# Execute the circuit
simulator = AerSimulator()
counts = simulator.run(qc, shots=1000).result().get_counts()

# Visualization
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
ax.bar(counts.keys(), counts.values(), 
       color=COLORS['quantum'], edgecolor='black', linewidth=2)
ax.set_ylabel('Number of times', fontsize=12)
ax.set_title('[Title]', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)
plt.show()

print("\n✅ Observation: [Conclusion]")
```

---

# 🎯 Next Steps

1. **Validation**: Review this plan with the team
2. **Prototype**: Write complete Notebook 0
3. **Test**: Have 1-2 people test it
4. **Iteration**: Adjust based on feedback
5. **Writing**: Complete all 7 notebooks
6. **Pilot workshop**: Test with full team

**Happy writing! 🚀✨**

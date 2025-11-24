"""
Beautiful plotting utilities for quantum computing workshop.

This module provides reusable plotting functions with a sparkly/unicorn theme 🦄✨
All plots use vibrant colors and clean, professional styling.
"""

from typing import Any, Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city


# Beautiful color palette - sparkly/unicorn theme 🦄✨
COLORS = {
    'primary': '#FF69B4',      # Hot pink
    'secondary': '#9370DB',    # Medium purple
    'accent': '#00CED1',       # Dark turquoise
    'highlight': '#FFD700',    # Gold
    'quantum': '#8A2BE2',      # Blue violet
    'classical': '#FF6B6B',    # Light red
    'success': '#51CF66',      # Green
    'info': '#4DABF7',         # Blue
}

# Extended palette for multiple states
PALETTE = ['#FF69B4', '#9370DB', '#00CED1', '#FFD700', '#8A2BE2', '#FF6B6B', '#51CF66', '#4DABF7']


def configure_beautiful_plots() -> None:
    """
    Configure matplotlib and seaborn for beautiful, sparkly plots.
    
    This function sets up the global plotting style for the workshop.
    Call this once at the beginning of each notebook.
    
    Returns:
        None
    
    Example:
        >>> configure_beautiful_plots()
        >>> # Now all plots will use the beautiful style
    """
    # Set seaborn style
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    
    # Set matplotlib defaults
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['savefig.dpi'] = 150
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 16
    plt.rcParams['figure.titleweight'] = 'bold'
    
    # Use beautiful color cycle
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=PALETTE)


def plot_histogram_comparison(
    data1: Dict[str, int],
    data2: Dict[str, int],
    title1: str = "Classical",
    title2: str = "Quantum",
    overall_title: Optional[str] = None,
    figsize: Tuple[int, int] = (14, 5),
) -> Figure:
    """
    Create beautiful side-by-side histogram comparison.
    
    Perfect for comparing classical probability vs quantum superposition,
    or simulator vs hardware results.
    
    Args:
        data1: Dictionary of counts for first dataset (e.g., {'0': 500, '1': 500})
        data2: Dictionary of counts for second dataset
        title1: Title for first histogram
        title2: Title for second histogram
        overall_title: Optional overall figure title
        figsize: Figure size as (width, height)
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> classical_counts = {'0': 485, '1': 515}
        >>> quantum_counts = {'0': 501, '1': 499}
        >>> fig = plot_histogram_comparison(classical_counts, quantum_counts)
        >>> plt.show()
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, dpi=150)
    
    # Extract keys and values (maintain order)
    keys1 = sorted(data1.keys())
    values1 = [data1[k] for k in keys1]
    
    keys2 = sorted(data2.keys())
    values2 = [data2[k] for k in keys2]
    
    # Plot first histogram
    bars1 = ax1.bar(keys1, values1, color=COLORS['classical'], alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_title(title1, fontsize=16, fontweight='bold', pad=15)
    ax1.set_xlabel('State', fontsize=12)
    ax1.set_ylabel('Counts', fontsize=12)
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Plot second histogram
    bars2 = ax2.bar(keys2, values2, color=COLORS['quantum'], alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_title(title2, fontsize=16, fontweight='bold', pad=15)
    ax2.set_xlabel('State', fontsize=12)
    ax2.set_ylabel('Counts', fontsize=12)
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Set same y-axis limits for fair comparison
    max_count = max(max(values1), max(values2))
    ax1.set_ylim(0, max_count * 1.15)
    ax2.set_ylim(0, max_count * 1.15)
    
    if overall_title:
        fig.suptitle(overall_title, fontsize=18, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    return fig


def plot_bloch_sphere(
    state: Union[Statevector, QuantumCircuit],
    title: str = "Quantum State on Bloch Sphere",
    figsize: Tuple[int, int] = (8, 8),
) -> Figure:
    """
    Plot quantum state on Bloch sphere with beautiful styling.
    
    Args:
        state: Statevector or QuantumCircuit to visualize
        title: Title for the plot
        figsize: Figure size as (width, height)
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> from qiskit.quantum_info import Statevector
        >>> state = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])
        >>> fig = plot_bloch_sphere(state)
        >>> plt.show()
    """
    # Convert circuit to statevector if needed
    if isinstance(state, QuantumCircuit):
        state = Statevector(state)
    
    # Create Bloch sphere visualization
    fig = plot_bloch_multivector(state, figsize=figsize)
    fig.suptitle(title, fontsize=16, fontweight='bold', y=0.95)
    
    return fig


def plot_circuit(
    circuit: QuantumCircuit,
    title: Optional[str] = None,
    style: str = 'iqp',
    figsize: Optional[Tuple[int, int]] = None,
) -> Figure:
    """
    Draw beautiful quantum circuit diagram.
    
    Args:
        circuit: Quantum circuit to draw
        title: Optional title for the circuit
        style: Drawing style ('iqp', 'clifford', or 'bw')
        figsize: Optional figure size as (width, height)
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> from qiskit import QuantumCircuit
        >>> qc = QuantumCircuit(2)
        >>> qc.h(0)
        >>> qc.cx(0, 1)
        >>> fig = plot_circuit(qc, title="Bell State Circuit")
        >>> plt.show()
    """
    # Determine figure size based on circuit depth if not specified
    if figsize is None:
        depth = circuit.depth()
        width = min(max(8, depth * 1.5), 20)
        height = min(max(4, circuit.num_qubits * 1.5), 12)
        figsize = (width, height)
    
    # Draw circuit
    fig = circuit.draw('mpl', style=style)
    
    if isinstance(fig, Figure):
        if title:
            fig.suptitle(title, fontsize=16, fontweight='bold', y=0.98)
        fig.set_size_inches(figsize)
        fig.set_dpi(150)
    
    return fig


def plot_correlation_matrix(
    data: np.ndarray,
    labels: Optional[List[str]] = None,
    title: str = "Correlation Matrix",
    figsize: Tuple[int, int] = (8, 7),
    cmap: str = 'RdPu',
) -> Figure:
    """
    Plot beautiful correlation matrix heatmap.
    
    Perfect for visualizing entanglement correlations.
    
    Args:
        data: 2D numpy array of correlation values
        labels: Optional labels for axes
        title: Title for the plot
        figsize: Figure size as (width, height)
        cmap: Colormap name (default: 'RdPu' for sparkly pink-purple)
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> correlation = np.array([[1.0, 0.95], [0.95, 1.0]])
        >>> fig = plot_correlation_matrix(correlation, labels=['Qubit 0', 'Qubit 1'])
        >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=figsize, dpi=150)
    
    # Create heatmap with annotations
    sns.heatmap(
        data,
        annot=True,
        fmt='.3f',
        cmap=cmap,
        square=True,
        linewidths=2,
        linecolor='white',
        cbar_kws={'label': 'Correlation'},
        ax=ax,
        vmin=-1,
        vmax=1,
        center=0,
    )
    
    if labels:
        ax.set_xticklabels(labels, rotation=45, ha='right')
        ax.set_yticklabels(labels, rotation=0)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    
    plt.tight_layout()
    return fig


def plot_statevector(
    state: Union[Statevector, QuantumCircuit],
    title: str = "Quantum State Amplitudes",
    figsize: Tuple[int, int] = (10, 6),
    plot_type: str = 'bar',
) -> Figure:
    """
    Plot quantum state amplitudes (can show negative values!).
    
    This is crucial for demonstrating quantum interference, as it shows
    the amplitude values before squaring to get probabilities.
    
    Args:
        state: Statevector or QuantumCircuit to visualize
        title: Title for the plot
        figsize: Figure size as (width, height)
        plot_type: 'bar' for bar chart, 'city' for city plot
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> state = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])
        >>> fig = plot_statevector(state)
        >>> plt.show()
    """
    # Convert circuit to statevector if needed
    if isinstance(state, QuantumCircuit):
        state = Statevector(state)
    
    if plot_type == 'city':
        fig = plot_state_city(state, figsize=figsize)
        if isinstance(fig, Figure):
            fig.suptitle(title, fontsize=16, fontweight='bold', y=0.98)
    else:
        # Bar plot showing real and imaginary parts
        amplitudes = state.data
        n_states = len(amplitudes)
        state_labels = [f'|{i:0{int(np.log2(n_states))}b}⟩' for i in range(n_states)]
        
        real_parts = np.real(amplitudes)
        imag_parts = np.imag(amplitudes)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, dpi=150)
        
        # Real parts
        bars1 = ax1.bar(state_labels, real_parts, color=COLORS['primary'], alpha=0.8, edgecolor='black', linewidth=1.5)
        ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        ax1.set_title('Real Part', fontsize=14, fontweight='bold')
        ax1.set_xlabel('State', fontsize=12)
        ax1.set_ylabel('Amplitude', fontsize=12)
        ax1.grid(axis='y', alpha=0.3)
        
        # Imaginary parts
        bars2 = ax2.bar(state_labels, imag_parts, color=COLORS['secondary'], alpha=0.8, edgecolor='black', linewidth=1.5)
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        ax2.set_title('Imaginary Part', fontsize=14, fontweight='bold')
        ax2.set_xlabel('State', fontsize=12)
        ax2.set_ylabel('Amplitude', fontsize=12)
        ax2.grid(axis='y', alpha=0.3)
        
        # Set same y-axis limits
        max_amp = max(np.max(np.abs(real_parts)), np.max(np.abs(imag_parts)))
        ax1.set_ylim(-max_amp * 1.2, max_amp * 1.2)
        ax2.set_ylim(-max_amp * 1.2, max_amp * 1.2)
        
        fig.suptitle(title, fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
    
    return fig


def plot_multiple_histograms(
    data_list: List[Dict[str, int]],
    titles: List[str],
    overall_title: Optional[str] = None,
    ncols: int = 2,
    figsize: Optional[Tuple[int, int]] = None,
) -> Figure:
    """
    Plot multiple histograms in a grid layout.
    
    Perfect for comparing multiple quantum circuits or Bell states.
    
    Args:
        data_list: List of count dictionaries
        titles: List of titles for each histogram
        overall_title: Optional overall figure title
        ncols: Number of columns in grid
        figsize: Optional figure size, auto-calculated if None
        
    Returns:
        Matplotlib figure object
        
    Example:
        >>> data = [{'00': 500, '11': 500}, {'00': 0, '01': 500, '10': 500, '11': 0}]
        >>> titles = ['Bell Φ⁺', 'Bell Ψ⁺']
        >>> fig = plot_multiple_histograms(data, titles, overall_title='Bell States')
        >>> plt.show()
    """
    n_plots = len(data_list)
    nrows = (n_plots + ncols - 1) // ncols
    
    if figsize is None:
        figsize = (7 * ncols, 5 * nrows)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, dpi=150)
    
    # Flatten axes array for easier iteration
    if n_plots == 1:
        axes = [axes]
    elif nrows == 1 or ncols == 1:
        axes = axes.flatten()
    else:
        axes = axes.flatten()
    
    for idx, (data, title) in enumerate(zip(data_list, titles)):
        ax = axes[idx]
        
        keys = sorted(data.keys())
        values = [data[k] for k in keys]
        
        color = PALETTE[idx % len(PALETTE)]
        bars = ax.bar(keys, values, color=color, alpha=0.8, edgecolor='black', linewidth=1.5)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
        ax.set_xlabel('State', fontsize=11)
        ax.set_ylabel('Counts', fontsize=11)
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Hide unused subplots
    for idx in range(n_plots, len(axes)):
        axes[idx].axis('off')
    
    if overall_title:
        fig.suptitle(overall_title, fontsize=18, fontweight='bold', y=1.00)
    
    plt.tight_layout()
    return fig

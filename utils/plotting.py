"""
Beautiful plotting utilities for quantum computing visualizations.

This module provides a consistent, beautiful style for all visualizations
in the quantum computing workshop notebooks.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, Tuple

# Beautiful color palette (sparkly/unicorn theme 🦄✨)
COLORS = {
    'primary': '#FF69B4',      # Hot pink
    'secondary': '#9370DB',    # Medium purple
    'accent': '#00CED1',       # Dark turquoise
    'highlight': '#FFD700',    # Gold
    'quantum': '#8A2BE2',      # Blue violet
    'classical': '#FF7F50',    # Coral
    'success': '#32CD32',      # Lime green
    'error': '#DC143C',        # Crimson
}

# Extended color palettes for multiple elements
PALETTE_HUSL = sns.color_palette("husl", 8)
PALETTE_ROCKET = sns.color_palette("rocket", 8)
PALETTE_MAKO = sns.color_palette("mako", 8)
PALETTE_FLARE = sns.color_palette("flare", 8)


def configure_beautiful_plots() -> None:
    """
    Configure matplotlib and seaborn for beautiful, consistent plots.
    
    This function sets up:
    - Seaborn whitegrid style
    - Larger font sizes for readability
    - High DPI for crisp figures
    - Beautiful default color cycle
    """
    # Set seaborn style
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    
    # Configure matplotlib defaults
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    
    # Set default color cycle to our beautiful palette
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        COLORS['quantum'],
        COLORS['primary'],
        COLORS['accent'],
        COLORS['secondary'],
        COLORS['highlight'],
        COLORS['success'],
    ])


def plot_measurement_histogram(
    counts: dict,
    title: str = "Measurement Results",
    color: str = None,
    ax: Optional[plt.Axes] = None,
    show_percentage: bool = True,
) -> plt.Figure:
    """
    Plot a beautiful histogram of measurement results.
    
    Args:
        counts: Dictionary of measurement counts (e.g., {'0': 500, '1': 500})
        title: Title for the plot
        color: Bar color (defaults to 'quantum' from COLORS)
        ax: Matplotlib axes to plot on (creates new figure if None)
        show_percentage: Whether to show percentage labels on bars
        
    Returns:
        The matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    else:
        fig = ax.figure
    
    if color is None:
        color = COLORS['quantum']
    
    # Sort keys for consistent ordering
    states = sorted(counts.keys())
    values = [counts[k] for k in states]
    total = sum(values)
    
    # Create bars
    bars = ax.bar(states, values, color=color, edgecolor='black', 
                   linewidth=2, alpha=0.8)
    
    # Add percentage labels if requested
    if show_percentage and total > 0:
        for bar, value in zip(bars, values):
            height = bar.get_height()
            percentage = (value / total) * 100
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{percentage:.1f}%',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Styling
    ax.set_xlabel('Measured State', fontsize=12)
    ax.set_ylabel('Number of Measurements', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_statevector(
    statevector,
    ax: Optional[plt.Axes] = None,
    title: str = "State Amplitudes",
    show_phase: bool = True,
) -> plt.Figure:
    """
    Plot the amplitudes (and optionally phases) of a quantum statevector.
    
    Args:
        statevector: Qiskit Statevector object
        ax: Matplotlib axes to plot on (creates new figure if None)
        title: Title for the plot
        show_phase: Whether to show phase information
        
    Returns:
        The matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    else:
        fig = ax.figure
    
    # Get the statevector data
    data = statevector.data
    n_states = len(data)
    state_labels = [f'|{i:0{int(np.log2(n_states))}b}⟩' for i in range(n_states)]
    
    # Calculate amplitudes and phases
    amplitudes = np.abs(data)
    phases = np.angle(data)
    
    # Plot amplitudes
    bars = ax.bar(state_labels, amplitudes, color=COLORS['quantum'],
                   edgecolor='black', linewidth=2, alpha=0.8)
    
    # Add value labels
    for bar, amp in zip(bars, amplitudes):
        if amp > 0.01:  # Only show significant amplitudes
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{amp:.3f}',
                   ha='center', va='bottom', fontsize=9)
    
    # Styling
    ax.set_ylabel('Amplitude |ψᵢ|', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylim([0, 1.1])
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_comparison(
    data_dict: dict,
    title: str = "Comparison",
    ylabel: str = "Counts",
    colors: Optional[list] = None,
) -> plt.Figure:
    """
    Create a side-by-side comparison plot.
    
    Args:
        data_dict: Dictionary mapping labels to count dictionaries
                  e.g., {'Classical': {'0': 500, '1': 500}, 
                         'Quantum': {'0': 480, '1': 520}}
        title: Overall title for the figure
        ylabel: Label for y-axis
        colors: List of colors for each subplot (uses defaults if None)
        
    Returns:
        The matplotlib figure
    """
    n_plots = len(data_dict)
    fig, axes = plt.subplots(1, n_plots, figsize=(6*n_plots, 5), dpi=150)
    
    # Handle single plot case
    if n_plots == 1:
        axes = [axes]
    
    if colors is None:
        colors = [COLORS['classical'], COLORS['quantum'], COLORS['accent'], 
                  COLORS['primary']][:n_plots]
    
    for ax, (label, counts), color in zip(axes, data_dict.items(), colors):
        states = sorted(counts.keys())
        values = [counts[k] for k in states]
        
        ax.bar(states, values, color=color, edgecolor='black', 
               linewidth=2, alpha=0.8)
        ax.set_title(label, fontsize=13, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=12)
        ax.grid(axis='y', alpha=0.3)
    
    plt.suptitle(title, fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig


def add_progress_bar(
    ax: plt.Axes,
    current: int,
    total: int,
    position: Tuple[float, float] = (0.5, 0.95),
) -> None:
    """
    Add a progress bar to a plot.
    
    Args:
        ax: Matplotlib axes to add progress bar to
        current: Current progress (0 to total)
        total: Total number of steps
        position: (x, y) position in axes coordinates (0-1)
    """
    filled = '⬛' * current
    empty = '⬜' * (total - current)
    progress_text = f'{filled}{empty} ({current}/{total})'
    
    ax.text(position[0], position[1], progress_text,
           transform=ax.transAxes, ha='center', va='top',
           fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


# Export all public functions and constants
__all__ = [
    'COLORS',
    'PALETTE_HUSL',
    'PALETTE_ROCKET',
    'PALETTE_MAKO',
    'PALETTE_FLARE',
    'configure_beautiful_plots',
    'plot_measurement_histogram',
    'plot_statevector',
    'plot_comparison',
    'add_progress_bar',
]

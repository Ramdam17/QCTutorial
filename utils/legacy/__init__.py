"""
Quantum Computing Workshop Utilities

This package provides utility functions for the quantum computing workshop,
including beautiful visualizations and hardware backend configuration.
"""

from .plotting import (
    configure_beautiful_plots,
    plot_histogram_comparison,
    plot_bloch_sphere,
    plot_circuit,
    plot_correlation_matrix,
    plot_statevector,
    COLORS,
)

__all__ = [
    "configure_beautiful_plots",
    "plot_histogram_comparison",
    "plot_bloch_sphere",
    "plot_circuit",
    "plot_correlation_matrix",
    "plot_statevector",
    "COLORS",
]

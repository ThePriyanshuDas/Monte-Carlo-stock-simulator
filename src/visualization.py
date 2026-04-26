import matplotlib.pyplot as plt
import numpy as np


def plot_paths(paths, title="Monte Carlo Simulated Paths", show=True):
    """
    Plot simulated stock price paths.

    Parameters:
    - paths (ndarray): shape (time_steps, simulations)
    - title (str): plot title
    - show (bool): whether to display the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(paths, linewidth=0.8, alpha=0.7)
    plt.title(title)
    plt.xlabel("Time Steps")
    plt.ylabel("Price")
    plt.grid(True)

    if show:
        plt.show()

    return plt.gcf()


def plot_distribution(final_prices, bins=50, title="Final Price Distribution", show=True):
    """
    Plot histogram of final simulated prices.

    Parameters:
    - final_prices (array-like)
    - bins (int)
    - title (str)
    - show (bool)
    """
    plt.figure(figsize=(8, 5))
    plt.hist(final_prices, bins=bins, alpha=0.7)
    plt.title(title)
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.grid(True)

    if show:
        plt.show()

    return plt.gcf()


def plot_with_var(final_prices, var_level=5, bins=50, show=True):
    """
    Plot distribution with Value at Risk (VaR) line.

    Parameters:
    - final_prices (array-like)
    - var_level (int): percentile (e.g., 5 for 5% VaR)
    - bins (int)
    - show (bool)
    """
    var_value = np.percentile(final_prices, var_level)

    plt.figure(figsize=(8, 5))
    plt.hist(final_prices, bins=bins, alpha=0.7)
    plt.axvline(var_value, linestyle="--", linewidth=2)

    plt.title(f"Final Price Distribution with {var_level}% VaR")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.grid(True)

    if show:
        plt.show()

    return plt.gcf(), var_value
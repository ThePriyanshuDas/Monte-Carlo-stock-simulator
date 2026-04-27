import numpy as np


class GeometricBrownianMotion:
    """
    Geometric Brownian Motion (GBM) model for stock price simulation.

    dS = μS dt + σS dW
    """

    def __init__(self, mu: float, sigma: float):
        """
        Parameters:
        - mu (float): drift (annual return)
        - sigma (float): volatility (annual)
        """
        self.mu = float(mu)
        self.sigma = float(sigma)

    def simulate(self, S0: float, T: float, steps_per_year: int, n_simulations: int):
        """
        Simulate price paths using GBM.

        Parameters:
        - S0 (float): initial price
        - T (float): time horizon (years)
        - steps_per_year (int): time granularity (e.g., 252)
        - n_simulations (int): number of paths

        Returns:
        - paths (ndarray): shape (time_steps, n_simulations)
        """
        dt = 1 / steps_per_year
        N = int(T * steps_per_year)

        paths = np.zeros((N, n_simulations))
        paths[0] = S0

        for t in range(1, N):
            Z = np.random.standard_normal(n_simulations)
            paths[t] = paths[t - 1] * np.exp(
                (self.mu - 0.5 * self.sigma**2) * dt
                + self.sigma * np.sqrt(dt) * Z
            )

        return paths

    def simulate_vectorized(self, S0: float, T: float, steps_per_year: int, n_simulations: int):
        """
        Fully vectorized GBM simulation (faster, no loops).

        Returns:
        - paths (ndarray): shape (time_steps, n_simulations)
        """
        dt = 1 / steps_per_year
        N = int(T * steps_per_year)

        # Random shocks
        Z = np.random.standard_normal((N, n_simulations))

        # Drift + diffusion
        increments = (
            (self.mu - 0.5 * self.sigma**2) * dt
            + self.sigma * np.sqrt(dt) * Z
        )

        # Cumulative sum → log prices
        log_paths = np.cumsum(increments, axis=0)

        # Convert to price paths
        paths = S0 * np.exp(log_paths)

        # Fix first row explicitly
        paths[0] = S0

        return paths
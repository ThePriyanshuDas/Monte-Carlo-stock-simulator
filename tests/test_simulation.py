import numpy as np
import pytest

from src.simulation import simulate_gbm
from models.gbm import GeometricBrownianMotion


def test_simulation_shape():
    """Ensure output shape is correct."""
    paths = simulate_gbm(
        S0=100,
        mu=0.1,
        sigma=0.2,
        T=1,
        steps_per_year=252,
        n_simulations=500
    )

    assert paths.shape == (252, 500)


def test_initial_value():
    """First row should equal initial price."""
    S0 = 123.45
    paths = simulate_gbm(S0, 0.1, 0.2, 1, 252, 100)

    assert np.allclose(paths[0], S0)


def test_positive_prices():
    """GBM should always produce positive prices."""
    paths = simulate_gbm(100, 0.1, 0.2, 1, 252, 1000)

    assert np.all(paths > 0)


def test_zero_volatility():
    """With sigma = 0, path should be deterministic exponential growth."""
    S0 = 100
    mu = 0.1
    sigma = 0.0

    paths = simulate_gbm(S0, mu, sigma, 1, 252, 1)

    # deterministic expected path
    dt = 1 / 252
    expected = np.array([
        S0 * np.exp(mu * dt * t) for t in range(252)
    ])

    assert np.allclose(paths[:, 0], expected, atol=1e-2)


def test_gbm_class_vs_function():
    """Compare class-based GBM with function implementation."""
    S0 = 100
    mu = 0.1
    sigma = 0.2

    gbm = GeometricBrownianMotion(mu, sigma)

    paths_class = gbm.simulate(S0, 1, 252, 100)
    paths_func = simulate_gbm(S0, mu, sigma, 1, 252, 100)

    # shapes should match
    assert paths_class.shape == paths_func.shape


def test_vectorized_vs_loop():
    """Vectorized and loop versions should produce similar distributions."""
    gbm = GeometricBrownianMotion(mu=0.1, sigma=0.2)

    paths_loop = gbm.simulate(100, 1, 252, 500)
    paths_vec = gbm.simulate_vectorized(100, 1, 252, 500)

    # Compare mean of final prices (not exact paths)
    mean_loop = np.mean(paths_loop[-1])
    mean_vec = np.mean(paths_vec[-1])

    assert np.isclose(mean_loop, mean_vec, rtol=0.1)
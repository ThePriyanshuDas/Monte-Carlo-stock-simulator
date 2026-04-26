import numpy as np
import pandas as pd

from src.preprocessing import compute_log_returns, estimate_parameters


def test_log_returns_shape():
    prices = pd.Series([100, 101, 102, 103])
    returns = compute_log_returns(prices)

    assert len(returns) == len(prices) - 1


def test_log_returns_values():
    prices = pd.Series([100, 110])
    returns = compute_log_returns(prices)

    expected = np.log(110 / 100)
    assert np.isclose(returns.iloc[0], expected)


def test_estimate_parameters_output():
    returns = pd.Series([0.01, 0.02, -0.01, 0.03])

    mu, sigma = estimate_parameters(returns)

    assert isinstance(mu, float) or isinstance(mu, np.floating)
    assert isinstance(sigma, float) or isinstance(sigma, np.floating)


def test_zero_returns():
    returns = pd.Series([0, 0, 0, 0])

    mu, sigma = estimate_parameters(returns)

    assert mu == 0
    assert sigma == 0
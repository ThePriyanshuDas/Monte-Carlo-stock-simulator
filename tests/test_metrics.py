import numpy as np

from src.metrics import expected_price, compute_var


def test_expected_price():
    prices = np.array([100, 110, 120])

    result = expected_price(prices)

    assert result == np.mean(prices)


def test_var_calculation():
    prices = np.array([100, 90, 80, 70, 60])

    var_5 = compute_var(prices, alpha=5)

    expected = np.percentile(prices, 5)

    assert np.isclose(var_5, expected)


def test_var_bounds():
    prices = np.array([100, 200, 300])

    var = compute_var(prices, alpha=5)

    assert var <= np.max(prices)
    assert var >= np.min(prices)
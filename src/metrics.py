import numpy as np

def expected_price(final_prices):
    return np.mean(final_prices)

def compute_var(final_prices, alpha=5):
    return np.percentile(final_prices, alpha)
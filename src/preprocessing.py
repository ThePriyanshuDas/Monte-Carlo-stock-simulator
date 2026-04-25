import numpy as np

def compute_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

def estimate_parameters(log_returns):
    mu = log_returns.mean() * 252
    sigma = log_returns.std() * (252 ** 0.5)
    return mu, sigma
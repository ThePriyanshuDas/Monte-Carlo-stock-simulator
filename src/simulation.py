import numpy as np

def simulate_gbm(S0, mu, sigma, T, steps_per_year, n_simulations):
    dt = 1 / steps_per_year
    N = int(T * steps_per_year)

    paths = np.zeros((N, n_simulations))
    paths[0] = S0

    for t in range(1, N):
        Z = np.random.standard_normal(n_simulations)
        paths[t] = paths[t-1] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
        )

    return paths
import argparse

from src.data_loader import load_from_yahoo
from src.preprocessing import compute_log_returns, estimate_parameters
from src.simulation import simulate_gbm
from src.metrics import expected_price, compute_var
from src.visualization_plotly import plot_paths_interactive, plot_distribution_interactive


def run_simulation(ticker: str, simulations: int, T: int):
    # =========================
    # Load Data
    # =========================
    prices = load_from_yahoo(ticker)

    # =========================
    # Preprocessing
    # =========================
    log_returns = compute_log_returns(prices)
    mu, sigma = estimate_parameters(log_returns)

    # Ensure scalars
    mu = float(mu)
    sigma = float(sigma)

    S0 = float(prices.iloc[-1])

    # =========================
    # Simulation
    # =========================
    paths = simulate_gbm(
        S0=S0,
        mu=mu,
        sigma=sigma,
        T=T,
        steps_per_year=252,
        n_simulations=simulations
    )

    final_prices = paths[-1]

    # =========================
    # Metrics
    # =========================
    exp_price = expected_price(final_prices)
    var_5 = compute_var(final_prices, alpha=5)

    print(f"\n📊 Results for {ticker}")
    print(f"Expected Price: {exp_price:.2f}")
    print(f"Value at Risk (5%): {var_5:.2f}")
    print(f"Drift (μ): {mu:.4f}")
    print(f"Volatility (σ): {sigma:.4f}")

    # =========================
    # Visualization
    # =========================
    fig1 = plot_paths_interactive(paths[:, :100])
    fig1.show()

    fig2 = plot_distribution_interactive(final_prices)
    fig2.show()


def main():
    parser = argparse.ArgumentParser(description="Monte Carlo Stock Simulator")

    parser.add_argument("--ticker", type=str, default="AAPL", help="Stock ticker symbol")
    parser.add_argument("--simulations", type=int, default=1000, help="Number of simulations")
    parser.add_argument("--time", type=int, default=1, help="Time horizon (years)")

    args = parser.parse_args()

    run_simulation(
        ticker=args.ticker,
        simulations=args.simulations,
        T=args.time
    )


if __name__ == "__main__":
    main()
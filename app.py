import streamlit as st
import numpy as np
import yfinance as yf

from src.visualization_plotly import (
    plot_paths_interactive,
    plot_distribution_with_var
)

st.set_page_config(layout="wide")

# =========================
# Title
# =========================
st.title("📈 Monte Carlo Stock Simulator Dashboard")

# =========================
# Sidebar Inputs
# =========================
st.sidebar.header("⚙️ Simulation Settings")

ticker = st.sidebar.text_input("Stock Ticker", "AAPL")
start_date = st.sidebar.date_input("Start Date", value=None)

T = st.sidebar.slider("Time Horizon (Years)", 1, 5, 1)
steps = st.sidebar.selectbox("Steps per Year", [252, 365])
simulations = st.sidebar.slider("Simulations", 100, 5000, 1000)

run_button = st.sidebar.button("Run Simulation")

# =========================
# Data Loading
# =========================
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=start_date or "2020-01-01")

    # Handle multi-index columns (yfinance issue)
    if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    return data["Close"]
# =========================
# Simulation Function
# =========================
def simulate_gbm(S0, mu, sigma, T, steps, simulations):
    dt = 1 / steps
    N = int(T * steps)

    paths = np.zeros((N, simulations))
    paths[0] = S0

    for t in range(1, N):
        Z = np.random.standard_normal(simulations)
        paths[t] = paths[t-1] * np.exp(
            (mu - 0.5 * sigma**2)*dt + sigma * np.sqrt(dt)*Z
        )

    return paths

# =========================
# Run Simulation
# =========================
if run_button:
    prices = load_data(ticker)

    log_returns = np.log(prices / prices.shift(1)).dropna()
    mu = float(np.mean(log_returns)) * 252
    sigma = float(np.std(log_returns)) * np.sqrt(252)

    S0 = float(prices.iloc[-1])

    paths = simulate_gbm(S0, mu, sigma, T, steps, simulations)
    final_prices = paths[-1]

    # =========================
    # Metrics Row
    # =========================
    col1, col2, col3 = st.columns(3)

    col1.metric("📊 Expected Price", f"{np.mean(final_prices):.2f}")
    col2.metric("⚠️ VaR (5%)", f"{np.percentile(final_prices, 5):.2f}")
    col3.metric("📉 Volatility (σ)", f"{sigma:.2f}")

    st.divider()

    # =========================
    # Charts Row 1
    # =========================
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📈 Simulated Price Paths")
        fig_paths = plot_paths_interactive(paths[:, :100])  # limit for performance
        st.plotly_chart(fig_paths, use_container_width=True)

    with col_right:
        st.subheader("📊 Price Distribution + VaR")
        fig_dist, var = plot_distribution_with_var(final_prices)
        st.plotly_chart(fig_dist, use_container_width=True)

    st.divider()

    # =========================
    # Additional Insights
    # =========================
    st.subheader("📌 Insights")

    st.write(f"- Estimated drift (μ): {mu:.4f}")
    st.write(f"- Estimated volatility (σ): {sigma:.4f}")
    st.write(f"- Simulations: {simulations}")
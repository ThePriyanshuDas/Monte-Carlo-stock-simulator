import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("📈 Monte Carlo Stock Price Simulator")

st.markdown("Simulate future stock prices using Geometric Brownian Motion")

# Sidebar inputs
st.sidebar.header("Simulation Parameters")

S0 = st.sidebar.number_input("Initial Price", value=100.0)
mu = st.sidebar.number_input("Expected Return (μ)", value=0.1)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)
T = st.sidebar.slider("Time Horizon (Years)", 1, 5, 1)
steps = st.sidebar.selectbox("Steps per Year", [252, 365])
simulations = st.sidebar.slider("Number of Simulations", 100, 5000, 1000)

# Simulation function
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

# Run simulation
if st.button("Run Simulation"):
    paths = simulate_gbm(S0, mu, sigma, T, steps, simulations)
    final_prices = paths[-1]

    # Metrics
    st.subheader("📊 Results")
    st.write(f"Expected Price: {np.mean(final_prices):.2f}")
    st.write(f"Value at Risk (5%): {np.percentile(final_prices, 5):.2f}")

    # Plot paths
    st.subheader("📈 Simulated Paths")
    fig1, ax1 = plt.subplots()
    ax1.plot(paths)
    st.pyplot(fig1)

    # Distribution
    st.subheader("📉 Final Price Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(final_prices, bins=50)
    st.pyplot(fig2)
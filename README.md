# Monte Carlo Stock Price Simulator

A quantitative finance project that simulates future stock price paths using **Monte Carlo methods** and **Geometric Brownian Motion (GBM)**. This project estimates the distribution of possible future prices and evaluates financial risk metrics such as Value at Risk (VaR).

---

## 📌 Project Overview

Financial markets are inherently stochastic. Instead of predicting a single future price, this project generates **thousands of possible price trajectories** using probabilistic modeling.

The simulation helps answer:

* What is the expected future price of a stock?
* What is the downside risk?
* What is the probability of extreme losses?

---

## ⚙️ Mathematical Model

We model stock prices using **Geometric Brownian Motion (GBM)**:

$$
S_{t+1} = S_t \cdot \exp\left( (\mu - \frac{\sigma^2}{2})\Delta t + \sigma \sqrt{\Delta t} Z \right)
$$

Where:

* (S_t): Current stock price
* (\mu): Expected return (drift)
* (\sigma): Volatility
* (Z \sim N(0,1)): Random shock
* (\Delta t): Time step

---

## 🚀 Features

* Monte Carlo simulation of stock prices
* GBM-based stochastic modeling
* Risk metrics:

  * Expected future price
  * Value at Risk (VaR)
* Visualization of:

  * Simulated price paths
  * Final price distribution
* Modular and extensible codebase

---

## 📁 Project Structure

```
monte-carlo-stock-simulator/
│
├── data/
├── notebooks/
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── simulation.py
│   ├── metrics.py
│   └── visualization.py
│
├── tests/
├── config/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧪 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/monte-carlo-stock-simulator.git
cd monte-carlo-stock-simulator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the simulation:

```bash
python main.py
```

Example output:

```
Expected Price: 110.25
Value at Risk (5%): 85.10
```

---

## 📊 Example Results

* Simulated stock price trajectories over time
* Distribution of final stock prices
* Risk estimation using percentile-based VaR

---

## 📈 Data Source

This project can optionally use real historical stock data via
Yahoo Finance using the `yfinance` Python library.

---

## 🧠 Concepts Used

* Monte Carlo Simulation
* Geometric Brownian Motion
* Probability Distributions (Normal Distribution)
* Log Returns
* Volatility Estimation
* Risk Metrics (VaR)

---

## ⚠️ Limitations

* Assumes constant volatility
* Ignores market shocks and jumps
* Assumes log-normal distribution of returns
* Does not account for macroeconomic factors

---

## 🔧 Future Improvements

* Jump diffusion models (Merton model)
* Stochastic volatility (Heston model)
* Portfolio-level simulation
* Variance reduction techniques
* Streamlit dashboard for visualization
* CLI interface for dynamic inputs

---

## 🤝 Contributing

Contributions are welcome. Feel free to open issues or submit pull requests to improve the project.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgments

Inspired by quantitative finance methodologies used in derivative pricing and risk management.

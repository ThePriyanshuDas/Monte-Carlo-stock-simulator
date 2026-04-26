import numpy as np
import plotly.graph_objects as go


def plot_paths_interactive(paths, title="Monte Carlo Simulated Paths"):
    """
    Interactive plot of simulated price paths.
    """
    fig = go.Figure()

    # Add each simulation as a line
    for i in range(paths.shape[1]):
        fig.add_trace(
            go.Scatter(
                y=paths[:, i],
                mode="lines",
                line=dict(width=1),
                opacity=0.4,
                showlegend=False
            )
        )

    fig.update_layout(
        title=title,
        xaxis_title="Time Steps",
        yaxis_title="Price",
        template="plotly_dark"
    )

    return fig


def plot_distribution_interactive(final_prices, bins=50, title="Final Price Distribution"):
    """
    Interactive histogram of final prices.
    """
    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=final_prices,
            nbinsx=bins,
            opacity=0.75
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Price",
        yaxis_title="Frequency",
        template="plotly_dark"
    )

    return fig


def plot_distribution_with_var(final_prices, var_level=5, bins=50):
    """
    Histogram with VaR line.
    """
    var_value = np.percentile(final_prices, var_level)

    fig = go.Figure()

    # Histogram
    fig.add_trace(
        go.Histogram(
            x=final_prices,
            nbinsx=bins,
            opacity=0.75,
            name="Price Distribution"
        )
    )

    # VaR line
    fig.add_vline(
        x=var_value,
        line_dash="dash",
        line_width=2,
        annotation_text=f"{var_level}% VaR",
        annotation_position="top right"
    )

    fig.update_layout(
        title=f"Final Price Distribution with {var_level}% VaR",
        xaxis_title="Price",
        yaxis_title="Frequency",
        template="plotly_dark"
    )

    return fig, var_value
import numpy as np
import plotly.graph_objects as go


def create_blackhole(mass=5e11):
    """
    Create a simple black hole visualization.

    Parameters
    ----------
    mass : float
        Black hole mass in kg.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    # Scale radius for visualization only
    radius = np.clip(np.log10(mass) - 8, 8, 28)

    theta = np.linspace(0, 2*np.pi, 400)

    # Event Horizon
    x1 = radius * np.cos(theta)
    y1 = radius * np.sin(theta)

    # Photon Ring
    x2 = (radius * 1.25) * np.cos(theta)
    y2 = (radius * 1.25) * np.sin(theta)

    # Accretion Disk
    x3 = (radius * 2.1) * np.cos(theta)
    y3 = (radius * 0.8) * np.sin(theta)

    fig = go.Figure()

    # Accretion Disk
    fig.add_trace(
        go.Scatter(
            x=x3,
            y=y3,
            fill="toself",
            mode="lines",
            line=dict(color="orange", width=2),
            fillcolor="rgba(255,140,0,0.35)",
            hoverinfo="skip",
            showlegend=False
        )
    )

    # Photon Ring
    fig.add_trace(
        go.Scatter(
            x=x2,
            y=y2,
            mode="lines",
            line=dict(color="gold", width=3),
            hoverinfo="skip",
            showlegend=False
        )
    )

    # Event Horizon
    fig.add_trace(
        go.Scatter(
            x=x1,
            y=y1,
            fill="toself",
            mode="lines",
            line=dict(color="black"),
            fillcolor="black",
            hoverinfo="skip",
            showlegend=False
        )
    )

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        xaxis=dict(
            visible=False,
            range=[-60, 60]
        ),
        yaxis=dict(
            visible=False,
            range=[-60, 60],
            scaleanchor="x"
        ),
        height=600,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig

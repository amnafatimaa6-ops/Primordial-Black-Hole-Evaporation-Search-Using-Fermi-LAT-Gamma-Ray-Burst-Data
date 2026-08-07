import numpy as np
import plotly.graph_objects as go


def create_hawking_particles(
    mass=5e11,
    n_particles=400,
    seed=42
):
    """
    Simulate Hawking radiation escaping from
    a primordial black hole.

    Parameters
    ----------
    mass : float
        Black hole mass (kg)

    n_particles : int
        Number of particles

    Returns
    -------
    Plotly Figure
    """

    np.random.seed(seed)

    # ---------------------------------------
    # Visual scaling only
    # ---------------------------------------

    radius = np.clip(
        np.log10(mass) - 8,
        8,
        25
    )

    # Smaller BH -> hotter -> more energetic particles
    temperature_scale = np.clip(
        5e11 / mass,
        0.3,
        6
    )

    theta = np.random.uniform(
        0,
        2*np.pi,
        n_particles
    )

    distance = np.random.uniform(
        radius,
        radius + 25*temperature_scale,
        n_particles
    )

    x = distance * np.cos(theta)
    y = distance * np.sin(theta)

    speed = np.random.uniform(
        3,
        10,
        n_particles
    ) * temperature_scale

    size = np.random.uniform(
        2,
        6,
        n_particles
    ) * temperature_scale

    fig = go.Figure()

    # ---------------------------------------
    # Hawking particles
    # ---------------------------------------

    fig.add_trace(

        go.Scatter(

            x=x,

            y=y,

            mode="markers",

            marker=dict(

                size=size,

                color=speed,

                colorscale="Turbo",

                opacity=0.85,

                showscale=True,

                colorbar=dict(
                    title="Relative Energy"
                )

            ),

            hoverinfo="skip",

            showlegend=False

        )

    )

    # ---------------------------------------
    # Event Horizon
    # ---------------------------------------

    circle = np.linspace(
        0,
        2*np.pi,
        300
    )

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(circle),

            y=radius*np.sin(circle),

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

            range=[-70,70]

        ),

        yaxis=dict(

            visible=False,

            range=[-70,70],

            scaleanchor="x"

        ),

        margin=dict(

            l=0,

            r=0,

            t=0,

            b=0

        ),

        height=650

    )

    return fig

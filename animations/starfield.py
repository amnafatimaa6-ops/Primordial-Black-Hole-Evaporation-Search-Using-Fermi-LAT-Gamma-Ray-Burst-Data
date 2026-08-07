import numpy as np
import plotly.graph_objects as go


def create_starfield(
    n_stars=800,
    width=100,
    height=100,
    seed=42
):
    """
    Creates a simulated starfield using Plotly.

    Parameters
    ----------
    n_stars : int
        Number of stars.

    width : int
        Width of the virtual sky.

    height : int
        Height of the virtual sky.

    seed : int
        Random seed for reproducibility.

    Returns
    -------
    Plotly Figure
    """

    np.random.seed(seed)

    # ----------------------------------------
    # Random star positions
    # ----------------------------------------

    x = np.random.uniform(0, width, n_stars)

    y = np.random.uniform(0, height, n_stars)

    # ----------------------------------------
    # Random brightness
    # ----------------------------------------

    brightness = np.random.uniform(
        0.4,
        1.0,
        n_stars
    )

    # ----------------------------------------
    # Random sizes
    # ----------------------------------------

    size = np.random.uniform(
        1,
        5,
        n_stars
    )

    # ----------------------------------------
    # Create figure
    # ----------------------------------------

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=x,

            y=y,

            mode="markers",

            marker=dict(

                size=size,

                color=brightness,

                colorscale="Ice",

                opacity=0.95,

                showscale=False

            ),

            hoverinfo="skip"

        )

    )

    # ----------------------------------------

    fig.update_layout(

        paper_bgcolor="black",

        plot_bgcolor="black",

        margin=dict(

            l=0,
            r=0,
            t=0,
            b=0

        ),

        xaxis=dict(

            visible=False,

            range=[0, width]

        ),

        yaxis=dict(

            visible=False,

            range=[0, height],

            scaleanchor="x"

        ),

        height=500

    )

    return fig

import numpy as np
import plotly.graph_objects as go


def create_spacetime_grid(mass=5e11):
    """
    Creates a 3D spacetime curvature visualization.

    Parameters
    ----------
    mass : float
        Black hole mass in kilograms.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    # --------------------------------------------------
    # Scale the depth based on mass (visual only)
    # --------------------------------------------------

    depth = np.clip(np.log10(mass) - 9, 1, 5)

    # --------------------------------------------------
    # Grid
    # --------------------------------------------------

    x = np.linspace(-20, 20, 120)
    y = np.linspace(-20, 20, 120)

    X, Y = np.meshgrid(x, y)

    R = np.sqrt(X**2 + Y**2)

    # Avoid divide-by-zero
    R[R < 1] = 1

    # --------------------------------------------------
    # Gravity well (visual approximation)
    # --------------------------------------------------

    Z = -depth * 30 / R

    # Smooth center
    Z[R < 2] = Z[R < 2] - 3

    # --------------------------------------------------
    # Plot
    # --------------------------------------------------

    fig = go.Figure()

    fig.add_trace(

        go.Surface(

            x=X,

            y=Y,

            z=Z,

            colorscale="Viridis",

            showscale=False,

            hoverinfo="skip"

        )

    )

    fig.update_layout(

        paper_bgcolor="black",

        scene=dict(

            bgcolor="black",

            xaxis=dict(
                visible=False
            ),

            yaxis=dict(
                visible=False
            ),

            zaxis=dict(
                visible=False
            ),

            camera=dict(

                eye=dict(

                    x=1.5,

                    y=1.5,

                    z=0.8

                )

            )

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

import numpy as np
import plotly.graph_objects as go

from utils.hawking import hawking_temperature


def create_photon_spectrum(mass=5e11):
    """
    Creates a simplified Hawking photon spectrum.

    Parameters
    ----------
    mass : float
        Black hole mass in kilograms.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    # ---------------------------------------
    # Hawking temperature (MeV)
    # ---------------------------------------

    temperature = hawking_temperature(mass).value

    # ---------------------------------------
    # Energy axis (MeV)
    # ---------------------------------------

    energy = np.linspace(
        0.1,
        150,
        600
    )

    # ---------------------------------------
    # Simplified Planck spectrum
    # ---------------------------------------

    spectrum = (
        energy**2 /
        (
            np.exp(energy / temperature) - 1
        )
    )

    # Normalize for display
    spectrum /= spectrum.max()

    # ---------------------------------------
    # Figure
    # ---------------------------------------

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=energy,

            y=spectrum,

            mode="lines",

            line=dict(
                color="cyan",
                width=4
            ),

            name="Photon Spectrum"

        )

    )

    # Peak temperature marker

    fig.add_vline(

        x=temperature,

        line_dash="dash",

        line_color="red",

        annotation_text=f"T = {temperature:.1f} MeV"

    )

    fig.update_layout(

        title="Simplified Hawking Photon Spectrum",

        xaxis_title="Photon Energy (MeV)",

        yaxis_title="Relative Intensity",

        paper_bgcolor="black",

        plot_bgcolor="black",

        font=dict(color="white"),

        height=550,

        showlegend=False

    )

    return fig

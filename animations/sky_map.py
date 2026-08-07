import plotly.express as px
import pandas as pd


def create_sky_map(df):
    """
    Interactive sky map of Fermi-LAT Gamma-Ray Bursts.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    plotly.graph_objects.Figure
    """

    data = df.copy()

    # -------------------------------
    # Check required columns
    # -------------------------------

    required = [
        "name",
        "ra",
        "dec"
    ]

    for col in required:

        if col not in data.columns:
            raise ValueError(f"Missing column: {col}")

    # -------------------------------
    # Marker size
    # -------------------------------

    if "like_lat_ts" in data.columns:

        size = data["like_lat_ts"].fillna(5)

    else:

        size = 8

    # -------------------------------
    # Marker colour
    # -------------------------------

    if "PBH_consistency" in data.columns:

        color = "PBH_consistency"

    else:

        color = None

    # -------------------------------
    # Plot
    # -------------------------------

    fig = px.scatter(

        data,

        x="ra",

        y="dec",

        color=color,

        size=size,

        hover_name="name",

        hover_data={

            "ra": True,
            "dec": True,

            "gbm_cat_t90": True,

            "ext_emission_max_ene": True,

            "like_lat_ts": True,

            "redshift": True

        },

        color_continuous_scale="Turbo"

    )

    fig.update_layout(

        title="Fermi-LAT Gamma-Ray Burst Sky Map",

        paper_bgcolor="black",

        plot_bgcolor="black",

        font=dict(color="white"),

        xaxis_title="Right Ascension (°)",

        yaxis_title="Declination (°)",

        height=700

    )

    fig.update_xaxes(

        range=[360,0]

    )

    return fig

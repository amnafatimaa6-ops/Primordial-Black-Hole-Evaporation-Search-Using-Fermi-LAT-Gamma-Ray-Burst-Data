import streamlit as st
import numpy as np
import plotly.graph_objects as go

import astropy.constants as const
import astropy.units as u

# ------------------------------------------------------
# Page Configuration
# ------------------------------------------------------

st.set_page_config(
    page_title="Hawking Radiation",
    page_icon="🕳️",
    layout="wide"
)

st.title("🕳️ Hawking Radiation Simulator")

st.markdown("""
Explore how the properties of a black hole change as its mass decreases.
According to Stephen Hawking's theory, smaller black holes become hotter,
emit more energetic radiation, and evaporate more rapidly.
""")

st.divider()

# ------------------------------------------------------
# User Input
# ------------------------------------------------------

st.sidebar.header("Simulation Controls")

mass = st.sidebar.slider(
    "Primordial Black Hole Mass (kg)",
    min_value=1e10,
    max_value=1e13,
    value=5e11,
    step=1e10,
    format="%.2e"
)

M = mass * u.kg

# ------------------------------------------------------
# Physics Calculations
# ------------------------------------------------------

temperature = (
    const.hbar
    * const.c**3
    / (8 * np.pi * const.G * M * const.k_B)
)

temperature = temperature.to(
    u.MeV,
    equivalencies=u.temperature_energy()
)

radius = (
    2 * const.G * M
    / const.c**2
).to(u.m)

lifetime = (
    5120 * np.pi
    * const.G**2
    * M**3
    / (const.hbar * const.c**4)
).to(u.year)

# ------------------------------------------------------
# Display Metrics
# ------------------------------------------------------

st.header("Computed Properties")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Mass",
    f"{mass:.2e} kg"
)

c2.metric(
    "Hawking Temperature",
    f"{temperature.value:.2f} MeV"
)

c3.metric(
    "Schwarzschild Radius",
    f"{radius.value:.3e} m"
)

st.metric(
    "Estimated Lifetime",
    f"{lifetime.value:.3e} years"
)

st.divider()

# ------------------------------------------------------
# Temperature vs Mass
# ------------------------------------------------------

st.header("Temperature vs Mass")

masses = np.logspace(10, 13, 200)

temps = []

for m in masses:

    T = (
        const.hbar
        * const.c**3
        / (
            8
            * np.pi
            * const.G
            * (m * u.kg)
            * const.k_B
        )
    )

    temps.append(
        T.to(
            u.MeV,
            equivalencies=u.temperature_energy()
        ).value
    )

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=masses,

        y=temps,

        mode="lines",

        name="Temperature"

    )

)

fig.add_vline(

    x=mass,

    line_dash="dash",

    annotation_text="Selected Mass"

)

fig.update_layout(

    title="Hawking Temperature vs Black Hole Mass",

    xaxis_type="log",

    yaxis_type="log",

    xaxis_title="Mass (kg)",

    yaxis_title="Temperature (MeV)",

    height=550

)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ------------------------------------------------------
# Visual Representation
# ------------------------------------------------------

st.header("Illustration")

fraction = np.clip(
    (np.log10(mass) - 10) / 3,
    0,
    1
)

size = 20 + fraction * 120

fig2 = go.Figure()

fig2.add_trace(

    go.Scatter(

        x=[0],

        y=[0],

        mode="markers",

        marker=dict(

            size=size,

            opacity=0.9

        ),

        hoverinfo="skip"

    )

)

fig2.update_xaxes(visible=False)

fig2.update_yaxes(visible=False)

fig2.update_layout(

    title="Relative Black Hole Size",

    height=450,

    showlegend=False

)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ------------------------------------------------------
# Scientific Explanation
# ------------------------------------------------------

st.header("Scientific Interpretation")

if mass > 8e12:

    st.info("""
Large black holes are extremely cold and emit very little Hawking radiation.
Their evaporation times greatly exceed the current age of the Universe.
""")

elif mass > 1e12:

    st.warning("""
As the black hole loses mass, its temperature increases significantly.
The emitted photons become more energetic, and evaporation accelerates.
""")

else:

    st.error("""
Very low-mass primordial black holes become extremely hot.
Near the end of their lives, they may emit intense bursts of gamma rays,
making them potential targets for telescopes such as Fermi-LAT.
""")

st.divider()

# ------------------------------------------------------
# Project Connection
# ------------------------------------------------------

st.header("Connection to This Research")

st.markdown("""
For this project, a primordial black hole with a mass of approximately

**5 × 10¹¹ kg**

is used because theoretical models predict that such a black hole would
be completing its evaporation around the present age of the Universe.

The calculated Hawking temperature is approximately **21 MeV**, providing
the theoretical energy scale used to compare with observed gamma-ray bursts
from the Fermi-LAT catalogue.
""")

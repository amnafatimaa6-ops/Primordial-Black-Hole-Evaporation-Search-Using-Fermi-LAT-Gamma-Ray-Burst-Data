import streamlit as st
import plotly.express as px
import pandas as pd

from utils.download_data import load_fermi_data
from utils.scoring import calculate_pbh_candidates

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="PBH Candidates",
    page_icon="🕳️",
    layout="wide"
)

st.title("🕳️ PBH Candidate Explorer")

st.markdown("""
This page ranks short Gamma-Ray Bursts according to their similarity
to the expected observational signatures of primordial black hole (PBH)
evaporation.

The ranking is based on the custom **PBH Consistency Index**
developed in this project.
""")

st.divider()

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

df = load_fermi_data()

# Calculate PBH ranking
candidates = calculate_pbh_candidates(df)

# -------------------------------------------------------
# Top Metrics
# -------------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total GRBs",
    len(df)
)

c2.metric(
    "Short GRBs",
    len(candidates)
)

c3.metric(
    "Top Candidate",
    candidates.iloc[0]["name"]
)

st.divider()

# -------------------------------------------------------
# Ranking Table
# -------------------------------------------------------

st.header("🏆 Top PBH Candidates")

st.dataframe(

    candidates[
        [
            "name",
            "PBH_consistency",
            "gbm_cat_t90",
            "like_lat_ts",
            "ext_emission_max_ene",
            "like_best_grbindex",
            "redshift"
        ]
    ],

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Score Distribution
# -------------------------------------------------------

st.header("📈 PBH Consistency Distribution")

fig = px.histogram(

    candidates,

    x="PBH_consistency",

    nbins=20,

    title="Distribution of PBH Consistency Scores"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Candidate Explorer
# -------------------------------------------------------

st.header("🔭 Candidate Explorer")

selected = st.selectbox(

    "Select a Candidate",

    candidates["name"]

)

candidate = candidates[
    candidates["name"] == selected
].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "PBH Score",
        f"{candidate['PBH_consistency']:.3f}"
    )

    st.metric(
        "Duration (T90)",
        f"{candidate['gbm_cat_t90']:.3f} s"
    )

    st.metric(
        "LAT TS",
        f"{candidate['like_lat_ts']:.1f}"
    )

with col2:

    st.metric(
        "Maximum Photon Energy",
        f"{candidate['ext_emission_max_ene']:.1f} MeV"
    )

    st.metric(
        "Spectral Index",
        f"{candidate['like_best_grbindex']:.2f}"
    )

    st.metric(
        "Redshift",
        str(candidate["redshift"])
    )

st.divider()

# -------------------------------------------------------
# Duration vs Energy
# -------------------------------------------------------

st.header("⚡ Duration vs Maximum Photon Energy")

fig = px.scatter(

    candidates,

    x="gbm_cat_t90",

    y="ext_emission_max_ene",

    color="PBH_consistency",

    hover_name="name",

    size="PBH_consistency",

    title="PBH Candidate Comparison"

)

fig.add_vline(

    x=2,

    line_dash="dash",

    annotation_text="Short GRB Boundary"

)

fig.add_hline(

    y=21,

    line_dash="dash",

    annotation_text="Predicted Hawking Energy"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Top 10 Bar Chart
# -------------------------------------------------------

st.header("🥇 Highest-Ranked Candidates")

top10 = candidates.head(10)

fig = px.bar(

    top10,

    x="name",

    y="PBH_consistency",

    color="PBH_consistency",

    text="PBH_consistency"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Scientific Interpretation
# -------------------------------------------------------

st.header("📖 Scientific Interpretation")

st.markdown("""
The PBH Consistency Index combines four observational properties:

- Very short burst duration
- High LAT detection significance
- High maximum photon energy
- Hard photon spectrum

These quantities are normalized and combined using a weighted scoring
system to identify bursts that most closely resemble theoretical
predictions for terminal primordial black hole evaporation.

A high score **does not prove** a primordial black hole origin.
Instead, it identifies promising candidates for future
spectral, temporal, and multi-wavelength follow-up studies.

Several of the highest-ranked bursts exhibit properties broadly
consistent with Hawking radiation expectations, but none constitutes
definitive evidence for PBH evaporation.
""")

st.success(
    "The PBH Consistency Index is intended as a ranking tool, not a proof of PBH detection."
)

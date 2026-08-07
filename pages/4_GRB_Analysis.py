import streamlit as st
import pandas as pd
import plotly.express as px

from utils.download_data import load_fermi_data

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="GRB Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Gamma-Ray Burst Analysis")

st.markdown("""
This section explores the statistical properties of Gamma-Ray Bursts (GRBs)
observed by NASA's Fermi Large Area Telescope (Fermi-LAT) and compares them
with theoretical expectations for primordial black hole evaporation.
""")

st.divider()

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

df = load_fermi_data()

# Remove unnecessary columns

df = df.drop(
    columns=[
        "__row",
        "__x_ra_dec",
        "__y_ra_dec",
        "__z_ra_dec"
    ],
    errors="ignore"
)

# -------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------

st.sidebar.header("Analysis Filters")

duration_limit = st.sidebar.slider(

    "Maximum Duration (T90)",

    min_value=1,

    max_value=500,

    value=500

)

filtered = df[
    df["gbm_cat_t90"] <= duration_limit
].copy()

# -------------------------------------------------------
# Summary Statistics
# -------------------------------------------------------

st.header("📈 Summary Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(

    "GRBs",

    len(filtered)

)

col2.metric(

    "Median Duration",

    f"{filtered['gbm_cat_t90'].median():.2f} s"

)

col3.metric(

    "Mean Duration",

    f"{filtered['gbm_cat_t90'].mean():.2f} s"

)

st.divider()

# -------------------------------------------------------
# Duration Distribution
# -------------------------------------------------------

st.header("⏱ Duration Distribution")

fig = px.histogram(

    filtered,

    x="gbm_cat_t90",

    nbins=40,

    title="Gamma-Ray Burst Duration"

)

fig.add_vline(

    x=2,

    line_dash="dash",

    annotation_text="Short GRB"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

short_count = (filtered["gbm_cat_t90"] < 2).sum()

st.success(f"Short GRBs (T90 < 2 s): {short_count}")

st.divider()

# -------------------------------------------------------
# Photon Energy
# -------------------------------------------------------

st.header("⚡ Maximum Photon Energy")

energy = filtered[
    filtered["ext_emission_max_ene"] > 0
]

fig = px.histogram(

    energy,

    x="ext_emission_max_ene",

    nbins=40,

    title="Maximum Photon Energy"

)

fig.add_vline(

    x=21,

    line_dash="dash",

    annotation_text="PBH Prediction (21 MeV)"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.info(
"""
The dashed line represents the characteristic Hawking radiation
energy for a primordial black hole with a mass of
approximately 5 × 10¹¹ kg.
"""
)

st.divider()

# -------------------------------------------------------
# Spectral Index
# -------------------------------------------------------

st.header("📉 Spectral Index")

spec = filtered.dropna(
    subset=["like_best_grbindex"]
)

fig = px.histogram(

    spec,

    x="like_best_grbindex",

    nbins=35,

    title="Photon Spectral Index"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Detection Significance
# -------------------------------------------------------

st.header("📡 LAT Detection Significance")

ts = filtered.dropna(
    subset=["like_lat_ts"]
)

fig = px.histogram(

    ts,

    x="like_lat_ts",

    nbins=40,

    title="LAT Test Statistic"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Correlation Matrix
# -------------------------------------------------------

st.header("🔥 Correlation Matrix")

cols = [

    "gbm_cat_t90",

    "like_lat_ts",

    "ext_emission_max_ene",

    "like_best_flux",

    "like_best_grbindex"

]

corr = filtered[cols].corr(numeric_only=True)

fig = px.imshow(

    corr,

    text_auto=".2f",

    color_continuous_scale="RdBu_r",

    aspect="auto"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Scatter Explorer
# -------------------------------------------------------

st.header("🔭 Relationship Explorer")

numeric = filtered.select_dtypes(
    include="number"
).columns

x = st.selectbox(

    "X Axis",

    numeric,

    index=0

)

y = st.selectbox(

    "Y Axis",

    numeric,

    index=1

)

fig = px.scatter(

    filtered,

    x=x,

    y=y,

    hover_name="name",

    title=f"{x} vs {y}"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Redshift
# -------------------------------------------------------

st.header("🌍 Redshift Availability")

has_redshift = filtered["redshift"].notnull().value_counts()

pie = px.pie(

    values=has_redshift.values,

    names=["Missing", "Available"],

    title="Redshift Measurements"

)

st.plotly_chart(

    pie,

    use_container_width=True

)

st.divider()

# -------------------------------------------------------
# Interpretation
# -------------------------------------------------------

st.header("📝 Interpretation")

st.markdown("""
### Key Findings

- Most Gamma-Ray Bursts have durations greater than **2 seconds**.
- Only a small subset qualifies as short-duration GRBs.
- Most photon spectral indices cluster around **−2**.
- Detection significance generally increases with photon energy.
- Only a minority of bursts have measured redshifts.
- No single observable uniquely identifies a primordial black hole.

These findings motivate the development of a **PBH Consistency Index**,
which combines multiple observational properties to identify the most
promising candidate events.
""")

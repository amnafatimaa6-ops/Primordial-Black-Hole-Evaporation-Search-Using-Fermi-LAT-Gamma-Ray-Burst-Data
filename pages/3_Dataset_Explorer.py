import streamlit as st
import pandas as pd
import plotly.express as px
from animations.sky_map import create_sky_map

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Fermi-LAT Gamma-Ray Burst Dataset Explorer")

st.markdown("""
Explore the real Gamma-Ray Burst (GRB) observations from NASA's
Fermi Large Area Telescope (Fermi-LAT).
""")

st.divider()

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/fermi_grb.csv")

df = load_data()

# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

st.header("📊 Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total GRBs", len(df))
c2.metric("Features", len(df.columns))
c3.metric("Missing Values", int(df.isna().sum().sum()))
c4.metric("Complete Rows", int(df.dropna().shape[0]))

st.divider()

# -------------------------------------------------------
# Raw Dataset
# -------------------------------------------------------

st.header("📄 Browse Dataset")

st.dataframe(
    df,
    use_container_width=True,
    height=450
)

st.divider()

# -------------------------------------------------------
# Search GRB
# -------------------------------------------------------

st.header("🔍 Search a Gamma-Ray Burst")

if "name" in df.columns:

    grb = st.selectbox(
        "Choose a GRB",
        sorted(df["name"].dropna().unique())
    )

    st.write(
        df[df["name"] == grb]
    )

st.divider()

# -------------------------------------------------------
# Missing Values
# -------------------------------------------------------

st.header("🧹 Missing Values")

missing = (
    df.isnull()
      .sum()
      .sort_values(ascending=False)
)

missing = missing[missing > 0]

if len(missing) > 0:

    fig = px.bar(
        missing,
        x=missing.index,
        y=missing.values,
        labels={
            "x":"Column",
            "y":"Missing Values"
        },
        title="Missing Values per Feature"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.success("No missing values detected.")

st.divider()

# -------------------------------------------------------
# Data Types
# -------------------------------------------------------

st.header("📂 Dataset Information")

info = pd.DataFrame({

    "Column": df.columns,

    "Data Type": df.dtypes.astype(str),

    "Missing": df.isnull().sum(),

    "Unique Values": df.nunique()

})

st.dataframe(
    info,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Feature Distribution
# -------------------------------------------------------

st.header("📈 Explore a Feature")

numeric_cols = df.select_dtypes(
    include="number"
).columns

feature = st.selectbox(
    "Select Numeric Feature",
    numeric_cols
)

fig2 = px.histogram(
    df,
    x=feature,
    nbins=40,
    title=f"{feature} Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Correlation Explorer
# -------------------------------------------------------

st.header("📉 Scatter Plot Explorer")

x = st.selectbox(
    "X-axis",
    numeric_cols,
    index=0
)

y = st.selectbox(
    "Y-axis",
    numeric_cols,
    index=1
)

fig3 = px.scatter(
    df,
    x=x,
    y=y,
    hover_name="name" if "name" in df.columns else None,
    title=f"{x} vs {y}"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Download Dataset
# -------------------------------------------------------

st.header("⬇ Download Dataset")

csv = df.to_csv(index=False).encode()

st.download_button(

    label="Download CSV",

    data=csv,

    file_name="fermi_grb.csv",

    mime="text/csv"

)

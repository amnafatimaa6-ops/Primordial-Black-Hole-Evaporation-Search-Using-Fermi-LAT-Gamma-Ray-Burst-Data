import streamlit as st
from PIL import Image

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="PBH-FermiLAT Dashboard",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Logo
# -------------------------------------------------------

try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120)
except:
    pass

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🌌 Primordial Black Hole Evaporation Dashboard")

st.subheader(
    "Comparing Hawking Radiation Predictions with NASA Fermi-LAT Gamma-Ray Burst Observations"
)

st.divider()

# -------------------------------------------------------
# Hero Image
# -------------------------------------------------------

try:
    image = Image.open("assets/universe.jpg")
    st.image(image, use_container_width=True)
except:
    st.warning("Add universe.jpg inside the assets folder.")

# -------------------------------------------------------
# Overview
# -------------------------------------------------------

st.header("📖 Project Overview")

st.markdown("""
This interactive dashboard investigates whether Gamma-Ray Bursts (GRBs)
observed by NASA's **Fermi Large Area Telescope (Fermi-LAT)**
could be consistent with the terminal evaporation of
**Primordial Black Holes (PBHs)** predicted by Hawking Radiation.

The project combines:

- 🌌 Astrophysics
- 🛰 NASA observational data
- 📊 Data Science
- 🤖 Machine Learning
- 📈 Interactive Visualization

to explore one of the most fascinating questions in modern cosmology.
""")

st.divider()

# -------------------------------------------------------
# Dashboard Sections
# -------------------------------------------------------

st.header("📂 Dashboard Sections")

st.markdown("""
### 🌌 Introduction
Learn the scientific motivation behind the project.

### 🕳 Hawking Radiation
Interactively explore how black holes evaporate.

### 📡 Dataset Explorer
Browse the live NASA Fermi-LAT catalogue.

### 📊 GRB Analysis
Explore statistical properties of Gamma-Ray Bursts.

### ⭐ PBH Candidates
Rank the most promising candidate events.

### 🎯 Conclusions
Review the main findings and future work.
""")

st.divider()

# -------------------------------------------------------
# Features
# -------------------------------------------------------

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("Physics")

    st.markdown("""
- Hawking Temperature Calculator
- Schwarzschild Radius
- PBH Lifetime
- Theoretical Predictions
""")

with col2:

    st.success("Data Analysis")

    st.markdown("""
- Live NASA Data
- Interactive Charts
- PBH Candidate Ranking
- Correlation Analysis
""")

st.divider()

st.info("👈 Use the sidebar to navigate through the dashboard.")

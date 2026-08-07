import streamlit as st
from PIL import Image

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Introduction",
    page_icon="🌌",
    layout="wide"
)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("🌌 Primordial Black Hole Evaporation")
st.subheader("Searching for Hawking Radiation Signatures Using NASA Fermi-LAT Data")

st.divider()

# -------------------------------------------------------
# Hero Image
# -------------------------------------------------------

try:
    image = Image.open("assets/universe.jpg")
    st.image(image, use_container_width=True)
except:
    st.info("Add 'universe.jpg' inside the assets folder.")

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("📖 Project Overview")

st.markdown("""
Primordial Black Holes (PBHs) are hypothetical black holes that may have formed
during the first fraction of a second after the Big Bang.

Unlike stellar black holes, PBHs could possess extremely small masses.
According to Stephen Hawking's theory, black holes slowly lose mass by emitting
thermal radiation, known as **Hawking Radiation**.

As a PBH approaches the end of its lifetime, it becomes extremely hot and may
produce a brief burst of high-energy gamma rays.

This project investigates whether any Gamma-Ray Bursts (GRBs) observed by
NASA's **Fermi Large Area Telescope (Fermi-LAT)** exhibit characteristics
consistent with the theoretical predictions of PBH evaporation.
""")

st.divider()

# -------------------------------------------------------
# Research Question
# -------------------------------------------------------

st.header("🎯 Research Question")

st.info("""
Can primordial black holes evaporating today produce gamma-ray bursts
detectable by the Fermi Large Area Telescope, and do any observed gamma-ray
bursts resemble the predicted signatures of Hawking radiation?
""")

st.divider()

# -------------------------------------------------------
# Objectives
# -------------------------------------------------------

st.header("🚀 Project Objectives")

col1, col2 = st.columns(2)

with col1:

    st.success("Physics")

    st.markdown("""
- Compute Hawking temperature
- Study PBH evaporation
- Compare theory with observations
- Estimate characteristic photon energies
    """)

with col2:

    st.success("Data Science")

    st.markdown("""
- Load NASA Fermi-LAT catalogue
- Explore GRB properties
- Build PBH Consistency Index
- Identify potential PBH candidates
    """)

st.divider()

# -------------------------------------------------------
# Workflow
# -------------------------------------------------------

st.header("🛰 Research Workflow")

st.markdown("""
1. Download the Fermi-LAT Gamma-Ray Burst catalogue.

2. Clean and preprocess the observational data.

3. Compute theoretical Hawking radiation properties.

4. Compare observations with theoretical predictions.

5. Rank Gamma-Ray Bursts using a custom PBH Consistency Index.

6. Investigate the highest-ranking candidate events.
""")

st.divider()

# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

st.header("📡 Dataset")

c1, c2, c3 = st.columns(3)

c1.metric("Total GRBs", "231")
c2.metric("Features", "111")
c3.metric("Instrument", "Fermi-LAT")

st.divider()

# -------------------------------------------------------
# Scientific Background
# -------------------------------------------------------

st.header("🌠 Scientific Background")

st.markdown("""
### Hawking Radiation

Stephen Hawking proposed that black holes are not completely black.
Instead, quantum effects near the event horizon allow black holes to emit
particles and gradually lose mass.

As the black hole becomes smaller:

- Temperature increases
- Radiation becomes more energetic
- Mass decreases
- Evaporation accelerates

Eventually, the black hole reaches a final explosive phase that may produce
high-energy gamma rays.
""")

st.divider()

# -------------------------------------------------------
# Expected PBH Signature
# -------------------------------------------------------

st.header("⭐ Expected PBH Observational Signature")

st.markdown("""
A primordial black hole nearing the end of its lifetime is expected to produce:

- ⏱ Very short gamma-ray burst
- ⚡ High-energy gamma rays
- 📈 Significant gamma-ray detection
- 🌌 Hard photon spectrum
- 🌍 Little or no measured redshift
""")

st.divider()

# -------------------------------------------------------
# Navigation
# -------------------------------------------------------

st.success("➡ Continue to **Hawking Radiation** from the left sidebar.")

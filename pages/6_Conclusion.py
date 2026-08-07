import streamlit as st

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Conclusion",
    page_icon="🎯",
    layout="wide"
)

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🎯 Research Conclusions")

st.markdown("""
This project investigated whether gamma-ray bursts observed by NASA's
**Fermi Large Area Telescope (Fermi-LAT)** could contain signatures
consistent with the terminal evaporation of primordial black holes (PBHs)
predicted by Hawking radiation.
""")

st.divider()

# -------------------------------------------------------
# Research Question
# -------------------------------------------------------

st.header("❓ Research Question")

st.info("""
Can primordial black holes evaporating today produce gamma-ray bursts
detectable by Fermi-LAT, and do any observed bursts resemble the
predicted signatures of Hawking radiation?
""")

st.divider()

# -------------------------------------------------------
# Methodology
# -------------------------------------------------------

st.header("🧪 Methodology")

st.markdown("""
The study combined **theoretical astrophysics** with **observational data analysis**.

The workflow consisted of:

1. Downloading the latest Fermi-LAT Gamma-Ray Burst catalogue.
2. Cleaning and preprocessing the observational data.
3. Computing Hawking radiation properties for an evaporating PBH.
4. Exploring the statistical properties of observed GRBs.
5. Selecting short-duration bursts.
6. Developing a custom **PBH Consistency Index**.
7. Ranking bursts according to their similarity to theoretical predictions.
""")

st.divider()

# -------------------------------------------------------
# Main Results
# -------------------------------------------------------

st.header("📊 Key Findings")

c1, c2, c3 = st.columns(3)

c1.metric("GRBs Analysed", "231")
c2.metric("Short GRBs", "21")
c3.metric("Predicted Hawking Temperature", "≈21 MeV")

st.markdown("""

### Main observations

- Most observed GRBs have durations much longer than expected for PBH evaporation.

- Only a small subset of short-duration bursts satisfies the first observational criterion for PBH candidates.

- The majority of observed photon spectral indices cluster around **−2**, consistent with conventional GRBs.

- Maximum detected photon energies often extend into the GeV range, exceeding the characteristic Hawking temperature but remaining compatible with the high-energy tail of Hawking emission.

- No single observational property uniquely identifies a primordial black hole.
""")

st.divider()

# -------------------------------------------------------
# PBH Consistency Index
# -------------------------------------------------------

st.header("⭐ PBH Consistency Index")

st.markdown("""
A custom **PBH Consistency Index** was developed to compare observed
Gamma-Ray Bursts with theoretical expectations.

The score combines:

- Burst duration
- Maximum photon energy
- LAT detection significance
- Photon spectral index

Each feature is normalized before applying physics-motivated weights,
allowing bursts to be ranked according to their similarity to expected
PBH evaporation signatures.
""")

st.success("""
The PBH Consistency Index is designed as a prioritization tool for
future investigation rather than a method for confirming PBH detections.
""")

st.divider()

# -------------------------------------------------------
# Scientific Interpretation
# -------------------------------------------------------

st.header("🔬 Scientific Interpretation")

st.markdown("""
Several short-duration Gamma-Ray Bursts exhibit observational properties
that are broadly consistent with theoretical expectations for primordial
black hole evaporation.

However, these characteristics can also be explained by well-established
astrophysical phenomena such as:

- Compact binary mergers
- Magnetar giant flares
- Other high-energy transient events

Consequently, the present analysis does **not** provide definitive
evidence for primordial black holes.

Instead, it identifies a small number of promising candidates that merit
future observational and theoretical investigation.
""")

st.divider()

# -------------------------------------------------------
# Limitations
# -------------------------------------------------------

st.header("⚠ Limitations")

st.markdown("""
This project has several limitations:

- The catalogue records observed photon properties rather than complete spectra.

- Many bursts lack measured redshifts.

- Hawking radiation predicts a continuous emission spectrum rather than a single photon energy.

- The PBH Consistency Index is heuristic and does not represent a statistical probability.

- Candidate events require detailed spectral and temporal analysis before any physical conclusions can be drawn.
""")

st.divider()

# -------------------------------------------------------
# Future Work
# -------------------------------------------------------

st.header("🚀 Future Work")

st.markdown("""
Potential extensions include:

- Machine learning classification of PBH candidates.

- Bayesian likelihood analysis.

- Time-resolved spectral fitting.

- Cross-matching with Swift and Fermi-GBM catalogues.

- Simulating complete Hawking radiation spectra.

- Incorporating future observations from next-generation gamma-ray observatories.
""")

st.divider()

# -------------------------------------------------------
# Technologies
# -------------------------------------------------------

st.header("💻 Technologies Used")

st.markdown("""
- Python
- Streamlit
- Astroquery
- Astropy
- Pandas
- NumPy
- Plotly
- Scikit-learn
- NASA HEASARC Database
- Fermi Large Area Telescope (Fermi-LAT)
""")

st.divider()

# -------------------------------------------------------
# Final Statement
# -------------------------------------------------------

st.header("🌌 Final Conclusion")

st.markdown("""
This project demonstrates how **theoretical astrophysics**, **observational astronomy**, and **data science** can be combined to investigate one of the most intriguing questions in modern cosmology.

Although no definitive evidence for primordial black hole evaporation was found, the developed framework provides a reproducible approach for identifying and ranking candidate events using publicly available NASA observations.

The methodology can be extended as new gamma-ray observations become available, offering a foundation for future studies of Hawking radiation and primordial black holes.
""")

st.divider()

# -------------------------------------------------------
# Acknowledgements
# -------------------------------------------------------

st.header("🙏 Acknowledgements")

st.markdown("""
This project makes use of publicly available observational data from:

- NASA HEASARC
- Fermi Gamma-ray Space Telescope
- Fermi Large Area Telescope (LAT)

Theoretical calculations are based on Hawking's theory of black hole evaporation and standard general relativity.
""")

st.divider()

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.caption(
    "Primordial Black Hole Evaporation Research Dashboard • Built with Streamlit and Python"
)

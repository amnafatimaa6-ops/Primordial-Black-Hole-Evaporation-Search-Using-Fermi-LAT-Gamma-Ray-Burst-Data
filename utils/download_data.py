from astroquery.heasarc import Heasarc
import streamlit as st


@st.cache_data(show_spinner="Downloading latest Fermi-LAT catalogue from NASA...")
def load_fermi_data():

    heasarc = Heasarc()

    query = """
    SELECT *
    FROM fermilgrb
    """

    results = heasarc.query_tap(query)

    table = results.to_table()

    df = table.to_pandas()

    return df

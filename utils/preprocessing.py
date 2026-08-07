import pandas as pd


def preprocess_data(df):

    df = df.copy()

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

    # Replace invalid photon energies

    if "ext_emission_max_ene" in df.columns:

        df.loc[
            df["ext_emission_max_ene"] <= 0,
            "ext_emission_max_ene"
        ] = pd.NA

    # Boolean column

    if "redshift" in df.columns:

        df["has_redshift"] = df["redshift"].notnull()

    return df

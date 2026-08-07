import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler


def calculate_pbh_candidates(df):

    df = df.copy()

    # Select relevant columns

    cols = [

        "name",

        "gbm_cat_t90",

        "like_lat_ts",

        "ext_emission_max_ene",

        "like_best_grbindex",

        "redshift"

    ]

    short = df[cols].copy()

    # Keep short bursts

    short = short[
        short["gbm_cat_t90"] < 2
    ]

    # Remove invalid photon energies

    short.loc[
        short["ext_emission_max_ene"] <= 0,
        "ext_emission_max_ene"
    ] = np.nan

    features = [

        "gbm_cat_t90",

        "like_lat_ts",

        "ext_emission_max_ene",

        "like_best_grbindex"

    ]

    analysis = short[
        features
    ].dropna().copy()

    # Physics transformations

    analysis["gbm_cat_t90"] = (
        1 / analysis["gbm_cat_t90"]
    )

    analysis["like_best_grbindex"] = (
        -analysis["like_best_grbindex"]
    )

    scaler = MinMaxScaler()

    scaled = pd.DataFrame(

        scaler.fit_transform(analysis),

        columns=features,

        index=analysis.index

    )

    weights = {

        "gbm_cat_t90": 0.40,

        "like_lat_ts": 0.20,

        "ext_emission_max_ene": 0.30,

        "like_best_grbindex": 0.10

    }

    scaled["PBH_consistency"] = (

        weights["gbm_cat_t90"]
        * scaled["gbm_cat_t90"]

        +

        weights["like_lat_ts"]
        * scaled["like_lat_ts"]

        +

        weights["ext_emission_max_ene"]
        * scaled["ext_emission_max_ene"]

        +

        weights["like_best_grbindex"]
        * scaled["like_best_grbindex"]

    )

    short["PBH_consistency"] = np.nan

    short.loc[
        scaled.index,
        "PBH_consistency"
    ] = scaled["PBH_consistency"]

    short = short.sort_values(

        "PBH_consistency",

        ascending=False

    )

    return short

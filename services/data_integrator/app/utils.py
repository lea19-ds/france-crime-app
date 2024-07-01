"""Module providing utils functions for cleaning"""

import pandas as pd
from unidecode import unidecode

def nettoyer_nom_des_colonnes(df : pd.DataFrame):
    """Function standardizing column names"""
    df.columns = [
        unidecode(col.lower().replace(".", "_"))
        for col in df.columns.to_list()
    ]
    return df

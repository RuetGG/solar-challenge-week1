# for loading, cleaning and filtering data

import pandas as pd
import numpy as np

def load_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath, parse_dates=['Timestamp'])
    

def drop_high_missing(df: pd.DataFrame, threshold: int = 5) -> pd.DataFrame:
    missing_cols = [c for c in df.columns if df[c].isna().sum() > threshold and c != "Timestamp"]
    return df.drop(columns=missing_cols)
     
    
def clean_outliers(df: pd.DataFrame, zscore_columns=None, clip_columns=None, threshold=3):
    
    df_clean = df.copy()
    if zscore_columns:
        z = (df_clean[zscore_columns] - df_clean[zscore_columns].mean()) / df_clean[zscore_columns].std()
        df_clean = df_clean[(np.abs(z) <= threshold).all(axis=1)]

    if clip_columns:
        for col in clip_columns:
            if col in df_clean.columns:
                lower = df_clean[col].quantile(0.01)
                upper = df_clean[col].quantile(0.99)
                df_clean.loc[:, col] = df_clean[col].clip(lower, upper)

    return df_clean

def detect_outliers(df:pd.DataFrame , cols, threshold=3):
    z = (df[cols] - df[cols].mean()) / df[cols].std()
    df["outlier_flag"] = (np.abs(z) > threshold).any(axis=1)
    return df

def clean_limit(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "GHI" in df.columns:
        df.loc[:, "GHI"] = df["GHI"].clip(lower=0)
    if "DNI" in df.columns:
        df.loc[:, "DNI"] = df["DNI"].clip(lower=0)
    if "DHI" in df.columns:
        df.loc[:, "DHI"] = df["DHI"].clip(lower=0)
    if "Tamb" in df.columns:
        df = df[df["Tamb"].between(-10, 60)]
        
    return df

def finalize_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.set_index('Timestamp')
    df = df.sort_index()
    return df

def save_clean(df: pd.DataFrame, filepath: str):
    df.to_csv(filepath)
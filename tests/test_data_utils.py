from src.data_utils import load_data
import pandas as pd

def test_load_data():
    df = load_data("data/benin_clean.csv")
    assert isinstance(df, pd.DataFrame)
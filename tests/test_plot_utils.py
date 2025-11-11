from src.plot_utils import plot_metrix
import pandas as pd

def test_plot_metric_runs():
    df = pd.DataFrame({"country" : ["A", "B"], "GHI": [1,2]})
    plot_metrix(df, "GHI")
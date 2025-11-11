import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_time_series(df: pd.DataFrame, columns, figsize=(12,4)):
    for var in columns:
        plt.figure(figsize=figsize)
        plt.plot(df.index, df[var])
        plt.title(f"{var} vs Timestamp")
        plt.xlabel("Timestamp")
        plt.ylabel(var)
        plt.show()
        
def plot_monthly_average(df: pd.DataFrame, columns, figsize=(12,4)):
    monthly = df.resample('ME').mean()

    for var in columns:
        plt.figure(figsize=(12,4))
        plt.plot(monthly.index, monthly[var])
        plt.title(f"Monthly Average {var}")
        plt.xlabel("Month")
        plt.ylabel(var)
        plt.show()
        
def plot_daily_pattern(df: pd.DataFrame, column, date=None, figsize = (12,4)):
    day_date = df.index[0].date()
    day_data = df.loc[str(day_date)]

    plt.figure(figsize=figsize)
    plt.plot(day_data.index, day_data[column])
    plt.title(f"{column} Daily Pattern on {day_date}")
    plt.xlabel("Hour of Day")
    plt.ylabel(column)
    plt.show()
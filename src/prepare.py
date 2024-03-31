from curses import flash
import pandas as pd
import numpy as np
def extract_columns(df:pd.DataFrame):
    monthly_mean = df['MonthlyMeanTemperature']
    means = []
    for mean in monthly_mean:
        if not np.isnan(mean):
            means.append(mean)
    monthly_df = {'monthly' : means}
    monthly_df = pd.DataFrame(monthly_df)
    monthly_df.to_csv('data/monthly_mean.csv', index=False)

def convert_to_df():
    df = pd.read_csv('data/file1.csv')
    return df

if __name__ == '__main__':
    df = convert_to_df()
    extract_columns(df)

from curses import flash
import pandas as pd
import numpy as np
from ruamel.yaml import YAML

def extract_columns(df:pd.DataFrame):
    monthly_mean = df['MonthlyMeanTemperature']
    means = []
    for mean in monthly_mean:
        mean = float(mean)
        if not np.isnan(mean):
            means.append(mean)
    monthly_df = {'monthly' : means}
    monthly_df = pd.DataFrame(monthly_df)
    monthly_df.to_csv('data/monthly_mean.csv', index=False)

def convert_to_df(file_idx):
    df = pd.read_csv(f'data/file_{file_idx}.csv', dtype="str")
    return df

if __name__ == '__main__':
    yaml = YAML(typ="safe")
    params = yaml.load(open("params.yaml", encoding="utf-8"))
    df = convert_to_df(file_idx=params['process']['file'])
    extract_columns(df)


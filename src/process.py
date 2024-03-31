# Process the HourlyDryBulbTemp and MonthlyMeanTemperature
import pandas as pd
import numpy as np
from tomlkit import date

def compute_aggregate(df):
    monthly_data = []
    for i in range(12):
        monthly_data.append([])
    for i in range(len(df)):

        date_str = df['DATE'][i]
        month_str = date_str[5:7]
        month = eval(month_str[1]) if month_str[0] =='0' else eval(month_str)
        temp = df['HourlyDryBulbTemperature'][i]
        if(isinstance(temp, str) and temp[-1] == 's'):
            temp = temp[:len(temp)-1]
        if(np.isnan(float(temp))):
            monthly_data[month - 1].append(0)
        else:
            monthly_data[month - 1].append(float(temp))
    monthly_avg = []
    for month in monthly_data:
        monthly_avg.append(np.mean(np.array(month)))
    monthly_avg_df = pd.DataFrame({'computed_monthly_mean' : monthly_avg})
    monthly_avg_df.to_csv('data/computed_monthly_mean.csv', index=False)

def convert_to_df():
    df = pd.read_csv('data/file1.csv', dtype="str")
    return df

if __name__ == '__main__':
    df = convert_to_df()
    compute_aggregate(df)

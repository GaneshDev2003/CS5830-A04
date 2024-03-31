import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
def compute_r2(computed_mean, actual_mean):
    print("R2 score of the Monthly Average Temperature is : ")
    print(r2_score(computed_mean, actual_mean))

def extract_data():
    computed_mean_df = pd.read_csv('data/computed_monthly_mean.csv')
    acutal_mean_df = pd.read_csv('data/monthly_mean.csv')
    return computed_mean_df['computed_monthly_mean'], acutal_mean_df['monthly']

if __name__ == '__main__':
    computed_mean, actual_mean = extract_data()
    compute_r2(computed_mean, actual_mean)

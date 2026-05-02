import pandas as pd
import numpy as np

df = pd.read_csv('data/hr_data.csv')

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nNull counts:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSample rows:")
print(df.head())
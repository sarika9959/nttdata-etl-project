import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('outputs', exist_ok=True)

print("=== STEP 1: INGESTION ===")
df = pd.read_csv('data/hr_data.csv')
raw_count = len(df)
print(f"Raw records loaded: {raw_count}")

print("\n=== STEP 2: DATA QUALITY CHECKS ===")
quality_report = {
    'total_records': len(df),
    'duplicate_records': df.duplicated().sum(),
    'null_values': df.isnull().sum().sum(),
    'columns_with_nulls': df.columns[df.isnull().any()].tolist()
}
for k, v in quality_report.items():
    print(f"  {k}: {v}")

print("\n=== STEP 3: CLEANING ===")
df = df.drop_duplicates()
df = df.dropna()
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
clean_count = len(df)
print(f"  Records after cleaning: {clean_count}")
print(f"  Records removed: {raw_count - clean_count}")

print("\n=== STEP 4: TRANSFORMATION ===")
df['salary_band'] = pd.cut(
    df['monthlyincome'],
    bins=[0, 3000, 6000, 10000, 25000],
    labels=['Low', 'Medium', 'High', 'Very High']
)
df['tenure_group'] = pd.cut(
    df['yearsatcompany'],
    bins=[0, 2, 5, 10, 40],
    labels=['New', 'Growing', 'Experienced', 'Veteran']
)
df['age_group'] = pd.cut(
    df['age'],
    bins=[18, 30, 40, 50, 65],
    labels=['20s', '30s', '40s', '50s+']
)
print("  Derived columns added: salary_band, tenure_group, age_group")

print("\n=== STEP 5: DEPARTMENT LOOKUP JOIN ===")
dept_lookup = pd.DataFrame({
    'department': ['Sales', 'Research & Development', 'Human Resources'],
    'dept_code': ['SALES', 'R&D', 'HR'],
    'budget_tier': ['High', 'Very High', 'Medium']
})
df = df.merge(dept_lookup, on='department', how='left')
print("  Department lookup joined successfully")
print(f"  Columns now: {df.shape[1]}")

print("\n=== STEP 6: DATA VALIDATION ===")
assert df['attrition'].isin([0,1]).all(), "Attrition has invalid values"
assert df['age'].between(18, 65).all(), "Age out of range"
assert df['monthlyincome'].gt(0).all(), "Income has zero/negative values"
assert df.duplicated().sum() == 0, "Duplicates still exist"
print("  All validation checks passed")

print("\n=== STEP 7: SAVE OUTPUTS ===")
df.to_csv('outputs/hr_clean.csv', index=False)
df.to_excel('outputs/hr_clean.xlsx', index=False)

summary = pd.DataFrame({
    'metric': ['Raw Records', 'Clean Records', 'Removed', 'Columns Added', 'Validation Checks'],
    'value': [raw_count, clean_count, raw_count - clean_count, 3, 4]
})
summary.to_csv('outputs/pipeline_summary.csv', index=False)

print("\nOutputs saved to /outputs folder")
print(f"Final dataset: {df.shape[0]} rows x {df.shape[1]} columns")
print("\n=== PIPELINE COMPLETE ===")
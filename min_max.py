import pandas as pd
df = pd.read_csv("D:/crop_yield.csv")

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df_numeric = df[numeric_cols]

df_normalized = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())

for col in df.columns:
    if col not in numeric_cols:
        df_normalized[col] = df[col]

X = df_normalized.drop('Yield', axis=1)
y = df_normalized['Yield']



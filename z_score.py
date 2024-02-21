import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("D:/crop_yield.csv")
df = pd.get_dummies(df)

# Separate the target variable (Yield) from the features
X = df.drop('Yield', axis=1)
y = df['Yield']

scaler = StandardScaler()

scaled_features = scaler.fit_transform(X)

scaled_df = pd.DataFrame(scaled_features, columns=X.columns)
print(scaled_df.head())

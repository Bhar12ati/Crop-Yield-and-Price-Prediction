import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the dataset using pd.read_csv()
df = pd.read_csv("D:/edai/crop_yield.csv")

# Filter data for Wheat, Rice, and Bajra crops
selected_crops = ['Wheat', 'Rice', 'Bajra']
filtered_data = df[df['Crop'].isin(selected_crops)]

# Plot the graph for Crop_Year vs Yield for Wheat, Rice, and Bajra with solid lines
plt.figure(figsize=(10, 6))
sns.lineplot(x="Crop_Year", y="Yield", hue="Crop", data=filtered_data, markers=False, style="Crop", ci=None, dashes=False)
plt.title('Crop Year vs Yield for Wheat, Rice, and Bajra')
plt.xlabel('Crop Year')
plt.ylabel('Yield')
plt.legend(title='Crop')
plt.show()

# Specify features (X) and target variable (y)
# Replace 'target_column' with the actual name of your target column
X = df.drop('Yield', axis=1)  # Features
y = df['Yield']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the sizes of the subsets and the original dataset
print("Original dataset size:", df.shape)
print("Training set size:", X_train.shape, y_train.shape)
print("Testing set size:", X_test.shape, y_test.shape)

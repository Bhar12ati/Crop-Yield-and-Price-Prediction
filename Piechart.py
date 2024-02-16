import pandas as pd
import plotly.express as px

# Load the dataset using pd.read_csv()
df = pd.read_csv("D:/edai/crop_yield.csv")

# Exclude 'Coconut' from the data
filtered_data = df[df['Crop'].str.strip() != 'Coconut']

# Group data by Crop and sum the Yield for each crop (excluding Coconut)
crop_yield_sum = filtered_data.groupby('Crop')['Yield'].sum().reset_index()

# Plot an interactive pie chart with hover labels
fig = px.pie(crop_yield_sum, values='Yield', names='Crop', title='Distribution of Yield Across Crops (excluding Coconut)',
             hover_data=['Crop'], labels={'Crop': 'Crops'}, hole=0.3)

fig.update_traces(textinfo='none')  # Hide percentage labels

fig.show()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the combined DataFrame
combined_df = pd.read_csv('combined_df.csv')

# Set the title of the dashboard
st.title('Air Quality Dashboard')

# Create a sidebar for selecting the year
year = st.sidebar.selectbox('Select Year', combined_df['year'].unique())

# Filter the data by the selected year
filtered_df = combined_df[combined_df['year'] == year]

# Create a section for displaying the trend of air quality index over the years
st.header('Trend of Air Quality Index Over the Years')
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='datetime', y='AQI')
plt.title('Trend of Air Quality Index Over the Years')
plt.xlabel('Date')
plt.ylabel('Average AQI')
plt.show()
st.pyplot()

# Create a section for displaying the most significant pollutants affecting air quality
st.header('Most Significant Pollutants Affecting Air Quality')
plt.figure(figsize=(10, 6))
sns.barplot(x=filtered_df['AQI'].drop('AQI').sort_values(ascending=False).values, y=filtered_df['AQI'].drop('AQI').sort_values(ascending=False).index, palette='coolwarm')
plt.title('Correlation of Pollutants with AQI')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Pollutants')
plt.show()
st.pyplot()

# Print the correlation values
st.write("Correlation of pollutants with AQI:")
st.write(filtered_df['AQI'].drop('AQI').sort_values(ascending=False))

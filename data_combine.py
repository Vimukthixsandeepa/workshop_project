import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = './Wine_Stats'

# Load all CSV files into a list of DataFrames
dataframes = []
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Combine all DataFrames into a single DataFrame
wine_df = pd.concat(dataframes, ignore_index=True)

# Display the first few rows
print(wine_df.head())

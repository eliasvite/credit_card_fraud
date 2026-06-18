import os
import zipfile
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths relative to the project structure
project_root = os.path.dirname(script_dir)
data_folder = os.path.join(project_root, 'data')
zip_file_path = os.path.join(project_root, 'credit-card.zip')

# 1. Initialize and authenticate Kaggle API client
print("Authenticating with Kaggle API...")
api = KaggleApi()
api.authenticate()

# 2. Download dataset files directly using the library method
print("Downloading dataset from Kaggle...")
api.dataset_download_files('mishra5001/credit-card', path=project_root, unzip=False)

# 3. Extract the downloaded zip file into the targeted data directory
print("Extracting zip file package into data directory...")
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(data_folder)

# 4. Clean up the local environment by removing the temporary zip file
print("Cleaning up temporary compressed files...")
os.remove(zip_file_path)

# 5. Dynamically search for the extracted CSV file inside the data folder
extracted_files = os.listdir(data_folder)
csv_files = [file for file in extracted_files if file.endswith('.csv')]

if not csv_files:
    raise FileNotFoundError("No CSV file was found in the data directory.")

# Select the first available CSV file found
target_csv_name = csv_files[0]
csv_file_path = os.path.join(data_folder, target_csv_name)

# 6. Read the dataset into a pandas DataFrame to verify correct execution
df = pd.read_csv(csv_file_path) 
print("Data ingestion pipeline completed successfully!")
print(f"Loaded file name: {target_csv_name}")
print(f"Dataset dimensions: {df.shape}")
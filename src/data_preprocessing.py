import os
import requests
import pandas as pd

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

data_dir = '../data/'
online_retail_id = '12Z6DOV-tZ5ujLajzpOa6SmhU4v5HWThw'
online_retail_path = os.path.join(data_dir, 'online_retail.xlsx')
amazon_reviews_path = os.path.join(data_dir, 'amazon_reviews.csv')

# Download online_retail.xlsx if it doesn't exist
if not os.path.exists(online_retail_path):
    print(f"Downloading {online_retail_path}...")
    download_file_from_google_drive(online_retail_id, online_retail_path)
    print(f"Downloaded {online_retail_path}")

# Load the datasets
online_retail_df = pd.read_excel(online_retail_path)
amazon_reviews_df = pd.read_csv(amazon_reviews_path)

# Display shapes and head of dataframes before preprocessing
print(f"Online Retail Dataset Shape: {online_retail_df.shape}")
print(f"Amazon Reviews Dataset Shape: {amazon_reviews_df.shape}")
print("Online Retail Dataset Sample:\n", online_retail_df.head())
print("Amazon Reviews Dataset Sample:\n", amazon_reviews_df.head())

# Perform preprocessing steps
online_retail_df.drop_duplicates(inplace=True)
amazon_reviews_df.drop_duplicates(inplace=True)

# Display shapes and head of dataframes after preprocessing
print(f"Online Retail Dataset Shape after preprocessing: {online_retail_df.shape}")
print(f"Amazon Reviews Dataset Shape after preprocessing: {amazon_reviews_df.shape}")
print("Online Retail Dataset Sample after preprocessing:\n", online_retail_df.head())
print("Amazon Reviews Dataset Sample after preprocessing:\n", amazon_reviews_df.head())

# Save the preprocessed data if needed
preprocessed_online_retail_path = os.path.join(data_dir, 'preprocessed_online_retail.csv')
preprocessed_amazon_reviews_path = os.path.join(data_dir, 'preprocessed_amazon_reviews.csv')

online_retail_df.to_csv(preprocessed_online_retail_path, index=False)
amazon_reviews_df.to_csv(preprocessed_amazon_reviews_path, index=False)

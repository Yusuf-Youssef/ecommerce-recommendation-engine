# src/data_preprocessing.py

import pandas as pd
import requests

# Function to download a file from Google Drive
def download_file_from_google_drive(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

# URLs to the large datasets
online_retail_url = https://drive.google.com/uc?export=download&id=12Z6DOV-tZ5ujLajzpOa6SmhU4v5HWThw
amazon_reviews_url = https://drive.google.com/uc?export=download&id=10H9z9sI6055zrjhGKdkRSq6zTZq9hcfp

# Download the files
download_file_from_google_drive(online_retail_url, '../data/online_retail.xlsx')
download_file_from_google_drive(amazon_reviews_url, '../data/amazon_reviews.csv')

# Load the datasets
online_retail = pd.read_excel('../data/online_retail.xlsx')
amazon_reviews = pd.read_csv('../data/amazon_reviews.csv')
retail_sales = pd.read_csv('../data/retail_sales_dataset.csv')

# Data Cleaning
# Handle missing values
online_retail.fillna(method='ffill', inplace=True)
amazon_reviews.fillna(method='ffill', inplace=True)
retail_sales.fillna(method='ffill', inplace=True)

# Remove duplicates
online_retail.drop_duplicates(inplace=True)
amazon_reviews.drop_duplicates(inplace=True)
retail_sales.drop_duplicates(inplace=True)

# Feature Engineering
# Normalize numerical features for online_retail
from sklearn.preprocessing import StandardScaler, LabelEncoder

scaler = StandardScaler()
online_retail['Quantity'] = scaler.fit_transform(online_retail[['Quantity']])
online_retail['UnitPrice'] = scaler.fit_transform(online_retail[['UnitPrice']])

# Encode categorical features for amazon_reviews
label_encoder = LabelEncoder()
amazon_reviews['product_category'] = label_encoder.fit_transform(amazon_reviews['product_category'])

# Save preprocessed data
online_retail.to_csv('../data/processed_online_retail.csv', index=False)
amazon_reviews.to_csv('../data/processed_amazon_reviews.csv', index=False)
retail_sales.to_csv('../data/processed_retail_sales.csv', index=False)


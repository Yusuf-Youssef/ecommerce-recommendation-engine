import pandas as pd

# Load preprocessed data
preprocessed_online_retail_path = '../data/preprocessed_online_retail.csv'
preprocessed_amazon_reviews_path = '../data/preprocessed_amazon_reviews.csv'

online_retail_df = pd.read_csv(preprocessed_online_retail_path)
amazon_reviews_df = pd.read_csv(preprocessed_amazon_reviews_path)

# Display basic information and statistics
print("Online Retail Dataset Info:")
print(online_retail_df.info())
print("\nOnline Retail Dataset Description:")
print(online_retail_df.describe())

print("\nAmazon Reviews Dataset Info:")
print(amazon_reviews_df.info())
print("\nAmazon Reviews Dataset Description:")
print(amazon_reviews_df.describe())


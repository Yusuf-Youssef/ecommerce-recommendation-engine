import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Load preprocessed data
preprocessed_amazon_reviews_path = '../data/preprocessed_amazon_reviews.csv'
amazon_reviews_df = pd.read_csv(preprocessed_amazon_reviews_path)

# Print column names and data sample for debugging
print("Amazon Reviews DataFrame Columns:", amazon_reviews_df.columns)
print("Amazon Reviews DataFrame Sample:\n", amazon_reviews_df.head())

# Convert the Amazon Reviews dataset into Surprise format
reader = Reader(rating_scale=(1, 5))
try:
    # Change 'Rating' to 'Score'
    data = Dataset.load_from_df(amazon_reviews_df[['UserId', 'ProductId', 'Score']], reader)
except KeyError as e:
    print(f"KeyError: {e}. Ensure the column names are correct in the DataFrame.")
    raise

# Use SVD algorithm for recommendations
algo = SVD()

# Evaluate the performance using cross-validation
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Train the algorithm on the full dataset
trainset = data.build_full_trainset()
algo.fit(trainset)

# Example: Predict rating for a specific user and product
user_id = 'A1M2LQ8TIY51I9'  # Replace with an actual user ID from your dataset
product_id = 'B00006HAXW'   # Replace with an actual product ID from your dataset
pred = algo.predict(user_id, product_id)
print(f"Predicted rating for user {user_id} and product {product_id}: {pred.est}")

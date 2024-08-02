import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate

# Load preprocessed data
preprocessed_amazon_reviews_path = '../data/preprocessed_amazon_reviews.csv'
amazon_reviews_df = pd.read_csv(preprocessed_amazon_reviews_path)

# Convert the Amazon Reviews dataset into Surprise format
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(amazon_reviews_df[['UserId', 'ProductId', 'Rating']], reader)

# Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Initialize the SVD algorithm
algo = SVD()

# Train the algorithm on the training data
algo.fit(trainset)

# Evaluate the performance on the test set
predictions = algo.test(testset)
accuracy.rmse(predictions)
accuracy.mae(predictions)

# Example: Predict rating for a specific user and product
def predict_rating(user_id, product_id):
    pred = algo.predict(user_id, product_id)
    return pred.est

# Example usage
user_id = 'A1M2LQ8TIY51I9'  # Replace with an actual user ID from your dataset
product_id = 'B00006HAXW'   # Replace with an actual product ID from your dataset
predicted_rating = predict_rating(user_id, product_id)
print(f"Predicted rating for user {user_id} and product {product_id}: {predicted_rating}")

# Evaluate the performance using cross-validation
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

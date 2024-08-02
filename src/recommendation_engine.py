import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the preprocessed data
online_retail_path = '../data/preprocessed_online_retail.csv'
amazon_reviews_path = '../data/preprocessed_amazon_reviews.csv'

# Load datasets
online_retail_df = pd.read_csv(online_retail_path)
amazon_reviews_df = pd.read_csv(amazon_reviews_path)

# Data Preprocessing
def preprocess_data(df):
    df.dropna(subset=['description'], inplace=True)  # Drop rows with missing descriptions
    df['description'] = df['description'].astype(str)  # Ensure descriptions are strings
    return df

online_retail_df = preprocess_data(online_retail_df)
amazon_reviews_df = preprocess_data(amazon_reviews_df)

# Build the Recommendation Engine
def build_recommendation_model(df):
    # Use TF-IDF Vectorizer for text features
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Generate Recommendations
def recommend_products(df, cosine_sim, index, top_n=10):
    # Get similarity scores for the specified product
    sim_scores = list(enumerate(cosine_sim[index]))
    
    # Sort products based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the top_n most similar products
    sim_scores = sim_scores[1:top_n+1]
    
    # Get the indices of the top_n most similar products
    product_indices = [i[0] for i in sim_scores]
    
    # Return the top_n most similar products
    return df.iloc[product_indices]

# Example Usage
def main():
    # Build the recommendation model
    cosine_sim = build_recommendation_model(online_retail_df)
    
    # Example: Get recommendations for a product at index 0
    product_index = 0
    recommendations = recommend_products(online_retail_df, cosine_sim, product_index)
    
    # Print recommendations
    print("Recommended Products:")
    print(recommendations[['product_id', 'description']])

if __name__ == "__main__":
    main()


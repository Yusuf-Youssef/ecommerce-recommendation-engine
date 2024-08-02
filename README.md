# eCommerce Recommendation Engine

## Overview

This project is an AI-powered recommendation engine designed to provide personalized product recommendations using collaborative filtering. The recommendation model is built using Singular Value Decomposition (SVD) and evaluated using metrics such as RMSE and MAE. This README provides instructions on how to set up the environment, run the scripts, and understand the evaluation process.

## Requirements

1. **Data Collection and Preprocessing:** 
   - Data is collected from the provided sources and preprocessed to ensure it is suitable for training the recommendation model.

2. **Model Development:**
   - A collaborative filtering model using SVD (Singular Value Decomposition) is implemented to generate recommendations.

3. **Scalability and Performance:**
   - Basic scalability and performance testing have been conducted. For deployment, further testing in a high-traffic environment is recommended.

4. **Evaluation and Optimization:**
   - The model is evaluated using RMSE (Root Mean Square Error) and MAE (Mean Absolute Error). Continuous evaluation and optimization strategies can be implemented for further improvement.

## Getting Started

### Prerequisites

- Python 3.12
- Virtual environment (recommended)

### Installation Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Yusuf-Youssef/ecommerce-recommendation-engine.git
   cd ecommerce-recommendation-engine
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   If installing the dependencies directly from the requirements.txt file doesn't work, please install them manually.

   **`requirements.txt` includes:**
   ```
   pandas
   scikit-surprise
   openpyxl
   requests
   numpy==1.26
   ```

### Data Preparation

1. **Download the Data Files:**
   - **Online Retail Data:** Download from [Google Drive link](https://drive.google.com/uc?export=download&id=12Z6DOV-tZ5ujLajzpOa6SmhU4v5HWThw) and save as `online_retail.xlsx` in the `data` directory.
   - **Amazon Reviews Data:** Due to its large size, download manually from the link provided in the text file and save as `amazon_reviews.csv` in the `data` directory.

2. **Run Data Preprocessing:**
   ```bash
   cd src
   python data_preprocessing.py
   ```

   This will preprocess the data and save the cleaned files as `preprocessed_online_retail.csv` and `preprocessed_amazon_reviews.csv` in the `data` directory.

### Running the Recommendation Engine

1. **Execute the Recommendation Engine Script:**
   ```bash
   python recommendation_engine.py
   ```

   This script will evaluate the recommendation model and output performance metrics along with a sample prediction.

## How It Works

1. **Data Preprocessing:** 
   - Data is cleaned and saved in a format suitable for the recommendation engine. This includes removing duplicates and ensuring proper data types.

2. **Model Training and Evaluation:**
   - The recommendation model is trained using SVD. The performance is evaluated using cross-validation, measuring RMSE and MAE.

3. **Sample Prediction:**
   - The script outputs a sample prediction for a specified user and product ID to demonstrate the functionality of the recommendation engine.

## Troubleshooting

- **Missing Dependencies:** Ensure all dependencies are installed as per the `requirements.txt`. Reinstall them manually if needed.
- **Data File Issues:** Verify that the data files are correctly placed in the `data` directory.
- **Virtual Environment Issues:** Ensure the virtual environment is properly activated before running scripts.

## Further Enhancements

- **Scalability Testing:** Conduct performance testing in a production-like environment to ensure the system handles high traffic efficiently.
- **Optimization:** Implement additional optimization strategies such as hyperparameter tuning or using additional features for improved recommendations.

## Conclusion

This recommendation engine provides a functional prototype for personalized product recommendations. By following the instructions above, evaluators should be able to set up, run, and test the recommendation system.

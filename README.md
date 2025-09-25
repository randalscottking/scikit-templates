# Scikit-learn Templates

This repository contains a collection of machine learning templates using scikit-learn for various common use cases and scenarios. Each template demonstrates different machine learning algorithms and techniques applied to real-world problems.

## Project Structure

### Churn Prediction
Located in `/churn/` directory, this module focuses on customer churn prediction using different algorithms:
- Decision Trees (`churn_dec_tree.py`)
- K-Nearest Neighbors (`churn_knn.py`)
- Logistic Regression (`churn_log_reg.py`)
- Support Vector Machines (`churn_svm.py`)
- Base churn module (`churn.py`)

The churn prediction models use data from:
- Training dataset: `customer_churn_dataset-training-master.csv`
- Testing dataset: `customer_churn_dataset-testing-master.csv`

### Credit Card Fraud Detection
Located in `/credit_card_fraud/` directory, this module focuses on detecting fraudulent credit card transactions using machine learning techniques.
- Main script: `credit_card_fraud.py`
- Uses data from: `data/data.csv`

### Forecasting
Located in `/forecast/` directory, this module demonstrates time series forecasting:
- Prophet forecasting implementation (`prophet_forecast.py`)

### Linear Regression
Located in `/linear_regression/` directory:
- Basic linear regression implementation (`src/linearRegression.py`)

### Miscellaneous Utilities
Located in `/misc/` directory, contains various utility scripts:
- Database import functionality (`Import from Database.py`)
- Schema inference (`inferSchema.py`)
- Label encoding examples (`label_encoding.py`)
- One-hot encoding examples (`one_hot_encoding.py`)
- Ordinal encoding and data splitting (`ordinal-encode_and_split.py`)

## Requirements

Each module may have its own specific requirements. For the churn prediction module, dependencies are listed in `churn/requirements.txt`.

## Getting Started

1. Clone this repository
2. Navigate to the specific module you want to use
3. Install the required dependencies (e.g., for churn prediction: `pip install -r requirements.txt`)
4. Run the desired script (e.g., `python src/churn_dec_tree.py`)

## Module Details

### Churn Prediction
This module implements various machine learning algorithms to predict customer churn. Each implementation offers a different approach to the same problem, allowing for comparison of different techniques:

- Decision Trees: Uses tree-based learning for interpretable predictions
- KNN: Utilizes nearest neighbor classification
- Logistic Regression: Implements probabilistic classification
- SVM: Uses support vector machines for classification

### Credit Card Fraud Detection
This module implements machine learning techniques to identify fraudulent credit card transactions. It processes transaction data to classify transactions as either legitimate or fraudulent.

### Time Series Forecasting
The forecasting module uses Facebook's Prophet library to perform time series forecasting. Prophet is particularly useful for forecasting with strong seasonal effects and historical trends.

### Linear Regression
A basic implementation of linear regression for understanding the fundamental concepts of predictive modeling with continuous variables.

### Utility Scripts
The misc directory contains various utility scripts that demonstrate common data preprocessing tasks:
- Database integration
- Schema inference for datasets
- Different encoding techniques for categorical variables
- Data splitting strategies

For detailed usage of any specific module, please refer to the comments within each script.

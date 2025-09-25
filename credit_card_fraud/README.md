# Credit Card Fraud Detection

This module implements machine learning techniques to identify fraudulent credit card transactions using scikit-learn.

## Overview

The credit card fraud detection system processes transaction data to classify transactions as either legitimate or fraudulent. It uses machine learning algorithms to identify patterns that may indicate fraudulent activity.

## Implementation

The main implementation is in `src/credit_card_fraud.py`. The system:
1. Loads and preprocesses transaction data
2. Handles class imbalance (as fraudulent transactions are typically rare)
3. Trains a machine learning model
4. Evaluates the model's performance

## Data

The module uses data from `data/data.csv`. The dataset should contain transaction features and a binary label indicating whether each transaction is fraudulent.

## Usage

1. Ensure your data is in the correct format in `data/data.csv`
2. Run the script:
   ```bash
   python src/credit_card_fraud.py
   ```

## Evaluation

The model's performance is evaluated using:
- Precision
- Recall
- F1-score
- ROC curve

These metrics are particularly important in fraud detection where class imbalance is common and false positives/negatives have different business impacts.
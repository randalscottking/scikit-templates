# Customer Churn Prediction

This module implements various machine learning algorithms to predict customer churn using scikit-learn. It provides multiple implementations using different algorithms to allow for comparison of their performance and characteristics.

## Models Implemented

1. **Decision Trees** (`src/churn_dec_tree.py`)
   - Uses tree-based learning for interpretable predictions
   - Advantages: Easy to interpret, handles non-linear relationships
   - Disadvantages: Can overfit without proper tuning

2. **K-Nearest Neighbors** (`src/churn_knn.py`)
   - Classification based on nearest neighbors
   - Advantages: Simple, non-parametric, adapts to the data
   - Disadvantages: Computationally intensive for large datasets

3. **Logistic Regression** (`src/churn_log_reg.py`)
   - Probabilistic classification approach
   - Advantages: Fast, probabilistic output, works well with linear relationships
   - Disadvantages: May underperform with non-linear relationships

4. **Support Vector Machines** (`src/churn_svm.py`)
   - Uses hyperplanes for classification
   - Advantages: Effective in high-dimensional spaces, robust to overfitting
   - Disadvantages: Computationally intensive, sensitive to feature scaling

5. **Base Module** (`src/churn.py`)
   - Contains common functionality used by all models

## Data

The module uses two datasets:
- `data/customer_churn_dataset-training-master.csv`: Training dataset
- `data/customer_churn_dataset-testing-master.csv`: Testing dataset

## Requirements

All required dependencies are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

## Usage

1. Install dependencies
2. Choose the model you want to use
3. Run the corresponding script:
   ```bash
   python src/churn_dec_tree.py  # for decision tree
   python src/churn_knn.py       # for KNN
   python src/churn_log_reg.py   # for logistic regression
   python src/churn_svm.py       # for SVM
   ```

## Model Selection

- Use **Decision Trees** when interpretability is important
- Use **KNN** for smaller datasets or when you need a non-parametric approach
- Use **Logistic Regression** for fast training and when relationships are mostly linear
- Use **SVM** when you need robust performance and have computational resources available
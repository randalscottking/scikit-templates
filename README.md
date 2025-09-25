# Scikit-learn Templates

This repository contains a comprehensive collection of machine learning templates using scikit-learn and other ML libraries for various common use cases and scenarios. Each template demonstrates different machine learning algorithms and techniques applied to real-world problems.

## Project Overview

This collection includes templates for:
- Classification (Churn Prediction, Credit Card Fraud)
- Regression (Linear Regression)
- Time Series (Prophet Forecasting)
- Natural Language Processing (Sentiment Analysis)
- Educational Analytics (Student Placement Prediction)
- Data Preprocessing and Utilities

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
- Basic linear regression implementation (`src/linear_regression.py`)

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

### Sentiment Analysis
Located in `/sentiment/` directory, this module implements sentiment analysis for movie reviews:
- Uses BERT for sequence classification
- Includes data visualization and preprocessing
- Handles both positive and negative sentiment classification
- Features comprehensive error analysis and model evaluation

### Student Placement Prediction
Located in `/placement-prediction/` directory, this module predicts student placement outcomes:
- Uses Random Forest and Logistic Regression models
- Processes academic and extracurricular data
- Provides comparative model performance analysis
- Features automated data preprocessing pipeline

## Common Requirements

Common dependencies across projects include:
```bash
numpy>=1.19.2
pandas>=1.2.3
scikit-learn>=0.24.1
matplotlib>=3.3.4
```

Each module may have additional specific requirements listed in their respective directories.

## Getting Started

1. Clone this repository
```bash
git clone https://github.com/yourusername/scikit-templates.git
cd scikit-templates
```

2. Choose a project:
```bash
cd [project-directory]  # e.g., cd sentiment
```

3. Install dependencies:
```bash
pip install -r requirements.txt  # if available
# or install common requirements:
pip install numpy pandas scikit-learn matplotlib
```

4. Run the desired script:
```bash
python src/[script-name].py  # e.g., python src/sentiment.py
```

## Project-Specific Documentation

Each project directory contains its own README.md with detailed information about:
- Project-specific requirements
- Dataset details and structure
- Model architectures and parameters
- Usage examples and expected outputs
- Performance metrics and evaluations

For detailed usage of any specific module, please refer to the project's README and the comments within each script.

## Contributing

Feel free to contribute by:
1. Adding new ML templates
2. Improving existing implementations
3. Enhancing documentation
4. Reporting issues or suggesting improvements

## License

This project is licensed under the MIT License - see the individual project directories for specific details.
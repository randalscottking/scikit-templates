# Student Placement Prediction

This project implements machine learning models to predict student placement outcomes based on various academic and extracurricular factors.

## Project Overview

The placement predictor:
- Uses Random Forest and Logistic Regression models
- Processes student data including academic performance and activities
- Predicts whether a student will be placed during campus recruitment
- Compares performance between different ML models

## Features

The model considers various student attributes:
- Academic performance metrics
- Extracurricular activities
- Placement training participation
- Other relevant student data

## Project Structure

```
placement-prediction/
├── README.md
├── data/
│   └── placementdata.csv
└── src/
    └── placement.py
```

## Dependencies

- NumPy: For numerical computations
- Pandas: For data processing and CSV handling
- scikit-learn: For machine learning models
  - RandomForestClassifier
  - LogisticRegression
  - train_test_split for data splitting

## Models Used

1. **Random Forest Classifier**
   - Ensemble learning method
   - Handles both numerical and categorical features
   - Provides feature importance insights

2. **Logistic Regression**
   - Binary classification model
   - Baseline model for comparison
   - Provides probability scores

## Data Processing

The pipeline includes:
- Loading student data from CSV
- Removing unnecessary columns (e.g., StudentID)
- One-hot encoding of categorical variables
- Train-test splitting (78% training, 22% testing)
- Feature normalization where needed

## Usage

1. Ensure all dependencies are installed
2. Place your student data in the `data/` directory
3. Run the model:
   ```bash
   python src/placement.py
   ```

## Model Evaluation

The models are evaluated using:
- Accuracy score on test data
- Comparison between Random Forest and Logistic Regression performance
- Cross-validation scores (where applicable)

## Future Improvements

Potential enhancements:
- Feature importance analysis
- Hyperparameter tuning
- Additional models (SVM, XGBoost)
- More detailed performance metrics

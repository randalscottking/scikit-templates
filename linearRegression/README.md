# Linear Regression

This module provides a basic implementation of linear regression using scikit-learn.

## Overview

Linear regression is a fundamental machine learning algorithm that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.

## Implementation

The implementation in `linearRegression.py` demonstrates:
- Data preprocessing
- Model fitting
- Prediction
- Model evaluation

## Mathematical Background

The linear regression equation:
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

Where:
- y is the dependent variable
- x₁, x₂, ..., xₙ are independent variables
- β₀ is the y-intercept
- β₁, β₂, ..., βₙ are coefficients
- ε is the error term

## Usage

1. Prepare your data with features (X) and target variable (y)
2. Run the script:
   ```bash
   python linearRegression.py
   ```

## Model Evaluation

The implementation includes:
- R-squared score
- Mean squared error
- Root mean squared error
- Model coefficients interpretation

## Best Practices

1. Scale features if they're on different scales
2. Check for multicollinearity
3. Validate assumptions:
   - Linearity
   - Independence
   - Homoscedasticity
   - Normality of residuals
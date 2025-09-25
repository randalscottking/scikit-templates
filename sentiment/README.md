# Movie Review Sentiment Analysis

This project implements a sentiment analysis model for movie reviews using BERT (Bidirectional Encoder Representations from Transformers) and the IMDB Movie Reviews dataset.

## Project Overview

The sentiment analyzer:
- Downloads and processes the IMDB Movie Review Dataset
- Implements BERT-based text classification
- Provides visualization of sentiment distribution
- Evaluates model performance on test data

## Features

- **Data Processing**: Handles both positive and negative movie reviews
- **BERT Integration**: Uses pre-trained BERT model for sequence classification
- **Visualizations**: 
  - Sentiment distribution plots
  - Word clouds for review content analysis
- **Performance Metrics**: Classification report with precision, recall, and F1-score

## Dependencies

- TensorFlow
- Transformers (Hugging Face)
- pandas
- BeautifulSoup4
- matplotlib
- plotly
- WordCloud
- scikit-learn

## Dataset

Uses the IMDB Movie Reviews dataset (aclImdb), which includes:
- 25,000 training reviews
- 25,000 test reviews
- Binary sentiment labels (positive/negative)

## Usage

1. The script will automatically download the IMDB dataset if not present
2. Data preprocessing includes:
   - Text cleaning
   - HTML tag removal
   - Dataset balancing
3. Model training and evaluation are performed automatically

## Code Structure

- `sentiment.py`: Main script containing:
  - Dataset download and extraction
  - Data preprocessing functions
  - Model training and evaluation
  - Visualization generation

## Output

The model provides:
- Binary sentiment classification (positive/negative)
- Confidence scores for predictions
- Performance metrics on test data
- Visual analysis of sentiment distribution

## Model Performance

The BERT-based model achieves strong performance on movie review sentiment classification, with metrics calculated using scikit-learn's classification_report.
# Miscellaneous Utilities

This directory contains various utility scripts for common data preprocessing tasks in machine learning workflows.

## Available Scripts

### 1. Database Import (`Import from Database.py`)
- Functionality for importing data from databases
- Supports SQL queries and database connections
- Handles data type conversion

### 2. Schema Inference (`inferSchema.py`)
- Automatically detects data types in datasets
- Identifies categorical and numerical columns
- Provides schema suggestions for data loading

### 3. Label Encoding (`label_encoding.py`)
- Implements label encoding for categorical variables
- Converts categorical text data to numerical format
- Useful for ordinal categorical variables

### 4. One-Hot Encoding (`one_hot_encoding.py`)
- Implements one-hot encoding for categorical variables
- Creates binary columns for each category
- Handles dummy variable trap
- Suitable for nominal categorical variables

### 5. Ordinal Encoding and Data Splitting (`ordinal-encode_and_split.py`)
- Combines ordinal encoding with data splitting
- Maintains encoding consistency between train and test sets
- Includes stratification options

## Usage

Each script can be run independently:
```bash
python Import\ from\ Database.py
python inferSchema.py
python label_encoding.py
python one_hot_encoding.py
python ordinal-encode_and_split.py
```

## Best Practices

1. **Database Import**
   - Use connection pooling for efficiency
   - Always close database connections
   - Use parameterized queries

2. **Schema Inference**
   - Verify inferred types
   - Handle missing values
   - Consider memory constraints

3. **Encoding**
   - Choose appropriate encoding for your data type
   - Consider cardinality of categorical variables
   - Handle unknown categories in test data

4. **Data Splitting**
   - Use stratification for imbalanced datasets
   - Maintain feature independence
   - Consider temporal aspects if relevant
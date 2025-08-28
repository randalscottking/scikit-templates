import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    auc,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv(
    "/kaggle/input/customer-churn-dataset/customer_churn_dataset-training-master.csv"
)

dataset.dropna(inplace=True)


# Encode categorical variables to numeric values
encoded_dataset = dataset.copy()
encoded_dataset["Gender"] = encoded_dataset["Gender"].apply(
    lambda x: 1 if x == "Male" else 0
)

subscription_map = {"Basic": 0, "Standard": 1, "Premium": 2}
encoded_dataset["Subscription Type"] = encoded_dataset["Subscription Type"].map(
    subscription_map
)

contract_map = {"Monthly": 0, "Quarterly": 1, "Annual": 2}
encoded_dataset["Contract Length"] = encoded_dataset["Contract Length"].map(
    contract_map
)

X = encoded_dataset.drop("Churn", axis=1)
y = encoded_dataset["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42, stratify=y
)

# Standardize numerical features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


models = {
    "Decision Tree": DecisionTreeClassifier(),
}

import time

# Initialize lists to store ROC data
roc_data = {}

# Train, evaluate, and collect ROC curve data
timed_results = []

for model_name, model in models.items():
    print(f"Processing: {model_name}...")

    # Measure training time
    start_time = time.time()
    model.fit(X_train_scaled, y_train)
    train_time = time.time() - start_time

    # Measure prediction time
    start_time = time.time()
    y_pred = model.predict(X_test_scaled)
    predict_time = time.time() - start_time

    # Get probabilities for ROC curve if available
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    elif hasattr(model, "decision_function"):
        y_prob = model.decision_function(X_test_scaled)
    else:
        y_prob = None

    # Evaluate metrics
    metrics = {
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "Training Time (s)": train_time,
        "Prediction Time (s)": predict_time,
    }
    for key, value in metrics.items():
        print(f"\t{key}: {value}")
    timed_results.append(metrics)
    print("==============================")

    # Collect ROC curve data
    if y_prob is not None:
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        roc_data[model_name] = (fpr, tpr, roc_auc)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=model.classes_ if hasattr(model, "classes_") else [0, 1],
    )
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f"Confusion Matrix: {model_name}")
    plt.show()

# Convert results to DataFrame
timed_results_df = pd.DataFrame(timed_results)

# Plot ROC curves for all models
plt.figure(figsize=(10, 8))
for model_name, roc_values in roc_data.items():
    fpr, tpr, roc_auc = roc_values
    plt.plot(fpr, tpr, label=f"{model_name} (AUC = {roc_auc:.6f})")
plt.plot([0, 1], [0, 1], "k--", lw=2, label="Random Guess")
plt.title("ROC Curve Comparison")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.show()

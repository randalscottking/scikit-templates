from sklearn.preprocessing import OrdinalEncoder

X, y = diamonds.drop("cut", axis=1), diamonds[["cut"]]

# Encode y to numeric
y_encoded = OrdinalEncoder().fit_transform(y)

# Extract text features
cats = X.select_dtypes(exclude=np.number).columns.tolist()

# Convert to pd.Categorical
for col in cats:
    X[col] = X[col].astype("category")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, random_state=1, stratify=y_encoded
)

import pickle 
import numpy as np
import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_excel(r'C:\Users\USER\Desktop\Replenishment\Testset.xlsx')

# new_df = df.copy()
with open(r"C:\Users\USER\Desktop\Replenishment\Replenishment_pickle.pkl", 'rb') as file:
    file = pickle.load(file)

# cat_features = df.select_dtypes(include=['object']).columns
# num_features = df.select_dtypes(include=['int64', 'float64']).columns

# # Initialize label encoders for each categorical feature
# label_encoders = {col: LabelEncoder() for col in cat_features}
encoder = file['encoders']
model = file['model']

cat_features = ['transaction_name', 'sku_number']

# Encode the categorical features
for col in cat_features:
    df[col] = encoder[col].fit_transform(df[col])

# # Combine the numerical and encoded categorical features
# dataset_preprocessed = pd.concat([new_df[cat_features], new_df[num_features]], axis=1)

# feature scaling
# Scale the features
scaler = StandardScaler()
X_test = scaler.fit_transform(df)

y_pred = model.predict(X_test)

# Convert predictions to int to ignore float values 
y_pred = y_pred.astype(int)

# Append the formatted predictions to the original DataFrame
df['transaction_quantity'] = y_pred
print(df)


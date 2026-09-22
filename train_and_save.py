import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesClassifier
from imblearn.over_sampling import SMOTE

# 1. Load Data
df = pd.read_csv("liver_disease.csv", encoding_errors="ignore")
new_df = df.dropna().copy()

# 2. Gender Mapping
new_df["Gender of the patient"] = new_df["Gender of the patient"].map({"Male": 1, "Female": 0})
new_df.drop_duplicates(inplace=True)


feature_cols = [
    'Age of the patient',
    'Total Bilirubin',
    'Direct Bilirubin',
    'Alkphos Alkaline Phosphotase',
    'Sgpt Alamine Aminotransferase',
    'Sgot Aspartate Aminotransferase',
    'Total Protiens',
    'ALB Albumin',
    'A/G Ratio Albumin and Globulin Ratio'
]

scaler = StandardScaler()
new_df[feature_cols] = scaler.fit_transform(new_df[feature_cols])


X = new_df.drop("Result", axis=1)
y = new_df["Result"]


smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)


model = ExtraTreesClassifier(n_estimators=200, random_state=42)
model.fit(X_resampled, y_resampled)


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model aur Scaler saved!")



# ============================================
# PHASE 4 — MODÉLISATION (Baseline)
# Logistic Regression
# ============================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# --------------------------------------------
# Chargement des données issues de la phase 3
# --------------------------------------------
X_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/X_train_phase3.csv"
Y_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/y_train_phase3.csv"

X = pd.read_csv(X_PATH)
y = pd.read_csv(Y_PATH).squeeze()  # contenu en Series

# --------------------------------------------
# Split train / validation
# --------------------------------------------
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------------------
# Entraînement du modèle
# --------------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --------------------------------------------
# Évaluation
# --------------------------------------------
y_pred = model.predict(X_val)

accuracy = accuracy_score(y_val, y_pred)
print(f"Accuracy : {accuracy:.3f}\n")

print("Classification report :")
print(classification_report(y_val, y_pred))

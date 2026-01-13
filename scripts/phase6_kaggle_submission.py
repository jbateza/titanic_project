




# ============================================
# PHASE 5 — AMÉLIORATION & COMPARAISON MODÈLES
# Objectif : aller au-delà du baseline (Phase 4)
# ============================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score


# --------------------------------------------
# 1) Chargement des datasets issus de la Phase 3
# --------------------------------------------
X_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/X_train_phase3.csv"
Y_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/y_train_phase3.csv"

# ============================================
# PHASE 6 — GÉNÉRATION DE LA SOUMISSION KAGGLE
# ============================================

import pandas as pd
from sklearn.linear_model import LogisticRegression

# --------------------------------------------
# 1) Charger les données
# --------------------------------------------
TRAIN_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/train.csv"
TEST_PATH = "C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/test.csv"

train_df = pd.read_csv(TRAIN_PATH)
test_df = pd.read_csv(TEST_PATH)

# --------------------------------------------
# 2) PREPROCESSING (copie de la Phase 3)
# --------------------------------------------
def preprocess(df):
    df = df.copy()

    # Colonnes conservées
    cols = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    df = df[cols]

    # Valeurs manquantes
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    # Encodage
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

    # Feature engineering
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

    return df


# --------------------------------------------
# 3) Appliquer le preprocessing
# --------------------------------------------
X_train = preprocess(train_df)
y_train = train_df["Survived"]

X_test = preprocess(test_df)

# S'assurer que les colonnes sont identiques
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# --------------------------------------------
# 4) Entraîner le modèle final
# --------------------------------------------
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# --------------------------------------------
# 5) Prédictions avec seuil 0.5
# --------------------------------------------
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= 0.5).astype(int)

# --------------------------------------------
# 6) Création du fichier submission.csv
# --------------------------------------------
submission = pd.DataFrame({
    "PassengerId": test_df["PassengerId"],
    "Survived": y_pred
})

submission.to_csv("C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/submission.csv", index=False)

print("✅ submission.csv généré avec succès")
print(submission.head())

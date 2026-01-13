




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


X = pd.read_csv(X_PATH)
y = pd.read_csv(Y_PATH).squeeze()  # Series


# --------------------------------------------
# 2) Split train / validation (même split pour tout comparer)
# --------------------------------------------
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------
# Utilitaire : évaluer un modèle proprement
# --------------------------------------------
def evaluate_model(model, X_val, y_val, y_pred, label: str):
    """
    Calcule quelques métriques clés et affiche un rapport.
    On suit particulièrement le recall sur la classe 1 (survivants).
    """
    acc = accuracy_score(y_val, y_pred)
    rec1 = recall_score(y_val, y_pred, pos_label=1)
    f1_1 = f1_score(y_val, y_pred, pos_label=1)

    print(f"\n================ {label} ================")
    print(f"Accuracy : {acc:.3f}")
    print(f"Recall (classe 1 - survivants) : {rec1:.3f}")
    print(f"F1-score (classe 1 - survivants) : {f1_1:.3f}\n")
    print(classification_report(y_val, y_pred))

    return {
        "model": label,
        "accuracy": round(acc, 3),
        "recall_1": round(rec1, 3),
        "f1_1": round(f1_1, 3),
    }


# --------------------------------------------
# PHASE 5.1 — Logistic Regression baseline + interprétation
# --------------------------------------------
def phase5_1_logreg_baseline():
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    results = evaluate_model(model, X_val, y_val, y_pred, "LogReg baseline")

    # Interprétation : coefficients
    coefs = pd.Series(model.coef_[0], index=X.columns).sort_values(ascending=False)

    print("\nTop 10 variables qui augmentent la survie :")
    print(coefs.head(10))

    print("\nTop 10 variables qui diminuent la survie :")
    print(coefs.tail(10))

    return results, model, coefs


# --------------------------------------------
# PHASE 5.2 — Logistic Regression équilibrée + test de seuil
# --------------------------------------------
def phase5_2_logreg_balanced_threshold():
    # Version balanced : aide souvent quand la classe 1 est moins bien détectée
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train, y_train)

    # Probabilité d'être survivant (classe 1)
    y_proba = model.predict_proba(X_val)[:, 1]

    # Tester plusieurs seuils
    thresholds = [0.4, 0.5, 0.6]
    all_results = []

    for t in thresholds:
        y_pred = (y_proba >= t).astype(int)
        res = evaluate_model(model, X_val, y_val, y_pred, f"LogReg balanced (threshold={t})")
        all_results.append(res)

    return all_results, model


# --------------------------------------------
# PHASE 5.3 — RandomForest (modèle non linéaire)
# --------------------------------------------
def phase5_3_random_forest():
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    results = evaluate_model(model, X_val, y_val, y_pred, "RandomForest")

    # Feature importance
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nTop 10 importances RandomForest :")
    print(importances.head(10))

    return results, model, importances


# --------------------------------------------
# PHASE 5.4 — Résumé final (tableau)
# --------------------------------------------
def summary_table(results_list):
    df_results = pd.DataFrame(results_list).sort_values(by=["recall_1", "f1_1", "accuracy"], ascending=False)
    print("\n================ RÉSUMÉ PHASE 5 ================")
    print(df_results)
    return df_results


def main():
    all_results = []

    # 5.1 Logistic Regression baseline + coefficients
    res_lr, model_lr, coefs_lr = phase5_1_logreg_baseline()
    all_results.append(res_lr)

    # 5.2 Logistic Regression balanced + seuils
    res_balanced_list, model_balanced = phase5_2_logreg_balanced_threshold()
    all_results.extend(res_balanced_list)

    # 5.3 RandomForest + importances
    res_rf, model_rf, importances_rf = phase5_3_random_forest()
    all_results.append(res_rf)

    # 5.4 Résumé final
    summary_table(all_results)


if __name__ == "__main__":
    main()

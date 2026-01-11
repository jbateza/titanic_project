import pandas as pd

# ============================================
# PHASE 1 — EXPLORATION DES DONNÉES TITANIC
# ============================================

# 🟢 ÉTAPE 1 — Charger & inspecter
#
# 🎯 Objectif :
# Comprendre la structure du dataset Titanic
#
# À faire :
# 1️⃣ Charger train.csv avec pandas
# 2️⃣ Afficher les 5 premières lignes
# 3️⃣ Afficher :
#    - le nombre de lignes
#    - le nombre de colonnes
# 4️⃣ Examiner les types des colonnes (.info())
# 5️⃣ Identifier les colonnes avec valeurs manquantes
#
# 📌 Questions à se poser :
# - Quelles colonnes ont des valeurs manquantes ?
# - Les valeurs manquantes sont-elles nombreuses ou rares ?
# - Quelles colonnes semblent numériques ? catégorielles ?

DATA_PATH = r"C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/train.csv"


# --------------------------------------------
# FONCTION — Charger le dataset
# --------------------------------------------
def load_dataset(path: str) -> pd.DataFrame:
    # 1️⃣ Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(path)
    return df


# --------------------------------------------
# FONCTION — Inspection du dataset
# --------------------------------------------
def inspect_dataset(df: pd.DataFrame) -> None:
    # 2️⃣ Afficher les 5 premières lignes
    print("=== Aperçu des données (head) ===")
    print(df.head(), "\n")

    # 3️⃣ Afficher le nombre de lignes et de colonnes
    print("=== Dimensions du dataset ===")
    print(f"Nombre de lignes : {df.shape[0]}")
    print(f"Nombre de colonnes : {df.shape[1]}\n")

    # 4️⃣ Examiner les types et valeurs non nulles
    print("=== Types & valeurs non nulles ===")
    df.info()

    # 5️⃣ Identifier les colonnes avec valeurs manquantes
    print("\n=== Valeurs manquantes par colonne ===")
    print(df.isna().sum())

    print("\n=== Pourcentage de valeurs manquantes ===")
    print((df.isna().mean() * 100).round(2),"\n")





# 🟢 ÉTAPE 2 — Statistiques descriptives
#
# 🎯 Objectif :
# Obtenir les premiers chiffres globaux du dataset
#
# À faire :
# 1️⃣ Afficher les statistiques globales avec .describe()
# 2️⃣ Calculer :
#    - la moyenne de Age
#    - la moyenne de Fare
#    - la médiane de Fare
# 3️⃣ Comparer ces résultats avec ceux obtenus en Python pur
#
# 📌 Questions à se poser :
# - Les moyennes sont-elles proches ?
# - Pourquoi la médiane de Fare est-elle différente de la moyenne ?
# - Que dit cela sur la distribution de Fare ?


def stat_descriptive(df: pd.DataFrame) -> None:
    # 1️⃣ Statistiques globales
    print("=== Statistiques descriptives globales ===")
    print(df.describe(), "\n")

    # 2️⃣ Statistiques ciblées
    age_mean = df["Age"].mean()
    fare_mean = df["Fare"].mean()
    fare_median = df["Fare"].median()

    print("=== Statistiques ciblées ===")
    print(f"Âge moyen : {round(age_mean, 2)} ans")
    print(f"Prix moyen du billet (Fare) : {round(fare_mean, 2)}")
    print(f"Médiane du prix du billet (Fare) : {round(fare_median, 2)}")






# 🟢 ÉTAPE 3 — Valeurs manquantes
#
# 🎯 Objectif :
# Identifier les colonnes problématiques et préparer les décisions de nettoyage
#
# À faire :
# 1️⃣ Compter les valeurs manquantes par colonne
# 2️⃣ Calculer le pourcentage de valeurs manquantes
# 3️⃣ Identifier les colonnes :
#    - exploitables telles quelles
#    - à nettoyer plus tard
#    - potentiellement à supprimer
#
# 📌 Questions à se poser :
# - Quelles colonnes ont beaucoup de valeurs manquantes ?
# - Existe-t-il des colonnes presque vides ?
# - Ces colonnes sont-elles importantes pour la prédiction ?
#
# 📌 Décisions attendues (à écrire dans les notes) :
# - Colonnes à garder sans modification
# - Colonnes à imputer plus tard
# - Colonnes à supprimer ou transformer


def missing_values_analysis(df: pd.DataFrame) -> None:
    # 1️⃣ Compter les valeurs manquantes par colonne
    missing_count = df.isna().sum()

    print("=== Nombre de valeurs manquantes par colonne ===")
    print(missing_count, "\n")

    # 2️⃣ Calculer le pourcentage de valeurs manquantes
    missing_percent = (df.isna().mean() * 100).round(2)

    print("=== Pourcentage de valeurs manquantes par colonne ===")
    print(missing_percent, "\n")

    # 3️⃣ Colonnes avec valeurs manquantes (filtrage simple)
    print("=== Colonnes avec valeurs manquantes ===")
    print(missing_count[missing_count > 0])

   



#🟢 ÉTAPE 4 — Analyses ciblées (EDA métier)

#À faire :

#taux de survie global

#survie par sexe

#survie par classe

#âge moyen par survie

#👉 Utiliser groupby.

# 🟢 ÉTAPE 4 — Analyses ciblées (EDA métier)
# Objectif : répondre à des questions simples et concrètes
# sur la survie des passagers du Titanic
# --------------------------------------------------------



def etape4_analyses(df: pd.DataFrame):
    # ----------------------------------------------------
    # 1️⃣ Taux de survie global
    # ----------------------------------------------------
    # Survived est codé :
    # 0 = non survécu
    # 1 = survécu
    #
    # La moyenne d'une variable binaire correspond
    # directement à la proportion de 1
    taux_survie_global = df["Survived"].mean() * 100

    print("=== Taux de survie global ===")
    print(f"{taux_survie_global:.2f} %\n")

    # ----------------------------------------------------
    # 2️⃣ Taux de survie par sexe
    # ----------------------------------------------------
    # groupby("Sex") :
    # - sépare le dataset en groupes (male / female)
    # mean() sur Survived :
    # - calcule le taux de survie par groupe
    survie_par_sexe = (df.groupby("Sex")["Survived"].mean().mul(100))

    print("=== Taux de survie par sexe ===")
    print(survie_par_sexe, "\n")

    # ----------------------------------------------------
    # 3️⃣ Taux de survie par classe
    # ----------------------------------------------------
    # Même logique que pour le sexe
    survie_par_classe = (df.groupby("Pclass")["Survived"].mean().mul(100))

    print("=== Taux de survie par classe ===")
    print(survie_par_classe, "\n")

    # ----------------------------------------------------
    # 4️⃣ Âge moyen selon la survie
    # ----------------------------------------------------
    # On ignore automatiquement les âges manquants (NaN)
    age_moyen_par_survie = (df.groupby("Survived")["Age"].mean())

    print("=== Âge moyen selon la survie ===")
    print(age_moyen_par_survie, "\n")








# --------------------------------------------
# MAIN — Orchestration
# --------------------------------------------
def main():
    # Charger le dataset une seule fois
    df_train = load_dataset(DATA_PATH)

    # Étape 1 — Inspection
    #inspect_dataset(df_train)

    # Étape 2 — Statistiques descriptives
    #stat_descriptive(df_train)

    # Étape 3 — Valeurs manquantes
    missing_values_analysis(df_train)

    # Lancer l'étape 4
    etape4_analyses(df_train)


if __name__ == "__main__":
    main()

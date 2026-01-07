# ============================================
# PHASE 1 — EXPLORATION DES DONNÉES TITANIC
# Objectif : compréhension des données brutes
# ============================================

import csv

# Chemins vers les fichiers (train = phase 1 principale)
DATA_PATH = r"C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/train.csv"
DATA_PATH1 = r"C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/test.csv"
DATA_PATH2 = r"C:/Users/junio/OneDrive/Documents/PythonLearning/titanic_project/data/gender_submission.csv"


# --------------------------------------------
# FONCTION UTILITAIRE — Lecture du CSV
# --------------------------------------------
def read_csv(path: str):
    """
    Lit un fichier CSV et retourne :
    - rows : liste de dictionnaires (1 dict = 1 passager)
    - fieldnames : noms des colonnes
    """
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)  # utilise la première ligne comme header
        rows = list(reader)
        return rows, reader.fieldnames


# --------------------------------------------
# ÉTAPE 1 — Chargement & structure des données
# Objectif :
# - vérifier que les données sont lisibles
# - comprendre le nombre de lignes et de colonnes
# --------------------------------------------
def run_etape1(rows, cols):
    print("Nombre de lignes (passagers) :", len(rows))
    print("Nombre de colonnes (variables) :", len(cols))
    print("Colonnes :", cols)

    # Vérification simple : PassengerId non vide
    nb_passenger_id = sum(1 for row in rows if row["PassengerId"] != "")
    # (optionnel) print("PassengerId non vides :", nb_passenger_id)


# --------------------------------------------
# ÉTAPE 2 — Types de variables
# Objectif :
# - identifier les colonnes avec valeurs manquantes
# - cette étape sert surtout à alimenter les NOTES
# --------------------------------------------
def count_missing(rows, cols):
    """
    Compte le nombre de valeurs manquantes par colonne.
    Une valeur est considérée manquante si vide ou None.
    """
    missing = {col: 0 for col in cols}

    for row in rows:
        for col in cols:
            if row[col] == "" or row[col] is None:
                missing[col] += 1

    return missing


def run_etape2(rows, cols):
    count = count_missing(rows, cols)
    print("Nombre de valeurs manquantes par colonne :")
    print(count)


# --------------------------------------------
# ÉTAPE 3 — Valeurs manquantes (pourcentages)
# Objectif :
# - quantifier la “saleté” des données
# - préparer les décisions de nettoyage futures
# --------------------------------------------
def missing_percentages(missing_counts, n_rows):
    """
    Convertit des comptes de valeurs manquantes
    en pourcentages par rapport au nombre total de lignes.
    """
    pct = {}
    for col, count in missing_counts.items():
        pct[col] = (count / n_rows * 100) if n_rows > 0 else 0.0
    return pct


def run_etape3(rows, cols):
    # On réutilise le comptage de l'étape 2
    count = count_missing(rows, cols)
    pourcentage = missing_percentages(count, len(rows))

    print("Pourcentage de valeurs manquantes par colonne :")
    print({k: round(v, 2) for k, v in pourcentage.items()})


# --------------------------------------------
# ÉTAPE 4 — Statistiques simples (globales)
# Objectif :
# - extraire les premiers chiffres clés
# - sans modèle, sans visualisation
# --------------------------------------------
def taux_survie(rows):
    """
    Calcule le taux de survie global (%) sur le dataset.
    """
    total = len(rows)
    survivants = 0

    for row in rows:
        if row.get("Survived", "") == "1":
            survivants += 1

    return (survivants / total) * 100 if total else 0.0


def age_moyen(rows):
    """
    Calcule l'âge moyen en ignorant les valeurs manquantes.
    """
    ages = [float(row["Age"]) for row in rows if row.get("Age", "") != ""]
    return sum(ages) / len(ages) if ages else None


def prix_moyen_par_classe(rows):
    """
    Calcule le prix moyen du billet par classe (Pclass).
    """
    totaux = {}
    comptes = {}

    for row in rows:
        classe = row.get("Pclass", "")
        fare = row.get("Fare", "")

        if fare != "" and classe != "":
            totaux[classe] = totaux.get(classe, 0) + float(fare)
            comptes[classe] = comptes.get(classe, 0) + 1

    return {c: round(totaux[c] / comptes[c], 2) for c in totaux}


# --------------------------------------------
# ÉTAPE 5 — Comparaisons simples
# Objectif :
# - tester des hypothèses simples (sexe, classe)
# --------------------------------------------
def survie_par_sexe_et_par_classe(rows):
    """
    Calcule le taux de survie (%) :
    - par sexe
    - par classe
    """
    survivants_sexe = {}
    survivants_classe = {}
    totaux_sexe = {}
    totaux_classe = {}

    for row in rows:
        sexe = row.get("Sex", "")
        survie = row.get("Survived", "")
        classe = row.get("Pclass", "")

        if sexe != "":
            totaux_sexe[sexe] = totaux_sexe.get(sexe, 0) + 1
        if classe != "":
            totaux_classe[classe] = totaux_classe.get(classe, 0) + 1

        if survie == "1":
            if sexe != "":
                survivants_sexe[sexe] = survivants_sexe.get(sexe, 0) + 1
            if classe != "":
                survivants_classe[classe] = survivants_classe.get(classe, 0) + 1

    taux_sexe = {}
    taux_classe = {}

    for sexe in totaux_sexe:
        taux_sexe[sexe] = round(
            (survivants_sexe.get(sexe, 0) / totaux_sexe[sexe]) * 100, 2
        )

    for classe in totaux_classe:
        taux_classe[classe] = round(
            (survivants_classe.get(classe, 0) / totaux_classe[classe]) * 100, 2
        )

    return taux_sexe, taux_classe


def run_etape4(rows, cols):
    """
    Lance les calculs des étapes 4 et 5
    et affiche les résultats.
    """
    taux = taux_survie(rows)
    age = age_moyen(rows)
    prix = prix_moyen_par_classe(rows)
    taux_sexe, taux_classe = survie_par_sexe_et_par_classe(rows)

    print(f"Taux de survie global : {round(taux, 2)} %")
    print(f"Âge moyen : {round(age, 2)} ans" if age is not None else "Âge moyen : N/A")
    print(f"Prix moyen du billet par classe : {prix}")
    print("")
    print(f"Taux de survie par sexe (%) : {taux_sexe}")
    print(f"Taux de survie par classe (%) : {taux_classe}")


# --------------------------------------------
# MAIN — Orchestration des étapes
# --------------------------------------------
def main():
    fichiers = [
        ("TRAIN.CSV", DATA_PATH),
        ("TEST.CSV", DATA_PATH1),
        ("GENDER_SUBMISSION.CSV", DATA_PATH2),
    ]

    for nom, path in fichiers:
        print(f"\n================ {nom} ================")

        rows, cols = read_csv(path)

        print("=== étape 1 ===")
        run_etape1(rows, cols)
        print("")

        print("=== étape 2 ===")
        run_etape2(rows, cols)
        print("")

        print("=== étape 3 ===")
        run_etape3(rows, cols)
        print("")

        print("=== étape 4 & 5 ===")
        run_etape4(rows, cols)
        print("")
if __name__ == "__main__":
    main()

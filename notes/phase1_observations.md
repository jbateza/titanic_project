# Phase 1 — Exploration des données Titanic

## Fichiers analysés
- `train.csv` (dataset d’entraînement : contient la cible `Survived`)
- `test.csv` (dataset de test : ne contient pas `Survived`)
- `gender_submission.csv` (fichier de soumission baseline : contient seulement `PassengerId` et `Survived`)

---

# ✅ TRAIN.CSV

## Étape 1 — Structure du dataset
- Nombre de passagers (lignes) : **891**
- Nombre de variables (colonnes) : **12**
- Colonnes : PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

Description :
- 1 ligne = 1 passager.
- `Survived` est la variable cible (0/1).
- Mélange de variables :
  - numériques : Age, Fare, SibSp, Parch, Pclass (ordinale)
  - catégorielles : Sex, Embarked
  - textuelles / identifiants : Name, Ticket, Cabin (semi-textuel)

## Étape 2 — Types de variables (réflexion humaine)
🧍‍♂️ Survived  
- Type : numérique  
- Nature : discrète (binaire)  
- Valeurs : {0, 1}  
- Valeurs manquantes : ❌ non  
➡️ Catégorielle encodée en numérique.

🎟️ Pclass  
- Type : numérique  
- Nature : discrète (ordinale)  
- Valeurs : {1, 2, 3}  
- Valeurs manquantes : ❌ non  
➡️ Attention : ordinale (hiérarchie), pas une mesure.

🚻 Sex  
- Type : catégorielle  
- Nature : nominale  
- Valeurs : {male, female}  
- Valeurs manquantes : ❌ non

🎂 Age  
- Type : numérique  
- Nature : continue  
- Valeurs manquantes : ✅ oui  
➡️ Variable importante mais incomplète.

💰 Fare  
- Type : numérique  
- Nature : continue  
- Valeurs manquantes : ❌ non (dans train.csv)

🚢 Embarked  
- Type : catégorielle  
- Nature : nominale  
- Valeurs : {C, Q, S}  
- Valeurs manquantes : ✅ oui (rare)

(Autres colonnes)
- Cabin : très manquante, probablement difficile à exploiter directement.
- Name / Ticket : textuelles → utiles pour feature engineering (titres, groupes, etc.) mais pas en phase 1.

## Étape 3 — Valeurs manquantes (chiffres + interprétation)
Comptes :
- Age manquant : **177 / 891**
- Embarked manquant : **2 / 891**
- Cabin manquant : **687 / 891**

Pourcentages :
- Age : **19.87%**
- Embarked : **0.22%**
- Cabin : **77.10%**

Interprétation :
- `Age` : ~20% manquant → il faudra une stratégie d’imputation (médiane globale ou par groupes Sex/Pclass).
- `Embarked` : très peu de manquants → imputation simple (mode) ou catégorie “Unknown”.
- `Cabin` : très fortement manquante → soit suppression, soit création d’une variable “Cabin renseigné (oui/non)”, soit extraction de la lettre du pont pour les rares valeurs.

## Étape 4 — Statistiques globales (chiffres clés + méthode)
- Taux de survie global : **38.38%**
- Âge moyen (sans âges manquants) : **29.7 ans**
- Prix moyen du billet par classe :
  - Classe 1 : **84.15**
  - Classe 2 : **20.66**
  - Classe 3 : **13.68**

Méthode :
- Âge moyen calculé en ignorant les valeurs manquantes.
- Prix moyen calculé par classe via accumulation (boucles + compteurs).

## Étape 5 — Comparaisons & hypothèses (résultats + interprétation)
Survie par sexe :
- male : **18.89%**
- female : **74.20%**

➡️ Hypothèse confirmée : les femmes survivent beaucoup plus que les hommes (fort pouvoir explicatif).

Survie par classe :
- Pclass 1 : **62.96%**
- Pclass 2 : **47.28%**
- Pclass 3 : **24.24%**

➡️ Hypothèse confirmée : la survie diminue avec la classe → dimension socio-économique forte.

Conclusion train.csv :
- Variables très informatives en phase 1 : **Sex, Pclass, Fare, (Age après imputation), Embarked**
- Problèmes data majeurs : **Age manquant (~20%), Cabin manquant (~77%)**, variables textuelles à transformer.

---

# ✅ TEST.CSV

## Étape 1 — Structure du dataset
- Nombre de passagers : **418**
- Nombre de variables : **11**
- Colonnes : PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
➡️ `Survived` est absent (normal : c’est le dataset de test Kaggle).

## Étape 3 — Valeurs manquantes (chiffres + interprétation)
Comptes :
- Age manquant : **86 / 418**
- Fare manquant : **1 / 418**
- Cabin manquant : **327 / 418**
- Embarked manquant : **0 / 418**

Pourcentages :
- Age : **20.57%**
- Fare : **0.24%**
- Cabin : **78.23%**
- Embarked : **0.00%**

Interprétation :
- Les patterns sont proches de train : `Age` et surtout `Cabin` manquants.
- `Fare` a 1 valeur manquante → imputation simple plus tard (médiane / moyenne selon Pclass).

## Étape 4 & 5 — Remarque importante
Le script affiche :
- Taux de survie global : **0.0%**
- Survie par sexe/classe : **0.0%**

➡️ Ce résultat ne reflète PAS la réalité : `test.csv` ne contient pas la colonne `Survived`.  
Le 0% vient du fait que le code utilise `row.get("Survived", "")`, donc aucun passager n’est compté comme survivant.

---

# ✅ GENDER_SUBMISSION.CSV

## Étape 1 — Structure du dataset
- Nombre de lignes : **418**
- Nombre de variables : **2**
- Colonnes : PassengerId, Survived

➡️ C’est un fichier baseline (format de soumission), pas un dataset complet.

## Étape 4 — Statistiques globales
- Taux de survie global dans ce fichier : **36.36%**
- Age : **N/A** (colonne absente)
- Fare : {} (colonnes absentes)
- Comparaisons (Sex/Pclass) : {} (colonnes absentes)

Interprétation :
- Ce fichier sert uniquement à fournir des prédictions “baseline” associées à PassengerId.
- On ne peut pas faire d’analyse descriptive dessus car il manque toutes les variables explicatives.

---

## Conclusion générale (Phase 1)
- `train.csv` est le seul fichier permettant une analyse complète survie + variables.
- `test.csv` présente une structure proche mais sans `Survived` et avec des manquants similaires (Age, Cabin).
- `gender_submission.csv` est un fichier de soumission minimal (PassengerId + Survived), non exploitable pour EDA des variables.

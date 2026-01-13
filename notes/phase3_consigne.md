# PHASE 3 — Feature Engineering (Titanic)

## Objectif de la phase 3

Transformer les données brutes issues de `train.csv` en un dataset :
- propre (sans valeurs manquantes),
- entièrement numérique,
- explicable,
- prêt à être utilisé par un modèle de machine learning.

Cette phase vise à montrer la capacité à prendre des décisions data,
à les justifier, et à créer des variables pertinentes métier.

---

## Fichier de travail

- Environnement : **Jupyter Notebook (VS Code)**
- Fichier : `phase3_feature_engineering.ipynb`
- Données source : `data/train.csv`
- Documentation des décisions : `notes/phase3_decisions.md`

---

## 🟢 ÉTAPE 1 — Chargement et inspection des données

### À faire
- Charger `train.csv` avec pandas.
- Afficher les premières lignes.
- Examiner la structure du dataset (`info()`).
- Identifier les colonnes contenant des valeurs manquantes.

### Objectif
Vérifier que les données sont correctement chargées et comprendre leur structure
avant toute transformation.

---

## 🟢 ÉTAPE 2 — Sélection des colonnes utiles

### À faire
À partir de `train.csv`, décider :

#### Colonnes à conserver
- Survived (cible)
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

#### Colonnes à supprimer
- PassengerId
- Name
- Ticket
- Cabin

### Objectif
Réduire le bruit, supprimer les variables non exploitables en l’état
et préparer un dataset orienté modélisation.

### Exigence
Chaque suppression ou conservation doit être **justifiée dans `phase3_decisions.md`**.

---

## 🟢 ÉTAPE 3 — Traitement des valeurs manquantes

### À faire
- Remplacer les valeurs manquantes de `Age` par la **médiane**.
- Remplacer les valeurs manquantes de `Embarked` par la **valeur la plus fréquente**.
- Vérifier qu’il ne reste plus aucune valeur manquante.

### Objectif
Garantir un dataset complet, compatible avec les algorithmes de machine learning.

### Exigence
Justifier les choix d’imputation dans `phase3_decisions.md`.

---

## 🟢 ÉTAPE 4 — Encodage des variables catégorielles

### À faire
- Transformer `Sex` en variable numérique binaire.
- Encoder `Embarked` via one-hot encoding (`get_dummies()`).
- Conserver `Pclass` comme variable numérique ordinale.

### Objectif
Transformer toutes les variables en format numérique tout en respectant leur nature
(catégorielle nominale vs ordinale).

### Exigence
Comparer encodage manuel et one-hot encoding dans l’explication écrite.

---

## 🟢 ÉTAPE 5 — Création de nouvelles variables (Feature Engineering)

### À faire
Créer au minimum les variables suivantes :

- **FamilySize** = SibSp + Parch + 1
- **IsAlone** = 1 si FamilySize = 1, sinon 0
- **FarePerPerson** = Fare / FamilySize

### Objectif
Créer des variables dérivées plus informatives que les données brutes,
basées sur une intuition métier explicable.

### Exigence
Expliquer l’intuition derrière chaque variable dans `phase3_decisions.md`.

---

## 🟢 Dataset final attendu

À la fin de la phase 3 :
- aucune valeur manquante,
- uniquement des variables numériques,
- séparation claire entre :
  - `X` : variables explicatives
  - `y` : variable cible (`Survived`)

### Vérifications attendues
- `df.isna().sum()`
- `X.dtypes`
- `X.shape` et `y.shape`

---

## 📦 Livrables de la phase 3

À l’issue de cette phase, le projet doit contenir :

1. Un notebook Jupyter clair et structuré.
2. Un dataset propre et prêt pour la modélisation.
3. Un fichier `phase3_decisions.md` documentant toutes les décisions.
4. Des features explicables et défendables en entretien.

---

## Transition vers la phase 4

La phase 4 consistera à :
- entraîner un premier modèle baseline,
- évaluer ses performances,
- interpréter les résultats.

➡️ La phase 3 doit être **entièrement terminée et validée** avant de commencer la phase 4.

## Étape 1 — Chargement et inspection
- Dataset chargé avec succès dans VS Code via Jupyter.
- 891 lignes, 12 colonnes.
- Valeurs manquantes sur Age, Cabin, Embarked.



## Étape 2 — Sélection des variables
- Réduction du dataset à 8 variables pertinentes.
- Suppression des colonnes textuelles et fortement manquantes.
- Dataset plus simple et orienté modélisation.


## Étape 3 — Valeurs manquantes
- Age rempli par la médiane (choix robuste).
- Embarked rempli par la valeur la plus fréquente (mode).
- Contrôle final : aucun NaN restant.


# Étape 4 — Encodage des variables catégorielles

Les variables catégorielles ont été transformées afin d’être compatibles avec les modèles de machine learning.

- Sex : encodage manuel (male = 0, female = 1).

    Variable binaire simple et interprétable.

- Embarked : encodage one-hot via get_dummies().

    Évite d’introduire un ordre artificiel entre les catégories.

- Pclass : conservée comme variable numérique.

    Variable ordinale dont l’ordre (1 < 2 < 3) a un sens métier.

À l’issue de cette étape, le dataset ne contient que des variables numériques.


Étape 5 — Création de nouvelles variables

L’objectif de cette étape est d’enrichir le dataset avec des variables plus informatives que les données brutes, en s’appuyant sur une intuition métier liée au contexte du Titanic.

1️⃣ FamilySize

Définition :
FamilySize = SibSp + Parch + 1

Justification :
Cette variable représente le nombre total de personnes voyageant ensemble pour un passager donné.
Voyager seul, en petit groupe ou en grande famille peut influencer les comportements lors de l’évacuation et donc les chances de survie.

Cette variable permet de capturer un effet non linéaire difficile à observer avec SibSp et Parch séparément.

2️⃣ IsAlone

Définition :
IsAlone = 1 si FamilySize = 1, sinon 0

Justification :
Les passagers voyageant seuls peuvent être désavantagés lors d’un événement de crise, notamment en l’absence d’entraide familiale.
Cette variable binaire isole explicitement cet effet et simplifie son exploitation par les modèles.

3️⃣ FarePerPerson

Définition :
FarePerPerson = Fare / FamilySize

Justification :
Le prix total du billet ne reflète pas toujours le niveau de confort réel par passager, en particulier pour les familles.
Cette variable fournit une mesure plus fine du statut économique individuel, complémentaire à Pclass.









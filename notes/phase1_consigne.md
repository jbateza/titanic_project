PHASE 1 — PLAN DE TRAVAIL CONCRET (EXERCICES)

On commence uniquement avec train.csv.

🟢 ÉTAPE 1 — Charger et comprendre la structure
🎯 Objectif

Vérifier que tu sais lire le fichier et comprendre ses colonnes.

À faire

Ouvrir train.csv avec csv.reader

Lire l’en-tête

Afficher :

le nombre de colonnes

les noms des colonnes

Compter le nombre de lignes (passagers)

📌 Questions à noter dans phase1_observations.md :

Combien de passagers ?

Combien de variables ?

🟢 ÉTAPE 2 — Identifier les types de variables
🎯 Objectif

Comprendre la nature des données.

À faire (sans automatisme)

Pour chaque colonne principale :

Survived

Pclass

Sex

Age

Fare

Embarked

👉 Écris pour chacune :

numérique / catégorielle

continue / discrète

présence de valeurs manquantes (oui / non)

📌 Exercice écrit, pas du code.

🟢 ÉTAPE 3 — Valeurs manquantes (clé data analyst)
🎯 Objectif

Identifier les colonnes “sales”.

À faire

Parcourir toutes les lignes

Compter :

nombre de valeurs manquantes pour Age

nombre de valeurs manquantes pour Embarked

Calculer le pourcentage de valeurs manquantes

📌 Question :

Est-ce acceptable ?

Que pourrait-on faire plus tard ?

🟢 ÉTAPE 4 — Statistiques simples (sans pandas)
🎯 Objectif

Premiers chiffres clés.

À faire

Calculer :

taux de survie global

nombre de survivants

nombre de non-survivants

âge moyen (en ignorant les âges manquants)

prix moyen du billet (Fare)

📌 Note :

comment as-tu géré les valeurs manquantes ?

🟢 ÉTAPE 5 — Comparaisons simples (logique data)
🎯 Objectif

Tester tes hypothèses de la phase 0.

À faire

Calculer :

taux de survie des hommes

taux de survie des femmes

taux de survie par classe (Pclass)

👉 Toujours :

avec des boucles

avec des compteurs

sans pandas
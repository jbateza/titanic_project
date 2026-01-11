# Phase 1 — Exploration des données Titanic


## Étape 1 — Structure du dataset


## Étape 2 — Types de variables (réflexion humaine)


## Étape 3 — Valeurs manquantes (chiffres + interprétation)
La colonne Cabin contient plus de 75% de valeurs manquantes, ce qui la rend difficile à exploiter directement. Elle sera soit supprimée, soit transformée en variable binaire (“Cabin renseignée ou non”).

La colonne Age présente environ 20% de valeurs manquantes. Étant une variable importante, elle sera imputée ultérieurement (médiane globale ou médiane par groupes).


La colonne Embarked contient très peu de valeurs manquantes (<1%) et pourra être imputée simplement avec la modalité la plus fréquente.

## Étape 4 — Statistiques globales (chiffres clés + méthode)


## Étape 5 — Comparaisons & hypothèses (résultats + interprétation)

🟢 ÉTAPE 5 — Insights clés (Phase 1)
Insight 1 — Le sexe est le facteur le plus discriminant de survie

Les femmes présentent un taux de survie de 74.20%, contre seulement 18.89% pour les hommes.
👉 Une femme avait donc environ 4 fois plus de chances de survivre qu’un homme, ce qui indique une priorité claire donnée aux femmes lors de l’évacuation.

Insight 2 — La classe sociale influence fortement les chances de survie

Le taux de survie décroît fortement avec la classe :

Classe 1 : 62.96%

Classe 2 : 47.28%

Classe 3 : 24.24%

👉 Un passager de première classe avait plus de 2,5 fois plus de chances de survivre qu’un passager de troisième classe, révélant un fort biais socio-économique.

Insight 3 — La majorité des passagers n’ont pas survécu

Le taux de survie global est de 38.38%, ce qui signifie que près de 62% des passagers sont décédés.
👉 Le naufrage constitue un événement à mortalité élevée, ce qui renforce l’importance des facteurs discriminants observés (sexe, classe).

Insight 4 — L’âge est une variable clé mais incomplète

L’âge moyen des passagers est de 29.7 ans, mais 19.87% des âges sont manquants.
👉 L’âge est potentiellement explicatif (enfants vs adultes), mais nécessite une imputation réfléchie avant toute modélisation pour éviter un biais.

Insight 5 — La variable Cabin est trop manquante pour une exploitation directe

La variable Cabin est manquante dans 77.10% des cas, ce qui limite fortement son utilisation brute.
👉 En revanche, une variable dérivée simple (“Cabin renseignée : oui/non”) pourrait capturer une information indirecte liée au statut social.
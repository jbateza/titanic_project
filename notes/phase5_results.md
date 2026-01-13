
# Phase 5.1 — Interprétation Logistic Regression

## Top variables (direction du modèle)
- Variables qui augmentent la survie : (copier le top 10)
- Variables qui diminuent la survie : (copier le bottom 10)

# Phase 5 — Amélioration & comparaison de modèles

## Objectif
Améliorer la baseline (Logistic Regression) et comparer plusieurs approches en suivant
prioritairement la capacité à détecter les survivants (recall sur la classe 1).

## Résumé des modèles testés
| Modèle | Accuracy | Recall (classe 1) | F1 (classe 1) |
|---|---:|---:|---:|
| LogReg baseline | 0.804 | 0.681 | 0.729 |
| LogReg balanced (threshold=0.4) | 0.777 | 0.812 | 0.737 |
| LogReg balanced (threshold=0.5) | 0.810 | 0.783 | 0.761 |
| LogReg balanced (threshold=0.6) | 0.804 | 0.696 | 0.733 |
| RandomForest | 0.804 | 0.725 | 0.741 |

## Choix final
Le modèle retenu est **Logistic Regression avec class_weight="balanced" et threshold=0.5** :
- meilleur compromis global (accuracy la plus élevée : 0.810)
- meilleur F1-score sur la classe survivants (0.761)
- recall classe 1 élevé (0.783), nettement supérieur à la baseline (0.681)

## Interprétation (cohérence métier)
- La variable **Sex** est la plus discriminante (effet fortement positif sur la survie).
- **Pclass** a un effet fortement négatif : la survie diminue lorsque la classe sociale est plus basse.
- **IsAlone** diminue la probabilité de survie : voyager seul est défavorable.
- RandomForest confirme l’importance de **Age** et des variables économiques (**Fare**, **FarePerPerson**).

## Next steps (si on continue)
- tester une standardisation des variables (scaling) pour stabiliser les coefficients de la régression logistique
- ajouter des features avancées (Title depuis Name, Deck depuis Cabin, etc.)
- générer une submission Kaggle avec le modèle retenu

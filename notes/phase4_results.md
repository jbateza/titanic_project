# Phase 4 — Modélisation (baseline)

## Modèle
- Logistic Regression
- Split : 80% train / 20% validation (stratifié)
- Taille validation : 179 passagers

## Résultats
- Accuracy : 0.804

### Détail par classe
- Non-survivants (classe 0) :
  - Precision = 0.82
  - Recall = 0.88
- Survivants (classe 1) :
  - Precision = 0.78
  - Recall = 0.68

## Interprétation
Le modèle baseline obtient une performance globale correcte (~80%).
Il identifie bien les non-survivants, mais rate une partie des survivants (recall plus faible sur la classe 1).
La suite du travail consistera à améliorer la capacité à détecter les survivants (rappel), soit par ajustement du seuil, soit via un modèle ou des features supplémentaires.




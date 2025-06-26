# devine_achat_v2

[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1h2tF3GxeMeXhcqK0z9fzLT8bD-IR9epw)

Ce projet prédit si un utilisateur va acheter un produit en fonction de son âge et de son salaire.  
L’IA apprend et s’améliore à chaque interaction avec l’utilisateur.

| Fichier              | Description                                  |
|----------------------|----------------------------------------------|
| `devine_achat.ipynb` | Notebook principal du projet                 |
| `profils_achat.csv`  | Données d'entraînement initiales             |
| `historique.csv`     | Réponses utilisateur ajoutées automatiquement |
| `README.md`          | Explication du projet                        |
| `requirements.txt`   | Dépendances nécessaires                      |

#Fonctionnement

- L’IA est entraînée sur un petit dataset initial (`profils_achat.csv`)
- L’utilisateur entre ses données ➝ l’IA prédit s’il va acheter
- L’utilisateur confirme ou corrige la prédiction
- Sa réponse est ajoutée dans `historique.csv`
- Le modèle est automatiquement mis à jour

# Exemple de prédiction

Entrez votre âge : 30
Entrez votre salaire : 35000
L’IA pense que vous achèterez.
Avez-vous acheté ? (1 = oui, 0 = non) : 1
Votre réponse a été enregistrée.

# Librairies utilisées

- `pandas`
- `numpy`
- `scikit-learn`
- `seaborn`
- `matplotlib`

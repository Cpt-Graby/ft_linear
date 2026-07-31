# ft-linear

Voici un petit projet pour découvrir ce qu'est une régression linéaire.  
Et parce que c'est pas un projet très difficile.

L'objectif : prédire le prix d'une voiture en fonction de son kilométrage, à partir d'un jeu de données `km,price`.

## Régression linéaire
```
En statistiques, un modèle de régression linéaire est un modèle de régression qui cherche à établir une relation linéaire entre une variable, dite expliquée, et une ou plusieurs variables, dites explicatives.
```
source: [https://fr.wikipedia.org/wiki/Régression_linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_(statistiques))

## Installation

```bash
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

## Programme

Le projet est composé de deux programmes :

- `main_linear.py` : entraîne le modèle sur un jeu de données et calcule les coefficients de la régression (`theta0`, `theta1`).
- `estimate_price.py` : estime le prix d'une voiture à partir de son kilométrage et des coefficients obtenus.

### Entraîner le modèle

```bash
python main_linear.py data/data.csv
```

Options :

| Option | Description | Défaut |
|---|---|---|
| `-l`, `--learning_rate` | Taux d'apprentissage de la descente de gradient | `0.01` |
| `-i`, `--iteration` | Nombre d'itérations | `1000` |

La commande affiche `beta0`/`beta1` (calculés par la méthode fermée, à titre de comparaison) ainsi que `theta0`/`theta1` (calculés par descente de gradient sur les données normalisées).

### Estimer un prix

```bash
python estimate_price.py 150000 -a <theta0> -x <theta1>
```

| Argument | Description | Défaut |
|---|---|---|
| `millage` | Kilométrage de la voiture (positionnel) | — |
| `-a`, `--theta0` | Coefficient theta0 obtenu à l'entraînement | `0.0` |
| `-x`, `--theta1` | Coefficient theta1 obtenu à l'entraînement | `0.0` |

## Format des données

Le fichier CSV doit contenir exactement deux colonnes numériques avec un en-tête, par exemple :

```csv
km,price
240000,3650
139800,3800
```

## Méthode

Deux approches sont calculées pour comparaison :

- **Méthode fermée** (`_methode_fermee`) : calcul direct des coefficients par formule analytique (régression linéaire simple).
- **Descente de gradient normalisée** (`gradient_descent_norm`) : les données sont normalisées (min-max) avant l'entraînement pour stabiliser la convergence, puis les coefficients sont dénormalisés pour revenir à l'échelle réelle (km, prix).

## Credits

Ce README est redigé par l'IA

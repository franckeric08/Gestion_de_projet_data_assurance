# Portfolio Data - Gestion de Projets Décisionnels

Ce projet est un **portfolio interactif** qui met en avant mes compétences en analyse de données, Machine Learning, et SQL, en utilisant Streamlit pour visualiser les résultats.

## Fonctionnalités

### 1. **Visualisations SQL**
- Analyse des données assurantielles avec des requêtes SQL.
- Visualisation dynamique des résultats (clients, contrats, sinistres).
- Filtres interactifs pour explorer les données par région ou type de contrat.

### 2. **Cas d’Usage Machine Learning**
- Prédiction du renouvellement des contrats en utilisant un modèle de régression logistique.
- Entrées utilisateur pour tester le modèle avec des paramètres personnalisés.
- Évaluation du modèle via des métriques (rapport de classification, matrice de confusion).

### 3. **Tableau de Bord**
- Visualisation des sinistres par région.
- Analyse des montants des contrats par type.
- Comparaison des performances des contrats.

---

## Structure du Projet

Le projet est organisé pour mettre en évidence les différentes fonctionnalités, avec des fichiers dédiés à chaque composante :

### **Fichiers Principaux**
1. **`portfolio_streamlit.py`**
   - Fichier principal pour lancer l'application Streamlit.
   - Contient la structure de l'application avec des sections dynamiques.
   - Regroupe :
     - Page d'accueil pour la présentation du portfolio.
     - Navigation entre les différentes fonctionnalités.

2. **`visualisations_SQL.py`**
   - Page dédiée aux visualisations SQL.
   - Montre des analyses basées sur des requêtes SQL avec des données fictives, telles que :
     - Analyse des sinistres par région et type.
     - Répartition des contrats par type.
   - Intègre des filtres interactifs pour personnaliser les résultats.

3. **`analyse_contrat_specifique.py`**
   - Page dédiée à l'analyse des contrats spécifiques.
   - Fonctionnalités :
     - Filtrer les contrats par région et type.
     - Afficher les détails d'un contrat sélectionné.
     - Comparer le montant annuel d'un contrat avec la moyenne générale.
   - Intégrée dans Streamlit avec des graphiques et métriques dynamiques.

4. **`reg_logistic.py`**
   - Implémente un modèle de régression logistique pour prédire le renouvellement des contrats.
   - Fonctionnalités :
     - Entraînement et évaluation d'un modèle supervisé sur les données des contrats.
     - Affichage des métriques de performance (rapport de classification, matrice de confusion).
     - Prédiction dynamique basée sur les entrées utilisateur :
       - Âge du client.
       - Montant annuel.
       - Type de contrat.
       - Région.


---

## Installation et Lancement

### **1. Cloner le dépôt**
```bash
git clone https://github.com/votre_nom_utilisateur/portfolio-data.git
cd portfolio-data

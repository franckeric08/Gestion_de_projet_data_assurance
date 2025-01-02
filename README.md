# Portfolio Data - Gestion de Projets Décisionnels

Ce projet est un **portfolio interactif** qui met en avant mes compétences en analyse de données, Machine Learning, et SQL, en utilisant Streamlit pour visualiser les résultats.

# Projet Data Décisionnel en Assurance

## Objectifs

### Automatiser l'analyse des données assurantielles :
- Identifier les contrats rentables et les zones à risque.
- Suivre les indicateurs clés de performance (KPI).

### Faciliter la prise de décision :
- Créer des tableaux de bord interactifs pour les équipes métiers.
- Mettre en évidence les tendances et anomalies dans les données.

### Prédire le comportement des clients :
- Utiliser un modèle de machine learning pour anticiper le renouvellement des contrats.

---

## Méthodologie

### Collecte et Simulation des Données :
- Données sur les clients, contrats, sinistres, et paiements.
- Organisation des données dans des tables relationnelles.

### Exploration et Analyse :
- Requêtes SQL pour extraire des insights sur les sinistres par région et par type.
- Analyse des renouvellements de contrats et des performances financières.

### Modélisation Machine Learning :
- Entraînement d’un modèle de régression logistique pour prédire le renouvellement des contrats.
- Évaluation du modèle avec des métriques (précision, rappel, matrice de confusion).

### Visualisations Interactives :
- Création de tableaux de bord avec Streamlit pour explorer les données en temps réel.
- Intégration de filtres dynamiques pour personnaliser les analyses par région, type de contrat, ou période.

---

## Résultats

### Visualisations SQL :
- Répartition des sinistres par région et type, avec identification des régions les plus coûteuses.
- Taux de renouvellement par type de contrat.

### Prédictions Machine Learning :
- Précision de 85% sur les prédictions de renouvellement des contrats.
- Mise en évidence des facteurs influençant le renouvellement, comme l'âge du client ou le montant annuel.

### Tableaux de Bord :
- Tableau de bord interactif pour les KPI décisionnels.
- Comparaison des revenus et des objectifs atteints par région.

---

## Outils et Technologies

- **SQL** : Extraction et analyse des données relationnelles.
- **Python** : Modélisation et création de l'application Streamlit.
- **Pandas & NumPy** : Manipulation et traitement des données.
- **Scikit-learn** : Machine Learning.
- **Matplotlib** : Visualisation statique.
- **Streamlit** : Tableau de bord interactif.

---

## Impact

- Automatisation des analyses assurantielles pour un gain de temps significatif.
- Identification rapide des zones à améliorer (contrats peu rentables, sinistres élevés).
- Meilleure compréhension des comportements des clients grâce aux prédictions.


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

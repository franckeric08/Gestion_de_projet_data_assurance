import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import streamlit as st

# Génération de données 
np.random.seed(42)

# Table Contrats (features et label)
contrats = pd.DataFrame({
    'id_contrat': range(1, 101),
    'age_client': np.random.randint(18, 80, size=100),
    'type_contrat': np.random.choice(['Habitation', 'Auto', 'Santé', 'Professionnel'], size=100),
    'region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], size=100),
    'montant_annuel': np.random.randint(200, 2000, size=100),
    'statut': np.random.choice(['actif', 'résilié', 'renouvelé'], size=100, p=[0.5, 0.3, 0.2])
})

# Encodage de la variable cible
contrats['label'] = contrats['statut'].apply(lambda x: 1 if x == 'renouvelé' else 0)

# Encodage des variables catégoriques
contrats_encoded = pd.get_dummies(contrats, columns=['type_contrat', 'region'], drop_first=True)

# Sélection des features et de la target
features = contrats_encoded.drop(columns=['id_contrat', 'statut', 'label'])
target = contrats_encoded['label']


#entrainement du modele

# Séparation des données en train et test
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Entraînement d'un modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Évaluation
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)


#tableau de bord

# Prédiction pour un nouvel exemple
st.subheader("Prédiction pour un Nouveau Contrat")
age_client = st.slider("Âge du Client :", 18, 80, 35)
montant_annuel = st.slider("Montant Annuel (€) :", 200, 2000, 800)
type_contrat = st.selectbox("Type de Contrat :", ['Habitation', 'Auto', 'Santé', 'Professionnel'])
region = st.selectbox("Région :", ['Nord', 'Sud', 'Est', 'Ouest'])

# Préparation des features pour la prédiction
new_data = pd.DataFrame({
    'age_client': [age_client],
    'montant_annuel': [montant_annuel],
    f'type_contrat_{type_contrat}': [1 if type_contrat != 'Habitation' else 0],
    f'region_{region}': [1 if region != 'Nord' else 0]
}, index=[0])

# Standardisation : Ajout des colonnes manquantes avec une valeur par défaut
for col in features.columns:
    if col not in new_data.columns:
        new_data[col] = 0

# Réorganisation des colonnes pour correspondre à l'ordre du jeu d'entraînement
new_data = new_data[features.columns]

# Prédiction
new_pred = model.predict(new_data)
st.write("Le client va-t-il renouveler son contrat ?")
st.write("**Oui**" if new_pred[0] == 1 else "**Non**")

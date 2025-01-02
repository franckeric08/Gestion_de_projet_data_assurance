import streamlit as st
import pandas as pd
import numpy as np

# Génération de données 
np.random.seed(42)

# Table Contrats
contrats = pd.DataFrame({
    'id_contrat': range(1, 101),
    'type_contrat': np.random.choice(['Habitation', 'Auto', 'Santé', 'Professionnel'], size=100),
    'region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], size=100),
    'montant_annuel': np.random.randint(200, 2000, size=100),
    'statut': np.random.choice(['actif', 'résilié', 'renouvelé'], size=100, p=[0.5, 0.3, 0.2]),
    'date_creation': pd.to_datetime(np.random.choice(pd.date_range('2015-01-01', '2022-01-01'), size=100))
})

# Configuration de la page
st.title("Analyses pour des Contrats Spécifiques")

# Filtres Dynamiques
st.sidebar.header("Filtres Dynamiques")
selected_type = st.sidebar.multiselect(
    "Type de Contrat :", options=contrats['type_contrat'].unique(), default=contrats['type_contrat'].unique()
)
selected_region = st.sidebar.multiselect(
    "Région :", options=contrats['region'].unique(), default=contrats['region'].unique()
)

# Application des Filtres
contrats_filtered = contrats[
    (contrats['type_contrat'].isin(selected_type)) &
    (contrats['region'].isin(selected_region))
]

# Analyse des Contrats Filtrés
st.header("Analyse des Contrats Filtrés")
st.write("Données filtrées :")
st.dataframe(contrats_filtered)

# Agrégations des Contrats
st.subheader("Statistiques Agrégées")
stats = contrats_filtered.groupby('type_contrat').agg(
    nb_contrats=('id_contrat', 'count'),
    montant_moyen=('montant_annuel', 'mean'),
    montant_total=('montant_annuel', 'sum')
).reset_index()
st.dataframe(stats)

# Visualisation des Montants par Type de Contrat
st.subheader("Visualisation : Montants par Type de Contrat")
fig1 = st.bar_chart(data=stats, x='type_contrat', y='montant_total', use_container_width=True)

# Analyse Individuelle
st.header("Analyse Individuelle")
selected_contract_id = st.selectbox(
    "Choisir un Contrat ID pour une Analyse Détaillée :", options=contrats_filtered['id_contrat']
)
selected_contract = contrats_filtered[contrats_filtered['id_contrat'] == selected_contract_id]

# Affichage des Détails du Contrat
st.subheader("Détails du Contrat Sélectionné")
st.write(selected_contract)

# Analyse des Montants
st.subheader("Montant Annuel Comparé à la Moyenne des Contrats Filtrés")
average_amount = contrats_filtered['montant_annuel'].mean()
st.metric(
    label="Montant Annuel du Contrat Sélectionné",
    value=f"{selected_contract['montant_annuel'].values[0]} €",
    delta=f"{selected_contract['montant_annuel'].values[0] - average_amount:.2f} €",
)

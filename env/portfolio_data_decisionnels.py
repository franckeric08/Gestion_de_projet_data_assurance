import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Génération de données pour le projet
np.random.seed(42)

# Table Clients
clients = pd.DataFrame({
    'id_client': range(1, 101),
    'nom': [f'Client_{i}' for i in range(1, 101)],
    'age': np.random.randint(18, 80, size=100),
    'region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], size=100),
    'date_inscription': pd.to_datetime(np.random.choice(pd.date_range('2015-01-01', '2022-01-01'), size=100))
})

# Table Sinistres par région
sinistres_par_region = pd.DataFrame({
    'region': ['Nord', 'Sud', 'Est', 'Ouest'],
    'nb_sinistres': [15, 12, 18, 10],
    'cout_total': [170000, 125000, 134000, 91500]
})

# Table Contrats
contrats = pd.DataFrame({
    'id_contrat': range(1, 11),
    'type_contrat': ['Habitation', 'Auto', 'Santé', 'Professionnel', 'Habitation',
                     'Auto', 'Santé', 'Professionnel', 'Habitation', 'Auto'],
    'montant_annuel': [1200, 900, 700, 1500, 1400, 800, 600, 1600, 1250, 950],
    'statut': ['actif', 'renouvelé', 'résilié', 'renouvelé', 'renouvelé',
               'actif', 'résilié', 'renouvelé', 'actif', 'résilié']
})

# Agrégation des contrats par type
contrats_par_type = contrats.groupby('type_contrat').agg(
    nb_contrats=('id_contrat', 'count'),
    total_montant=('montant_annuel', 'sum')
).reset_index()

# Calcul du renouvellement
renouvellement = contrats.groupby('type_contrat').agg(
    nb_renouvelés=('statut', lambda x: (x == 'renouvelé').sum()),
    total=('id_contrat', 'count')
).reset_index()
renouvellement['taux_renouvellement'] = (renouvellement['nb_renouvelés'] / renouvellement['total']) * 100

# Configuration du titre et introduction
st.title("Portfolio Data - Gestion de Projets Décisionnels")
st.write("Bienvenue dans mon portfolio ! Explorez mes projets data décisionnels dans le secteur des assurances.")

# Projet 1 : Analyse des Sinistres
st.write("Utilisez le menu à gauche pour naviguer entre les sections.")
st.header("Projet 1 : Analyse des Sinistres")
st.write("Analyse des sinistres par région et visualisation des coûts totaux.")

# Graphique : Sinistres par région
fig1, ax1 = plt.subplots()
ax1.bar(sinistres_par_region['region'], sinistres_par_region['cout_total'], color='skyblue')
ax1.set_title("Coût Total des Sinistres par Région")
ax1.set_xlabel("Région")
ax1.set_ylabel("Coût Total (€)")
st.pyplot(fig1)

# Tableau : Sinistres par région
st.subheader("Données des sinistres par région")
st.dataframe(sinistres_par_region)

# Projet 2 : Répartition des Contrats par Type
st.header("Projet 2 : Répartition des Contrats par Type")

# Graphique : Répartition des contrats
fig2, ax2 = plt.subplots()
ax2.pie(
    contrats_par_type['nb_contrats'],
    labels=contrats_par_type['type_contrat'],
    autopct='%1.1f%%',
    startangle=140
)
ax2.set_title("Répartition des Contrats par Type")
st.pyplot(fig2)

# Projet 3 : Taux de Renouvellement
st.header("Projet 3 : Taux de Renouvellement par Type de Contrat")

# Graphique : Taux de renouvellement
fig3, ax3 = plt.subplots()
ax3.bar(renouvellement['type_contrat'], renouvellement['taux_renouvellement'], color='lightgreen')
ax3.set_title("Taux de Renouvellement par Type de Contrat")
ax3.set_xlabel("Type de Contrat")
ax3.set_ylabel("Taux de Renouvellement (%)")
for i, v in enumerate(renouvellement['taux_renouvellement']):
    ax3.text(i, v + 1, f"{v:.2f}%", ha='center')
st.pyplot(fig3)

# Lien vers GitHub
st.write("Consultez le code sur [GitHub](https://github.com/franckeric08)")

# Contact
st.header("Contact")
st.write("Pour toute question ou collaboration, contactez-moi via [LinkedIn](https://linkedin.com/in/franck-kabran-745b25170) ou GitHub.")


import streamlit as st
import pandas as pd

# Données 
clients = pd.DataFrame({
    'id_client': range(1, 101),
    'nom': [f'Client_{i}' for i in range(1, 101)],
    'region': pd.Series(['Nord', 'Sud', 'Est', 'Ouest']).sample(100, replace=True).tolist(),
    'age': pd.Series(range(18, 80)).sample(100, replace=True).tolist(),
})

sinistres = pd.DataFrame({
    'id_client': pd.Series(range(1, 101)).sample(50, replace=True).tolist(),
    'region': pd.Series(['Nord', 'Sud', 'Est', 'Ouest']).sample(50, replace=True).tolist(),
    'type_sinistre': pd.Series(['Vol', 'Accident', 'Incendie', 'Dégâts des eaux']).sample(50, replace=True).tolist(),
    'cout': pd.Series(range(500, 10000, 500)).sample(50, replace=True).tolist(),
})

contrats = pd.DataFrame({
    'id_contrat': range(1, 101),
    'type_contrat': pd.Series(['Habitation', 'Auto', 'Santé', 'Professionnel']).sample(100, replace=True).tolist(),
    'region': pd.Series(['Nord', 'Sud', 'Est', 'Ouest']).sample(100, replace=True).tolist(),
    'montant_annuel': pd.Series(range(200, 2000, 100)).sample(100, replace=True).tolist(),
})

# Titre de la page
st.title("Visualisations SQL avec Filtres Dynamiques")

# Filtres dynamiques
st.sidebar.header("Filtres Dynamiques")
region_filter = st.sidebar.multiselect("Filtrer par Région :", options=clients['region'].unique(), default=clients['region'].unique())
type_contrat_filter = st.sidebar.multiselect("Filtrer par Type de Contrat :", options=contrats['type_contrat'].unique(), default=contrats['type_contrat'].unique())

# Application des filtres
clients_filtered = clients[clients['region'].isin(region_filter)]
contrats_filtered = contrats[contrats['region'].isin(region_filter) & contrats['type_contrat'].isin(type_contrat_filter)]
sinistres_filtered = sinistres[sinistres['region'].isin(region_filter)]

# Visualisation 1 : Analyse des clients par région
st.header("Visualisation 1 : Analyse des Clients par Région")
st.code("""
SELECT region, COUNT(*) AS nb_clients
FROM clients
GROUP BY region
ORDER BY nb_clients DESC;
""", language="sql")
clients_summary = clients_filtered.groupby('region').size().reset_index(name='nb_clients')
st.bar_chart(data=clients_summary, x='region', y='nb_clients', use_container_width=True)

# Visualisation 2 : Analyse des contrats par type
st.header("Visualisation 2 : Répartition des Contrats par Type")
st.code("""
SELECT type_contrat, COUNT(*) AS nb_contrats, AVG(montant_annuel) AS montant_moyen
FROM contrats
WHERE region IN (<regions>)
GROUP BY type_contrat;
""", language="sql")
contrats_summary = contrats_filtered.groupby('type_contrat').agg(
    nb_contrats=('id_contrat', 'count'),
    montant_moyen=('montant_annuel', 'mean')
).reset_index()
st.bar_chart(data=contrats_summary, x='type_contrat', y='nb_contrats', use_container_width=True)

# Visualisation 3 : Analyse des sinistres par région et type
st.header("Visualisation 3 : Analyse des Sinistres par Région et Type")
st.code("""
SELECT region, type_sinistre, SUM(cout) AS cout_total
FROM sinistres
WHERE region IN (<regions>)
GROUP BY region, type_sinistre;
""", language="sql")
sinistres_summary = sinistres_filtered.groupby(['region', 'type_sinistre']).agg(
    cout_total=('cout', 'sum')
).reset_index()
sinistres_pivot = sinistres_summary.pivot(index='region', columns='type_sinistre', values='cout_total').fillna(0)
st.dataframe(sinistres_pivot, use_container_width=True)
st.bar_chart(data=sinistres_pivot, use_container_width=True)

# Visualisation 4 : Montant total des contrats par région
st.header("Visualisation 4 : Montant Total des Contrats par Région")
st.code("""
SELECT region, SUM(montant_annuel) AS montant_total
FROM contrats
WHERE region IN (<regions>)
GROUP BY region;
""", language="sql")
contrats_region_summary = contrats_filtered.groupby('region').agg(
    montant_total=('montant_annuel', 'sum')
).reset_index()
st.bar_chart(data=contrats_region_summary, x='region', y='montant_total', use_container_width=True)

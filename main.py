import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement du fichier traité
df = pd.read_csv('Census_2016_2021.csv')

# DataFrame contenant uniquement les municipalités
# Ajout de copy pour éviter les warnings de tentatives de modification du dataframe
df_municipalites = df[df['Type'] == 'MÉ'].copy()

# Affichage nombre de municipalités
nombre_municipalites = len(df_municipalites)
print("Nombre de municipalités :", nombre_municipalites)

# Calcul de la population moyenne en 2016 et en 2021 pour les municipalités
population_moyenne_2016 = df_municipalites['Pop16'].mean()
population_moyenne_2021 = df_municipalites['Pop21'].mean()
print("Population moyenne en 2016 :", population_moyenne_2016)
print("Population moyenne en 2021 :", population_moyenne_2021)

# Création de la figure et des axes pour les subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Calcul du pourcentage d'accroissement en fonction de la population en 2021
pourcentage_accroissement = ((df_municipalites['Pop21'] - df_municipalites['Pop16']) / df_municipalites['Pop16']) * 100
axes[0].scatter(df_municipalites['Pop21'], pourcentage_accroissement)
axes[0].set_xlabel('Population en 2021')
axes[0].set_ylabel('% Accroissement de la population (2016-2021)')
axes[0].set_title('Accroissement de la population en fonction de la population en 2021')

# Classification des municipalités selon leur population en 2021
# bins pour découper en tranche de valeurs discrète
bins = [0, 2000, 9999, 24999, 99999, np.inf]
# légendes à afficher
labels = ['Moins de 2000', '2000 à 9999', '10000 à 24999', '25000 à 99999', '100000 et plus']
# nouveau df avec les tranches choisies
df_municipalites['Population_Category'] = pd.cut(df_municipalites['Pop21'], bins=bins, labels=labels)

# Diagramme en barres horizontales du nombre de municipalités dans chaque catégorie
counts = df_municipalites['Population_Category'].value_counts()
counts.plot(kind='barh', ax=axes[1])
# légende des axes
axes[1].set_xlabel('Nombre de municipalités')
axes[1].set_ylabel('Catégorie de population en 2021')
axes[1].set_title('Nombre de municipalités dans chaque catégorie de population en 2021')

# ajustement automatique pour éviter les superpositions
plt.tight_layout()
# affichage des graphiques
plt.show()

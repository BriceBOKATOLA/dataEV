import numpy as np
import matplotlib.pyplot as plt

# Exercise 1 Charger les fichiers en tant que tableaux 1D numpy

tmin = np.loadtxt('data/2016/tmin.csv')
tmax = np.loadtxt('data/2016/tmax.csv')
tmoy = np.loadtxt('data/2016/tmoy.csv')

# Affichage des listes pour vérifier l'importation
print("Températures minimales :", tmin)
print("Températures maximales :", tmax)
print("Températures moyennes :", tmoy)

# Exercise 2  Combiner les trois tableaux 1D en un tableau 2D avec 366 lignes et 3 colonnes

tableau_temp = np.column_stack((tmin, tmax, tmoy))

# Affichage du tableau 2D pour vérification
print("Tableau 2D des températures :")
print(tableau_temp)

# Exercise 3 Calcul du delta de température entre Tmax et Tmin

delta_temp = tmax - tmin

# Ajouter la colonne delta_temp au tableau existant
tableau_temp = np.column_stack((tableau_temp, delta_temp))

# Affichage du tableau 2D avec la colonne delta
print("Tableau 2D des températures avec delta :")
print(tableau_temp)

# Exercice 4 : Une boucle pour charger et traiter les données de chaque année
data_annuelle = {}

for annee in range(2016, 2023):
    # Chargement des données des fichiers pour chaque année
    tmin = np.loadtxt(f'data/{annee}/tmin.csv')
    tmax = np.loadtxt(f'data/{annee}/tmax.csv')
    tmoy = np.loadtxt(f'data/{annee}/tmoy.csv')
    
    # Création du tableau avec les colonnes Tmin, Tmax et Tmoy
    tableau = np.column_stack((tmin, tmax, tmoy))
    
    # Calcul du delta de température
    delta_temp = tmax - tmin
    
    # Ajout de la colonne delta au tableau
    tableau = np.column_stack((tableau, delta_temp))
    
    # Stockage du tableau dans le dictionnaire avec l'année comme clé
    data_annuelle[annee] = tableau

# Exercice 5 : Calcul des statistiques annuelles
statistiques_annuelles = {}
for annee, tableau in data_annuelle.items():
    temp_max_annuelle = tableau[:, 1].max()   # max 
    temp_min_chaud_jour = tableau[tableau[:, 1].argmax(), 0]  #min
    temp_moy_annuelle = tableau[:, 2].mean()
    moy_delta_temp = tableau[:, 3].mean()
    
    statistiques_annuelles[annee] = {
        "Temp_max_annuelle": temp_max_annuelle,
        "Temp_min_chaud_jour": temp_min_chaud_jour,
        "Temp_moy_annuelle": temp_moy_annuelle,
        "Moy_delta_temp": moy_delta_temp
    }

# Exercice 6 : Création du graphique
annees = list(statistiques_annuelles.keys())
temp_max = [statistiques_annuelles[annee]["Temp_max_annuelle"] for annee in annees]
temp_min_chaud = [statistiques_annuelles[annee]["Temp_min_chaud_jour"] for annee in annees]
temp_moy = [statistiques_annuelles[annee]["Temp_moy_annuelle"] for annee in annees]
moy_delta_temp = [statistiques_annuelles[annee]["Moy_delta_temp"] for annee in annees]

plt.figure(figsize=(10, 6))
plt.plot(annees, temp_max, label="Température maximale", color='red')
plt.plot(annees, temp_min_chaud, label="Temp. min du jour le plus chaud", color='orange')
plt.plot(annees, temp_moy, label="Température moyenne annuelle", color='blue')
plt.plot(annees, moy_delta_temp, label="Moyenne des écarts (Tmax - Tmin)", color='green')

plt.title("Évolution des températures de 2016 à 2022")
plt.xlabel("Année")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid()
plt.show()

# Exercice 7 : Observations

# On observe une tendance générale à la hausse de la température maximale annuelle,
# accompagnée d'une légère augmentation de la température moyenne. 
# Les écarts entre Tmax et Tmin semblent quant à eux se stabiliser au fil du temps.



# Créez un container qui exécute un fichier python 
# qui demande 4 éléments d’une liste de course 
# et qui l’affiche dans un dataframe pandas

import pandas as pd

element_liste = []
while len(element_liste)<4:
    element = input("que voulez vous ajouter à la liste de course")
    element_liste.append(element)


print("Voici la liste de course")
df = pd.DataFrame(element_liste, columns=['Numbers'])
print(df)
#Créez un container qui exécute un fichier python 
# dans lequel on retrouve une boucle while avec un input et la blague 
# “répète et pépète sont dans un bateau, pépète tombe à l’eau qui y reste?” 
# (répondre stop arrêtera la boucle)

reponse = ""

while reponse.upper() != "STOP":
    reponse = input("répète et pépète sont dans un bateau, pépète tombe à l’eau qui y reste?")
print("ok j'arrète")


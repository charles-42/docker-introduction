from fastapi import FastAPI, HTTPException

liste_de_couse = [
{"element":"farine","quantite":200,"unite":"grammes"},
{"element":"oeuf", "quantite":6,"unite":"unité"}
]

dictionnaire_de_couse = {
"farine": [200,"grammes"],
"oeuf": [6,"unité"]
}


app = FastAPI()

@app.get("/")
def index():
    """
    Retourne un message de bienvenue.
    """
    return {"message": "Bonjour bienvenue sur l’API liste de course"}

@app.get("/get_list")
def get_list():
    """
    Retourne la liste de course.
    """
    if len(liste_de_couse)== 0:
        return {"message": "La liste est vide"}
    else:
        return {"content": liste_de_couse}
    
@app.get("/get_dictionnaire")
def get_dictionnaire():
    """
    Retourne le dictionnaire de course.
    """
    if len(dictionnaire_de_couse)== 0:
        return {"message": "Le dictionnaire est vide"}
    else:
        return {"content": dictionnaire_de_couse}




@app.post("/add_to_liste")
def add_to_liste(element: str, quantite:int, unite:None|str=None):
    # vérifier si l'element est déja dans le dictionnaire
    ma_lite_comprehension = [dico["element"] for dico in liste_de_couse]
    if element in ma_lite_comprehension :
        index_element = ma_lite_comprehension.index(element)
        if unite:
            # si il est dans le dictionnaire on vérifie que l'unité est la meme
            if unite == liste_de_couse[index_element]["unite"]:
                # si l'unité est la memme, on ajoute les quantités
                liste_de_couse[index_element]["quantite"]+=quantite
                return {"content":liste_de_couse[index_element]}
                # si l'unité est pas la meme, on renvoit un message d'erreur
            else:
                raise HTTPException(
                                    status_code=400, 
                                    detail=f"Not the good unit for element, {element} is in {liste_de_couse[index_element]["unite"]} "
                                    )
        # pas d'unité fournie, j'ajoute par défault
        else:
            liste_de_couse[index_element]["quantite"]+=quantite
            return {"content":liste_de_couse[index_element]}

    else:
        # si non, on ajoute l'element au dictionnaire
        if unite:
            liste_de_couse.append(
                {"element":element,
                "quantite":quantite,
                "unite":unite}
            )
            
            return {"content":liste_de_couse[-1]}
        else:
            raise HTTPException(
                                status_code=400, 
                                detail=f"For new element, you need to give a unit"
                                )
        

@app.post("/add_to_dictionnaire")
def add_to_dictionnaire(element: str, quantite:int, unite:None|str=None):
    # vérifier si l'element est déja dans le dictionnaire
    if element in dictionnaire_de_couse:
        if unite:
            # si il est dans le dictionnaire on vérifie que l'unité est la meme
            if unite == dictionnaire_de_couse[element][1]:
                # si l'unité est la memme, on ajoute les quantités
                dictionnaire_de_couse[element][0]+=quantite
                return {element:dictionnaire_de_couse[element]}
                # si l'unité est pas la meme, on renvoit un message d'erreur
            else:
                raise HTTPException(
                                    status_code=400, 
                                    detail=f"Not the good unit for element, {element} is in {dictionnaire_de_couse[element][1]} "
                                    )
        # pas d'unité fournie, j'ajoute par défault
        else:
            dictionnaire_de_couse[element][0]+=quantite
            return {element:dictionnaire_de_couse[element]}

    else:
        # si non, on ajoute l'element au dictionnaire
        if unite:
            dictionnaire_de_couse[element] = [quantite,unite]
            return {element:dictionnaire_de_couse[element]}
        else:
            raise HTTPException(
                                    status_code=400, 
                                    detail=f"For new element, you need to give a unit"
                                    )

        


# @app.delete("/liste")
# def remove_from_list(element: int):
#     """
#     Supprime un entier de la liste.
    
#     Args:
#     - element (int): L'entier à supprimer de la liste.
    
#     Returns:
#     - dict: La liste mise à jour après la suppression de l'élément.
    
#     Raises:
#     - HTTPException: Si l'élément n'est pas trouvé dans la liste.
#     """
#     try:
#         ma_liste_integer.remove(element)
#         return {"content": ma_liste_integer}
#     except ValueError:
#         raise HTTPException(status_code=404, detail="Element not found in the list")


# #  uvicorn main:app --reload
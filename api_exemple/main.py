from fastapi import FastAPI, HTTPException

ma_liste_integer = []

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/liste")
def get_list():
    return {"content": ma_liste_integer}

@app.post("/liste")
def add_to_list(element:int):
    ma_liste_integer.append(element)
    return {"content": ma_liste_integer}

@app.delete("/liste") 
def remove_from_list(element: int): 
    try: 
        ma_liste_integer.remove(element) 
        return {"content": ma_liste_integer} 
    except ValueError: 
        raise HTTPException(status_code=404, detail="Element not found in the list") 



#  uvicorn main:app --reload
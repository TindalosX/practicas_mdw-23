from fastapi import FastAPI
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

    
class Pasajero(BaseModel):
    id: str
    Name: str
    Pclass:str
    Survived:str
    Sex:str
    Age:str
    SibSp:str
    Parch:str
    Ticket:str
    Fare:str
    #Cabin:str
    Embarked:str
             
pass_list = []


@app.get("/pasaclass/")
async def usersclass():
    return (pass_list)


@app.post("/pasaclass/")
async def usersclass(pasajero:Pasajero):
    
    for index, saved_user in enumerate(pass_list):
        if saved_user.id == pasajero.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        pass_list.append(pasajero)
        return pasajero

@app.get("/pasaclass/")
async def usersclass():
    return (pass_list)

#PUT
@app.put("/pasaclass/")
async def usersclass(pasajero:Pasajero):
    
    found = False

    for index, saved_user in enumerate(pass_list):
        if saved_user.id == pasajero.id:
            pass_list[index] = pasajero
            found = True
            
    if not found:
        return {"error":"No se realizo la actualización"}
    else:
        return pasajero, {"respuesta":"Usuario Actualizado"}

#from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import APIRouter

from fastapi import HTTPException, status

#Creamos un objeto a partir de la clase FastAPI
#app= FastAPI()

router = APIRouter()

    
class Pasajero(BaseModel):
    Id: int #Id
    Name: str
    Pclass: int
    Survived:int
    Sex:str
    Age:str
    Ticket:str
             
pass_list=[
Pasajero(Id = 50, Name = "Arnold-Franchi, Mrs. Josef (Josefine Franchi)", Pclass = 3, Survived = 0, Sex = "female", Age = "18", Ticket = "349237"),
Pasajero(Id = 51, Name = "Panula, Master. Juha Niilo", Pclass = 3, Survived = 0, Sex = "male", Age = "7", Ticket = "3101295"),
Pasajero(Id = 52, Name = "Nosworthy, Mr. Richard Cater", Pclass = 3, Survived = 0, Sex = "male", Age = "21", Ticket = "A/4. 39886"),
Pasajero(Id = 53, Name = "Harper, Mrs. Henry Sleeper (Myna Haxtun)", Pclass = 1, Survived = 1, Sex = "female", Age = "49", Ticket = "PC 17572"),
Pasajero(Id = 54, Name = "Faunthorpe, Mrs. Lizzie (Elizabeth Anne Wilkinson)", Pclass = 2, Survived = 1, Sex = "female", Age = "29", Ticket = "2926"),
Pasajero(Id = 55, Name = "Ostby, Mr. Engelhart Cornelius", Pclass = 1, Survived = 0, Sex = "male", Age = "65", Ticket = "113509"),
Pasajero(Id = 56, Name = "Woolner, Mr. Hugh", Pclass = 1, Survived = 1, Sex = "male", Age = "", Ticket = "19947"),
Pasajero(Id = 57, Name = "Rugg, Miss. Emily", Pclass = 2, Survived = 1, Sex = "female", Age = "21", Ticket = "C.A. 31026"),
Pasajero(Id = 58, Name = "Novel, Mr. Mansouer", Pclass = 3, Survived = 0, Sex = "male", Age = "28.5", Ticket = "2697"),
Pasajero(Id = 59, Name = "West, Miss. Constance Mirium", Pclass = 2, Survived = 1, Sex = "female", Age = "5", Ticket = "C.A. 34651"),
Pasajero(Id = 60, Name = "Goodwin, Master. William Frederick", Pclass = 3, Survived = 0, Sex = "male", Age = "11", Ticket = "CA 2144"),
Pasajero(Id = 61, Name = "Sirayanian, Mr. Orsen", Pclass = 3, Survived = 0, Sex = "male", Age = "22", Ticket = "2669"),
Pasajero(Id = 62, Name = "Icard, Miss. Amelie", Pclass = 1, Survived = 1, Sex = "female", Age = "38", Ticket = "113572"),
Pasajero(Id = 63, Name = "Harris, Mr. Henry Birkhardt", Pclass = 1, Survived = 0, Sex = "male", Age = "45", Ticket = "36973"),
Pasajero(Id = 64, Name = "Skoog, Master. Harald", Pclass = 3, Survived = 0, Sex = "male", Age = "4", Ticket = "347088"),
Pasajero(Id = 65, Name = "Stewart, Mr. Albert A", Pclass = 1, Survived = 0, Sex = "male", Age = "", Ticket = "PC 17605")

]

#GET
@router.get("/50a65pasaclass/")
async def usersclass():
    return (pass_list)

#POST
#"/25pasaclass/", response_model=Pasajero, status_code=201
@router.post("/50a65pasaclass/")
async def usersclass(pasajero:Pasajero):
    found=False 
    
    for index, saved_user in enumerate(pass_list):
        if saved_user.Id == pasajero.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        pass_list.append(pasajero)
        return pasajero

#PUT
@router.put("/50a65pasaclass/")
async def usersclass(pasajero:Pasajero):
    
    found = False

    for index, saved_user in enumerate(pass_list):
        if saved_user.Id == pasajero.Id:
            pass_list[index] = pasajero
            found = True
    
    if not found:
        #raise HTTPException(status_code= status.HTTP_204_NO_CONTENT,detail="El usuario no existe")
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="Id no encontrado")
    else:
        return pasajero, {"respuesta":"Registro Actualizado"}

#DELETE
@router.delete("/50a65pasaclass/")
async def usersclass(pasajero:Pasajero):
    
    found = False

    for index, saved_user in enumerate(pass_list):
        if saved_user.Id == pasajero.Id:
            del pass_list[index]
            found = True

    if not found:
        #raise HTTPException(status_code= status.HTTP_204_NO_CONTENT,detail="El usuario no existe")
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="El usuario no existe")
    else:
        return pasajero, {"respuesta":"Registro Borrado"}


#source /home/tindalos/Code/ambientes_python/prac-mdw23/bin/activate
#http://127.0.0.1:8000/50a65pasaclass/
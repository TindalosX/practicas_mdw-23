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
    #SibSp:str
    #Parch:str
    Ticket:str
    #Fare:str
    #Cabin:str
    #Embarked:str
             
pass_list=[
    Pasajero(Id = 1, Name = "Braund, Mr. Owen Harris", Pclass = 3, Survived = 0, Sex = "male", Age = "22", Ticket = "A/5 21171"),
Pasajero(Id = 2, Name = "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Pclass = 1, Survived = 1, Sex = "female", Age = "38", Ticket = "PC 17599"),
Pasajero(Id = 3, Name = "Heikkinen, Miss. Laina", Pclass = 3, Survived = 1, Sex = "female", Age = "26", Ticket = "STON/O2. 3101282"),
Pasajero(Id = 4, Name = "Futrelle, Mrs. Jacques Heath (Lily May Peel)", Pclass = 1, Survived = 1, Sex = "female", Age = "35", Ticket = "113803"),
Pasajero(Id = 5, Name = "Allen, Mr. William Henry", Pclass = 3, Survived = 0, Sex = "male", Age = "35", Ticket = "373450"),
Pasajero(Id = 6, Name = "Moran, Mr. James", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "330877"),
Pasajero(Id = 7, Name = "McCarthy, Mr. Timothy J", Pclass = 1, Survived = 0, Sex = "male", Age = "54", Ticket = "17463"),
Pasajero(Id = 8, Name = "Palsson, Master. Gosta Leonard", Pclass = 3, Survived = 0, Sex = "male", Age = "2", Ticket = "349909"),
Pasajero(Id = 9, Name = "Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", Pclass = 3, Survived = 1, Sex = "female", Age = "27", Ticket = "347742"),
Pasajero(Id = 10, Name = "Nasser, Mrs. Nicholas (Adele Achem)", Pclass = 2, Survived = 1, Sex = "female", Age = "14", Ticket = "237736"),
Pasajero(Id = 11, Name = "Sandstrom, Miss. Marguerite Rut", Pclass = 3, Survived = 1, Sex = "female", Age = "4", Ticket = "PP 9549"),
Pasajero(Id = 12, Name = "Bonnell, Miss. Elizabeth", Pclass = 1, Survived = 1, Sex = "female", Age = "58", Ticket = "113783"),
Pasajero(Id = 13, Name = "Saundercock, Mr. William Henry", Pclass = 3, Survived = 0, Sex = "male", Age = "20", Ticket = "A/5. 2151"),
Pasajero(Id = 14, Name = "Andersson, Mr. Anders Johan", Pclass = 3, Survived = 0, Sex = "male", Age = "39", Ticket = "347082"),
Pasajero(Id = 15, Name = "Vestrom, Miss. Hulda Amanda Adolfina", Pclass = 3, Survived = 0, Sex = "female", Age = "14", Ticket = "350406"),
Pasajero(Id = 16, Name = "Hewlett, Mrs. (Mary D Kingcome) ", Pclass = 2, Survived = 1, Sex = "female", Age = "55", Ticket = "248706"),
Pasajero(Id = 17, Name = "Rice, Master. Eugene", Pclass = 3, Survived = 0, Sex = "male", Age = "2", Ticket = "382652"),
Pasajero(Id = 18, Name = "Williams, Mr. Charles Eugene", Pclass = 2, Survived = 1, Sex = "male", Age = "", Ticket = "244373"),
Pasajero(Id = 19, Name = "Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Pclass = 3, Survived = 0, Sex = "female", Age = "31", Ticket = "345763"),
Pasajero(Id = 20, Name = "Masselmani, Mrs. Fatima", Pclass = 3, Survived = 1, Sex = "female", Age = "", Ticket = "2649"),
Pasajero(Id = 21, Name = "Fynney, Mr. Joseph J", Pclass = 2, Survived = 0, Sex = "male", Age = "35", Ticket = "239865"),
Pasajero(Id = 22, Name = "Beesley, Mr. Lawrence", Pclass = 2, Survived = 1, Sex = "male", Age = "34", Ticket = "248698"),
Pasajero(Id = 23, Name = "McGowan, Miss. Anna Annie", Pclass = 3, Survived = 1, Sex = "female", Age = "15", Ticket = "330923"),
Pasajero(Id = 24, Name = "Sloper, Mr. William Thompson", Pclass = 1, Survived = 1, Sex = "male", Age = "28", Ticket = "113788"),
Pasajero(Id = 25, Name = "Palsson, Miss. Torborg Danira", Pclass = 3, Survived = 0, Sex = "female", Age = "8", Ticket = "349909"),
]

#GET
@router.get("/25pasaclass/")
async def usersclass():
    return (pass_list)

#POST
#"/25pasaclass/", response_model=Pasajero, status_code=201
@router.post("/25pasaclass/")
async def usersclass(pasajero:Pasajero):
    found=False 
    
    for index, saved_user in enumerate(pass_list):
        if saved_user.Id == pasajero.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        pass_list.append(pasajero)
        return pasajero

#PUT
@router.put("/25pasaclass/")
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
@router.delete("/25pasaclass/")
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
#http://127.0.0.1:8000/25pasaclass/
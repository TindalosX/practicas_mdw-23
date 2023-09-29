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
    Pasajero(Id = 25, Name = "Palsson, Miss. Torborg Danira", Pclass = 3, Survived = 0, Sex = "female", Age = "8", Ticket = "349909"),
    Pasajero(Id = 26, Name = "Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)", Pclass = 3, Survived = 1, Sex = "female", Age = "38", Ticket = "347077"),
    Pasajero(Id = 27, Name = "Emir, Mr. Farred Chehab", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "2631"),
    Pasajero(Id = 28, Name = "Fortune, Mr. Charles Alexander", Pclass = 1, Survived = 0, Sex = "male", Age = "19", Ticket = "19950"),
    Pasajero(Id = 29, Name = "O'Dwyer, Miss. Ellen Nellie", Pclass = 3, Survived = 1, Sex = "female", Age = "", Ticket = "330959"),
    Pasajero(Id = 30, Name = "Todoroff, Mr. Lalio", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "349216"),
    Pasajero(Id = 31, Name = "Uruchurtu, Don. Manuel E", Pclass = 1, Survived = 0, Sex = "male", Age = "40", Ticket = "PC 17601"),
    Pasajero(Id = 32, Name = "Spencer, Mrs. William Augustus (Marie Eugenie)", Pclass = 1, Survived = 1, Sex = "female", Age = "", Ticket = "PC 17569"),
    Pasajero(Id = 33, Name = "Glynn, Miss. Mary Agatha", Pclass = 3, Survived = 1, Sex = "female", Age = "", Ticket = "335677"),
    Pasajero(Id = 34, Name = "Wheadon, Mr. Edward H", Pclass = 2, Survived = 0, Sex = "male", Age = "66", Ticket = "C.A. 24579"),
    Pasajero(Id = 35, Name = "Meyer, Mr. Edgar Joseph", Pclass = 1, Survived = 0, Sex = "male", Age = "28", Ticket = "PC 17604"),
    Pasajero(Id = 36, Name = "Holverson, Mr. Alexander Oskar", Pclass = 1, Survived = 0, Sex = "male", Age = "42", Ticket = "113789"),
    Pasajero(Id = 37, Name = "Mamee, Mr. Hanna", Pclass = 3, Survived = 1, Sex = "male", Age = "", Ticket = "2677"),
    Pasajero(Id = 38, Name = "Cann, Mr. Ernest Charles", Pclass = 3, Survived = 0, Sex = "male", Age = "21", Ticket = "A./5. 2152"),
    Pasajero(Id = 39, Name = "Vander Planke, Miss. Augusta Maria", Pclass = 3, Survived = 0, Sex = "female", Age = "18", Ticket = "345764"),
    Pasajero(Id = 40, Name = "Nicola-Yarred, Miss. Jamila", Pclass = 3, Survived = 1, Sex = "female", Age = "14", Ticket = "2651"),
    Pasajero(Id = 41, Name = "Ahlin, Mrs. Johan (Johanna Persdotter Larsson)", Pclass = 3, Survived = 0, Sex = "female", Age = "40", Ticket = "7546"),
    Pasajero(Id = 42, Name = "Turpin, Mrs. William John Robert (Dorothy Ann Wonnacott)", Pclass = 2, Survived = 0, Sex = "female", Age = "27", Ticket = "11668"),
    Pasajero(Id = 43, Name = "Kraeff, Mr. Theodor", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "349253"),
    Pasajero(Id = 44, Name = "Laroche, Miss. Simonne Marie Anne Andree", Pclass = 2, Survived = 1, Sex = "female", Age = "3", Ticket = "SC/Paris 2123"),
    Pasajero(Id = 45, Name = "Devaney, Miss. Margaret Delia", Pclass = 3, Survived = 1, Sex = "female", Age = "19", Ticket = "330958"),
    Pasajero(Id = 46, Name = "Rogers, Mr. William John", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "S.C./A.4. 23567"),
    Pasajero(Id = 47, Name = "Lennon, Mr. Denis", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "370371"),
    Pasajero(Id = 48, Name = "O'Driscoll, Miss. Bridget", Pclass = 3, Survived = 1, Sex = "female", Age = "", Ticket = "14311"),
    Pasajero(Id = 49, Name = "Samaan, Mr. Youssef", Pclass = 3, Survived = 0, Sex = "male", Age = "", Ticket = "2662")
]

#GET
@router.get("/25a49pasaclass/")
async def usersclass():
    return (pass_list)

#POST
#"/25pasaclass/", response_model=Pasajero, status_code=201
@router.post("/25a49pasaclass/")
async def usersclass(pasajero:Pasajero):
    found=False 
    
    for index, saved_user in enumerate(pass_list):
        if saved_user.Id == pasajero.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        pass_list.append(pasajero)
        return pasajero

#PUT
@router.put("/25a49pasaclass/")
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
@router.delete("/25a49pasaclass/")
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
#http://127.0.0.1:8000/pasaclass/
#from fastapi import Query
from pydantic import BaseModel
from fastapi import HTTPException, status, Depends

from fastapi import APIRouter, FastAPI

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt, JWTError

from passlib.context import CryptContext
from datetime import datetime, timedelta

from fastapi.staticfiles import StaticFiles

#Para  HTML
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

#Implementamos algoritmo de haseo para encriptar contraseña
ALGORITHM = "HS256"
#Duración de autenticación 
ACCESS_TOKEN_DURATION= 10
#Creamos un secret
SECRET="123456789"


#template HTML
templates = Jinja2Templates(directory="templates")

#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")

#Autenticación por contraseña para eso:
#Creamos un endpoint llamado "login"
oauth2=OAuth2PasswordBearer(tokenUrl="login")

#Creamos contexto de encriptación para eso importamos libreria passlib y elegimos algoritmo de incriptación "bcrypt"
#Utilizamos bcrypt generator para encriptar nuestras contraseñas
crypt= CryptContext(schemes="bcrypt")

# generamos la contraseña encriptada para guardarla en base de datos
#https://bcrypt-generator.com/


class User(BaseModel):
    username:str
    full_name: str
    email:str
    tel: str
    disabled:bool

#Definimos la clase para el usuario de base de datos
class UserDB(User):
    password:str
    
#Creo una base de datos no relacional de usuarios 
users_db ={
    "Yosselin":{
         "username":"Yosselin",
         "full_name": "Yosselin Pablo Ruiz",
         "email": "yosselin.pablo@alumno.buap.mx",
         "tel": "2288358188",
         "disabled": False,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    },
    "Abraham":{
         "username":"Abraham",
         "full_name": "Abraham Coagtle Temis",
         "email": "abraham.coagtle@alumno.buap.mx",
         "tel": "2731327748",
         "disabled": False,
         "password": "$2a$12$fHDD765CyJCFR8mvhKNZPuCVKFK0c/rJoSJmWh0sL8Vp5wt8SsbQS"#"a5678"
    },
    "Juan":{
         "username":"Juan",
         "full_name": "Juan Pablo Mendoza",
         "email": "juan.mendoza@alumno.buap.mx",
         "tel": "228 177 6285",
         "disabled": False,
         "password": "$2a$12$mF0agZCBrp2aFBx5404HuOzRvhTkssFfsZK26qcexJEHeqpwcDqka"#"1234"
    },
    "Kevin":{
         "username":"Kevin",
         "full_name": "Kevin Armas Hernández",
         "email": "kevin.armas@alumno.buap.mx",
         "tel": "61 41 99 89 90",
         "disabled": False,
         "password": "$2a$12$j/uUIhnv.x0KcvVCE8H0WeWl0VohOY5AJWjSy5n9wCD9WkTWzSB7e"#"k1234"
    },
    "Luis":{
         "username":"Luis",
         "full_name": "Luis Delfino Castro Nava",
         "email": "luis.castro@alumno.buap.mx",
         "tel": "81 10 50 26 39",
         "disabled": False,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    },
    "Estefania":{
         "username":"Estefania",
         "full_name": "Estefania Rodríguez Martínez",
         "email": "estefania.rodríguez@alumno.buap.mx",
         "tel": "22 28 66 92 27",
         "disabled": False,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    },
    "Pilar":{
         "username":"Pilar",
         "full_name": "Pilar Hernandez Zambrano",
         "email": "pilar.hernandez@alumno.buap.mx",
         "tel": "20 19 29 98 97",
         "disabled": False,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    },
    "Vicente":{
         "username":"Vicente",
         "full_name": "Vicente Zavaleta Sanchez",
         "email": "vicente.zavaleta@alumno.buap.mx",
         "tel": "22 12 67 84 49",
         "disabled": False,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    },
    "Arruch4":{
         "username":"Arruch4",
         "full_name": "Jose Eduardo Arrucha Álvarez",
         "email": "jose.arrucha@alumno.buap.mx",
         "tel": "22 13 31 70 79",
         "disabled": False,
         "password": "$2a$12$fr1Ju7ST5hWQ3YcafHZwGeOKhFuR7EVtHVuBSMROqTfG0gGD9qm8W"#"pokemon"
    }
}


#1 Función para regresar el usuario completo de la base de datos (users_db), con contraseña encriptada
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username]) #** devuelve todos los parámetros del usuario que coincida con username

#4 Función final para devolver usuario a la solicitud del backend   
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
    #3 Esta es la dependencia para buscar al usuario
async def auth_user(token:str=Depends(oauth2)):
    try:
        username= jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")

    return search_user(username) #Esta es la entrega final, usuario sin password

#2 Función para determinar si usuario esta inactivo 
async def current_user(user:User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user
        
####################################################################################3
        
@router.post("/login/")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    #Busca en la base de datos "users_db" el username que se ingreso en la forma 
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    # Se obtienen los atributos incluyendo password del usuario que coincida el username de la forma 
    user= search_user_db(form.username)     
    
    #user.password es la contraseña encriptada en la base de datos
    #form.password es la contraseña original que viene en formulario
    if not crypt.verify(form.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    #Creamos expiración de 1 min a partir de la hora actual
    access_token_expiration=timedelta(minutes=ACCESS_TOKEN_DURATION)
    #Tiempo de expiración: hora actual mas 1 minuto
    expire=datetime.utcnow()+access_token_expiration
    
    access_token={"sub": user.username,"exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM), "token_type":"bearer"}

@router.get("/users/me/")
async def me(user:User= Depends (current_user)): #Crea un user de tipo User que depende de la función (current_user)
    return user


@router.get("/cuenta", response_class=HTMLResponse)
async def cuenta_usario(request:Request, user:User= Depends (current_user)):
    user_data = {
        "full_name": user.full_name,
        "email": user.email,
        "tel": user.tel,
        "image_path": f"/static/images/{user.username.lower()}.jpg",
    }
    return templates.TemplateResponse("user.html", {"request": request, "user": user_data})
    #return "Router"

#http://127.0.0.1:8000/login/
#http://127.0.0.1:8000/cuenta

#username:Freddy
#password:1234

#http://127.0.0.1:8000/users/me/

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
#from router import file_r1, file_r2, file_r3, file_r4, file_r5, file_r6
from router import db

#nuevo 4 de octubre
from fastapi.staticfiles import StaticFiles


#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Creamos un router a partir de la clase
app.include_router(db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")
async def imprimir():
    return "JWT"


#http://127.0.0.1:8000/login/

#username:Freddy
#password:1234

#http://127.0.0.1:8000/users/me/

#https://bcrypt-generator.com/

#Cinammon
# source /home/zayas/practicas-env/bin/activate
#Victoria
#source /home/tindalos/Code/ambientes_python/prac-mdw23/bin/activate
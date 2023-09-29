#########################################Primera Parte################################################

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
from routers import file_r1, file_r2, file_r3, file_r4, file_r5 #, router_DB_10


#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Creamos un router a partir de la clase
#file_r1: tracks
app.include_router(file_r1.router)

#file_r2: pasajeros
app.include_router(file_r2.router)

#file_r3: pasajeros
app.include_router(file_r3.router)

#file_r4: pasajeros
app.include_router(file_r4.router)

#file_r5: tracks
app.include_router(file_r5.router)

#Creamos un router a partir de la clase router_DB_10
#app.include_router(router_DB_10.router)


#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Practica Routers"


#Levantamos el server Uvicorn
#-uvicorn main:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000

#########################################Segunda Parte################################################

#creamos la función asincrona con formato JSON
@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}

# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/Git

######################################CLASE 3################################

#Detener server con: ctrl + c


#Documentación con Swagger:  http://127.0.0.1:8000/docs
#Documentación con Redocly:  http://127.0.0.1:8000/redoc

# source /home/zayas/practicas-env/bin/activate
#source /home/tindalos/Code/ambientes_python/prac-mdw23/bin/activate

#Consultas:
#http://127.0.0.1:8000/tracksclass/?Year=2005
#http://127.0.0.1:8000/tracksclass/year-artista/?Year=2005&Artista=depeche+mode
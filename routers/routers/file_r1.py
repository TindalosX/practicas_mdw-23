from fastapi import Query
from pydantic import BaseModel
from fastapi import HTTPException, status

from fastapi import APIRouter

#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

class Tracks(BaseModel):
    Id: int
    Artista: str
    Cancion: str
    Genero: str
    Year: int
    Rate: int

tracks = [
Tracks(Id=0, Artista="nirvana", Cancion="breed", Genero="grunge", Year=2011, Rate=1),
Tracks(Id=1, Artista="lisa", Cancion="guren", Genero="rock", Year=2011, Rate=10),
Tracks(Id=2, Artista="the cure", Cancion="just like heaven", Genero="rock", Year=1995, Rate=7),
Tracks(Id=3, Artista="nirvana", Cancion="smell like teen spirit", Genero="grunge", Year=1991, Rate=4),
Tracks(Id=4, Artista="the cure", Cancion="a night like this", Genero="rock", Year=2017, Rate=8),
Tracks(Id=5, Artista="the pixies", Cancion="bone machine", Genero="rock", Year=2019, Rate=3),
Tracks(Id=6, Artista="the pixies", Cancion="gigantic", Genero="rock", Year=1993, Rate=7),
Tracks(Id=7, Artista="the pixies", Cancion="head on", Genero="rock", Year=2010, Rate=7),
Tracks(Id=8, Artista="the pixies", Cancion="hey", Genero="rock", Year=2006, Rate=1),
Tracks(Id=9, Artista="the pixies", Cancion="where is my mind?", Genero="rock", Year=2000, Rate=9),
Tracks(Id=10, Artista="the pixies", Cancion="cactus", Genero="rock", Year=2023, Rate=9),
Tracks(Id=11, Artista="venom", Cancion="burn in hell", Genero="metal", Year=2009, Rate=4),
Tracks(Id=12, Artista="venom", Cancion="house of pain", Genero="metal", Year=2002, Rate=4),
Tracks(Id=13, Artista="venom", Cancion="warhead", Genero="metal", Year=2004, Rate=3),
Tracks(Id=14, Artista="slipknot", Cancion="before i forget", Genero="nu-metal", Year=2010, Rate=10),
Tracks(Id=15, Artista="slipknot", Cancion="duality", Genero="nu-metal", Year=2022, Rate=7),
Tracks(Id=16, Artista="slipknot", Cancion="duality", Genero="nu-metal", Year=2011, Rate=3),
Tracks(Id=17, Artista="slipknot", Cancion="killpop", Genero="nu-metal", Year=2009, Rate=6),
Tracks(Id=18, Artista="slipknot", Cancion="lech", Genero="nu-metal", Year=2000, Rate=1),
Tracks(Id=19, Artista="slipknot", Cancion="psychosocial", Genero="nu-metal", Year=2020, Rate=4),
Tracks(Id=20, Artista="slipknot", Cancion="sulfur", Genero="nu-metal", Year=2007, Rate=4),
Tracks(Id=21, Artista="slipknot", Cancion="vendetta", Genero="nu-metal", Year=2010, Rate=9),
Tracks(Id=22, Artista="slipknot", Cancion="custer", Genero="nu-metal", Year=2011, Rate=1),
Tracks(Id=23, Artista="slipknot", Cancion="dead memories", Genero="nu-metal", Year=2015, Rate=6),
Tracks(Id=24, Artista="system of a down", Cancion="aerials", Genero="nu-metal", Year=2013, Rate=6),
]

#GET
@router.get("/0a24tracks/")
async def usersclass():
    try:
        return (tracks)
    except:
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="Id no encontrado")

#POST
@router.post("/0a24tracks/")
async def usersclass(track:Tracks):
    found=False 
    
    for index, saved_user in enumerate(tracks):
        if saved_user.Id == track.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        tracks.append(track)
        return track
    
#PUT
@router.put("/0a24tracks/")
async def usersclass(track:Tracks):
    
    found = False

    for index, saved_user in enumerate(tracks):
        if saved_user.Id == track.Id:
            tracks[index] = track
            found = True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="Id no encontrado")
    else:
        return track, {"respuesta":"Registro Actualizado"}

#DELETE
@router.delete("/0a24tracks/")
async def usersclass(track:Tracks):
    
    found = False

    for index, saved_user in enumerate(tracks):
        if saved_user.Id == track.Id:
            del tracks[index]
            found = True

    if not found:
        #raise HTTPException(status_code= status.HTTP_204_NO_CONTENT,detail="El usuario no existe")
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="El usuario no existe")
    else:
        return track, {"respuesta":"Registro Borrado"}

# http://127.0.0.1:8000/0a24tracks/
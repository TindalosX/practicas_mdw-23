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
Tracks(Id=50, Artista="alice in chains", Cancion="man in the box", Genero="grunge", Year=2004, Rate=5),
Tracks(Id=51, Artista="alice in chains", Cancion="them bones", Genero="grunge", Year=2002, Rate=2),
Tracks(Id=52, Artista="alice in chains", Cancion="would?", Genero="grunge", Year=2006, Rate=10),
Tracks(Id=53, Artista="alice in chains", Cancion="got me wrong", Genero="grunge", Year=2008, Rate=7),
Tracks(Id=54, Artista="iron maiden", Cancion="aces high", Genero="heavy metal", Year=2007, Rate=5),
Tracks(Id=55, Artista="iron maiden", Cancion="dance of death", Genero="heavy metal", Year=2001, Rate=8),
Tracks(Id=56, Artista="iron maiden", Cancion="fear of the dark", Genero="heavy metal", Year=2000, Rate=3),
Tracks(Id=57, Artista="iron maiden", Cancion="phantom of the opera", Genero="heavy metal", Year=2008, Rate=6),
Tracks(Id=58, Artista="iron maiden", Cancion="run to the hills", Genero="heavy metal", Year=2014, Rate=2),
Tracks(Id=59, Artista="iron maiden", Cancion="the number of the beast", Genero="heavy metal", Year=2004, Rate=8),
Tracks(Id=60, Artista="iron maiden", Cancion="the trooper", Genero="heavy metal", Year=2014, Rate=1),
Tracks(Id=61, Artista="iron maiden", Cancion="the wicker man", Genero="heavy metal", Year=2010, Rate=1),
Tracks(Id=62, Artista="iron maiden", Cancion="wasted years", Genero="heavy metal", Year=2005, Rate=8),
Tracks(Id=63, Artista="iron maiden", Cancion="2 minutes to midnight", Genero="heavy metal", Year=2014, Rate=10),
Tracks(Id=64, Artista="black sabbath", Cancion="paranoid", Genero="heavy metal", Year=1996, Rate=9),
Tracks(Id=65, Artista="black sabbath", Cancion="iron man", Genero="heavy metal", Year=2006, Rate=4),
Tracks(Id=66, Artista="black sabbath", Cancion="lady evil", Genero="heavy metal", Year=2005, Rate=5),
Tracks(Id=67, Artista="black sabbath", Cancion="N.I.B", Genero="heavy metal", Year=2010, Rate=9),
Tracks(Id=68, Artista="black sabbath", Cancion="electric funeral", Genero="heavy metal", Year=2017, Rate=3),
Tracks(Id=69, Artista="black sabbath", Cancion="rat salad", Genero="heavy metal", Year=1996, Rate=10),
Tracks(Id=70, Artista="black sabbath", Cancion="war pig", Genero="heavy metal", Year=1997, Rate=2),
Tracks(Id=71, Artista="black sabbath", Cancion="crazy train", Genero="heavy metal", Year=1995, Rate=4),
Tracks(Id=72, Artista="blink 182", Cancion="always", Genero="punk-rock", Year=1991, Rate=4),
Tracks(Id=73, Artista="blink 182", Cancion="adam's song", Genero="punk-rock", Year=2009, Rate=9),
Tracks(Id=74, Artista="blink 182", Cancion="feeling this", Genero="punk-rock", Year=2014, Rate=3),
Tracks(Id=75, Artista="blink 182", Cancion="all of this", Genero="punk-rock", Year=2016, Rate=6)
]

#GET
@router.get("/50a75tracks/")
async def usersclass():
    try:
        return (tracks)
    except:
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="Id no encontrado")

#POST
@router.post("/50a75tracks/")
async def usersclass(track:Tracks):
    found=False 
    
    for index, saved_user in enumerate(tracks):
        if saved_user.Id == track.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        tracks.append(track)
        return track
    
#PUT
@router.put("/50a75tracks/")
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
@router.delete("/50a75tracks/")
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

# http://127.0.0.1:8000/50a75tracks/
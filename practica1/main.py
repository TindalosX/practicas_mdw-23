from fastapi import FastAPI

#Objeto
app = FastAPI()

tracks = [
    {
    "artista":"nirvana",
    "cancion": "breed",
    "genero": "grunge"
    },
    {
    "artista":"lisa",
    "cancion": "guren",
    "genero": "rock"
    },
    {
    "artista":"the cure",
    "cancion": "just like heaven",
    "genero": "rock"
    },
    {
    "artista":"nirvana",
    "cancion": "smell like teen spirit",
    "genero": "grunge"
    },
    {
    "artista":"the cure",
    "cancion": "a night like this",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "bone machine",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "gigantic",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "head on",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "hey",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "where is my mind?",
    "genero": "rock"
    },
    {
    "artista":"the pixies",
    "cancion": "cactus",
    "genero": "rock"
    },
    {
    "artista":"venom",
    "cancion": "burn in hell",
    "genero": "metal"
    },
    {
    "artista":"venom",
    "cancion": "house of pain",
    "genero": "metal"
    },
    {
    "artista":"venom",
    "cancion": "warhead",
    "genero": "metal"
    },
    {
    "artista":"slipknot",
    "cancion": "before i forget",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "duality",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "duality",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "killpop",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "lech",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "psychosocial",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "sulfur",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "vendetta",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "custer",
    "genero": "nu-metal"
    },
    {
    "artista":"slipknot",
    "cancion": "dead memories",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "aerials",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "lonely day",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "psycho",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "revenga",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "sad statue",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "roulette",
    "genero": "nu-metal"
    },
    {
    "artista":"system of a down",
    "cancion": "toxicity",
    "genero": "nu-metal"
    },
    {
    "artista":"green day",
    "cancion": "american idiot",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "basket case",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "boulevard of the broken dreams",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "chump",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "21 guns",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "holiday",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "lady cobra",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "oh love",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "she",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "whatsername",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "longview",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "wake me up when september ends",
    "genero": "punk-rock"
    },
    {
    "artista":"green day",
    "cancion": "when i come around",
    "genero": "punk-rock"
    },
    {
    "artista":"the ramones",
    "cancion": "i love you",
    "genero": "punk-rock"
    },
    {
    "artista":"the ramones",
    "cancion": "blitzkrieg bop",
    "genero": "punk-rock"
    },
    {
    "artista":"the ramones",
    "cancion": "i wanna be sedated",
    "genero": "punk-rock"
    },
    {
    "artista":"nirvana",
    "cancion": "in bloom",
    "genero": "grunge"
    },
    {
    "artista":"nirvana",
    "cancion": "scoff",
    "genero": "grunge"
    },
    {
    "artista":"nirvana",
    "cancion": "love buzz",
    "genero": "grunge"
    },
    {
    "artista":"alice in chains",
    "cancion": "man in the box",
    "genero": "grunge"
    },
    {
    "artista":"alice in chains",
    "cancion": "them bones",
    "genero": "grunge"
    },
    {
    "artista":"alice in chains",
    "cancion": "would?",
    "genero": "grunge"
    },
    {
    "artista":"alice in chains",
    "cancion": "got me wrong",
    "genero": "grunge"
    },
    {
    "artista":"iron maiden",
    "cancion": "aces high",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "dance of death",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "fear of the dark",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "phantom of the opera",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "run to the hills",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "the number of the beast",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "the trooper",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "the wicker man",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "wasted years",
    "genero": "heavy metal"
    },
    {
    "artista":"iron maiden",
    "cancion": "2 minutes to midnight",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "paranoid",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "iron man",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "lady evil",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "N.I.B",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "electric funeral",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "rat salad",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "war pig",
    "genero": "heavy metal"
    },
    {
    "artista":"black sabbath",
    "cancion": "crazy train",
    "genero": "heavy metal"
    },
    {
    "artista":"blink 182",
    "cancion": "always",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "adam's song",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "feeling this",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "all of this",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "asthenia",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "carousel",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "down",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "easy target",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "first date",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "go",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "here's tou letter",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "i miss you",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "i'm lost without you",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "obvious",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "stockholm syndrome",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "violence",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "dammit",
    "genero": "punk-rock"
    },
    {
    "artista":"blink 182",
    "cancion": "mutt",
    "genero": "punk-rock"
    },
    {
    "artista":"megadeth",
    "cancion": "addicted to chaos",
    "genero": "thrash metal"
    },
    {
    "artista":"megadeth",
    "cancion": "die dead enough",
    "genero": "thrash metal"
    },
    {
    "artista":"megadeth",
    "cancion": "in my darkest hour",
    "genero": "thrash metal"
    },
    {
    "artista":"megadeth",
    "cancion": "trust",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "enter sandman",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "master of puppets",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "fuel",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "my apocalypse",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "nothing else matters",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "one",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "sad but true",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "seek and destroy",
    "genero": "thrash metal"
    },
    {
    "artista":"metallica",
    "cancion": "whiskey in the jar",
    "genero": "thrash metal"
    },
]

@app.get("/tracks")
async def imprimir():
    print(len(tracks))
    return {"Total": tracks}

@app.get("/tracks/canciones")
async def mostrar_canciones():
    o = {}
    fl = []
    for i in range(len(tracks)):
        o[i] = tracks[i]["cancion"]
        fl.append(o[i].title())
    return {"Tracks": fl}
    
@app.get("/tracks/artistas")
async def mostrar_artistas():
    o = {}
    fl = []
    for i in range(len(tracks)):
        o[i] = tracks[i]["artista"]
        fl.append(o[i].title())
    return {"Artistas": fl}
    
@app.get("/tracks/generos")
async def mostrar_generos():
    o = {}
    fl = []
    for i in range(len(tracks)):
        o[i] = tracks[i]["genero"]
        fl.append(o[i].title())
    return {"Generos": fl}

@app.get("/tracks/nirvana")
async def artista_nirvana():
    o = {}
    fl = []
    for i in range(len(tracks)):
        if tracks[i]["artista"] == "nirvana":
            fl.append(tracks[i])
    return {"Nirvana": fl}
    
@app.get("/tracks/nirvana/canciones")
async def canciones_nirvana():
    fl = []
    for i in range(len(tracks)):
        if tracks[i]["artista"] == "nirvana":
            fl.append(tracks[i]["cancion"])
    return {"Nirvana": fl}
    
@app.get("/tracks/artistas/genero")
async def mostrar_canciones():
    o = {}
    for i in range(len(tracks)):
        # ~ tracks[i]["artista"] = tracks[i]["genero"]
        o[tracks[i]["artista"] ] = tracks[i]["genero"]
    return {"Genero-Artista": o}
    
@app.get("/tracks/artistas/canciones")
async def artistas_canciones():
    o = {}
    for i in range(len(tracks)):
        # ~ tracks[i]["artista"] = tracks[i]["genero"]
        o[tracks[i]["artista"] ] = tracks[i]["cancion"]
    return {"Genero-Artista": o}



from fastapi import FastAPI
from pydantic import BaseModel

import random

#Objeto
app = FastAPI()

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
Tracks(Id=25, Artista="system of a down", Cancion="lonely day", Genero="nu-metal", Year=2020, Rate=10),
Tracks(Id=26, Artista="system of a down", Cancion="psycho", Genero="nu-metal", Year=1991, Rate=4),
Tracks(Id=27, Artista="system of a down", Cancion="revenga", Genero="nu-metal", Year=2005, Rate=6),
Tracks(Id=28, Artista="system of a down", Cancion="sad statue", Genero="nu-metal", Year=2013, Rate=3),
Tracks(Id=29, Artista="system of a down", Cancion="roulette", Genero="nu-metal", Year=2018, Rate=4),
Tracks(Id=30, Artista="system of a down", Cancion="toxicity", Genero="nu-metal", Year=1990, Rate=6),
Tracks(Id=31, Artista="green day", Cancion="american idiot", Genero="punk-rock", Year=2022, Rate=5),
Tracks(Id=32, Artista="green day", Cancion="basket case", Genero="punk-rock", Year=2004, Rate=9),
Tracks(Id=33, Artista="green day", Cancion="boulevard of the broken dreams", Genero="punk-rock", Year=1992, Rate=7),
Tracks(Id=34, Artista="green day", Cancion="chump", Genero="punk-rock", Year=2009, Rate=4),
Tracks(Id=35, Artista="green day", Cancion="21 guns", Genero="punk-rock", Year=1995, Rate=6),
Tracks(Id=36, Artista="green day", Cancion="holiday", Genero="punk-rock", Year=2016, Rate=1),
Tracks(Id=37, Artista="green day", Cancion="lady cobra", Genero="punk-rock", Year=2008, Rate=1),
Tracks(Id=38, Artista="green day", Cancion="oh love", Genero="punk-rock", Year=1999, Rate=4),
Tracks(Id=39, Artista="green day", Cancion="she", Genero="punk-rock", Year=2024, Rate=3),
Tracks(Id=40, Artista="green day", Cancion="whatsername", Genero="punk-rock", Year=2015, Rate=5),
Tracks(Id=41, Artista="green day", Cancion="longview", Genero="punk-rock", Year=1995, Rate=9),
Tracks(Id=42, Artista="green day", Cancion="wake me up when september ends", Genero="punk-rock", Year=2003, Rate=4),
Tracks(Id=43, Artista="green day", Cancion="when i come around", Genero="punk-rock", Year=2000, Rate=1),
Tracks(Id=44, Artista="the ramones", Cancion="i love you", Genero="punk-rock", Year=1996, Rate=7),
Tracks(Id=45, Artista="the ramones", Cancion="blitzkrieg bop", Genero="punk-rock", Year=2017, Rate=5),
Tracks(Id=46, Artista="the ramones", Cancion="i wanna be sedated", Genero="punk-rock", Year=2019, Rate=9),
Tracks(Id=47, Artista="nirvana", Cancion="in bloom", Genero="grunge", Year=2020, Rate=2),
Tracks(Id=48, Artista="nirvana", Cancion="scoff", Genero="grunge", Year=2000, Rate=3),
Tracks(Id=49, Artista="nirvana", Cancion="love buzz", Genero="grunge", Year=2000, Rate=3),
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
Tracks(Id=75, Artista="blink 182", Cancion="all of this", Genero="punk-rock", Year=2016, Rate=6),
Tracks(Id=76, Artista="blink 182", Cancion="asthenia", Genero="punk-rock", Year=1990, Rate=3),
Tracks(Id=77, Artista="blink 182", Cancion="carousel", Genero="punk-rock", Year=1999, Rate=2),
Tracks(Id=78, Artista="blink 182", Cancion="down", Genero="punk-rock", Year=2020, Rate=10),
Tracks(Id=79, Artista="blink 182", Cancion="easy target", Genero="punk-rock", Year=2022, Rate=7),
Tracks(Id=80, Artista="blink 182", Cancion="first date", Genero="punk-rock", Year=1994, Rate=9),
Tracks(Id=81, Artista="blink 182", Cancion="go", Genero="punk-rock", Year=2013, Rate=6),
Tracks(Id=82, Artista="blink 182", Cancion="here's tou letter", Genero="punk-rock", Year=2011, Rate=8),
Tracks(Id=83, Artista="blink 182", Cancion="i miss you", Genero="punk-rock", Year=1995, Rate=10),
Tracks(Id=84, Artista="blink 182", Cancion="i'm lost without you", Genero="punk-rock", Year=2005, Rate=8),
Tracks(Id=85, Artista="blink 182", Cancion="obvious", Genero="punk-rock", Year=1990, Rate=1),
Tracks(Id=86, Artista="blink 182", Cancion="stockholm syndrome", Genero="punk-rock", Year=2005, Rate=6),
Tracks(Id=87, Artista="blink 182", Cancion="violence", Genero="punk-rock", Year=2019, Rate=6),
Tracks(Id=88, Artista="blink 182", Cancion="dammit", Genero="punk-rock", Year=2011, Rate=8),
Tracks(Id=89, Artista="blink 182", Cancion="mutt", Genero="punk-rock", Year=1994, Rate=8),
Tracks(Id=90, Artista="megadeth", Cancion="addicted to chaos", Genero="thrash metal", Year=2021, Rate=6),
Tracks(Id=91, Artista="megadeth", Cancion="die dead enough", Genero="thrash metal", Year=2015, Rate=3),
Tracks(Id=92, Artista="megadeth", Cancion="in my darkest hour", Genero="thrash metal", Year=2006, Rate=5),
Tracks(Id=93, Artista="megadeth", Cancion="trust", Genero="thrash metal", Year=2002, Rate=8),
Tracks(Id=94, Artista="metallica", Cancion="enter sandman", Genero="thrash metal", Year=2024, Rate=5),
Tracks(Id=95, Artista="metallica", Cancion="master of puppets", Genero="thrash metal", Year=1998, Rate=10),
Tracks(Id=96, Artista="metallica", Cancion="fuel", Genero="thrash metal", Year=1996, Rate=5),
Tracks(Id=97, Artista="metallica", Cancion="my apocalypse", Genero="thrash metal", Year=2017, Rate=10),
Tracks(Id=98, Artista="metallica", Cancion="nothing else matters", Genero="thrash metal", Year=2002, Rate=6),
Tracks(Id=99, Artista="metallica", Cancion="one", Genero="thrash metal", Year=2018, Rate=1),
Tracks(Id=100, Artista="metallica", Cancion="sad but true", Genero="thrash metal", Year=2005, Rate=9),
Tracks(Id=101, Artista="metallica", Cancion="seek and destroy", Genero="thrash metal", Year=2018, Rate=4),
Tracks(Id=102, Artista="metallica", Cancion="whiskey in the jar", Genero="thrash metal", Year=2019, Rate=8),
Tracks(Id=103, Artista="metallica", Cancion="enter sandman", Genero="thrash metal", Year=2000, Rate=4),
Tracks(Id=104, Artista="metallica", Cancion="one", Genero="thrash metal", Year=2004, Rate=1),
Tracks(Id=105, Artista="metallica", Cancion="fuel", Genero="thrash metal", Year=2012, Rate=8),
Tracks(Id=106, Artista="metallica", Cancion="battery", Genero="thrash metal", Year=1996, Rate=8),
Tracks(Id=107, Artista="metallica", Cancion="the day that never comes ", Genero="thrash metal", Year=1994, Rate=7),
Tracks(Id=108, Artista="nirvana", Cancion="dumb", Genero="grunge", Year=2019, Rate=8),
Tracks(Id=109, Artista="nirvana", Cancion="all apologies", Genero="grunge", Year=2014, Rate=7),
Tracks(Id=110, Artista="nirvana", Cancion="polly", Genero="grunge", Year=1998, Rate=8),
Tracks(Id=111, Artista="nirvana", Cancion="very ape", Genero="grunge", Year=2015, Rate=10),
Tracks(Id=112, Artista="nirvana", Cancion="oh, me", Genero="grunge", Year=1995, Rate=1),
Tracks(Id=113, Artista="nirvana", Cancion="downer", Genero="grunge", Year=1993, Rate=4),
Tracks(Id=114, Artista="nirvana", Cancion="sappy", Genero="grunge", Year=2000, Rate=4),
Tracks(Id=115, Artista="nirvana", Cancion="stain", Genero="grunge", Year=2014, Rate=1),
Tracks(Id=116, Artista="nirvana", Cancion="about a girl", Genero="grunge", Year=2021, Rate=6),
Tracks(Id=117, Artista="nirvana", Cancion="milk it", Genero="grunge", Year=2024, Rate=6),
Tracks(Id=118, Artista="nirvana", Cancion="school", Genero="grunge", Year=2007, Rate=5),
Tracks(Id=119, Artista="nirvana", Cancion="dive", Genero="grunge", Year=2024, Rate=6),
Tracks(Id=120, Artista="nirvana", Cancion="d-7", Genero="grunge", Year=1998, Rate=10),
Tracks(Id=121, Artista="nirvana", Cancion="lithium", Genero="grunge", Year=2017, Rate=3),
Tracks(Id=122, Artista="nirvana", Cancion="lounge act", Genero="grunge", Year=1996, Rate=6),
Tracks(Id=123, Artista="nirvana", Cancion="blew", Genero="grunge", Year=1991, Rate=7),
Tracks(Id=124, Artista="nirvana", Cancion="aero zeppelin", Genero="grunge", Year=1995, Rate=2),
Tracks(Id=125, Artista="linkin park", Cancion="dont' stay", Genero="nu-metal", Year=2021, Rate=4),
Tracks(Id=126, Artista="linkin park", Cancion="somewhere i belong", Genero="nu-metal", Year=2020, Rate=4),
Tracks(Id=127, Artista="linkin park", Cancion="lying frim you", Genero="nu-metal", Year=1997, Rate=10),
Tracks(Id=128, Artista="linkin park", Cancion="hit the floor", Genero="nu-metal", Year=2019, Rate=1),
Tracks(Id=129, Artista="linkin park", Cancion="easier to run", Genero="nu-metal", Year=1995, Rate=10),
Tracks(Id=130, Artista="linkin park", Cancion="faint", Genero="nu-metal", Year=2010, Rate=10),
Tracks(Id=131, Artista="linkin park", Cancion="figure.09", Genero="nu-metal", Year=2015, Rate=5),
Tracks(Id=132, Artista="linkin park", Cancion="breaking the habit", Genero="nu-metal", Year=2005, Rate=10),
Tracks(Id=133, Artista="linkin park", Cancion="from the inside", Genero="nu-metal", Year=2010, Rate=10),
Tracks(Id=134, Artista="linkin park", Cancion="nobody's listenig", Genero="nu-metal", Year=2015, Rate=7),
Tracks(Id=135, Artista="linkin park", Cancion="numb", Genero="nu-metal", Year=2020, Rate=10),
Tracks(Id=136, Artista="linkin park", Cancion="the catalyst", Genero="nu-metal", Year=2012, Rate=3),
Tracks(Id=137, Artista="linkin park", Cancion="in the end", Genero="nu-metal", Year=1992, Rate=9),
Tracks(Id=138, Artista="linkin park", Cancion="crawling", Genero="nu-metal", Year=1994, Rate=9),
Tracks(Id=139, Artista="linkin park", Cancion="bleed it out", Genero="nu-metal", Year=1994, Rate=7),
Tracks(Id=140, Artista="foo fighters", Cancion="everlong", Genero="rock", Year=2012, Rate=3),
Tracks(Id=141, Artista="foo fighters", Cancion="the pretender", Genero="rock", Year=2002, Rate=8),
Tracks(Id=142, Artista="foo fighters", Cancion="best of you", Genero="rock", Year=2018, Rate=7),
Tracks(Id=143, Artista="foo fighters", Cancion="my hero", Genero="rock", Year=2018, Rate=5),
Tracks(Id=144, Artista="foo fighters", Cancion="rope", Genero="rock", Year=1998, Rate=4),
Tracks(Id=145, Artista="foo fighters", Cancion="these days", Genero="rock", Year=2022, Rate=4),
Tracks(Id=146, Artista="foo fighters", Cancion="walk", Genero="rock", Year=2003, Rate=3),
Tracks(Id=147, Artista="foo fighters", Cancion="run", Genero="rock", Year=1990, Rate=1),
Tracks(Id=148, Artista="foo fighters", Cancion="let it die", Genero="rock", Year=2023, Rate=6),
Tracks(Id=149, Artista="foo fighters", Cancion="come alive", Genero="rock", Year=1993, Rate=8),
Tracks(Id=150, Artista="foo fighters", Cancion="long road to ruin", Genero="rock", Year=2000, Rate=1),
Tracks(Id=151, Artista="foo fighters", Cancion="in your honor", Genero="rock", Year=1992, Rate=8),
Tracks(Id=152, Artista="foo fighters", Cancion="no way back", Genero="rock", Year=2022, Rate=4),
Tracks(Id=153, Artista="foo fighters", Cancion="the last song", Genero="rock", Year=2002, Rate=6),
Tracks(Id=154, Artista="exwhyz", Cancion="d.y.d", Genero="j-pop", Year=2000, Rate=10),
Tracks(Id=155, Artista="exwhyz", Cancion="stay with me", Genero="j-pop", Year=1999, Rate=1),
Tracks(Id=156, Artista="exwhyz", Cancion="obsession", Genero="j-pop", Year=1995, Rate=7),
Tracks(Id=157, Artista="exwhyz", Cancion="4:00 a.m", Genero="j-pop", Year=2023, Rate=10),
Tracks(Id=158, Artista="exwhyz", Cancion="weekend", Genero="j-pop", Year=2005, Rate=4),
Tracks(Id=159, Artista="exwhyz", Cancion="wanna dance", Genero="j-pop", Year=2006, Rate=2),
Tracks(Id=160, Artista="exwhyz", Cancion="you and me", Genero="j-pop", Year=2015, Rate=6),
Tracks(Id=161, Artista="exwhyz", Cancion="higher", Genero="j-pop", Year=2003, Rate=10),
Tracks(Id=162, Artista="exwhyz", Cancion="universe", Genero="j-pop", Year=2002, Rate=10),
Tracks(Id=163, Artista="exwhyz", Cancion="blaze", Genero="j-pop", Year=2001, Rate=6),
Tracks(Id=164, Artista="exwhyz", Cancion="des speeching", Genero="j-pop", Year=1992, Rate=7),
Tracks(Id=165, Artista="exwhyz", Cancion="answer", Genero="j-pop", Year=2005, Rate=3),
Tracks(Id=166, Artista="exwhyz", Cancion="dive", Genero="j-pop", Year=2005, Rate=10),
Tracks(Id=167, Artista="exwhyz", Cancion="lets's show", Genero="j-pop", Year=2014, Rate=8),
Tracks(Id=168, Artista="exwhyz", Cancion="chase your back", Genero="j-pop", Year=2023, Rate=9),
Tracks(Id=169, Artista="exwhyz", Cancion="iza!!", Genero="j-pop", Year=2002, Rate=4),
Tracks(Id=170, Artista="exwhyz", Cancion="happy with you", Genero="j-pop", Year=2010, Rate=2),
Tracks(Id=171, Artista="exwhyz", Cancion="error", Genero="j-pop", Year=2002, Rate=4),
Tracks(Id=172, Artista="exwhyz", Cancion="haggling", Genero="j-pop", Year=2014, Rate=6),
Tracks(Id=173, Artista="exwhyz", Cancion="hon-no", Genero="j-pop", Year=2013, Rate=3),
Tracks(Id=174, Artista="exwhyz", Cancion="rather", Genero="j-pop", Year=2011, Rate=9),
Tracks(Id=175, Artista="exwhyz", Cancion="have it my way", Genero="j-pop", Year=1999, Rate=2),
Tracks(Id=176, Artista="exwhyz", Cancion="right now", Genero="j-pop", Year=2013, Rate=3),
Tracks(Id=177, Artista="exwhyz", Cancion="tokyo moonlight", Genero="j-pop", Year=2017, Rate=5),
Tracks(Id=178, Artista="fuzzy bumble", Cancion="any other way", Genero="rock inde", Year=2002, Rate=1),
Tracks(Id=179, Artista="fuzzy bumble", Cancion="psychotic defect", Genero="rock inde", Year=2004, Rate=4),
Tracks(Id=180, Artista="fuzzy bumble", Cancion="nadasé", Genero="rock inde", Year=2012, Rate=10),
Tracks(Id=181, Artista="fuzzy bumble", Cancion="to kiss with concentration", Genero="rock inde", Year=2015, Rate=1),
Tracks(Id=182, Artista="velvet revolver", Cancion="let it roll", Genero="hard rock", Year=2002, Rate=8),
Tracks(Id=183, Artista="velvet revolver", Cancion="sucker train blues", Genero="hard rock", Year=1995, Rate=6),
Tracks(Id=184, Artista="velvet revolver", Cancion="set me free", Genero="hard rock", Year=2022, Rate=3),
Tracks(Id=185, Artista="velvet revolver", Cancion="slither", Genero="hard rock", Year=2017, Rate=8),
Tracks(Id=186, Artista="depeche mode", Cancion="enjoy the silence", Genero="rock", Year=2016, Rate=8),
Tracks(Id=187, Artista="depeche mode", Cancion="ghosts again", Genero="electronic rock", Year=2005, Rate=4),
Tracks(Id=188, Artista="depeche mode", Cancion="wrong", Genero="electronic  rock", Year=2008, Rate=6),
Tracks(Id=189, Artista="depeche mode", Cancion="precious", Genero="electronic rock", Year=2010, Rate=6),
Tracks(Id=190, Artista="soundgarden", Cancion="black hole sun", Genero="grunge", Year=2008, Rate=8),
Tracks(Id=191, Artista="audioslave", Cancion="like a stone", Genero="rock", Year=2013, Rate=7),
Tracks(Id=192, Artista="audioslave", Cancion="be yourself", Genero="rock", Year=2017, Rate=1),
Tracks(Id=193, Artista="audioslave", Cancion="i am the highway", Genero="rock", Year=2023, Rate=9),
Tracks(Id=194, Artista="audioslave", Cancion="gasoline", Genero="rock", Year=2005, Rate=2),
Tracks(Id=195, Artista="audioslave", Cancion="revelations", Genero="rock", Year=2005, Rate=6),
Tracks(Id=196, Artista="audioslave", Cancion="light my way", Genero="rock", Year=2019, Rate=10),
Tracks(Id=197, Artista="audioslave", Cancion="set it off", Genero="rock", Year=2007, Rate=3),
Tracks(Id=198, Artista="audioslave", Cancion="what you are", Genero="rock", Year=1991, Rate=2),
Tracks(Id=199, Artista="audioslave", Cancion="your time has coming", Genero="rock", Year=1997, Rate=10),
Tracks(Id=200, Artista="audioslave", Cancion="the worm", Genero="rock", Year=2014, Rate=10),
Tracks(Id=201, Artista="audioslave", Cancion="out of exile", Genero="rock", Year=2005, Rate=10),
Tracks(Id=202, Artista="audioslave", Cancion="spoonman", Genero="rock", Year=2001, Rate=3),
]

        
#***Get con Filtro Query: Year

#Busqueda por año, muestra solo el primer resultado que encunetre
@app.get("/tracksclass/")
async def trackssclass(Year:int):
    tracks_l = filter(lambda track: track.Year == Year, tracks) #Función de orden superior
    try:
        return list(tracks_l )[0]
    except:
        return{"error": "track no encontrado!"}

#Busqueda por año y artista, regresa una lista con todas las coincidencias
@app.get("/tracksclass/year-artista")
async def trackssclass(Year:int, Artista:str):
    tracks_l = filter(lambda track: track.Year == Year, tracks) #Función de orden superior
    tracks_l2 = filter(lambda track: track.Artista == Artista, tracks_l) 
    try:
        return list(tracks_l2)
    except:
        return{"error": "tracks no encontrado!"}

#Busqueda por año y genero, regresa una lista con todas las coincidencias
@app.get("/tracksclass/genero-year")
async def trackssclass(Genero:str, Year:int):
    tracks_l = filter(lambda track: track.Genero == Genero, tracks) #Función de orden superior
    tracks_l2 = filter(lambda track: track.Year == Year, tracks_l) 
    try:
        return list(tracks_l2)
    except:
        return{"error": "tracks no encontrado!"}

#Busqueda por año, genero y calificación, regresa una lista con todas las coincidencias
@app.get("/tracksclass/year-genero-rate")
async def trackssclass(Year:int, Genero:str, Rate: int):
    tracks_l = filter(lambda track: track.Year == Year, tracks) #Función de orden superior
    tracks_l2 = filter(lambda track: track.Genero == Genero, tracks_l) #Función de orden superior
    tracks_l3 = filter(lambda track: track.Rate == Rate, tracks_l2) 
    try:
        return list(tracks_l2)
    except:
        return{"error": "tracks no encontrado!"}

#Busqueda por año, artista y calificación, regresa una lista con todas las coincidencias
@app.get("/tracksclass/artista-year-rate")
async def trackssclass(Year:int, Artista:str, Rate: int):
    tracks_l = filter(lambda track: track.Year == Year, tracks) #Función de orden superior
    tracks_l2 = filter(lambda track: track.Artista == Artista, tracks_l) #Función de orden superior
    tracks_l3 = filter(lambda track: track.Rate == Rate, tracks_l2) 
    try:
        return list(tracks_l2)
    except:
        return{"error": "tracks no encontrado!"}

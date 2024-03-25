import py5
from bidang.PersegiPanjang import PersegiPanjang
from latar.darat_laut_langit import Darat_laut_langit
from latar.gunung import Gunung
from latar.pantai_sungai import Pantai
from latar.awan import Awan
from latar.evaporasi import Evaporasi
from latar.hujan import Hujan
from latar.gedung import Gedung
from latar.jalan import Jalan
from latar.pohon import Pohon
from latar.matahari import Matahari
from latar.mobil import Mobil

darat_laut = Darat_laut_langit(0, 0)
gunung = Gunung(0,0)
pantai = Pantai(0,0)
awan1 = Awan(-200,100,50)
awan2 = Awan(25,150,100)
evaporasi = Evaporasi(-250,100,450)
hujan = Hujan(0,0,300)
gedung = Gedung(0,0)
jalan = Jalan(0,0)
pohon = Pohon(0,0)
matahari = Matahari(0,0)
mobil = Mobil(0,0,400)
a = 0
b = 0
c = 0
dx = 2  

def setup():
    py5.size(800, 700)
    py5.stroke_weight(2)

def draw():
    py5.background(255, 255, 255, 255)
    global a, b, c, dx

    matahari.draw()
    awan1.draw()
    awan1.move(10,-10)
    awan2.draw()
    awan2.move(20,0)
    gedung.draw()
    pohon.draw()
    jalan.draw()
    mobil.draw()
    mobil.move(15,0)

py5.run_sketch()

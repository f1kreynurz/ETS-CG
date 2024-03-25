from primitif.color import Colors
class Gedung:
    def __init__(self, x, y, scale=1):
        from bidang.PersegiPanjang import PersegiPanjang
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.gedung = PersegiPanjang(self.x - 300, self.y + 100, 200, 300)
        self.jendelaGedung = PersegiPanjang(self.x - 275, self.y - 40, 40, 40)
        self.jendelaGedung1 = PersegiPanjang(self.x - 165, self.y - 40, 40, 40)
        self.jendelaGedung2 = PersegiPanjang(self.x - 275, self.y + 60, 40, 40)
        self.jendelaGedung3 = PersegiPanjang(self.x - 165, self.y + 60, 40, 40)

        self.gedung1 = PersegiPanjang(self.x - 100, self.y + 150, 200, 350)
        self.jendelaGedung4 = PersegiPanjang(self.x - 75, self.y + 10, 40, 40)
        self.jendelaGedung5 = PersegiPanjang(self.x + 35, self.y + 10, 40, 40)
        self.jendelaGedung6 = PersegiPanjang(self.x - 75, self.y + 110, 40, 40)
        self.jendelaGedung7 = PersegiPanjang(self.x + 35, self.y + 110, 40, 40)

        self.gedung2 = PersegiPanjang(self.x + 100, self.y + 100, 200, 300)
        self.jendelaGedung8 = PersegiPanjang(self.x + 125, self.y - 40, 40, 40)
        self.jendelaGedung9 = PersegiPanjang(self.x + 235, self.y - 40, 40, 40)
        self.jendelaGedung10 = PersegiPanjang(self.x + 125, self.y + 60, 40, 40)
        self.jendelaGedung11 = PersegiPanjang(self.x + 235, self.y + 60, 40, 40)
        
    def draw(self):
        self.gedung.draw()
        self.jendelaGedung.draw()
        self.jendelaGedung1.draw()
        self.jendelaGedung2.draw()
        self.jendelaGedung3.draw()

        self.gedung1.draw()
        self.jendelaGedung4.draw()
        self.jendelaGedung5.draw()
        self.jendelaGedung6.draw()
        self.jendelaGedung7.draw()
        
        self.gedung2.draw()
        self.jendelaGedung8.draw()
        self.jendelaGedung9.draw()
        self.jendelaGedung10.draw()
        self.jendelaGedung11.draw()
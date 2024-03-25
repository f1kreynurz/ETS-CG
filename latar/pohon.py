from primitif.color import Colors
class Pohon:
    def __init__(self, x, y, scale=1):
        from bidang.SegitigaKanan import SegitigaKanan
        from bidang.SegitigaKiri import SegitigaKiri
        from bidang.PersegiPanjang import PersegiPanjang
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.batangKiri = PersegiPanjang(self.x - 360, self.y - 100, 20, 100)
        self.pohonKiri1 = SegitigaKanan(self.x - 350, self.y - 100, 45, 100)
        self.pohonKiri2 = SegitigaKiri(self.x - 394, self.y - 100, 45, 100)
        self.pohonKiriAtas1 = SegitigaKanan(self.x - 350, self.y - 50, 35, 75)
        self.pohonKiriAtas2 = SegitigaKiri(self.x - 384, self.y - 50, 35, 75)

        self.batangKanan = PersegiPanjang(self.x + 345, self.y - 100, 20, 100)
        self.pohonKanan1 = SegitigaKanan(self.x + 354, self.y - 100, 45, 100)
        self.pohonKanan2 = SegitigaKiri(self.x + 310, self.y - 100, 45, 100)
        self.pohonKananAtas1 = SegitigaKanan(self.x + 354, self.y - 50, 35, 75)
        self.pohonKananAtas2 = SegitigaKiri(self.x + 320, self.y - 50, 35, 75)
        
    def draw(self):
        self.batangKiri.draw()
        self.pohonKiri1.draw()
        self.pohonKiri2.draw()
        self.pohonKiriAtas1.draw()
        self.pohonKiriAtas2.draw()

        self.batangKanan.draw()
        self.pohonKanan1.draw()
        self.pohonKanan2.draw()
        self.pohonKananAtas1.draw()
        self.pohonKananAtas2.draw()
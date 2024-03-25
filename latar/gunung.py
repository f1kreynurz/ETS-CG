from primitif.color import Colors
class Gunung:
    def __init__(self, x, y, scale=1):
        from bidang.SegitigaKanan import SegitigaKanan
        from bidang.SegitigaKiri import SegitigaKiri
        
        self.x = x
        self.y = y
        self.scale = scale
        self.gunung_kanan1 = SegitigaKanan(self.x + 375, self.y - 250, 75, 150)
        self.gunung_kanan2 = SegitigaKiri(self.x + 300, self.y - 250, 75, 150)
        self.gunung_kiri1 = SegitigaKanan(self.x + 215, self.y - 250, 50, 100)
        self.gunung_kiri2 = SegitigaKiri(self.x + 165, self.y - 250, 50, 100)
        self.gunung_tengah1 = SegitigaKanan(self.x + 300, self.y - 250, 100, 200)
        self.gunung_tengah2 = SegitigaKiri(self.x + 200, self.y - 250, 100, 200)
        
    def draw(self):
        self.gunung_kanan1.draw()
        self.gunung_kanan2.draw()
        self.gunung_kiri1.draw()
        self.gunung_kiri2.draw()
        self.gunung_tengah1.draw()
        self.gunung_tengah2.draw()
        
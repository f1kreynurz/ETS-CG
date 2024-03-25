from primitif.color import Colors
class Jalan:
    def __init__(self, x, y, scale=1):
        from bidang.PersegiPanjang import PersegiPanjang
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.trotoar = PersegiPanjang(self.x - 400, self.y - 200, 800, 20)
        self.aspal = PersegiPanjang(self.x - 400, self.y - 220, 800, 180)
        self.garisAspal1 = PersegiPanjang(self.x - 300, self.y - 300, 200, 20)
        self.garisAspal2 = PersegiPanjang(self.x + 50, self.y - 300, 200, 20)

        
    def draw(self):
        self.trotoar.draw()
        self.aspal.draw()
        self.garisAspal1.draw()
        self.garisAspal2.draw()
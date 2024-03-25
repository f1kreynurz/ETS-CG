from primitif.color import Colors
class Darat_laut_langit:
    def __init__(self, x, y, scale=1):
        from bidang.PersegiPanjang import PersegiPanjang
        from bidang.lingkaran import Lingkaran
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.matahari =  Lingkaran(self.x - 280, self.y + 200, 50)
        self.laut = PersegiPanjang(self.x - 400, self.y - 250, 450, 150, c=self.__colors.biru_laut)
        self.daratan = PersegiPanjang(self.x + 150, self.y - 250, 250, 150)
        
    def draw(self):
        self.matahari.draw()
        self.laut.draw()
        self.daratan.draw()
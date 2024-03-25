from bidang.Bidang import Bidang
from primitif.color import Colors
from primitif import basic


class Trapesium(Bidang):
    def __init__(self, x, y, aa, ab, tinggi, tm=None, c= Colors.biru_laut):
        super().__init__(x, y, tm, c)
        self.aa = aa
        self.ab = ab
        self.tinggi = tinggi

    def draw(self, c, fill_color):
        trapesium = basic.trapesium_siku(self.x, self.y, self.aa, self.ab, self.tinggi)
        basic.draw_bentuk_filled(trapesium, c, fill_color)
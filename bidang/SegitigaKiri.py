from bidang.Bidang import Bidang
from primitif.color import Colors
from primitif import basic


class SegitigaKiri(Bidang):
    def __init__(self, x, y, alas, tinggi, tm=None, c=Colors.hitam):
        super().__init__(x, y, tm, c)
        self.alas = alas
        self.tinggi = tinggi

    def draw(self):
        super().draw(basic.segitiga_kiri(self.x, self.y, self.alas, self.tinggi))
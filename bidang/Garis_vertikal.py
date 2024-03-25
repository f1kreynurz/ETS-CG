from bidang.Bidang import Bidang
from primitif.color import Colors
from primitif import basic


class GarisVertikal(Bidang):
    def __init__(self, x, y, panjang, tm=None, c= Colors.hitam):
        super().__init__(x, y, tm, c)
        self.panjang = panjang

    def draw(self):
        super().draw(basic.garis_vertikal(self.x, self.y, self.panjang))
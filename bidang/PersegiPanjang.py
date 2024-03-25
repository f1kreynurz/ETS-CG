from bidang.Bidang import Bidang
from primitif.color import Colors
from primitif import basic


class PersegiPanjang(Bidang):
    def __init__(self, x, y, panjang, lebar, tm=None, c= Colors.hitam):
        super().__init__(x, y, tm, c)
        self.panjang = panjang
        self.lebar = lebar

    def draw(self):
        super().draw(basic.persegi_panjang(self.x, self.y, self.panjang, self.lebar))
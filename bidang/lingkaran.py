from bidang.Bidang import Bidang
from primitif.color import Colors
from primitif import basic


class Lingkaran(Bidang):
    def __init__(self, x, y, r,  tm=None, c= Colors.hitam):
        super().__init__(x, y, tm, c)
        self.r = r

    def draw(self):
        super().draw(basic.lingkaran(self.x, self.y, self.r))

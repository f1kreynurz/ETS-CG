from bidang.Bidang import Bidang
from primitif import basic
from primitif.color import Colors


class Ellips(Bidang):
    def __init__(self, x, y, Rx, Ry, tm=None, c= Colors.hitam):
        super().__init__(x, y)
        self.Rx = Rx
        self.Ry = Ry

    def draw(self):
        super().draw(basic.ellips(self.x, self.y, self.Rx, self.Ry))
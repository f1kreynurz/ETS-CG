from primitif import basic, transformasiv2
from primitif.utility import convert_to_cartesian

class Bidang:
    def __init__(self, x, y, tm=None, c=[0,0,0,255]):
        self.x, self.y = convert_to_cartesian(x, y)
        self.tm = tm
        self.c = c
        self.a = 0

        self.axis_x = 'x'
        self.axis_y = 'y'

    def draw(self, bidang):
        basic.draw_bentuk(
            transformasiv2.transformPoints2D(bidang, self.tm),
            self.c
        )


    def scale(self, sx, sy):
        self.tm = transformasiv2.scale2D(sx, sy, self.x, self.y, self.tm)

    def rotate(self, a, x=None, y=None):
        if a is None or a == 0:
            a = self.a
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.tm = transformasiv2.rotate2D(a, x, y, self.tm)

    def shear(self, kx, ky):
        self.tm = transformasiv2.shear2D(kx, ky, self.x, self.y, self.tm)

    def translate(self, dx, dy):
        self.tm = transformasiv2.translate2D(dx, dy, self.tm)

    def anim_rotate(self, step=1, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.a += step
        self.rotate(self.a, x, y)

    def mirror(self, axis=None, refx=0, refy=0):
        if axis is None:
            axis = 'x'
        refx, refy = convert_to_cartesian(refx, refy)
        self.tm = transformasiv2.mirror2D(axis, refx, refy, self.tm)
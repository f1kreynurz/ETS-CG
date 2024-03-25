import primitif.line
import py5
import numpy as np
import math


def round(x):
    return int(x+0.5)


def draw_margin(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin, margin, width-margin, margin))
    py5.points(primitif.line.line_dda(
        margin, height-margin, width-margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, margin, margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        width-margin, margin, width-margin, height-margin))


def draw_grid(width, height, margin, c=[0, 0, 0, 255]):
    # Sumbu Y
    xa = margin
    ya = 2*margin
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)

    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa, ya, xb, ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa, ya, xa, yb))
        xa = xa + margin


def draw_kartesian(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2, margin, width/2, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, height/2, width-margin, height/2))

def draw_bentuk(pts, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(pts)


def persegi(xa, ya, panjang):
    return np.concatenate(

        [
            primitif.line.line_dda(xa, ya, xa+panjang, ya),
            primitif.line.line_dda(xa, ya+panjang, xa+panjang, ya + panjang),
            primitif.line.line_dda(xa, ya, xa, ya+panjang),
            primitif.line.line_dda(xa+panjang, ya, xa+panjang, ya+panjang),
        ],
        axis=0
    )

def garis_vertikal(xa, ya, panjang):
    return np.concatenate(
        [
            primitif.line.line_dda(xa, ya, xa, ya + panjang),
        ],
        axis=0
    )
    
def persegi_panjang(xa, ya, panjang, lebar):
    return np.concatenate(
        (
            primitif.line.line_dda(xa, ya, xa + panjang, ya),
            primitif.line.line_dda(xa, ya, xa, ya + lebar),
            primitif.line.line_dda(xa, ya + lebar, xa+ panjang, ya + lebar),
            primitif.line.line_dda(xa + panjang, ya + lebar, xa + panjang, ya),
        ),
        axis=0,
    )

    
def segitiga_kanan(xa, ya, alas, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya-tinggi,xa,ya)
            , primitif.line.line_bresenham(xa,ya,xa+alas,ya)
            , primitif.line.line_bresenham(xa+alas,ya,xa,ya-tinggi)
            ),
        axis=0
    )
def segitiga_kiri(xa, ya, alas, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa, ya, xa + alas, ya),
            primitif.line.line_bresenham(xa + alas, ya, xa + alas, ya - tinggi),
            primitif.line.line_bresenham(xa + alas, ya - tinggi, xa, ya)
        ),
        axis=0
    )


def trapesium_siku(xa, ya, aa, ab, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa, ya, xa+aa, ya),
            primitif.line.line_bresenham(xa, ya, xa, ya+tinggi),
            primitif.line.line_bresenham(xa, ya+tinggi, xa+ab, ya+tinggi),
            primitif.line.line_bresenham(xa+aa, ya, xa+ab, ya+tinggi)
        ),
        axis=0
    )


def kali(xa, ya, panjang):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa, ya, xa+panjang, ya+panjang),
            primitif.line.line_bresenham(xa, ya+panjang, xa+panjang, ya)
        ),
        axis=0
    )


def circlePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
    ]
    return res


def lingkaran(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius
    res = circlePlotPoints(xc, yc, x, y)
    while (x < y):
        x += 1
        if (p < 0):
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x-y) + 1

        res = np.concatenate(
            (
                res, circlePlotPoints(xc, yc, x, y)
            ), axis=0)
    return res


def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
    ]
    return np.array(res)

def ellips(xc, yc, Rx, Ry):
    points = []
    x = 0
    y = Ry
    p = round(Ry*Ry - Rx*Rx*Ry + 0.25*Rx*Rx)
    px = 0
    py = 2*Rx*Rx*y

    # Titik awal elips
    points.extend(ellipsePlotPoints(xc, yc, x, y))

    while (px < py):
        x += 1
        px += 2*Ry*Ry
        if (p < 0):
            p += Ry*Ry + px
        else:
            y -= 1
            py -= 2*Rx*Rx
            p += Ry*Ry + px - py
        points.extend(ellipsePlotPoints(xc, yc, x, y))

    p = round(Ry*Ry*(x+0.5)*(x+0.5) + Rx*Rx*(y-1)*(y-1) - Rx*Rx*Ry*Ry)

    while (y > 0):
        y -= 1
        py -= 2*Rx*Rx
        if (p > 0):
            p += Rx*Rx - py
        else:
            x += 1
            px += 2*Ry*Ry
            p += Rx*Rx - py + px
        points.extend(ellipsePlotPoints(xc, yc, x, y))
    
    return np.array(points)
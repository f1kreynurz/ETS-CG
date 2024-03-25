import numpy as np
import math


def translate2D(tx, ty, tm=None):
    # rumus translasi biasa
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    # Mengalikan matriks translasi dengan matriks transformasi yang diberikan
    tm_new = np.dot(tm, translation_matrix)

    return tm_new


def scale2D(sx, sy, refx, refy, tm=None):
    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    # rumus translasi titik referensi ke pusat koordinat
    tm = np.dot(np.array([[1, 0, -refx],
                          [0, 1, -refy],
                          [0, 0, 1]]), tm)
    # rumus skala biasa
    tm = np.dot(np.array([[sx, 0, 0],
                          [0, sy, 0],
                          [0, 0, 1]]), tm)

    # rumus translasi pusat koordinat ke titik referensi
    tm = np.dot(np.array([[1, 0, refx],
                          [0, 1, refy],
                          [0, 0, 1]]), tm)

    return tm


def rotate2D(a, refx, refy, tm=None):
    # Menghitung sudut rotasi dalam radian
    a_rad = math.radians(a)
    cos_a = math.cos(a_rad)
    sin_a = math.sin(a_rad)

    # Membuat matriks translasi titik referensi ke pusat koordinat
    translation_matrix1 = np.array([
        [1, 0, -refx],
        [0, 1, -refy],
        [0, 0, 1]
    ])

    # Membuat matriks translasi pusat koordinat ke titik referensi
    translation_matrix2 = np.array([
        [1, 0, refx],
        [0, 1, refy],
        [0, 0, 1]
    ])

    # Membuat matriks rotasi
    rotation_matrix = np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ])

    if tm is None:
        tm = np.eye(3)

    # Mengalikan matriks rotasi dengan matriks translasi
    rotated_matrix = np.dot(translation_matrix2, np.dot(
        rotation_matrix, translation_matrix1))

    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    # Mengalikan matriks rotasi baru dengan matriks transformasi yang diberikan
    return np.dot(rotated_matrix, tm)


def shear2D(kx, ky, refx, refy, tm=None):
    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    # Membuat matriks shear
    shear_matrix = np.array([
        [1, kx, -refx * kx],
        [ky, 1, -refy * ky],
        [0, 0, 1]
    ])

    return np.dot(shear_matrix, tm)


def mirror2D(axis, refx, refy, tm=None):
    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    if axis.lower() == 'x':
        # Membuat matriks mirror terhadap sumbu x
        mirror_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis.lower() == 'y':
        # Membuat matriks mirror terhadap sumbu y
        mirror_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    else:
        mirror_matrix = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, -1]
        ])

    # Membuat matriks translasi titik referensi ke pusat koordinat
    translation_matrix1 = np.array([
        [1, 0, -refx],
        [0, 1, -refy],
        [0, 0, 1]
    ])

    # Membuat matriks translasi pusat koordinat ke titik referensi
    translation_matrix2 = np.array([
        [1, 0, refx],
        [0, 1, refy],
        [0, 0, 1]
    ])

    # Mengalikan matriks mirror dengan matriks transformasi yang diberikan
    tm_new = np.dot(
        np.dot(
            np.dot(translation_matrix2, mirror_matrix),
            tm
        ),
        translation_matrix1
    )

    return tm_new


def transformPoints2D(pts, tm=None):
    # Jika tm belum diberikan, maka menggunakan matriks identitas
    if tm is None:
        tm = np.eye(3)

    i, _ = pts.shape

    for k in range(i):
        tmp = tm[0][0] * pts[k, 0] + tm[0][1] * pts[k, 1] + tm[0][2]
        pts[k, 1] = tm[1][0] * pts[k, 0] + tm[1][1] * pts[k, 1] + tm[1][2]
        pts[k, 0] = tmp

    return pts

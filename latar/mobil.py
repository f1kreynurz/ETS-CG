from bidang.PersegiPanjang import PersegiPanjang
from bidang.SegitigaKanan import SegitigaKanan
from bidang.SegitigaKiri import SegitigaKiri
from bidang.ellips import Ellips
from primitif.color import Colors


class Mobil:
    def __init__(self, x, y, target, scale=1):
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.awal_x = self.x
        self.awal_y = self.y
        self.target_x = target  # Menghapus self.awal_x + dari target
        self.target_y = self.awal_y  # Menggunakan self.awal_y karena mobil hanya bergerak ke kanan

        self.body = PersegiPanjang(self.x - 300, self.y - 230, 250, 70)
        self.bodyAtas = PersegiPanjang(self.x - 250, self.y - 180, 150, 50)
        self.bodyAtasKanan = SegitigaKanan(self.x - 100, self.y - 230, 30, 50)
        self.bodyAtasKiri = SegitigaKiri(self.x - 279, self.y - 230, 30, 50)

        self.bodyAtasClone = PersegiPanjang(self.x - 225, self.y - 190, 100, 30)
        self.bodyAtasKananClone = SegitigaKanan(self.x - 125, self.y - 220, 30, 30)
        self.bodyAtasKiriClone = SegitigaKiri(self.x - 254, self.y - 220, 30, 30)

        self.lampuDepan = PersegiPanjang(self.x - 50, self.y - 250, 10, 20)
        self.lampuBelakang = PersegiPanjang(self.x - 300, self.y - 250, 10, 20)
        
        self.banKanan = Ellips(self.x - 100, self.y - 290, 25, 25)
        self.banKiri = Ellips(self.x - 250, self.y - 290, 25, 25)
        
        
    def draw(self):
        self.body.draw()
        self.bodyAtas.draw()
        self.bodyAtasKanan.draw()
        self.bodyAtasKiri.draw()

        self.bodyAtasClone.draw()
        self.bodyAtasKananClone.draw()
        self.bodyAtasKiriClone.draw()

        self.lampuDepan.draw()
        self.lampuBelakang.draw()
        
        self.banKanan.draw()
        self.banKiri.draw()
    
    def move(self, dx, dy):
        # Memeriksa apakah mobil belum mencapai target_x
        if self.x < self.target_x:
            # Menggeser setiap bagian mobil sejauh dx
            self.body.translate(dx, dy)
            self.bodyAtas.translate(dx, dy)
            self.bodyAtasKanan.translate(dx, dy)
            self.bodyAtasKiri.translate(dx, dy)
            self.bodyAtasClone.translate(dx, dy)
            self.bodyAtasKananClone.translate(dx, dy)
            self.bodyAtasKiriClone.translate(dx, dy)
            self.lampuDepan.translate(dx, dy)
            self.lampuBelakang.translate(dx, dy)
            self.banKanan.translate(dx, dy)
            self.banKiri.translate(dx, dy)
            
            # Mengupdate posisi x mobil
            self.x += dx
        elif self.x >= self.target_x and self.x > self.awal_x:
            # Jika mobil telah mencapai atau melewati target_x dan belum kembali ke titik awal
            
            # Menggeser setiap bagian mobil sejauh -dx (mundur)
            self.body.translate(-dx, dy)
            self.bodyAtas.translate(-dx, dy)
            self.bodyAtasKanan.translate(-dx, dy)
            self.bodyAtasKiri.translate(-dx, dy)
            self.bodyAtasClone.translate(-dx, dy)
            self.bodyAtasKananClone.translate(-dx, dy)
            self.bodyAtasKiriClone.translate(-dx, dy)
            self.lampuDepan.translate(-dx, dy)
            self.lampuBelakang.translate(-dx, dy)
            self.banKanan.translate(-dx, dy)
            self.banKiri.translate(-dx, dy)
            
            # Mengupdate posisi x mobil
            self.x -= dx
        else:
            # Jika mobil telah kembali ke titik awal
            self.x = self.awal_x
            self.y = self.awal_y



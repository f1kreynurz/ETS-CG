from primitif.color import Colors
from bidang.ellips import Ellips
from bidang.lingkaran import Lingkaran

class Evaporasi:
    def __init__(self, x, y, target, scale=1):
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.awal_x = self.x
        self.awal_y = self.y
        self.target_x = self.awal_x +  target
        self.target_y = self.awal_y +  target   
        
        self.uap = []
        uap_positions = [
            (0, 0), (20, 20), (40, 0), (60, 20), (80, 0), 
            (100, 20), (120, 0), (140, 20), (160, 0), (0, 40), 
            (20, 60), (40, 40), (60, 60), (80, 40), 
            (100, 60), (120, 40), (140, 60), (160, 40)
        ]
        
        for pos in uap_positions:
            self.uap.append(Lingkaran(self.x + pos[0], self.y + pos[1], 6, c=self.__colors.sungai))

    def draw(self): 
        for uap in self.uap:
            uap.draw()
            
    def move(self, dx, dy):
        print(self.x, self.y)
        if self.y > self.awal_y and self.x == self.awal_x:  # Bergerak ke atas
            for uap in self.uap:
                uap.translate(0, -dy)
            self.y -= dy
        elif self.x < self.target_x and self.y == self.awal_y:  # Bergerak ke kanan
            for uap in self.uap:
                uap.translate(dx, 0)
            self.x += dx
        elif self.y < self.target_y and self.x == self.target_x:  # Bergerak ke bawah
            for uap in self.uap:
                uap.translate(0, dy)
            self.y += dy
        elif self.x > self.awal_x and self.y == self.target_y:  # Bergerak ke kiri
            for uap in self.uap:
                uap.translate(-dx, 0)
            self.x -= dx
        else:  # Kembali ke titik awal
            for uap in self.uap:
                uap.translate(-dx, 0)
            self.x -= dx
class Awan:
    def __init__(self, x, y, target,scale=1):
        from bidang.lingkaran import Lingkaran
        from bidang.ellips import Ellips
        
        self.x = x
        self.y = y
        self.scale = scale
        self.awan1 = Lingkaran(self.x + 25, self.y + 115, 50)
        self.awan2 = Ellips(self.x + 10, self.y + 65, 75, 50)
        self.awan3 = Ellips(self.x - 45, self.y + 65, 75, 50)
        self.awal_x = self.x
        self.awal_y = self.y
        self.target_x = self.awal_x +  target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        
    def draw(self): 
        self.awan1.draw()
        self.awan2.draw()
        self.awan3.draw()
        
    def move(self, dx, dy):
        if self.x < self.target_x:
            self.awan1.translate(dx, dy)
            self.awan2.translate(dx, dy)
            self.awan3.translate(dx, dy)
            self.awan1.rotate(-90)
            self.awan2.rotate(-90)
            self.awan3.rotate(-90)
            self.x += dx
            self.y += dy
        elif self.x == self.target_x:
            self.awan1.translate(self.awal_x - self.x, 0)
            self.awan2.translate(self.awal_x - self.x, 0)
            self.awan3.translate(self.awal_x - self.x, 0)
            self.awan1.translate(0, self.awal_y - self.y)
            self.awan2.translate(0, self.awal_y - self.y)
            self.awan3.translate(0, self.awal_y - self.y)
            self.x = self.awal_x
            self.y = self.awal_y

        
       
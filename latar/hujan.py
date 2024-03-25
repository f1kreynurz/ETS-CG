from bidang.Garis_vertikal import GarisVertikal
from primitif.color import Colors

class Hujan:
    def __init__(self, x, y, target, scale=1):
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        self.awal_x = self.x
        self.awal_y = self.y
        self.target_x = self.awal_x +  target
        self.target_y = self.awal_y +  target   
        
        self.hujan = []
        hujan_positions = [
            (370, 60), (350, 60), (330, 60), (310, 60), (290, 60), (270, 60), (250, 60), (230, 60), (210, 60), (190, 60),
            (360, 20), (340, 20), (320, 20), (300, 20), (280, 20), (260, 20), (240, 20), (220, 20), (200, 20),
            (370,-20), (350,-20), (330,-20), (310,-20), (290,-20), (270,-20), (250,-20), (230,-20), (210,-20), (190,-20),
            (360,-60), (340,-60), (320,-60), (300,-60), (280,-60), (260,-60), (240,-60), (220,-60), (200,-60),
        ]
        
        for pos in hujan_positions:
            self.hujan.append(GarisVertikal(self.x + pos[0], self.y + pos[1], 20, c=self.__colors.sungai))

    def draw(self): 
        for hujan in self.hujan:
            hujan.draw()
            
    def move(self, dx, dy):
        if self.y < self.target_y:
            for hujan in self.hujan:
                hujan.translate(dx, dy)
            self.y += dy
        elif self.y == self.target_y:
            for hujan in self.hujan:
                hujan.translate(0, self.awal_y - self.y)
            self.y = self.awal_y


from primitif.color import Colors
class Matahari:
    def __init__(self, x, y, scale=1):
        from bidang.ellips import Ellips
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        
        self.matahari = Ellips(self.x - 300, self.y + 210, 50, 50)

           
    def draw(self): 
        self.matahari.draw()
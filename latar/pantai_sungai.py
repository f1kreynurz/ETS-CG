from primitif.color import Colors
class Pantai:
    def __init__(self, x, y, scale=1):
        from bidang.PersegiPanjang import PersegiPanjang
        from bidang.ellips import Ellips
        
        self.x = x
        self.y = y
        self.scale = scale
        self.__colors =  Colors()
        
        self.pantai = PersegiPanjang(self.x + 50, self.y - 250, 100, 150, c=self.__colors.pantai)
        self.sungai1 = PersegiPanjang(self.x + 50, self.y - 295, 350, 10, c=self.__colors.sungai)                                                                                                                                                                                                                                                                                                                                                                                                                                           
        self.sungai2 = PersegiPanjang(self.x + 295, self.y - 251, 10, 150, c=self.__colors.sungai)
        
    def draw(self): 
        self.pantai.draw()
        self.sungai1.draw()
        self.sungai2.draw()
         
       
       
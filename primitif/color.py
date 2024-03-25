from random import randint

class Colors:
    putih = [255, 255, 255, 255]
    
    hitam = [0, 0, 0, 255]
    
    biru_laut = [0, 0, 255, 255]
    
    matahari =  [255, 189, 0, 255]
    
    gunung_kanan = [34, 150, 34, 255]
    
    gunung_kiri = [34, 200, 34, 255]
    
    daratan = [34, 200, 34, 255]
    
    pantai =  [127, 51, 0, 255]
    
    sungai = [0, 90, 255, 255]
    
    awan_hujan = [[64, 64, 64, 255]]
    

    def randomColor():
        randomColor = [randint(50, 255), randint(
            100, 255), randint(100, 255), 255]
        return randomColor

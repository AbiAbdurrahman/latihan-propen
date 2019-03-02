import math
# import raw_input

class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Garis:
    def __init__(self, titik1, titik2):
        self.titik1 = titik1
        self.titik2 = titik2

    def generateLength(self):
        selisihX = 0
        selisihY = 0
        
        if self.titik1.x > self.titik2.x:
            selisihX = self.titik1.x - self.titik2.x
        else:
            selisihX = self.titik2.x - self.titik2.x

        if self.titik1.y > self.titik2.y:
            selisihY = self.titik1.y - self.titik2.y
        else:
            selisihY = self.titik2.y - self.titik1.y

        panjang = math.sqrt(pow(selisihX,2) + pow(selisihY,2))
        return panjang

x1 = int(input("insert x1 : "))
y1 = int(input("insert y1 : "))
x2 = int(input("insert x2 : "))
y2 = int(input("insert y2 : "))

suatuGaris = Garis(Titik(x1,y1),Titik(x2,y2))

print(suatuGaris.generateLength())


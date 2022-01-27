from Code.Modele.COperation import COperation

class CPersonneVue:

    def __init__(self, canvas, x, y, rayon, color = 'DeepSkyBlue2', listcolor = ['DeepSkyBlue2', "DeepSkyBlue3","DodgerBlue2", "DodgerBlue3", "DeepSkyBlue4", "DodgerBlue4","midnightblue","navy","darkblue","black"], pression = 0):
        self.canvas = canvas
        self.image = COperation.create_circle(x, y, rayon, canvas, color)
        self.x = x
        self.y = y
        self.rayon = rayon
        self.color = color
        self.pression = pression
        self.listColor = listcolor

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getPression(self):
        return self.pression

    def setPression(self, pres):
        self.pression = pres
        if 0 <= self.pression <= 1:
            self.color = self.listColor[0]
        elif 1 < self.pression <= 2:
            self.color = self.listColor[1]
        elif 2 < self.pression <= 3:
            self.color = self.listColor[2]
        elif 3 < self.pression <= 4:
            self.color = self.listColor[3]
        elif 4 < self.pression <= 5:
            self.color = self.listColor[4]
        elif 5 < self.pression <= 6:
            self.color = self.listColor[5]
        elif 6 < self.pression <= 7:
            self.color = self.listColor[6]
        elif 7 < self.pression <= 8:
            self.color = self.listColor[7]
        elif 8 < self.pression <= 9:
            self.color = self.listColor[8]
        elif 9 < self.pression <= 10:
            self.color = self.listColor[9]
        elif  self.pression > 10:
            self.color = self.listColor[9]
        
    def move(self):
        self.canvas.delete(self.image)
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)

    def disparaitre(self):
        self.canvas.delete(self.image)

    def apparaitre(self):
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)

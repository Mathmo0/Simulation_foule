from Code.Modele.COperation import COperation

class CPersonneVue:

    def __init__(self, canvas, x, y, rayon, color):
        self.canvas = canvas
        self.image = COperation.create_circle(x, y, rayon, canvas, color)
        self.x = x
        self.y = y
        self.rayon = rayon
        self.color = color

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
        
    def bouger(self):
        self.canvas.delete(self.image)
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)
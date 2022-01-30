from Code.Modele.COperation import COperation

class CPersonneVue:

    def __init__(self, canvas, x, y, rayon, color = 'DeepSkyBlue2', listcolor = ['DeepSkyBlue2', "DeepSkyBlue3","DodgerBlue2", "DodgerBlue3", "DeepSkyBlue4", "DodgerBlue4","midnightblue","navy","darkblue","black"], pression = 0):
        self.__PVUcanvas = canvas
        self.__PVUimage = COperation.OPEcreate_circle(x, y, rayon, canvas, color)
        self.__fPVUx = x
        self.__fPVUy = y
        self.__iPVUrayon = rayon
        self.__sPVUcolor = color
        self.__fPVUpression = pression
        self.__lPVUlistColor = listcolor

    def getX(self):
        return self.__fPVUx

    def setX(self, x):
        self.__fPVUx = x


    def getY(self):
        return self.__fPVUy

    def setY(self, y):
        self.__fPVUy = y

    def setColor(self, color):
        self.__sPVUcolor = color

    def getColor(self):
        return self.__sPVUcolor

    def getPression(self):
        return self.__fPVUpression

    def setPression(self, pres):
        self.__fPVUpression = pres
        if 0 <= self.__fPVUpression <= 1:
            self.__sPVUcolor = self.__lPVUlistColor[0]
        elif 1 < self.__fPVUpression <= 2:
            self.__sPVUcolor = self.__lPVUlistColor[1]
        elif 2 < self.__fPVUpression <= 3:
            self.__sPVUcolor = self.__lPVUlistColor[2]
        elif 3 < self.__fPVUpression <= 4:
            self.__sPVUcolor = self.__lPVUlistColor[3]
        elif 4 < self.__fPVUpression <= 5:
            self.__sPVUcolor = self.__lPVUlistColor[4]
        elif 5 < self.__fPVUpression <= 6:
            self.__sPVUcolor = self.__lPVUlistColor[5]
        elif 6 < self.__fPVUpression <= 7:
            self.__sPVUcolor = self.__lPVUlistColor[6]
        elif 7 < self.__fPVUpression <= 8:
            self.__sPVUcolor = self.__lPVUlistColor[7]
        elif 8 < self.__fPVUpression <= 9:
            self.__sPVUcolor = self.__lPVUlistColor[8]
        elif 9 < self.__fPVUpression <= 10:
            self.__sPVUcolor = self.__lPVUlistColor[9]
        elif  self.__fPVUpression > 10:
            self.__sPVUcolor = self.__lPVUlistColor[9]
        
    def move(self):
        """
        Fonction permettant d'actualiser la position du cercle.

        @return : void
        """
        self.__PVUcanvas.delete(self.__PVUimage)
        self.__PVUimage = COperation.OPEcreate_circle(self.__fPVUx, self.__fPVUy, self.__iPVUrayon, self.__PVUcanvas, self.__sPVUcolor)

    def disparaitre(self):
        """
        Fonction permettant de faire disparaitre le cercle.

        @return : void
        """
        self.__PVUcanvas.delete(self.__PVUimage)

    def apparaitre(self):
        """
        Fonction permettant de faire apparaitre le cercle.

        @return : void
        """
        self.__PVUimage = COperation.OPEcreate_circle(self.__fPVUx, self.__fPVUy, self.__iPVUrayon, self.__PVUcanvas, self.__sPVUcolor)
import numpy as np
import tkinter

class COpetation:

    '''

    Cette focntion permet de savoir s'il est dans une cercle ou non

    :param CentreCercle0 : coordonnée x du centre du cercle
    :param CentreCercle1 : coordonnée y du centre du cercle
    :param Point0 : coordonnée x du point
    :param Point1 : coordonnée y du point

    :return boolean :
    '''
    @staticmethod
    def DetectionCercle(CentreCercle0, CentreCercle1, Point0, Point1, rayon):

        DIstance = (Point0 - CentreCercle0) ** 2 + (Point1 - CentreCercle1 ** 2)
        r2 = (rayon ** 2)
        print("DIstance = ", DIstance)
        if (DIstance <= r2):
            # if((Point[0]-CentreCercle[0])**2 + (Point[1]-CentreCercle[1])**2 <= rayon**2 ) :
            return True
        else:
            return False




    def FonctionTrajectoirePieton(self,Position, PositionDeltaT):
        '''
        Cette focntion permet de déterminer les coefficients a et b de la focntion linéaire f(x) = ax+b
        que suit les pieton entre 2 position

        :param Position: Position du pieton à l'intant t
        :param PositionDeltaT:  Position du pieton à l'intant t- DeltaT
        :return coef : coefficient de la fonction linéaire ax+b

        '''
        a = (Position[1] - PositionDeltaT[1]) / (Position[1] - PositionDeltaT[1])  # coef directeur
        b = Position[1] - Position[0] * a  # ordonne à l'origine
        coef = np.array([a, b]) #coefficients de la fonction linéaire
        return coef

    def Nabla(self,Position, PositionDeltaT, PositionB):
        """
        Cette fonction permet de calculer le nabla mathematique pour un vecteur position donnee

        :param Position:  Position du pieton à l'intant t
        :param PositionDeltaT: Position du pieton à l'intant t-DeltaT
        :param PositionB: Position de l'obstacle ou d'un autre piéton
        :return: vecteur nabla

        """
        coef = np.array([0, 0])
        rAlphaBeta = rAlphaObstacle = (Position - PositionB)
        coef = self.FonctionTrajectoirePieton(Position, PositionDeltaT)

        return np.array([-rAlphaBeta[1] + coef[0] + coef[1], coef[0] * rAlphaBeta[0] - 1 + coef[1]])



    def create_circle(cls, x, y, r, canvas, color):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color)

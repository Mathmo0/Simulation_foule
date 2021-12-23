import numpy as np
import tkinter

class COperation:

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

        DIstance = (Point0 - CentreCercle0) ** 2 + (Point1 - CentreCercle1) ** 2
        r2 = (rayon ** 2)
        if (DIstance <= r2):
            return True
        else:
            return False



    @staticmethod
    def FonctionTrajectoirePieton(Position, PositionDeltaT):
        '''
        Cette focntion permet de déterminer les coefficients a et b de la focntion linéaire f(x) = ax+b
        que suit les pieton entre 2 position

        :param Position: Position du pieton à l'intant t
        :param PositionDeltaT:  Position du pieton à l'intant t- DeltaT
        :return coef : coefficient de la fonction linéaire ax+b

        '''
        a = (Position[1] - PositionDeltaT[1]) / (Position[0] - PositionDeltaT[0])  # coef directeur
        b = Position[1] - Position[0] * a  # ordonne à l'origine
        coef = np.array([a, b]) #coefficients de la fonction linéaire
        return coef

    @staticmethod
    def Nabla(Position, PositionDeltaT, PositionB):
        """
        Cette fonction permet de calculer le nabla mathematique pour un vecteur position donnee

        :param Position:  Position du pieton à l'intant t
        :param PositionDeltaT: Position du pieton à l'intant t-DeltaT
        :param PositionB: Position de l'obstacle ou d'un autre piéton
        :return: vecteur nabla

        """
        #vecteur distance entre le pieton alpha et un pieton Beta ou un pieton alpha et un obstacle
        rAlphaBeta = rAlphaObstacle = Position - PositionB

        #coefficient a et b de la fonction trajectoire (f(x) = ax+b) du pieton alpha
        coef = COperation.FonctionTrajectoirePieton(Position, PositionDeltaT)

        return np.array([-rAlphaBeta[1] + coef[0] + coef[1], coef[0] * rAlphaBeta[0] - 1 + coef[1]])

    def create_circle(cls, x, y, r, canvas, color):
        """
        Cette focntion permet de créer un cercle dans un canvas

        @param x: coordonné x du centre du cercle
        @param y: coordonné y du centre du cercle
        @param r: rayon du cercle
        @param canvas : interface graphique dans lequel va être créer le cercle
        @param color: couleur du cercle
        @return: le canvas avec le cercle dedans
        """

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color)

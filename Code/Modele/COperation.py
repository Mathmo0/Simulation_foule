import numpy as np

class COperation:

    @staticmethod
    def OPEDetectionCercle(CentreCercle0, CentreCercle1, Point0, Point1, rayon):
        '''
        Cette fonction permet de savoir si un point est dans une cercle ou non

        @param CentreCercle0 : coordonnee x du centre du cercle
        @param CentreCercle1 : coordonnee y du centre du cercle
        @param Point0 : coordonnee x du point
        @param Point1 : coordonnee y du point

        @return boolean :
        '''
        DIstance = (Point0 - CentreCercle0) ** 2 + (Point1 - CentreCercle1) ** 2
        r2 = (rayon ** 2)
        if (DIstance <= r2):
            return True
        else:
            return False



    @staticmethod
    def OPEFonctionTrajectoirePieton(Position, PositionDeltaT):
        '''
        Cette focntion permet de determiner les coefficients a et b de la fonction lineaire f(x) = ax+b
        que suit les pieton entre 2 position

        @param Position: Position du pieton à l'intant t
        @param PositionDeltaT:  Position du pieton à l'intant t- DeltaT

        @return coef : coefficient de la fonction lineaire ax+b
        '''

        Denominateur = (Position[0] - PositionDeltaT[0])
        if Denominateur == 0 :
            a = 0
        else:
            a = (Position[1] - PositionDeltaT[1]) / (Position[0] - PositionDeltaT[0])  # coefficient directeur

        b = Position[1] - Position[0] * a  # ordonnee à l'origine
        coef = np.array([a, b]) #coefficients de la fonction lineaire
        return coef

    @staticmethod
    def OPENabla(Position, PositionDeltaT, PositionB):
        """
        Cette fonction permet de calculer le nabla mathematique pour un vecteur position donnee

        @param Position:  Position du pieton à l'intant t
        @param PositionDeltaT: Position du pieton à l'intant t-DeltaT
        @param PositionB: Position de l'obstacle ou d'un autre pieton

        @return: vecteur nabla

        """
        #vecteur distance entre le pieton alpha et un pieton Beta ou un pieton alpha et un obstacle
        rAlphaBeta = Position - PositionB

        #coefficient a et b de la fonction trajectoire (f(x) = ax+b) du pieton alpha
        coef = COperation.OPEFonctionTrajectoirePieton(Position, PositionDeltaT)

        return np.array([-rAlphaBeta[1] + coef[0] + coef[1], coef[0] * rAlphaBeta[0] - 1 + coef[1]])

    @staticmethod
    def OPEcreate_circle(x, y, r, canvas, color):
        """
        Cette focntion permet de creer un cercle dans un canvas

        @param x: coordonnee x du centre du cercle
        @param y: coordonnee y du centre du cercle
        @param r: rayon du cercle
        @param canvas : interface graphique dans lequel va etre creer le cercle
        @param color: couleur du cercle

        @return: le canvas avec le cercle dedans
        """

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill=color, width=0)

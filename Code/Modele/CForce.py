
import numpy as np
import math
from numpy import linalg as la

# constante :

c = 0.5
tau = 0.5  # s
SqrtTeta = 0.26  # m/s
Sigma = 1.6 # m
R = 0.2  # m
DeltaT = 2  # s
Phi = 100  # °
VAlphaBeta0 = 1.5 #5  # m**2
UAlphaObstacle0 = 10 # (m/s)**2

class CForce :

    #methode :

    def VitesseAlphaMax(self,vAlpha0):
        """
        Cette fonction permet de calculer la vitesse max d'un pieton

        @param vAlpha0: Vitesse initiale d'un pieton
        @return: Vitesse maximale d'un pieton

        """
        return 1.3 * vAlpha0

    def VecteurVitesse(self,Position, PositionDeltaT, t):
        """
        Cette fonction permet de calculer le vectur vitesse pour un pieton alpha à un instant t donnee

        @param Position : Position du pieton à l'intant t
        @param PositionDeltaT : Position du pieton à l'intant t+DeltaT
        @param t: instant t pour lequel est calulé le vecteur vittese
        @return: vecteur vitesse du pieton alpha à l'instant t

        """
        # Si t est égale à 0 alors le vecteur vitesse est initialise aux vecteur nul
        if (t == 0):
            return (0, 0)
        else:
            if (np.linalg.norm((Position - PositionDeltaT) / t) > 1.742):
                return [1.23, 1.23]
            else:
                return (Position - PositionDeltaT) / t

    def eAlpha(self,vRkAlpha, vRalpha):

        """
        Cette focntion permet de calculer le vecteur destination du pieton alpha

        @param vRkAlpha : destination du pieton alpha
        @param vRalpha : position du piéton alpha
        @return: vecteur destination
        """
        vdistance = vRkAlpha - vRalpha
        if(la.norm(vdistance) != 0) :
            return vdistance / la.norm(vdistance)
        else :
            return np.array([0.0,0.0])

    def b(self,Ralpha, Rbeta, vitesseBeta, vRkBeta):
        """
        Cette fonction pemret de calculer le coefficient b

        @param Ralpha : position du piéton alpha
        @param Rbeta : position du piéotn beta
        @param vitesseBeta : vitesse du piéton beta
        @param vRkBeta : destination du piéton Beta
        @return: valeur du coefficient b

        """
        RalphaBeta = Ralpha - Rbeta
        NormeRalphaBeta = la.norm(RalphaBeta)
        eBeta = self.eAlpha(vRkBeta, Rbeta)

        calcul = (NormeRalphaBeta + la.norm(RalphaBeta - vitesseBeta * DeltaT * eBeta)) ** 2 - (
                    vitesseBeta * DeltaT) ** 2

        Deuxb = math.sqrt(calcul)
        return Deuxb / 2

    def w(self,e, f):
        """
        @param e : est le vecteur sortie/obstacle
        @param f : est un vecteur force
        @return:
        """
        if (np.dot(e, f) >= la.norm(f) * math.cos(Phi)):
            return 1
        else:
            return c

    def VAlphaBeta(self,b):
        """
        Cette fonction permet de caculer le potentiel repulsif

        @param b: coeffcient b
        @return: return la valeur du coefficient repulsif

        """
        return VAlphaBeta0 * np.exp(-b / Sigma)

    def UAlphaObstacle(self,NormeVecteurRAlphaObstacle):
        """
        Cette focntion permet de calculer le potentiel décroissant répulsif et monotonique

        @param NormeVecteurRAlphaObstacle:
        @return: valeur du potentiel décroissant répulsif et monotonique
        """
        return UAlphaObstacle0 * np.exp(-NormeVecteurRAlphaObstacle / R)


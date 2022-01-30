import numpy as np
import math
from numpy import linalg as la

# constantes :

c = 0.5
tau = 0.5  # s
SqrtTeta = 0.26  # m/s
Sigma = 1.5 # m
R = 0.2 # m
DeltaT = 2 # s
Phi = 100  # °
VAlphaBeta0 = 12 # m**2
UAlphaObstacle0 = 0.5 #(m/s)**2
cst = 10

class CForce :

    #-------------------methodes------------------- :

    def FORVitesseAlphaMax(self, vAlpha0):
        """
        Cette fonction permet de calculer la vitesse max d'un pieton

        @param vAlpha0: Vitesse initiale d'un pieton

        @return: Vitesse maximale d'un pieton

        """
        return 1.3 * vAlpha0

    def FORVecteurVitesse(self, Position, PositionDeltaT, t):
        """
        Cette fonction permet de calculer le vecteur vitesse pour un pieton alpha à un instant t donnee

        @param Position : Position du pieton à l'intant t
        @param PositionDeltaT : Position du pieton à l'intant t+DeltaT
        @param t: instant t pour lequel est calcule le vecteur vittese

        @return: vecteur vitesse du pieton alpha à l'instant t

        """
        # Si t est egale à 0 alors le vecteur vitesse est initialise aux vecteur nul
        if (t == 0):
            return (0, 0)
        else:
            if (np.linalg.norm((Position - PositionDeltaT) / t) > 1.742):
                return [1.23, 1.23]
            else:
                return (Position - PositionDeltaT) / t

    def FOReAlpha(self, vRkAlpha, vRalpha):
        """
        Cette focntion permet de calculer le vecteur destination du pieton alpha

        @param vRkAlpha : destination du pieton alpha
        @param vRalpha : position du pieton alpha

        @return: vecteur destination
        """
        vdistance = vRkAlpha - vRalpha
        if(la.norm(vdistance) != 0) :
            return vdistance / la.norm(vdistance)
        else :
            return np.array([0.0,0.0])

    def FORb(self, Ralpha, Rbeta, vitesseBeta, vRkBeta):
        """
        Cette fonction permet de calculer le coefficient b

        @param Ralpha : position du pieton alpha
        @param Rbeta : position du pieton beta
        @param vitesseBeta : vitesse du pieton beta
        @param vRkBeta : destination du pieton Beta

        @return: valeur du coefficient b
        """
        RalphaBeta = Ralpha - Rbeta
        NormeRalphaBeta = la.norm(RalphaBeta)
        eBeta = self.FOReAlpha(vRkBeta, Rbeta)

        calcul = (NormeRalphaBeta + la.norm(RalphaBeta - vitesseBeta * DeltaT * eBeta)) ** 2 - (
                    vitesseBeta * DeltaT) ** 2

        Deuxb = math.sqrt(calcul)
        return Deuxb / 2

    def FORw(self, e, f):
        """
        Cette fonction permet de calculer l'influence des personnes derriere elles.

        @param e : est le vecteur sortie/obstacle
        @param f : est un vecteur force

        @return: 1 ou c selon l'influence du pieton
        """
        if (np.dot(e, f) >= la.norm(f) * math.cos(Phi)):
            return 1
        else:
            return c

    def FORVAlphaBeta(self, b):
        """
        Cette fonction permet de caculer le potentiel repulsif

        @param b: coeffcient b

        @return: return la valeur du coefficient repulsif
        """
        return VAlphaBeta0 * np.exp(-b / Sigma)

    def FORUAlphaObstacle(self, NormeVecteurRAlphaObstacle):
        """
        Cette fonction permet de calculer le potentiel decroissant repulsif et monotone

        @param NormeVecteurRAlphaObstacle: La distance entre le pieton et l'obstacle

        @return: valeur du potentiel decroissant repulsif et monotone
        """
        return UAlphaObstacle0 * np.exp(-NormeVecteurRAlphaObstacle / R)

    def FORW(self, normeRalphaI, t):
        """
        Cette fonction permet de calculer le potentiel pour la force d'attraction

        @param normeRalphaI: distance entre le pieton alpha et i
        @param t: temps

        @return: valeur du potentiel
        """
        return UAlphaObstacle0*np.exp(normeRalphaI)/t*cst

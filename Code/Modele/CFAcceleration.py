from Code.Modele.CForce import CForce, tau

import numpy as np
import math
from numpy import linalg as la

class CFAcceleration(CForce) :

    def __init__(self,tForceAcceleration = np.array([0,0]) ):

        self.__tFACForceAcceleration = tForceAcceleration;

    #getter et setter :

    def FACgetForceAcceleration(self):
        """
        getter pour l'attribut __tFACForceAcceleration

        @return: __tFACForceAcceleration
        """
        return self.__tFACForceAcceleration

    #methodes :

    def FACForceDacceleration(self,vAlpha, vAlpha0, vRkAlpha, vRalpha):
        """
        Cette fontion permet de calculer la force d'acceleration pour un pieton alpha

        @param vAlpha : vecteur vitesse du piéton alpha
        @param vAlpha0 : vitesse initiale du piéton
        @param vRkAlpha: Destination du pieton Alpha
        @param vRalpha: Position de pieton Alpha
        @return: Valeur de la force d'acceleration

        """
        eAlphaS = self.FOReAlpha(vRkAlpha, vRalpha)

        self.__tFACForceAcceleration = (1 / tau) * ((vAlpha0 * eAlphaS) - vAlpha)

        return self.__tFACForceAcceleration

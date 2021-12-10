from Modele.CForce import CForce, tau

import numpy as np
import math
from numpy import linalg as la

class CFAcceleration(CForce) :

    def __init__(self,tForceAcceleration = np.array([0,0]) ):

        self.__tForceAcceleration = tForceAcceleration;

    #getter et setter :

    def FACgetForceAcceleration(self):
        """
        getter pour l'attribut tForceAcceleration

        @return: tForceAcceleration
        """
        return self.__tForceAcceleration

    def FACsetForceAcceleration(self, ForceAcceleration = 0):
        """
        setter pour l'attribut tForceAcceleration
        @param ForceAcceleration: nouvelle valeur pour tForceAcceleration
        @return: rien
        """
        self.__tForceAcceleration = ForceAcceleration

    #methodes :

    def FACForceDacceleration(self,vAlpha, vAlpha0, vRkAlpha, vRalpha):
        """
        @param vAlpha : vecteur vitesse du piéton alpha
        @param vAlpha0 : vitesse initiale du piéton
        @param vRkAlpha: Destination du pieton Alpha
        @param vRalpha: Position de pieton Alpha
        @return: Valeur de la force d'acceleration

        """
        eAlphaS = self.eAlpha(vRkAlpha, vRalpha)

        self.__tForceAcceleration = (1 / tau) * ((vAlpha0 * eAlphaS) - vAlpha)

        return self.__tForceAcceleration
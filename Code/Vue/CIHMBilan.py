import matplotlib as plt
import numpy as np
from Code.Modele.CForce import DeltaT

class CIHMBilan :

    def __init__(self, listcoord = [] ,tpsSimulation = 0):

        self.__listcoord = listcoord
        self.__tpsSimulation = tpsSimulation
        self.__listCarteChaleur = np.zeros((400,400))

    def heatmap2d(arr: np.ndarray):
        plt.imshow(arr, cmap='viridis')
        plt.colorbar()
        plt.show()

    def calculCarteChaleur(self):
        for uiBoucle1 in range(len(self.__listcoord)):
            px1 = (self.__listcoord[uiBoucle1][0])
            px2 = (self.__listcoord[uiBoucle1][1])
            self.__listCarteChaleur[round(px1)][round(px2)] += 1

    def calculTpsSimulation(self):

        self.__tpsSimulation = len(self.__listcoord[0])*DeltaT


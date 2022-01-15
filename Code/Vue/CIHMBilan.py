import matplotlib as plt
import numpy as np

class CIHMBilan :

    def __init__(self, listcoord = [] , tpsSimulation = 0):

        self.__listcoord = listcoord
        self.__tpsSimulation = tpsSimulation
        self.__listCarteChaleur = np.zeros((400,400))

    def heatmap2d(arr: np.ndarray):
        plt.imshow(arr, cmap='viridis')
        plt.colorbar()
        plt.show()

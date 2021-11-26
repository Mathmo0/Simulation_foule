import numpy as np


class CBilan:
    """
    Classe du Bilan
    """

    # -------------------Constructeur-------------------#
    def __init__(self, duree = 0.0, position = np.array([(0, 0)])):
        self.dDuree = duree
        self.tPosition = position


    # -------------------Getters-------------------#
    def getDuree(self):
        return self.dDuree

    def getPosition(self):
        return self.tPosition


    # ---------------------Setters---------------------#
    def setDuree(self, duree):
        self.dDuree = duree

    def setPosition(self, position):
        self.tPosition = position


    # -------------------Methodes-------------------#

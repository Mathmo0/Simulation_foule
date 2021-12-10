from tkinter import *
import numpy as np
from Modele import CEnvironnement
from Modele import CPersonne

class CIHMSimulation:

    # -------------------Constructeur-------------------#
    def __init__(self, environnement):
        self.ENVenvironnement = environnement


    def getEnvironnement(self):
        """
            getter pour l'environnement

            @return : environnement

        """
        return self.ENVenvironnement

    def setEnvironnement(self, environnement):
        """
        setter pour l'environnement

        @return : void
        """
        self.ENVenvironnement = environnement

    def lancerSimulation(self):
        window = Tk()

        WIDTH = 1000
        HEIGHT = 1000

        canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = 'snow')

richard = CPersonne(np.array([0,0]))

list_sorties = np.array([(3, 4), (2, 4)])


test2 = CEnvironnement("Chambre", 34, 20, list_sorties, list_personnes, list_objets)

Sim = CIHMSimulation()
Sim.lancerSimulation()
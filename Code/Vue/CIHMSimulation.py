from tkinter import *
import CEnvironnement

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


Sim = CIHMSimulation()
Sim.lancerSimulation()
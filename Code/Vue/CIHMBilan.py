import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from Code.Modele.CForce import DeltaT
from Code.Vue.CIHM import CIHM
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class CIHMBilan(CIHM):

    #-----------------------Constructeur-----------------------:
    def __init__(self, listcoord ,tpsSimulation = 0):
        super().__init__("Bilan de l'évacuation d'une foule")
        self.__listcoord = listcoord
        self.__tpsSimulation = tpsSimulation
        self.__listCarteChaleur = np.zeros((self._iIHMWidth, self._iIHMHeight))

        """
         -----------------------  Affichage de la carte des chaleurs  ------------------------------
        """
        self.__BILfigure = Figure()
        self.BILCalculCarteChaleur()
        self.__BILdiagramme = self.__BILfigure.add_subplot(111)
        self.BILHeatmap()
        self.__BILcanvasSimulation = FigureCanvasTkAgg(self.__BILfigure, self.IHMgetWindow())

        self.__BILcanvasSimulation.get_tk_widget().grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

        self.__BILfigure = Figure(figsize=(5, 5), dpi = 90)
        self.BILCalculCarteChaleur()

        self.BILHeatmap()
        self.__BILcanvasSimulation = FigureCanvasTkAgg(self.__BILfigure, self.IHMgetWindow())

        self.__BILcanvasSimulation.get_tk_widget().grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

        """
        -----------------------  Affichage du temps de simulation  ------------------------------
        """
        self.__BILtempsSimulation = Label()
        self.BILAfficherTempsSimulation()

        self._IHMWindow.mainloop()

    #-----------------------Getter-----------------------:
    def getWindowB(self):
        return self._IHMWindow

    #-----------------------Methodes-----------------------
    def BILHeatmap(self):
        """
        Fonction permettant d'afficher la carte des chaleurs.

        @return : void
        """
        self.__BILdiagramme = sns.heatmap(self.__listCarteChaleur, annot=None, vmin=0.0, vmax=20)
        plt.show()

    def BILCalculCarteChaleur(self):
        """
        Fonction permettant de calculer la matrice correspondant a la carte des chaleurs.

        @return : void
        """
        for uiBoucle1 in range(len(self.__listcoord)):
            px1 = (self.__listcoord[uiBoucle1][0])
            px2 = (self.__listcoord[uiBoucle1][1])
            if 400 > px1 > 0 and 400 > px2 > 0:
                self.__listCarteChaleur[round(px1)][round(px2)] += 10

    def BILCalculTpsSimulation(self):
        """
        Fonction permettant de calculer le temps d'evacuation.

        @return : void
        """
        self.__tpsSimulation = len(self.__listcoord[0])*DeltaT

    def BILAfficherTempsSimulation(self):
        """
        Fonction permettant d'afficher le temps d'evacuation.

        @return : void
        """
        self.__BILtempsSimulation = Label(self.IHMgetWindow(), text=str(self.__tpsSimulation) + " secondes", font=("Arial", 15), bg='light grey')
        self.__BILtempsSimulation.grid(column=3, row=6, sticky='W')

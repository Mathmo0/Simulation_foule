import matplotlib.pyplot as plt
#plt.use("TkAgg")
import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import seaborn as sns
from Code.Modele.CForce import DeltaT
from Code.Vue.CIHM import CIHM


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class CIHMBilan(CIHM):

    def __init__(self, listcoord ,tpsSimulation = 0):
        super().__init__("Bilan de l'évacuation d'une foule")
        self.__listcoord = listcoord
        self.__tpsSimulation = tpsSimulation
        self.__listCarteChaleur = np.zeros((self.__iIHMWidth, self.__iIHMHeight))

        """
         -----------------------  Affichage de la carte des chaleurs  ------------------------------
        """
        self.figure = Figure(figsize=(5, 5))
        self.calculCarteChaleur()
        self.c = self.figure.add_subplot(111)
        # self.c.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.heatmap2d()
        self.CanvasSimulation = FigureCanvasTkAgg(self.figure, self.IHMgetWindow())

        self.CanvasSimulation.get_tk_widget().grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')


        #self.Creation_Zone_Simulation()
        self.figure = Figure(figsize=(5, 5))
        self.calculCarteChaleur()
        #self.c = self.figure.add_subplot(111)
        #self.c.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.heatmap2d()
        self.CanvasSimulation = FigureCanvasTkAgg(self.figure, self.IHMgetWindow())

        self.CanvasSimulation.get_tk_widget().grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

        """self.toolBar = NavigationToolbar2Tk(self.CanvasSimulation, self.getWindow())
        self.toolBar.update()

        self.CanvasSimulation.get_tk_widget().grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')
"""


        self.__IHMWindow.mainloop()

    def heatmap2d(self):
        self.c = plt.imshow(self.__listCarteChaleur, cmap='viridis')
        self.c = plt.colorbar() #ticks=[0, 1, 2, 3,4,5]
        #self.c.plot(self.__listCarteChaleur)
        #self.c = sns.heatmap(self.__listCarteChaleur, linewidth=0.5)
        plt.show()

    def calculCarteChaleur(self):
        for uiBoucle1 in range(len(self.__listcoord)):
            px1 = (self.__listcoord[uiBoucle1][0])
            px2 = (self.__listcoord[uiBoucle1][1])
            self.__listCarteChaleur[round(px1)][round(px2)] += 1

    def calculTpsSimulation(self):
        self.__tpsSimulation = len(self.__listcoord[0])*DeltaT

    def getWindowB(self):
        return self.__IHMWindow

#test = CIHMBilan()

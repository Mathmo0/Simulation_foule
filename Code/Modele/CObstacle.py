import numpy as np

class CObstacle :
    """
    Classe des obstacles
    """

    # -------------------Constructeur-------------------#
    def __init__(self, coordonneesSommet = np.array([0,0])):
        self._iOBSSuperficie = 0
        self._tOBSCoordonneesSommet = [coordonneesSommet]


    # -------------------Getters-------------------#
    def OBSgetSuperficie(self):
        """
        getter pour l'attribut __iOBSSuperficie

        @return: __iOBSSuperficie
        """
        return self._iOBSSuperficie

    def OBSgetCoordonneesSommet(self):
        """
        getter pour l'attribut __tOBSCoordonneesSommet

        @return: __tOBSCoordonneesSommet
        """
        return self._tOBSCoordonneesSommet


    # ---------------------Setters---------------------#
    def OBSsetCoordonneesSommet(self, coordonneesSommets):
        """
        setter pour l'attribut __tOBSCoordonneesSommet
        @param coordonneesSommets: nouvelle coordonnees pour le sommet

        @return: rien
        """
        self._tOBSCoordonneesSommet = coordonneesSommets


    # -------------------Methodes-------------------#
    def OBSToString(self):
        """
         fonction pemettant d'afficher les differentes informations de l'obstacle

        @return: rien
        """

        print("Coordonnees : {}\n"
              "Superficie : {}\n"
              .format(self.OBSgetCoordonneesSommet(), self.OBSgetSuperficie()))

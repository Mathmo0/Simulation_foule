from Code.Modele.CObstacle import CObstacle

import numpy as np

class CObstacleQuadrilatere(CObstacle):
    """
    Classe des obstacles de type quadrilatere
    """

    # -------------------Constructeur-------------------#
    def __init__(self, hauteur = 0, largeur = 0, coordonneesSommets = np.array([0, 0])):
        super().__init__(coordonneesSommets)
        self.__iOBQSuperficie = hauteur * largeur
        self.__iOBQHauteur = hauteur
        self.__iOBQLargeur = largeur


    # -------------------Getters-------------------#
    def OBQgetHauteur(self):
        """
        getter pour l'attribut __iOBQHauteur

        @return: __iOBQHauteur
        """
        return self.__iOBQHauteur

    def OBQgetLargeur(self):
        """
        getter pour l'attribut __iOBQLargeur
        @return: __iOBQLargeur
        """
        return self.__iOBQLargeur


    # ---------------------Setters---------------------#
    def OBQsetHauteur(self, hauteur):
        """
        setter pour l'attribut __iOBQHauteur

        @param hauteur: nouvelle hauteur pour l'obstacle
        @return: rien
        """
        self.__iOBQHauteur = hauteur
        self.__iOBQSuperficie = self.__iOBQHauteur * self.__iOBQLargeur

    def OBQsetLargeur(self, largeur):
        """
        setter pour l'attribut __iOBQLargeur
        @param largeur: nouvelle largeur pour l'obstacle
        @return: rien
        """
        self.__iOBQLargeur = largeur
        self.__iOBQSuperficie = self.__iOBQHauteur * self.__iOBQLargeur


    # -------------------Methodes-------------------#
    def OBSToString(self):
        """
         fonction pemettant d'afficher les differentes informations de l'obstacle
        @return: rien
        """
        print("\nCoordonnees : {}\n"
              "Superficie : {}\n"
              "Hauteur : {}\n"
              "Largeur : {}\n"
              .format(self.OBSgetCoordonneesSommet(), self.OBSgetSuperficie(), self.OBQgetHauteur(), self.OBQgetLargeur()))

    def OBQcalculerCoordonnees(self):
        """
        fonction permettant de calculer les 3 autre sommets de l'obstacle

        @return: rien
        """
        coinTopRight = np.array([self._tOBSCoordonneesSommet[0][0] + self.__iOBQLargeur, self._tOBSCoordonneesSommet[0][1]])
        coinBottomLeft = np.array([self._tOBSCoordonneesSommet[0][0], self._tOBSCoordonneesSommet[0][1] - self.__iOBQHauteur])
        coinBottomRight = np.array([self._tOBSCoordonneesSommet[0][0] + self.__iOBQLargeur, self._tOBSCoordonneesSommet[0][1] - self.__iOBQHauteur])
        self._tOBSCoordonneesSommet.append(coinTopRight)
        self._tOBSCoordonneesSommet.append(coinBottomLeft)
        self._tOBSCoordonneesSommet.append(coinBottomRight)


"""list_sorties = np.array([(3, 4), (2, 4)])
carreONE = CObstacleQuadrilatere(12, 12, list_sorties)
carreONE.OBSToString()"""

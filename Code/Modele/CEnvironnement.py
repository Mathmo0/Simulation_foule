import numpy as np
from Code.Modele.CPersonne import CPersonne
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere

class CEnvironnement:
    """
    Classe de l'environnement
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nom="", hauteur=1, largeur=1, sorties= np.array([(0, 0)]), listePersonnes = [CPersonne()], listeObstacles = [CObstacleQuadrilatere()]):
        self.__sENVNom = nom

        self.__iENVHauteur = hauteur
        self.__iENVLargeur = largeur

        self.__fENVSuperficie = hauteur * largeur

        self.__lENVListePersonnes = listePersonnes

        self.__lENVListeObstacles = listeObstacles

        self.__iENVNbPersonnes = len(listePersonnes)
        self.__iENVNbObstacles = len(listeObstacles)

        self.__tENVSorties = sorties

        self.ENVAttribuerSortie()

    def ENVCEnvironnementFichier(self, fichier):
        """
        Cette fonction permet de contruire un environnement a partir d'un fichier

        @param fichier: fichier .csv contenant les informations sur l'environnement
        @return: rien
        """
        self.__sENVNom, self.__iENVHauteur, self.__iENVLargeur, self.__tENVSorties, self.__lENVListePersonnes, self.__lENVListeObstacles = fichier.FICLireFichierEnvironnement()

        self.__fENVSuperficie = self.__iENVHauteur * self.__iENVLargeur

        self.__iENVNbPersonnes = len(self.__lENVListePersonnes)
        self.__iENVNbObstacles = len(self.__lENVListeObstacles)

        self.ENVAttribuerSortie()

    def ENVCEnvironnementCopie(self, environnement):
        """
        Constructeur de recopie

        @param environnement: environnement qu'on veut copier
        @return: rien
        """
        self.__sENVNom = environnement.__sENVNom

        self.__iENVHauteur = environnement.__iOBQHauteur
        self.__iENVLargeur = environnement.__iOBQLargeur

        self.__fENVSuperficie = environnement.__iOBQHauteur * environnement.__iOBQLargeur

        self.__lENVListePersonnes = environnement.__lSIMListePersonnes

        self.__lENVListeObstacles = environnement.__lENVListeObstacles

        self.__iENVNbPersonnes = len(environnement.__iENVNbPersonnes)
        self.__iENVNbObstacles = len(environnement.__iENVNbObstacles)

        self.__tENVSorties = environnement.__tENVSorties

        self.ENVAttribuerSortie()

    # -------------------Getters------------------- #
    def ENVgetNom(self):
        """
        getter pour l'attribut __sENVNom

        @return: __sENVNom
        """
        return self.__sENVNom

    def ENVgetSuperficie(self):
        """
        getter pour l'attribut __iENVNbPersonnes
        @return: __iENVNbPersonnes
        """
        return self.__fENVSuperficie

    def ENVgetNbPersonnes(self):
        """
        getter pour l'attribut __iENVNbPersonnes
        @return: __iENVNbPersonnes
        """
        return self.__iENVNbPersonnes

    def ENVgetNbObstacles(self):
        """
        getter pour l'attribut __iENVNbObstacles
        @return: __iENVNbObstacles
        """
        return self.__iENVNbObstacles

    def ENVgetSorties(self):
        """
        getter pour l'attribut __tENVSorties
        @return: __tENVSorties
        """
        return self.__tENVSorties

    def ENVgetHauteur(self):
        """
        getter pour l'attribut __iENVHauteur
        @return: __iENVHauteur
        """
        return self.__iENVHauteur

    def ENVgetLargeur(self):
        """
        getter pour l'attribut __iENVLargeur
        @return: __iENVLargeur
        """
        return self.__iENVLargeur

    def ENVgetListePersonnes(self):
        """
        getter pour l'attribut __lENVListePersonnes
        @return: __lENVListePersonnes
        """
        return self.__lENVListePersonnes

    def ENVgetListeObstacles(self):
        """
        getter pour l'attribut __lENVListeObstacles
        @return: __lENVListeObstacles
        """
        return self.__lENVListeObstacles


    # ---------------------Setters---------------------#
    def ENVsetNom(self, nom):
        """
        setter pour l'attribut __sENVNom

        @param nom: nouveau nom de l'environnement
        @return: rien
        """
        self.__sENVNom = nom

    def ENVsetHauteur(self, hauteur):
        """
        setter pour l'attribut __iENVHauteur

        @param hauteur: nouvelle hauteur de l'environnement
        @return: rien
        """
        self.__iENVHauteur = hauteur
        self.superficie = self.__iENVHauteur * self.__iENVLargeur


    def ENVsetLargeur(self, largeur):
        """
        setter pour l'attribut __iENVLargeur

        @param largeur: nouvelle largeur de l'environnement
        @return: rien
        """
        self.__iENVLargeur = largeur
        self.superficie = self.__iENVHauteur * self.__iENVLargeur

    def ENVsetSorties(self, list_sorties):
        """
        setter pour l'attribut __tENVSorties

        @param list_sorties: nouvelles sorties pour l'environnement
        @return: rien
        """
        self.__tENVSorties = list_sorties

    def ENVsetListePersonnes(self, listePersonnes):
        """
        setter pour l'attribut __lENVListePersonnes

        @param listePersonnes: nouvelles personnes qui sont dans l'environnement
        @return: rien
        """
        self.__lENVListePersonnes = listePersonnes
        self.__iENVNbPersonnes = len(self.__lENVListePersonnes)

    def ENVsetListeObstacles(self, listeObstacles):
        """
        setter pour l'attribut __lENVListeObstacles

        @param listeObstacles: nouveau obstacle qui sont dans lenvironnement
        @return: rien
        """
        self.__lENVListeObstacles = listeObstacles
        self.__iENVNbObstacles = len(self.__lENVListeObstacles)


    # -------------------Methodes-------------------#
    def ENVToString(self):
        """

        Cette fonction permet d'afficher les differentes informations sur l'environnement

        @return: rien

        """
        print(
            "\nSalle : {}\n" 
            "Superficie : {} m2\n" 
            "Hauteur : {} m\n" 
            "Largeur : {} m\n" 
            "Nombre de personnes : {}\n" 
            "Nombre d'obstacles : {}\n" 
            "Liste de sorties : {}\n"
                .format(self.ENVgetNom(), self.ENVgetSuperficie(), self.ENVgetHauteur(), self.ENVgetLargeur(), self.ENVgetNbPersonnes(), self.ENVgetNbObstacles(), self.ENVgetSorties()))
        print("\nListe des obstacles :")
        for obs in self.ENVgetListeObstacles():
            obs.OBSToString()

    def ENVAttribuerSortie(self):
        """
        Cette fonction permet d'attribuer une sortie a une personne

        @return: rien

        """
        for personnes in self.__lENVListePersonnes:
            personnes.PERajouterDirection(self.__tENVSorties)
            personnes.PERPlusCourtChemin()



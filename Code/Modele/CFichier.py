import csv
import re
import numpy as np

from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CPersonne import CPersonne
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
from Code.Controller.CEnvironnementController import CEnvironnementController


class CFichier:
    """
    Classe du fichier
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nomFichier=""):
        self.__sFICNomFichier = nomFichier# + ".csv"

    # -------------------Getters-------------------#
    def FICgetNomFichier(self):
        """
        getter pour l'attribut __sFICNomFichier

        @return: __sFICNomFichier
        """
        return self.__sFICNomFichier

    # ---------------------Setters---------------------#
    def FICsetNomFichier(self, nomFichier):
        """
        setter pour l'attribut __sFICNomFichier

        @param nomFichier: nouveau nom de fichier
        @return: rien
        """
        self.__sFICNomFichier = nomFichier

    # -------------------Methodes-------------------#
    def FICLireFichierPosition(self):
        """
        Fonction permettant de stocker les informations du fichier csv dans une liste

        @return : liste contenant les positions des personnes.
        """


        # Creation de la liste des positions
        listPositions = []

        # Ouverture du fichier
        with open(self.__sFICNomFichier, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(csv_file)
            for row in reader:
                # Stockage des positions dans la liste
                listPositions.append([float(x) for x in row])

        return listPositions

    def FICParserListeCSV(self, row):
        """
        Recupere la ligne d'un fichier CSV et la parse en format liste

        @param row:
        @return: liste
        """
        str = ""  #Variable temp pour recuper et parser
        list_coord = [np.array([0,0]) for i in range(1, len(row))]
        k = 0 #Variable pour gerer le decalage si case vide entre case renmplie

        for i in range(1, len(row)):
            if (row[i] != ''):
                str = str.join(re.split("[(,)]", row[i]))

                listtemp = [0 for i in range(2)]
                listtemp[0], listtemp[1] = str.split(" ", 1)

                listtemp[0] = int(listtemp[0])
                listtemp[1] = int(listtemp[1])

                tupletemp = np.array([listtemp[0], listtemp[1]])#(int(listtemp[0]), int(listtemp[1]))

                list_coord[i - k - 1] = tupletemp
                str = ""
            else:
                #list_coord = [list_coord[i] for i in range(0, len(list_coord) - 1)]
                list_coord.pop(i - k - 1)
                k += 1

        return list_coord

    def FICLireFichierEnvironnement(self):
        """
            fonction pour construire un objet CEnvironnement a partir d'un fichier csv

            @return : list des différents attribut récupérer par le parsing

        """
        # variables
        nom, hauteur, largeur, sorties, list_personnes, list_obstacles = "", 1, 1, np.array([np.array([0,0])]), [], []
        list_coord_obstacles = np.array([(0, 0)])
        liste_dimensions_obstacles = np.array([(0, 0)])

        # ouverture du fichier
        with open(self.__sFICNomFichier, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:

                # recuperer le nom
                if (row[0] == 'Nom'):
                    nom = row[1]

                # recuperer la hauteur
                elif (row[0] == 'Hauteur'):
                    hauteur = int(row[1])

                # recuperer la largeur
                elif (row[0] == 'Largeur'):
                    largeur = int(row[1])

                # recuperer la liste des sorties
                elif (row[0] == 'Sortie(s)'):
                    sorties = self.FICParserListeCSV(row)
                    for sortie in sorties:
                        sortie[0], sortie[1] = CEnvironnementController.ENCControleInCanvas(sortie[0], sortie[1], hauteur, largeur)
                        sortie[0] = 400 * sortie[0] / largeur
                        sortie[1] = 400 * sortie[1] / hauteur

                # recuperer la liste des personnes
                elif (row[0] == 'Liste de personnes'):
                    list_coord = self.FICParserListeCSV(row)
                    for coord in list_coord:
                        coord[0], coord[1] = CEnvironnementController.ENCControleInCanvas(coord[0], coord[1], hauteur, largeur)
                        coord[0] = 400 * coord[0] / largeur
                        coord[1] = 400 * coord[1] / hauteur
                    list_personnes = [CPersonne(False,coord) for coord in list_coord]

                # recuperer la liste des obstacles
                elif (row[0] == 'Liste coordonnees d\'obstacles'):
                    list_coord_obstacles = self.FICParserListeCSV(row)
                    k = 0
                    for coord in list_coord_obstacles:
                        if CEnvironnementController.ENCControleObstaclesInCanvas(coord[0], coord[1], hauteur, largeur) == 1:
                            coord[0] = 400 * coord[0] / largeur
                            coord[1] = 400 * coord[1] / hauteur
                        else :
                            list_coord_obstacles = [list_coord_obstacles[i] for i in range(0, len(list_coord_obstacles) - 1)]
                            k += 1

                # recuperer la liste des dimensions d'obstacles
                elif(row[0] == 'Liste dimensions d\'obstacles (H,L)'):
                    liste_dimensions_obstacles = self.FICParserListeCSV(row)
                    for coord in liste_dimensions_obstacles:
                        coord[0] = 400 * abs(coord[0]) / hauteur
                        coord[1] = 400 * abs(coord[1]) / largeur

            #Construction de la liste des obstacles
            print(list_coord_obstacles)
            list_obstacles = [CObstacleQuadrilatere(0,0,coordO) for coordO in list_coord_obstacles] #initilisation de la liste
            for i in range(min(len(list_coord_obstacles), len(liste_dimensions_obstacles))):
                list_obstacles[i].OBQsetHauteur(liste_dimensions_obstacles[i][0])
                list_obstacles[i].OBQsetLargeur(liste_dimensions_obstacles[i][1])

            for obs in list_obstacles:
                obs.OBQcalculerCoordonnees()

            return nom, hauteur, largeur, sorties, list_personnes, list_obstacles



import csv
import re
import numpy as np

from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CPersonne import CPersonne
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere


class CFichier:
    """
    Classe du fichier
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nomFichier=""):
        self.sNomFichier = nomFichier + ".csv"

    # -------------------Getters-------------------#
    def getNomFichier(self):
        return self.sNomFichier

    # ---------------------Setters---------------------#
    def setNomFichier(self, nomFichier):
        self.sNomFichier = nomFichier

    # -------------------Methodes-------------------#
    def LireFichierPosition(self):
        """
        Fonction permettant de stocker les informations du fichier csv dans une liste

        @return : liste contenant les positions des personnes.
        """


        # Creation de la liste des positions
        listPositions = []

        # Ouverture du fichier
        with open(self.sNomFichier, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(csv_file)
            for row in reader:
                # Stockage des positions dans la liste
                listPositions.append([float(x) for x in row])

        return listPositions

    def ParserListeCSV(self, row):
        """
        Recupere la ligne d'un fichier CSV et la parse en format liste

        :param row:
        :return: liste
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
                list_coord = [list_coord[i] for i in range(0, len(list_coord) - 1)]
                k += 1

        return list_coord

    def LireFichierEnvironnement(self):
        """
            fonction pour construire un objet CEnvironnement a partir d'un fichier csv

            @return :

        """
        # variables
        nom, hauteur, largeur, sorties, list_personnes, list_obstacles = "", 0, 0, np.array([np.array([0,0])]), [], []
        list_coord_objstacles = np.array([(0, 0)])
        liste_dimensions_obstacles = np.array([(0, 0)])

        # ouverture du fichier
        with open(self.sNomFichier, newline='') as csvfile:
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
                    sorties = self.ParserListeCSV(row)

                # recuperer la liste des personnes
                elif (row[0] == 'Liste de personnes'):
                    list_coord = self.ParserListeCSV(row)
                    list_personnes = [CPersonne(False,coord) for coord in list_coord]

                # recuperer la liste des obstacles
                elif (row[0] == 'Liste coordonnées d\'obstacles'):
                    list_coord_obstacles = self.ParserListeCSV(row)

                # recuperer la liste des dimensions d'obstacles
                elif(row[0] == 'Liste dimensions d\'obstacles (H,L)'):
                    liste_dimensions_obstacles = self.ParserListeCSV(row)

            #Construction de la liste des obstacles
            print(list_coord_obstacles)
            list_obstacles = [CObstacleQuadrilatere(0,0,coordO) for coordO in list_coord_obstacles] #initilisation de la liste
            for i in range(min(len(list_coord_obstacles), len(liste_dimensions_obstacles))):
                list_obstacles[i].setHauteur(liste_dimensions_obstacles[i][0])
                list_obstacles[i].setLargeur(liste_dimensions_obstacles[i][1])

            return nom, hauteur, largeur, sorties, list_personnes, list_obstacles

"""fichier = CFichier("../../environnements/Environnement_0")

test = CEnvironnement()
test.CEnvironnementFichier(fichier)
test.ENVToString()"""

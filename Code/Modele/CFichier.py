import csv
import re
import numpy as np

from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CPersonne import CPersonne


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

    def LireFichierEnvironnement(self):
        """
            fonction pour construire un objet CEnvironnement a partir d'un fichier csv

            @return :

        """
        # variables
        nom, hauteur, largeur, sorties, list_personnes, list_obstacles = "", 0, 0, np.array([(0, 0)]), np.array([(0, 0)]), np.array([(0, 0)])

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
                    str = ""
                    sorties = np.array([(0, 0) for i in range(1, len(row))])
                    k = 0
                    for i in range(1, len(row)):
                        if(row[i] != ''):
                            str = str.join(re.split("[(,)]", row[i]))

                            listtemp = [0 for i in range(2)]
                            listtemp[0], listtemp[1] = str.split(" ", 1)

                            listtemp[0] = int(listtemp[0])
                            listtemp[1] = int(listtemp[1])

                            tupletemp = (int(listtemp[0]), int(listtemp[1]))

                            sorties[i - k - 1] = tupletemp
                            str = ""
                        else:
                            sorties = np.array([sorties[i] for i in range(0, len(sorties) - 1)])
                            k += 1

                # recuperer la liste des personnes
                elif (row[0] == 'Liste de personnes'):
                    str = ""
                    list_coord = np.array([(0, 0) for i in range(1, len(row))])
                    k = 0
                    for i in range(1, len(row)):
                        if(row[i] != ''):
                            str = str.join(re.split("[(,)]", row[i]))

                            listtemp = [0 for i in range(2)]
                            listtemp[0], listtemp[1] = str.split(" ", 1)

                            listtemp[0] = int(listtemp[0])
                            listtemp[1] = int(listtemp[1])

                            tupletemp = (int(listtemp[0]), int(listtemp[1]))

                            list_coord[i - k - 1] = tupletemp
                            str = ""
                        else:
                            list_coord = np.array([list_coord[i] for i in range(0, len(list_coord) - 1)])
                            k += 1
                    list_personnes = [CPersonne(coord) for coord in list_coord]

                # recuperer la liste des obstacles


            return nom, hauteur, largeur, sorties, list_personnes, list_obstacles

fichier = CFichier('E:\Projets\projets7_simulation\Environnements\Environnement_0')

test = CEnvironnement()
test.CEnvironnementFichier(fichier)
test.ENVToString()

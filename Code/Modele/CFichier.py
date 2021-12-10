import csv
import re
import numpy as np

from Modele.CEnvironnement import CEnvironnement


class CFichier:
    """
    Classe du fichier
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nomFichier=""):
        self.sNomFichier = nomFichier + ".csv"

    # -------------------Getters-------------------#
    def getNomFichier(self):
        """
            getter pour le nom du fichier

        """
        return self.sNomFichier

    # ---------------------Setters---------------------#
    def setNomFichier(self, nomFichier):
        """
            setter pour le nom du fichier

        """
        self.sNomFichier = nomFichier

    # -------------------Methodes-------------------#
    def LireFichierPositions(self):
        """
            fonction permettant de stocker les informations du fichier csv dans une liste.

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
        nom, hauteur, largeur, sorties, list_personnes, list_objets = "", 0, 0, np.array([(0, 0)]), np.array([(0, 0)]), np.array([(0, 0)])

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
                    for i in range(1, len(row)):
                        str = str.join(re.split("[(,)]", row[i]))

                        listeoe = [0 for i in range(2)]
                        listeoe[0], listeoe[1] = str.split(" ", 1)

                        listeoe[0] = int(listeoe[0])
                        listeoe[1] = int(listeoe[1])

                        tuplePLZ = (int(listeoe[0]), int(listeoe[1]))

                        sorties[i - 1] = tuplePLZ
                        str = ""

                # recuperer la liste des personnes

                # recuperer la liste des obstacles

            return nom, hauteur, largeur, sorties, list_personnes, list_objets

fichier = CFichier('E:\Projets\projets7_simulation\Environnements\Environnement_0')

#test = CEnvironnement(fichier)
#test = CEnvironnement(nom, hauteur, largeur, sorties, list_personnes, list_objets)
#test.ENVToString()

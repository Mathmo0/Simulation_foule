import csv

class CFichier:
    """
    Classe du fichier
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nomFichier = ""):
        self.sNomFichier = nomFichier+".csv"

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
        #Creation de la liste des positions
        listPositions = []

        #Ouverture du fichier
        with open(self.sNomFichier, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(csv_file)
            for row in reader:
                #Stockage des positions dans la liste
                listPositions.append([float(x) for x in row])

        return listPositions

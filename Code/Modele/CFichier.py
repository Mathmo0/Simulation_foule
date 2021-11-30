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
        return self.sNomFichier


    # ---------------------Setters---------------------#
    def setNomFichier(self, nomFichier):
        self.sNomFichier = nomFichier


    # -------------------Methodes-------------------#
    def LireFichier(self):
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

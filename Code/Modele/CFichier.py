

class CFichier:
    """
    Classe du fichier
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nomFichier = ""):
        self.sNomFichier = nomFichier

    # -------------------Getters-------------------#
    def getNomFichier(self):
        return self.sNomFichier


    # ---------------------Setters---------------------#
    def setNomFichier(self, nomFichier):
        self.sNomFichier = nomFichier


    # -------------------Methodes-------------------#


class CEnvironnementController:

    @staticmethod
    def ENCControleInCanvas(coordX, coordY, hauteur, largeur):
        """
        Fonction qui verifie si les coordonnees sont bien dans le canvas. Si ce n'est pas le cas on change la valeur pour qu'elle convienne

        @param coordX: coordonnee x
        @param coordY: coordonnee y
        @param hauteur: Hauteur de l'environnement
        @param largeur: Largeur de l'environnement

        @return: coordX, coordY
        """

        if coordX > largeur:
            coordX = largeur
        elif coordX < 0:
            coordX = 0

        if coordY > hauteur:
            coordY = hauteur
        elif coordY < 0:
            coordY = 0

        return coordX, coordY

    @staticmethod
    def ENCControlePersonnesInCanvas(coordX, coordY, hauteur, largeur):
        """
        Fonction qui verifie si les coordonnees de la personne sont bien dans le canvas. Si ce n'est pas le cas on change la valeur pour qu'elle convienne

        @param coordX: Coordonnee x de la personne
        @param coordY: Coordonnee y de la personne
        @param hauteur: Hauteur de l'environnement
        @param largeur: Largeur de l'environnement

        @return: void
        """
        return CEnvironnementController.ENCControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ENCControleSortieInCanvas(coordX, coordY, hauteur, largeur):
        """
        Fonction qui verifie si les coordonnees de la sortie sont bien dans le canvas. Si ce n'est pas le cas on change la valeur pour qu'elle convienne

        @param coordX: Coordonnee x de la sortie
        @param coordY: Coordonnee y de la sortie
        @param hauteur: Hauteur de l'environnement
        @param largeur: Largeur de l'environnement
        @return: void
        """
        return CEnvironnementController.ENCControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ENCControleObstaclesInCanvas(coordX, coordY, hauteur, largeur):
        """
        Fonction qui verifie si les coordonnees de l'obstacle  sont bien dans le canvas. Si les coordonnees sont bien dans le canvas on retourne 0 sinon on retourne 1

        @param coordX: Coordonnee x de l'obstacle
        @param coordY: Coordonnee y de l'obstacle
        @param hauteur: Hauteur de l'environnement
        @param largeur: Largeur de l'environnement

        @return: void

        """
        if coordX > largeur:
            return 0

        if coordY < 0:
            return 0

        return 1

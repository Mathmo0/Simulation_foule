import pygame
import sys
import numpy as np
import pygame

from Modele.CObstacle import CObstacle


class CObstacleQuadrilatere(CObstacle):
    """
    Classe des obstacles de type quadrilatere
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nom="", hauteur=0, largeur=0, coordonneesSommets=np.array([(0, 0)])):
        super().__init__(nom, coordonneesSommets)
        self.iSuperficie = hauteur * largeur
        self.iHauteur = hauteur
        self.iLargeur = largeur
        self.rect = pygame.Rect(self.tCoordonneesSommet[0, 0], self.tCoordonneesSommet[0, 1], self.iLargeur,
                                self.iHauteur)

    # -------------------Getters-------------------#
    def getHauteur(self):
        return self.iHauteur

    def getLargeur(self):
        return self.iLargeur

    # ---------------------Setters---------------------#
    def setHauteur(self, hauteur):
        self.iHauteur = hauteur
        self.iSuperficie = self.iHauteur * self.iLargeur

    def setLargeur(self, largeur):
        self.iLargeur = largeur
        self.iSuperficie = self.iHauteur * self.iLargeur

    # -------------------Methodes-------------------#
    def OBSToString(self):
        print("\nNom : {}\n"
              "Coordonnees : {}\n"
              "Superficie : {}\n"
              "Hauteur : {}\n"
              "Largeur : {}\n"
              .format(self.getNom(), self.getCoordoneesSommet(), self.getSuperficie(), self.getHauteur(),
                      self.getLargeur()))

    # -------------------Dessin-------------------#
    def Dessin(self):
        screen = pygame.display.set_mode((screen_width, screen_height))
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        pygame.display.flip()


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800

"""moving_rect = pygame.Rect(350, 350, 100, 100)"""
x_speed, y_speed = 5, 4

"""other_rect = pygame.Rect(300, 600, 200, 100)"""
"""other_speed = 2"""
list_sorties = np.array([(350, 350), (2, 4)])
list_sorties2 = np.array([(300, 300), (2, 4)])
carreONE = CObstacleQuadrilatere("carreone", 120, 120, list_sorties)
carreTWO = CObstacleQuadrilatere("carretwo", 120, 120, list_sorties)
carreONE.OBSToString()
carreTWO.OBSToString()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    clock.tick(60)
    carreONE.Dessin()
    carreTWO.Dessin()

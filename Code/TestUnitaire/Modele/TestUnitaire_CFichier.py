import unittest

import numpy as np

from Code.Modele.CFichier import CFichier
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
from Code.Modele.CPersonne import CPersonne

class TestUnitaire_CFichier(unittest.TestCase):

    def setUp(self) -> None:
        self.fichier0 = CFichier("../../environnements/Environnement_0")
        self.fichier1 = CFichier("../../environnements/Environnement_1")

        self.environnement0 = CEnvironnement().CEnvironnementFichier(self.fichier0)
        self.environnement1 = CEnvironnement().CEnvironnementFichier(self.fichier1)

        self.sorties0 = np.array([(3, 4), (2, 4), (5,6)])

        self.coord_Personne = np.array([(2,2), (1,1)])

        self.liste_Personnes = [CPersonne(coord) for coord in self.coord_Personne]

        self.coord_Obstacles = np.array([(6,4), (4,8), (8,8)])

        self.liste_Obstacles = [CObstacleQuadrilatere(0,0,coord) for coord in self.coord_Obstacles]

    def test_Lecture_Fichier_Environnement(self):
        self.assertEqual(self.environnement0, CEnvironnement("Burreau", 34, 20, self.sorties0))
        self.assertEqual(self.environnement1, CEnvironnement())

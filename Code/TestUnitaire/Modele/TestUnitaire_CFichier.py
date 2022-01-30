import unittest

import numpy as np

from Code.Modele.CFichier import CFichier
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
from Code.Modele.CPersonne import CPersonne

class TestUnitaire_CFichier(unittest.TestCase):

    def setUp(self) -> None:
        self.fichier0 = CFichier("../../../environnements/Environnement_0")
        self.fichier1 = CFichier("../../../environnements/Environnement_1")
        self.fichier2 = CFichier("../../../environnements/Environnement_2")


        self.environnement0 = CEnvironnement()
        self.environnement0.ENVCEnvironnementFichier(self.fichier0)

        self.environnement1 = CEnvironnement()
        self.environnement1.ENVCEnvironnementFichier(self.fichier1)

        self.environnement2 = CEnvironnement()
        self.environnement2.ENVCEnvironnementFichier(self.fichier2)

        self.sorties0 = np.array([(3, 4), (2, 4), (5,6)])

        self.coord_Personne = np.array([(2,2), (1,1), (3,3)])

        self.liste_Personnes = [CPersonne(coord) for coord in self.coord_Personne]

        self.coord_Obstacles = np.array([(6,4), (4,8), (8,8)])
        self.coord_dimension_obstacles = np.array([(25, 45), (12, 12)])

        self.liste_Obstacles = [CObstacleQuadrilatere(0,0,coord) for coord in self.coord_Obstacles]
        for i in range(min(len(self.coord_Obstacles), len(self.coord_dimension_obstacles))):
            self.liste_Obstacles[i].OBQsetHauteur(self.coord_dimension_obstacles[i][0])
            self.liste_Obstacles[i].OBQsetLargeur(self.coord_dimension_obstacles[i][1])

        self.environnementREF = CEnvironnement("Burreau", 34, 20, self.sorties0, self.liste_Personnes, self.liste_Obstacles)

    def test_Lecture_Fichier_Environnement(self):
        """
        verifie bien que l'objet est bien du bon type

        :return: rien
        """
        print("\ntest du type :\n")
        self.assertIsInstance(self.environnement0, CEnvironnement)
        self.assertIsInstance(self.environnement1, CEnvironnement)
        self.assertIsInstance(self.environnement2, CEnvironnement)
        print("OK\n")

    def test_Attributs_equal_Env0(self):
        print("\ntest de la bonne récupération des données dans le fichier environnement0.csv :\n")
        self.assertEqual(self.environnement0.ENVgetNom(), self.environnementREF.ENVgetNom())
        self.assertEqual(self.environnement0.ENVgetSuperficie(), self.environnementREF.ENVgetSuperficie())
        self.assertEqual(self.environnement0.ENVgetNbPersonnes(), self.environnementREF.ENVgetNbPersonnes())
        self.assertEqual(self.environnement0.ENVgetNbObstacles(), self.environnementREF.ENVgetNbObstacles())
        self.assertEqual(self.environnement0.ENVgetSorties().all(), self.environnementREF.ENVgetSorties().all())
        self.assertEqual(self.environnement0.ENVgetHauteur(), self.environnementREF.ENVgetHauteur())
        self.assertEqual(self.environnement0.ENVgetLargeur(), self.environnementREF.ENVgetLargeur())
        print("OK\n")


if __name__ == '__main__' :
    unittest.main()

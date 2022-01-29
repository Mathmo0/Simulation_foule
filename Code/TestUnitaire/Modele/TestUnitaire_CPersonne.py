import sys
sys.path.append('..')
import unittest
import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CPersonne import CPersonne
from Code.Modele.CObstacle import CObstacle

class TestUnitaire_CPersonne(unittest.TestCase) :

    def setUp(self) :
        self.Position = np.array([1, 3])
        self.PositionDeltaT = np.array([4, 9])
        self.Position3 = np.array([31, 33])
        self.personne = CPersonne(False,self.Position,2.0,10,1)
        self.Direction1 = np.array([10,11])
        self.Direction2 = np.array([20, 21])
        self.listDirection = [self.Direction2,self.Direction1]
        self.personne.PERsetListDirection(self.listDirection)

    def test_RecupererDirectionActuelle_is_OK(self):

        direction = self.personne.PERRecupererDirectionActuelle()

        self.assertEqual(direction[0],20)
        self.assertEqual(direction[1],21)

    def test_RecupererDerniereCoordonne_is_OK_for_1_element(self):
        self.personne.PERsetListCoordonnees([self.Position])

        coord = self.personne.PERRecupererDerniereCoordonne()

        self.assertEqual(coord[0],1)
        self.assertEqual(coord[1],3)

    def test_RecupererDerniereCoordonne_is_OK_for_2_element(self):
        self.personne.PERsetListCoordonnees([self.PositionDeltaT, self.Position])

        coord = self.personne.PERRecupererDerniereCoordonne()

        self.assertEqual(coord[0], 1)
        self.assertEqual(coord[1], 3)

    def test_ajouterCoordonnees_when_listcoord_is_empty(self) :

        self.personne.PERsetListCoordonnees([])
        self.personne.PERajouterCoordonnees(self.Position3)
        coord = self.personne.PERRecupererDerniereCoordonne()

        self.assertEqual(coord[0], 31)
        self.assertEqual(coord[1], 33)

    def test_ajouterCoordonnees_when_listcoord_is_full(self):
        self.personne.PERsetListCoordonnees([self.PositionDeltaT, self.Position])
        self.personne.PERajouterCoordonnees(self.Position3)
        coord = self.personne.PERRecupererDerniereCoordonne()

        self.assertEqual(coord[0], 31)
        self.assertEqual(coord[1], 33)

    def test_ajouterPersonne_is_OK(self) :
        personneAdd = CPersonne()
        self.personne.PERajouterPersonne(personneAdd)

        self.assertIn(personneAdd, self.personne.PERgetListPersonneProx())


    def test_ajouterDirection_is_OK(self):

        self.personne.PERajouterDirection(np.array([10, 10]))

        self.assertIn(np.array([10,10]), self.personne.PERgetListDirection())

    def test_ajouterObstacle_is_OK(self):

        obstacle = CObstacle()
        self.personne.PERajouterObstacle(obstacle)

        self.assertIn(obstacle, self.personne.PERgetlistObstacle())

    def test_ClearPersonneProximite_is_OK(self):
        personneAdd = CPersonne()
        self.personne.PERajouterPersonne(personneAdd)

        self.personne.PERClearPersonneProximite()

        self.assertEqual(len(self.personne.PERgetListPersonneProx()), 0)

    def test_ClearlistObstacleProx_is_OK(self):
        obstacle = CObstacle()
        self.personne.PERajouterObstacle(obstacle)

        self.personne.PERClearlistObstacleProx()

        self.assertEqual(len(self.personne.PERgetlistObstacle()), 0)

    #def test_CalculVitesse_normal_case(self):

    #def test_CalculVitesse_vitesse_trop_eleve(self):

    def test_sorti_is_False(self):

        self.personne.PERajouterCoordonnees(np.array([11, 11]))

        self.assertFalse(self.personne.PERsorti())

    def test_sorti_is_True(self):
        self.personne.PERajouterCoordonnees(np.array([21, 21]))

        self.assertTrue(self.personne.PERsorti())





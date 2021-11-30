import sys
sys.path.append('..')
import unittest
import numpy as np

from Code.Modele.CForce import CForce

class TestUnitaire_CForce(unittest.TestCase) :

    def setUp(self) -> None:
        self.force = CForce()
        self.Position = np.array([8.20717452, 13.00797169])
        self.PositionDeltaT = np.array([4.62152356, 9.02391506])
        self.vRkAlpha = np.array([1,5])

    def test_force_is_instance_of_CForce(self):
        self.assertIsInstance(self.force,CForce)

    def test_VitesseAlphaMax_is_OK(self):

        self.assertEqual(1.742, round(self.force.VitesseAlphaMax(1.34), 3))

    def test_VecteurVitesse_is_OK(self):
        t = 4
        vecteurVitesse = self.force.VecteurVitesse(self.Position, self.PositionDeltaT, t)

        self.assertEqual(0.89641274,round(vecteurVitesse[0],8))
        self.assertEqual(0.99601416,round(vecteurVitesse[1],8))

    def test_VecteurVitesse_when_t_equal_0(self):
        t = 0
        vecteurVitesse = self.force.VecteurVitesse(self.Position, self.PositionDeltaT, t)
        self.assertEqual(0,vecteurVitesse[0])
        self.assertEqual(0,vecteurVitesse[1])

    def test_eAlpha_is_OK(self) :
        eAlpha =self.force.eAlpha(self.vRkAlpha, self.Position)
        self.assertEqual(-0.66896473, round(eAlpha[0],8))
        self.assertEqual(-0.74329415, round(eAlpha[1],8))

    def test_b_is_OK(self) :
        resultat = self.force.b(np.array([10,15]),np.array([11,10]),1.34,np.array([1,5]))
        self.assertEqual(5.57,round(resultat,2))

    def test_VAlphaBeta_is_OK(self):
        self.assertEqual(3.4,round(self.force.VAlphaBeta(4)*(10**(6)),2))

    def test_UAlphaObstacle_is_OK(self):

        resultat = self.force.UAlphaObstacle(4)

        self.assertEqual(2.06,round(resultat * (10 ** (8)), 2))

if __name__ == '__main__' :
    unittest.main()

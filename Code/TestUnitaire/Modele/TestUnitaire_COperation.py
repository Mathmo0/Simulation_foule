import sys
sys.path.append('..')
import unittest
import numpy as np

from Code.Modele.COperation import COperation
class TestUnitaire_COperation(unittest.TestCase) :


    def setUp(self) :
        self.Position = np.array([1, 3])
        self.PositionDeltaT = np.array([4, 9])
        self.PositionB = np.array([5, 5])

    def test_DetectionCercle_is_OK(self) :
        self.assertTrue(COperation.DetectionCercle(0, 0, 1, 1, 3))

    def test_DetectionCercle_is_not_OK(self):
        self.assertFalse(COperation.DetectionCercle(0, 0, 3, 3, 1.5))

    def test_FonctionTrajectoirePieton_is_OK(self):

        resultat = COperation.FonctionTrajectoirePieton(self.Position, self.PositionDeltaT)
        self.assertEqual(resultat[0],2)
        self.assertEqual(resultat[1],1)

    def test_Nabla_is_OK(self):

        resultat = COperation.Nabla(self.Position, self.PositionDeltaT, self.PositionB)
        self.assertEqual(resultat[0], 5)
        self.assertEqual(resultat[1], -8)

    if __name__ == '__main__' :
        unittest.main()
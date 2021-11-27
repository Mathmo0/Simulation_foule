import sys
sys.path.append('..')
import unittest
from Code.Modele.COperation import COpetation
class TestUnitaire_COperation(unittest.TestCase) :

    def test_DetectionCercle_is_OK(self) :
        self.assertTrue(COpetation.DetectionCercle(0,0,1,1,3))

    def test_DetectionCercle_is_not_OK(self):
        self.assertFalse(COpetation.DetectionCercle(0, 0, 3, 3, 1.5))

    if __name__ == '__main__' :
        unittest.main()
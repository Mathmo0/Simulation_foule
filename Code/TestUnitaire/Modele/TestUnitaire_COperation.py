import unittest
from Code.Modele.COperation import COpetation
class TestUnitaire_COperation(unittest.TestCase) :

    def test_DetectionCercle_OK(self) :

        var = COpetation.DetectionCercle(0,0,1,1,3)
        self.assertTrue(var)
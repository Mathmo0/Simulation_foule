import unittest
import numpy as np

from Code.Modele.CFAcceleration import CFAcceleration
from Code.Modele.CForce import CForce

class TestUnitaire_CFAttraction(unittest.TestCase):

    def setUp(self) -> None:
        self.Acceleration = CFAcceleration()
        self.vAlpha = np.array([0,0])
        self.vAlpha0 = 1.34
        self.vRkAlpha = np.array([1,5])
        self.vRalpha = np.array([10,15])

    def test_CFAceleration_is_istance_of_CForce(self):
        self.assertIsInstance(self.Acceleration,CForce)

    def test_FACForceDacceleration_is_OK(self):
        acceleration = self.Acceleration.FACForceDacceleration(self.vAlpha,self.vAlpha0,self.vRkAlpha,self.vRalpha)
        self.assertEqual(-1.79,round(acceleration[0],2))
        self.assertEqual(-1.99,round(acceleration[1],2))




if __name__ == '__main__':
    unittest.main()

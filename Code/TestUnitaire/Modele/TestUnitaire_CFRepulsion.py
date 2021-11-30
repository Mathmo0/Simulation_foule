import unittest

from Code.Modele.CForce import CForce
from Code.Modele.CFRepulsion import CFRepulsion

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.repulsion = CFRepulsion()

    def Test_repulsion_is_instance_of_CForce(self):
        self.assertIsInstance(self.repulsion,CForce)

    def Test_FREEffetDeRepulsion_is_OK(self):
        self.assertEqual()

    def Test_FREForceDeRepulsionObstacle_is_OK(self):
        self.assertEqual()

    def Test_FREForceRepulsionPersonne_is_OK(self) :
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()

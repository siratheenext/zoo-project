import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_baby_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)
    
    def test_young_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(79), 100)
    
if __name__ == '__main__':
    unittest.main()
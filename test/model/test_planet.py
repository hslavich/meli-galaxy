import unittest

from model.Planet import Planet

class PlanetTest(unittest.TestCase):

    def test_initial_angle(self):
        planet = Planet('Ferengi', 1, 500)
        self.assertEqual(90, planet.angle)

    def test_move(self):
        planet = Planet('Ferengi', 1, 500, Planet.ANTICLOCKWISE)
        self.assertEqual(90, planet.angle)

        planet.move(1)
        self.assertEqual(91, planet.angle)

        planet.move(5)
        self.assertEqual(96, planet.angle)

    def test_position(self):
        planet = Planet('Ferengi', 1, 500, Planet.ANTICLOCKWISE)
        self.assertEqual((0, 500), planet.position)        
        self.assertEqual((-500, 0), planet.move(90))
        self.assertEqual((0, -500), planet.move(90))
        self.assertEqual((500, 0), planet.move(90))
        self.assertEqual((0, 500), planet.move(90))

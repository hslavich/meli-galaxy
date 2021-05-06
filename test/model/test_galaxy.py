import unittest
from unittest.mock import MagicMock

from model.Galaxy import Galaxy


class GalaxyTest(unittest.TestCase):

    def test_initial_state(self):
        galaxy = Galaxy()
        self.assertEqual(galaxy.status, Galaxy.STATUS_DROUGHT)

    def test_states(self):
        galaxy = Galaxy()

        positions = [(400, 500), (410, 1000), (420, 2000)]
        galaxy.planet_positions = MagicMock(return_value=positions)
        galaxy.check_status()
        self.assertEqual(galaxy.status, Galaxy.STATUS_OPTIMAL)

        positions = [(-211.31, -453.15), (819.15, 573.58), (-1931.85, -517.64)]
        galaxy.planet_positions.return_value = positions
        galaxy.check_status()
        self.assertEqual(galaxy.status, Galaxy.STATUS_RAINY)

        positions = [(211.31, -453.15), (819.15, 573.58), (1931.85, -517.64)]
        galaxy.planet_positions.return_value = positions
        galaxy.check_status()
        self.assertEqual(galaxy.status, Galaxy.STATUS_QUIET)

        positions = [(211.31, 0), (819.15, 0), (1931.85, 0)]
        galaxy.planet_positions.return_value = positions
        galaxy.check_status()
        self.assertEqual(galaxy.status, Galaxy.STATUS_DROUGHT)

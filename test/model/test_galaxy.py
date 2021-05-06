import unittest

from model.Galaxy import Galaxy


class GalaxyTest(unittest.TestCase):

    def test_initial_state(self):
        galaxy = Galaxy()
        self.assertEqual(galaxy.status, Galaxy.STATUS_DROUGHT)

import unittest

from model.Period import Period
from model.Galaxy import Galaxy


class PeriodTest(unittest.TestCase):

    def test_max_area(self):
        period = Period(1, Galaxy.STATUS_RAINY, 100)
        period.register_area(2, 200)
        period.register_area(3, 301.1)
        period.register_area(5, 301)
        self.assertEqual((3, 301.1), period.max_area)

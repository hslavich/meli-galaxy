import unittest
from unittest.mock import PropertyMock, patch

from model.Predictor import Predictor
from model.Galaxy import Galaxy
from model.Period import Period


class PredictorTest(unittest.TestCase):

    def test_count_periods(self):
        periods = []
        periods.append(Period(1, Galaxy.STATUS_RAINY, 100))
        periods.append(Period(10, Galaxy.STATUS_DROUGHT, 100))
        periods.append(Period(13, Galaxy.STATUS_RAINY, 100))
        periods.append(Period(18, Galaxy.STATUS_OPTIMAL, 100))
        periods.append(Period(20, Galaxy.STATUS_QUIET, 100))
        periods.append(Period(25, Galaxy.STATUS_DROUGHT, 100))
        predictor = Predictor()
        predictor.periods = periods
        self.assertEqual(len(predictor.drought_periods()), 2)
        self.assertEqual(len(predictor.rainy_periods()), 2)
        self.assertEqual(len(predictor.optimal_periods()), 1)

    @patch.object(Galaxy, 'status', create=True, new_callable=PropertyMock)
    @patch.object(Galaxy, 'area', create=True, new_callable=PropertyMock)
    def test_max_area(self, mock_area, mock_status):
        mock_area.return_value = 5000
        mock_status.return_value = Galaxy.STATUS_RAINY
        predictor = Predictor()
        predictor.run(50)
        self.assertEqual(predictor.max_rainy_day().max_area, (1, 5000))

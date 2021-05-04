import unittest

import utils.Utils as utils

class UtilsTest(unittest.TestCase):

    def test_are_points_aligned(self):
        points = [(0, 500), (0, 1000), (0, 2000)]
        self.assertTrue(utils.aligned(points))

        points = [(500, 0), (1000, 0), (2000, 0)]
        self.assertTrue(utils.aligned(points))

        points = [(0, 0), (1, 1), (2, 2)]
        self.assertTrue(utils.aligned(points))

    def test_line(self):
        # y = x
        points = [(0, 0), (1, 1)]
        m, b = utils.get_line(points[0], points[1])
        self.assertEqual(m, 1)
        self.assertEqual(b, 0)

        # y = 0
        points = [(0, 0), (1, 0)]
        m, b = utils.get_line(points[0], points[1])
        self.assertEqual(m, 0)
        self.assertEqual(b, 0)

        # y = 2x
        points = [(0, 0), (1, 2)]
        m, b = utils.get_line(points[0], points[1])
        self.assertEqual(m, 2)
        self.assertEqual(b, 0)

        # y = 2x + 2
        points = [(-1, 0), (1, 4)]
        m, b = utils.get_line(points[0], points[1])
        self.assertEqual(m, 2)
        self.assertEqual(b, 2)

    def test_line_intersects_circle(self):
        # y = 0 -- distancia 2
        self.assertFalse(utils.line_intersects_circle(0, 0, (1, 2), 1))
        self.assertTrue(utils.line_intersects_circle(0, 0, (1, 2), 2))

        # y = x distancia 1,41
        self.assertFalse(utils.line_intersects_circle(1, 0, (3, 1), 1))
        self.assertTrue(utils.line_intersects_circle(1, 0, (3, 1), 1.5))

    def test_triangle_area(self):
        self.assertEqual(utils.triangle_area([(0, 0), (0, 0), (0, 0)]), 0)
        self.assertEqual(utils.triangle_area([(0, 0), (1, 2), (2, 0)]), 2)
        self.assertEqual(utils.triangle_area([(0, 1), (1, 4), (2, 2)]), 2.5)

    def test_point_inside_triangle(self):
        triangle = [(0, 0), (1, 2), (2, 0)]
        self.assertTrue(utils.point_inside_triangle(triangle, (0, 0)))
        self.assertTrue(utils.point_inside_triangle(triangle, (1, 1)))
        self.assertFalse(utils.point_inside_triangle(triangle, (-1, -1)))

        triangle = [(-0.5, -0.5), (0, 5), (2, -1)]
        self.assertTrue(utils.point_inside_triangle(triangle, (0, 0)))
        self.assertFalse(utils.point_inside_triangle(triangle, (0, 5.1)))

        triangle = [(-211.31, -453.15), (819.15, 573.58), (-1931.85, -517.64)]
        self.assertTrue(utils.point_inside_triangle(triangle, (0, 0)))

        triangle = [(490.81, 95.4), (-573.58, 819.15), (-1677.34, -1089.28)]
        self.assertTrue(utils.point_inside_triangle(triangle, (0, 0)))

        triangle = [(489.07, -103.96), (-500.0, -866.03), (-1618.03, 1175.57)]
        self.assertTrue(utils.point_inside_triangle(triangle, (0, 0)))

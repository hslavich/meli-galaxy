import math
import numpy as np

def aligned(points):
    if all(p[0] == 0 for p in points):
        return True
    m, b = get_line(points[0], points[1])
    return line_intersects_circle(m, b, points[2], 150)

def get_line(point1, point2):
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point1[1] - m * point1[0]
    return m, b

def line_intersects_circle(m, b, point, r):
    '''
    https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    '''
    return abs(b + m * point[0] - point[1]) / math.sqrt(1 + m ** 2) <= r

def triangle_area(points):
    x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]
    return abs(0.5 * (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))))

def point_inside_triangle(points, p):
    area_triangle = triangle_area(points)
    area_abp = triangle_area([points[0], points[1], p])
    area_acp = triangle_area([points[0], points[2], p])
    area_bcp = triangle_area([points[1], points[2], p])
    return math.isclose(area_triangle, area_abp + area_acp + area_bcp)

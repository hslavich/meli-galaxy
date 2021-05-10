import math
import numpy as np

PLANET_RADIUS = 100


def aligned(points):
    '''Retorna si la recta difinida por los puntos esta alineada entre si y con respecto al (0,0)'''
    # Chequea si los puntos estan alineados verticalmente
    if all(p[0] == points[0][0] for p in points):
        return True, abs(points[0][0]) <= PLANET_RADIUS

    # Calcula la pendiente y ordenada de la recta de regresion lineal en el eje y
    m, b = np.polyfit([p[0] for p in points], [p[1] for p in points], 1)
    alig = all(line_intersects_circle(m, b, p, PLANET_RADIUS) for p in points)

    if not alig:
        # Calcula la pendiente y ordenada de la recta de regresion lineal en el eje x
        m, b = np.polyfit([p[1] for p in points], [p[0] for p in points], 1)
        alig = all(line_intersects_circle(m, b, (y, x), PLANET_RADIUS) for x, y in points)

    # Chequea si el sol (0, 0) esta cerca de la recta
    sun_alig = alig and line_intersects_circle(m, b, (0, 0), PLANET_RADIUS)
    return alig, sun_alig


def get_line(point1, point2):
    '''Calcula la pendiente y ordenada de la recta formado por dos puntos'''
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point1[1] - m * point1[0]
    return m, b


def line_intersects_circle(m, b, point, r):
    '''Retorna True si el circulo con centro point y radio r interseca la linea de pendiente m y ordenada b
    https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    '''
    return abs(b + m * point[0] - point[1]) / math.sqrt(1 + m ** 2) <= r


def triangle_area(points):
    '''Calcula el area del triangulo formado por tres puntos'''
    x1, x2, x3 = points[0][0], points[1][0], points[2][0]
    y1, y2, y3 = points[0][1], points[1][1], points[2][1]
    return abs(0.5 * (((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))))


def point_inside_triangle(points, p):
    '''Calcula si el punto p esta dentro del triangulo formado por los puntos'''
    area_triangle = triangle_area(points)
    area_abp = triangle_area([points[0], points[1], p])
    area_acp = triangle_area([points[0], points[2], p])
    area_bcp = triangle_area([points[1], points[2], p])
    return math.isclose(area_triangle, area_abp + area_acp + area_bcp)

from model.Planet import Planet
import utils.Utils as utils


class Galaxy:

    STATUS_QUIET = 'Normal'
    STATUS_DROUGHT = 'Sequia'
    STATUS_RAINY = 'Lluvia'
    STATUS_OPTIMAL = 'Optimo'

    def __init__(self):
        self.planets = []
        self.planets.append(Planet('Ferengi', 1, 500, Planet.CLOCKWISE))
        self.planets.append(Planet('Vulcano', 5, 1000, Planet.ANTICLOCKWISE))
        self.planets.append(Planet('Betasoide', 3, 2000, Planet.CLOCKWISE))
        self.current_day = 1
        self.check_status()

    def planet_positions(self):
        '''Retorna la lista de posiciones (x, y) de los planetas'''
        return [planet.position for planet in self.planets]

    def advance(self, day):
        '''Actualiza la posicion de los planetas y el estado de la galaxia sumando dias al actual'''
        [planet.move(day) for planet in self.planets]
        self.current_day += day
        self.check_status()

    def check_status(self):
        '''Calcula el estado actual de la galaxia en base a la posicion de los planetas'''
        positions = self.planet_positions()
        self.area = utils.triangle_area(positions)

        aligned, sun_aligned = utils.aligned(positions)
        if sun_aligned:
            self.status = Galaxy.STATUS_DROUGHT
        elif aligned:
            self.status = Galaxy.STATUS_OPTIMAL
        elif utils.point_inside_triangle(positions, (0, 0)):
            self.status = Galaxy.STATUS_RAINY
        else:
            self.status = Galaxy.STATUS_QUIET

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
        self.check_status()

    def planet_positions(self):
        return [planet.position for planet in self.planets]

    def advance(self, day):
        positions = [planet.move(day) for planet in self.planets]
        self.check_status()

    def check_status(self):
        positions = self.planet_positions()
        if utils.aligned(positions):
            self.status = Galaxy.STATUS_OPTIMAL
        elif utils.point_inside_triangle(positions, (0, 0)):
            self.status = Galaxy.STATUS_RAINY
        else:
            self.status = Galaxy.STATUS_QUIET

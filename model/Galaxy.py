from model.Planet import Planet

class Galaxy:

    def __init__(self):
        self.planets = []
        self.planets.append(Planet('Ferengi', 1, 500, Planet.CLOCKWISE))
        self.planets.append(Planet('Vulcano', 5, 1000, Planet.ANTICLOCKWISE))
        self.planets.append(Planet('Betasoide', 3, 2000, Planet.CLOCKWISE))

    def status(self, day):
        [planet.move(day) for planet in self.planets]

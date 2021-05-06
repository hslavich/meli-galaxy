import math


class Planet:

    CLOCKWISE = -1
    ANTICLOCKWISE = 1

    def __init__(self, name, speed, distance, direction=CLOCKWISE):
        self.name = name
        self.speed = speed
        self.distance = distance
        self.direction = direction
        self.angle = 90
        self.update_position()

    def move(self, days):
        self.angle = self.angle + (self.speed * days * self.direction)
        return self.update_position()

    def update_position(self):
        x = round(math.cos(math.radians(self.angle)) * self.distance, 2)
        y = round(math.sin(math.radians(self.angle)) * self.distance, 2)
        self.position = (x, y)
        return self.position

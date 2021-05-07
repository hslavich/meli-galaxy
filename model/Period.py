class Period:
    def __init__(self, start_day, status, area):
        self.start_day = start_day
        self.status = status
        self.end_day = None
        self.max_area = (start_day, area)

    def register_area(self, day, area):
        if area > self.max_area[1]:
            self.max_area = (day, area)

    def __repr__(self):
        return "[%s - (%s -> %s)]" % (self.status, self.start_day, self.end_day or '--')

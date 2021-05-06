class Period:
    def __init__(self, start_day, status):
        self.start_day = start_day
        self.status = status
        self.end_day = None
        self.max_area = None

    def __repr__(self):
        return "[%s - (%s -> %s)]" % (self.status, self.start_day, self.end_day or '--')

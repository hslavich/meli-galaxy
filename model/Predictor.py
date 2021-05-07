from model.Galaxy import Galaxy
from model.Period import Period


class Predictor:
    def __init__(self):
        self.galaxy = Galaxy()
        self.periods = [Period(self.galaxy.current_day, self.galaxy.status, self.galaxy.area)]

    def run(self, days):
        for _ in range(1, days):
            self.galaxy.advance(1)
            last_period = self.periods[-1]
            if last_period.status != self.galaxy.status:
                last_period.end_day = self.galaxy.current_day - 1
                new_period = Period(self.galaxy.current_day, self.galaxy.status, self.galaxy.area)
                self.periods.append(new_period)
            else:
                last_period.register_area(self.galaxy.current_day, self.galaxy.area)
        self.periods[-1].end_day = self.galaxy.current_day

    def get_data(self, days):
        data = {self.galaxy.current_day: {'dia': self.galaxy.current_day, 'clima': self.galaxy.status}}
        for _ in range(1, days):
            self.galaxy.advance(1)
            data[self.galaxy.current_day] = {'dia': self.galaxy.current_day, 'clima': self.galaxy.status}
        return data

    def filter_periods(self, status):
        return list(filter(lambda p: p.status == status, self.periods))

    def drought_periods(self):
        return self.filter_periods(Galaxy.STATUS_DROUGHT)

    def rainy_periods(self):
        return self.filter_periods(Galaxy.STATUS_RAINY)

    def optimal_periods(self):
        return self.filter_periods(Galaxy.STATUS_OPTIMAL)

    def max_rainy_day(self):
        return max(self.filter_periods(Galaxy.STATUS_RAINY), key=lambda p: p.max_area[1])

from model.Galaxy import Galaxy
from model.Period import Period


class Predictor:
    def __init__(self):
        self.galaxy = Galaxy()
        self.periods = [Period(self.galaxy.current_day, self.galaxy.status, self.galaxy.area)]

    def run(self, days):
        '''Simula el movimiento de la galaxia dia por dia dentro del lapso de tiempo y calcula los periodos formados'''
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
        '''Retorna la lista de estados dia por dia dentro de un lapso de tiempo (days)'''
        data = {self.galaxy.current_day: {'dia': self.galaxy.current_day, 'clima': self.galaxy.status}}
        for _ in range(1, days):
            self.galaxy.advance(1)
            data[self.galaxy.current_day] = {'dia': self.galaxy.current_day, 'clima': self.galaxy.status}
        return data

    def filter_periods(self, status):
        '''Retorna la lista de periodos que tienen el estado recibido como parametro'''
        return list(filter(lambda p: p.status == status, self.periods))

    def drought_periods(self):
        '''Retorna la lista de periodos de sequia'''
        return self.filter_periods(Galaxy.STATUS_DROUGHT)

    def rainy_periods(self):
        '''Retorna la lista de periodos de lluvia'''
        return self.filter_periods(Galaxy.STATUS_RAINY)

    def optimal_periods(self):
        '''Retorna la lista de periodos de temperatura optima'''
        return self.filter_periods(Galaxy.STATUS_OPTIMAL)

    def max_rainy_day(self):
        '''Retorna la tupla (dia, area) con el area maxima de todos los periodos de lluvia'''
        return max(self.filter_periods(Galaxy.STATUS_RAINY), key=lambda p: p.max_area[1])

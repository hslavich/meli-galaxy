from model.Galaxy import Galaxy
from model.Period import Period

galaxy = Galaxy()
periods = [Period(galaxy.current_day, galaxy.status)]

for _ in range(1, 3651):
    galaxy.advance(1)
    last_period = periods[-1]
    if last_period.status != galaxy.status:
        last_period.end_day = galaxy.current_day - 1
        new_period = Period(galaxy.current_day, galaxy.status)
        periods.append(new_period)

periods[-1].end_day = galaxy.current_day

print(periods)

print(sum(1 for p in periods if p.status == Galaxy.STATUS_DROUGHT))
print(sum(1 for p in periods if p.status == Galaxy.STATUS_RAINY))
print(sum(1 for p in periods if p.status == Galaxy.STATUS_OPTIMAL))

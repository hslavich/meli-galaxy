import sys
import json
from model.Predictor import Predictor


if __name__ == '__main__':
    predictor = Predictor()
    if len(sys.argv) > 1 and sys.argv[1] == 'generar-data':
        data = predictor.get_data(3650)
        with open('data.json', 'w') as fp:
            json.dump(data, fp)
    else:
        predictor.run(3650)
        print('Total períodos de sequía: %d' % len(predictor.drought_periods()))
        print('Total períodos de lluvia: %d' % len(predictor.rainy_periods()))
        print('Total períodos de condiciones óptimas: %d' % len(predictor.optimal_periods()))
        print(predictor.max_rainy_day().max_area[0])

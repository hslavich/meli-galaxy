from model.Predictor import Predictor


if __name__ == '__main__':
    predictor = Predictor()
    predictor.run(3650)
    print('Total períodos de sequía: %d' % len(predictor.drought_periods()))
    print('Total períodos de lluvia: %d' % len(predictor.rainy_periods()))
    print('Total períodos de condiciones óptimas: %d' % len(predictor.optimal_periods()))
    print(predictor.max_rainy_day().max_area[0])

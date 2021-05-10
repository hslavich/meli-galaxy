# meli-galaxy

![example workflow](https://github.com/hslavich/meli-galaxy/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/hslavich/meli-galaxy/branch/master/graph/badge.svg?token=RRGM0G64KR)](https://codecov.io/gh/hslavich/meli-galaxy)

Deploy en Google App Engine: https://meli-examen.rj.r.appspot.com/

## Instalación

- Buildear imagen docker
```
docker build -t meli-galaxy .
```
- Ejecutar script `main.py` que devuelve los resultados
```
docker run meli-galaxy python main.py
```
```
Total períodos de sequía: 41
Total períodos de lluvia: 81
Día pico máximo de lluvia: 79
Total períodos de condiciones óptimas: 122
```
- Ejecutar api
```
docker run -it -p 8080:8080 meli-galaxy python api.py
```

### Modo gráfico
Requiere python3 (probado con 3.8)
```
pip3 install -r requirements.txt
python3 gui.py
```

## Solución

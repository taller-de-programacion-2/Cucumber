# Ejemplo de uso de Cucumber con Flask

## Requisitos
Para poder utilizarlo es necesario tener instalado:
- Docker

## Ejecutar 
Para correr los test ejecutar el comando ```make test```.

## Liberias Relevantes Utilizadas

### behave
Behave es la implementacion de cucumber para python.

### requests_mock
Esta lib nos permite mockear request.

### coverage
Nos permite generar un reporte de coverage de los test ejecutados.

## Ejemplos

* [Setup Cucumber](https://github.com/taller-de-programacion-2/Cucumber/blob/Python/features/environment.py)
* [Api call (sin levantar el servicio)](https://github.com/taller-de-programacion-2/Cucumber/blob/Python/features/steps/ping.py#L17)
* [Mock request http](https://github.com/taller-de-programacion-2/Cucumber/blob/Python/features/steps/inscription.py#L15)
* [Reutilizacion de parte del step](https://github.com/taller-de-programacion-2/Cucumber/blob/Python/features/inscription.feature#L13)

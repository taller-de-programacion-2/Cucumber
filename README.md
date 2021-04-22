# Ejemplo de uso de Cucumber con Express

## Requisitos
Para poder utilizarlo es necesario tener instalado:
- Docker

## Ejecutar 
Para correr los test ejecutar el comando ```make test```.

## Liberias Relevantes Utilizadas

### cucumber
Behave es la implementacion de cucumber para js.

### fetch-mock
Esta lib nos permite mockear request.

### supertest
Esta lib nos permite poder usar la api desde los test sin tener que levantarla

## Ejemplos

* [Setup Cucumber](https://github.com/taller-de-programacion-2/Cucumber/blob/JavaScript/features/support/hooks.js)
* [Api call (sin levantar el servicio)](https://github.com/taller-de-programacion-2/Cucumber/blob/JavaScript/features/steps/ping.js#L7)
* [Mock request http](https://github.com/taller-de-programacion-2/Cucumber/blob/JavaScript/features/steps/inscription.js#L12)
* [Reutilizacion de parte del step](https://github.com/taller-de-programacion-2/Cucumber/blob/JavaScript/features/inscription.feature#L13)

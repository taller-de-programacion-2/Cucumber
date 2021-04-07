## Ejemplos de uso cucumber 

En la rama de cada respectivo lenguaje se encuentra un ejemplo de como usar la herramienta cucumber en cada uno. Se mencionan las libs mas relevantes que se utilizan y como ejecutar los tests.

Hay ejemplos de:

- Setup de hooks de cucumber(rollbacks, env vars, etc)
- Api calls desde los steps (sin necesidad de levantar la api)
- Mock de request http desde los steps
- Reutilizacion de parte de steps

## Motivacion

Cucumber es una herramienta para realizar "Feature Test", permite escribir tests en lenguaje natural que son automizables por esta razon es muy util dado que cualquiera puede leer estos tests sin tener conocimiento tecnico. En su buen uso permite la reutilizacion de codigo dado que los tests en lenguaje natural son parametrizables. Esta pensada para usarse con BDD. [(+)](https://cucumber.io/)

## Gherkin

Los test en cucumber estan escritores en Gherkin, algunas de las palabras claves que hay que conocer son la siguientes:

Sintaxis: 
```
Feature: Title of the Scenario
Given [Preconditions or Initial Context]
When [Event or Trigger]
Then [Expected output]
```
- **Feature:** Indica el nombre de la funcionalidad que vamos a probar. Debe ser un título claro y explícito.
- **Given:** Provee contexto para el escenario en que se va a ejecutar el test, tales como punto donde se ejecuta el test, o prerequisitos en los datos. Incluye los pasos necesarios para poner al sistema en el estado que se desea probar.
- **When:** Especifica el conjunto de acciones que lanzan el test. La interacción del usuario que acciona la funcionalidad que deseamos testear.
- **Then:** Especifica el resultado esperado en el test. Observamos los cambios en el sistema y vemos si son los deseados.

Ejemplo de Gherkin:
```
Feature: Buscar Fiuba en google
 
  Scenario: Search for Fiuba
    Given I have visited Google
    When I search for "Fiuba"
    Then I see "FIUBA | Facultad de Ingenieria - UBA"
```

### Lenguajes

* [Python](https://github.com/matfonseca/Cucumber/tree/Python)
* [JavaScript](https://github.com/matfonseca/Cucumber/tree/JavaScript)

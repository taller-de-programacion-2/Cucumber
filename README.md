## Ejemplos de uso cucumber 

En la rama de cada respectivo lenguaje se encuentra un ejemplo de cómo usar la herramienta cucumber en cada uno. Se mencionan las libs más relevantes que se utilizan y como ejecutar los tests.

Hay ejemplos de:

- Setup de hooks de cucumber(rollbacks, env vars, etc)
- Api calls desde los steps (sin necesidad de levantar la api)
- Mock de request http desde los steps
- Reutilización de parte de steps

## Motivación

Cucumber es una herramienta para realizar "Feature Test", permite escribir tests en lenguaje natural que son automatizables por esta razón es muy útil dado que cualquiera puede leer estos tests sin tener conocimiento técnico. En su buen uso permite la reutilizacion de codigo dado que los tests en lenguaje natural son parametrizables. Esta pensada para usarse con BDD. [(+)](https://cucumber.io/)

## Gherkin

Los test en cucumber estan escritores en Gherkin, algunas de las palabras claves que hay que conocer son la siguientes:

- **Feature:** Indica el nombre de la funcionalidad que vamos a probar. Debe ser un título claro y explícito.
- **Given:** Provee contexto para el escenario en que se va a ejecutar el test, tales como punto donde se ejecuta el test, o pre-requisitos en los datos. Incluye los pasos necesarios para poner al sistema en el estado que se desea probar.
- **When:** Especifica el conjunto de acciones que lanzan el test. La interacción del usuario que acciona la funcionalidad que deseamos testear.
- **Then:** Especifica el resultado esperado en el test. Observamos los cambios en el sistema y vemos si son los deseados.

Sintaxis: 
```
Feature: [high-level description of a software feature, and to group related scenarios]

 Scenario:[concrete example that illustrates a business rule]
  Given [Preconditions or Initial Context]
  When [Event or Trigger]
  Then [Expected output]
```

Ejemplo de Gherkin:
```
Feature: Google Homepage Search

 Scenario: User sees the header
   Given I’m on the homepage
   Then I see the header

 Scenario: User can search with “Google Search”
   Given I’m on the homepage
   When I type “random page” into the search field
   And I click the Google Search button
   Then I go to the random page search results

 Scenario: User can search with “I’m Feeling Lucky”
   Given I’m on the homepage
   When I type “random page” into the search field
   And I click the I’m Feeling Lucky button
   Then I go to a random page
```

### Lenguajes

* [Python](https://github.com/taller-de-programacion-2/Cucumber/Cucumber/tree/Python)
* [JavaScript](https://github.com/taller-de-programacion-2/Cucumber/tree/JavaScript)



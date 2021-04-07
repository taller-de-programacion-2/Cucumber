Feature: Inscripciones CRUD

  Scenario: Crear inscripcion
    Given que me quiero anotar a la materia Algoritmos y Programacion I
    When me inscribo indicando mi id de estudiante "88393" y el codigo de la materia "ALGO1"
    Then me indica que mi inscripcion fue exitosa

  Scenario: Pedir todas las inscripciones sin inscriptos
    Given que no hay alumnos inscriptos en ninguna materia
    When pido las inscripciones
    Then no me devuelve ninguna inscripcion

  #ejemplo de reutilizacion de la linea de when
  Scenario: Pedir todas las inscripciones con inscriptos
    Given hay 3 alumnos inscriptos en ninguna materia
    When pido las inscripciones
    Then me devuelve 3 inscripciones

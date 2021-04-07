Feature: Inscripciones CRUD

  Scenario: Crear inscripcion
    Given que me quiero anotar a la materia Algoritmos y Programacion I
    When me inscribo indicando mi id de estudiante "88393" y el codigo de la materia "ALGO1"
    Then me indica que mi inscripcion fue exitosa
 
 Scenario: Pedir todas las inscripciones sin inscriptos
    Given que no hay alumnos inscriptos en ninguna materia
    When pido las inscripciones
    Then no me devuelve ninguna inscripcion

 Scenario: Pedir todas las inscripciones con inscriptos
    Given hay 3 alumnos inscriptos en ninguna materia
    When pido las inscripciones
    Then me devuelve 3 inscripciones
  # Scenario: B1: Reserva basica
  #   Given que el usuario con id "12" quiere reservar la publicacion con id "9" y precio "100" con fecha de checkin "2021-1-01" y de checkout "2021-1-10"
  #   When el usuario aprieta en reservar
  #   Then se informa que se guarda correctamente la reserva

  # Scenario: B2: Reserva ya reservada
  #   Given que el usuario con id "12" quiere reservar la publicacion con id "9" y precio "100" con fecha de checkin "2021-1-01" y de checkout "2021-1-10"
  #   When el usuario aprieta en reservar y ya esta reservada
  #   Then se informa que la publicacion ya esta reservada

  # Scenario: B3: Obtener todas las reservas que relizo un usuario
  #   Given que el usuario con id "12" reservo la publicacion con id "9" y precio "100" y la publicacion con id "34" y precio "100"
  #   When el usuario aprieta para ver todas sus reservas
  #   Then se le muestra la reserva ya hecha

  # Scenario: B4: Obtener todas las reservas de un usuario que no hizo ninguna reserva
  #   Given que el usuario con id "12" no reservo nada
  #   When el usuario aprieta para ver todas sus reservas
  #   Then se le muestra que no tiene ninguna reserva hecha

  # Scenario: B5: Obtener todas las reservas de una publicación
  #   Given que la publicación existe con id '123' y tiene 2 reservas de usuarios
  #   When quiero obtener las reservas de esta
  #   Then se le muestra las reservas de los distintos usuario

  # Scenario: B6: Obtener si reserve en una publicación
  #   Given que el usuario con id "12" quiere reservar la publicacion con id "9" y precio "100" con fecha de checkin "2021-1-01" y de checkout "2021-1-10"
  #   When consulta si la reservo
  #   Then muestra que reservo en esa publicación

  # Scenario: B7: Obtener si reservaron en una publicación mia
  #   Given que el usuario con id "12" quiere reservar la publicacion con id "9" y precio "100" con fecha de checkin "2021-1-01" y de checkout "2021-1-10"
  #   When consulta si el usuario reservo en alguna publicación mia
  #   Then muestra que este reservo en una publicación

  # Scenario: B8: Obtener transacciones
  #   Given que existen 2 transacciones
  #   When pido las transacciones
  #   Then obtengo dos


  # Scenario: B8: Obtener bookings por dia ultimo mes
  #   Given hubo 2 reservas el mes pasado el dia 2
  #   And hubo 2 reservas este mes el dia 1
  #   And hubo 1 reservas este mes el dia 7
  #   And hubo 3 reservas este mes el dia 20
  #   When pido los bookings por dias del ultimo mes
  #   Then obtengo 2 reservar el dia "1", 1 reserva el dia "7" y 3 reservas el dia "20"
    
Feature: ping en la app

  Scenario: ping en la app
     Given la app esta encendida
      When si le pego al /ping
      Then recibo un mensaje "ok"
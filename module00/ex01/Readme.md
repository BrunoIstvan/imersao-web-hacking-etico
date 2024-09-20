## Módulo 00 / Exercício 01 - Explicação

A vulnerabilidade em questão é o CSRF (Cross-Site Request Forgery) do lado do servidor.

Esse tipo de vulnerabilidade pode ocorrer quando uma aplicação não possui mecanismo de autenticação nos processos transacionais, como por exemplo, transferência de fundos. Pode ocorrer também, mesmo quando há um mecanismo de autenticação na aplicação, mas não uma validação de que aquela transação é do usuário autenticado, ou seja, independente de quem esteja autenticado é possível executar transações manipulando dados de outros usuários, afetando o confiabilidade do sistema como um todo. 

Exemplos de danos às vítimas: 
* Realizar transações não desejadas pela vítima. Por exemplo, a vítima é induzida a acreditar que está em um ambiente online seguro, mas uma operação que ela realizar irá executar uma transferência de fundos para uma conta do atacante.
* Alterar configurações de conta, como email ou senha.
* Roubo de dados sensíveis.



## Módulo 01 / Exercício 00 - SSTI - Explicação

A vulnerabilidade em questão é conhecida como SSTI (Server-Side Template Injection) do lado do servidor. Essa vulnerabilidade às vezes é confundida com o XSS. Mas a principal diferença é que o SSTI tem o poder de executar comandos dentro do servidor remoto, enquanto o XSS executa script maliciosos no navegador das vítimas.

Essa vulnerabilidade ocorre quando existe alguma renderização dinâmica no navegador sem passar por algum tipo de sanitização dos dados de entrada.

Exemplos de danos causados pelo atacante utilizando o SSTI: 
* Acesso completo ao servidor
* Roubo de dados da companhia ou clientes
* Controle de todo o sistema
* Danos à reputação




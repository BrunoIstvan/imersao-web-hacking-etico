## Módulo 00 / Exercício 00 - Fix

A melhor maneira de assegurar que seus sites estejão livres de ataques do tipo XSS é realizar a validação de todos os dados de entrada dos usuários.

Exemplo:
    
* Removendo tags HTML. Assim os scripts acabam ficando desconfigurados;
* Sanitizar os dados de saída, evitando que possíveis scripts maliciosos armazenados anteriormente não sejam distribuídos para os usuários que acessam seu site.

## Dicas de sanitização

PHP:

* Utilizar a função **htmlentites()**


Python:

* Utilizar **html.escape()** e **html.isalnum()**

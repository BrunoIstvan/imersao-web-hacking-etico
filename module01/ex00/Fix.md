## Módulo 01 / Exercício 00 - SSTI - Fix

Para evitar vulnerabilidades SSTI, é essencial implementar práticas de codificação seguras:

* **Validação de entrada**: A entrada do usuário deve ser devidamente validada e higienizada antes de ser processada pelo mecanismo de modelo.

* **Codificação contextual**: Aplicando codificação contextual à entrada do usuário para evitar ataques de injeção. Por exemplo, a entrada do usuário deve ser criptografada antes de ser inserida em contextos HTML, JavaScript ou SQL.

* **Princípio do Menor Privilégio**: Aplique o princípio do privilégio mínimo para minimizar o impacto de vulnerabilidades potenciais. Deve-se garantir que os mecanismos de modelo e os aplicativos da web sejam executados com as permissões mínimas exigidas.

## Dicas de sanitização

PHP:

* Utilizar a função **htmlentites()**


Python:

* Utilizar **html.escape()** e **html.isalnum()**

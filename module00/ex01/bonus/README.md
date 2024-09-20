## Como executar o programa de teste?

Segue um exemplo de como realizar um teste desse tipo de vulnerabilidade:


### Parte 1:

Iniciar a aplicação disponível no exercício 01.

Abrir a página inicial no navegador.

    http://localhost:8080/

Verificar que o balance é 1000.


### Parte 2:

Instalar o virtualenv:

    pip install virtualenv

Na pasta raíz do projeto, executar o seguinte comando:

    python3 -m virtualenv .venv

Ativar o virtualenv da aplicação:

    source .venv/bin/activate 

Em seguida instalar as dependências do projeto:

    pip install -r requirements.txt

Executar a aplicação:

    python app.py


Abrir a página no navegador:

    http://127.0.0.1:5000/promotions


Imagine que o cliente receba um email que o induza aoa abrir para receber uma promoção, ao clicar em no botão "clique aqui para receber" a vulnerabilidade é executada.

Ao abrir novamente a página inicial do disponibilizado no exercício, será possível ver que o balance ficou zerado.

    http://localhost:8080/
    

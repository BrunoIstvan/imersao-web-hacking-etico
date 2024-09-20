from flask import Flask, request
from html import escape

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Vulnerabilidade XSS</h1>

        <div style="border-style: groove;">
            <form method="post" action="/xss">
                <h3>Aqui você irá submeter os dados de entrada para uma página vulnerável ao XSS</h3>
                <input type="text" name="input" value="<script>alert('XSS')</script>" />
                <input type="submit" value="Enviar" />
            </form>
        </div>

        <br />
        <br />
        <br />
        <br />
        <hr>
        <br />
        <br />
        <br />
        <br />


        <div style="border-style: groove;">
            <form method="post" action="/block-xss">
                <h3>Aqui você irá submeter os dados de entrada para uma página que trata dados de entrada e bloqueia ataque XSS</h3>
                <input type="text" name="input" value="<script>alert('XSS')</script>"/>
                <input type="submit" value="Enviar" />
            </form>
        </div>
    '''

@app.route('/xss', methods=['POST'])
def xss():
    user_input = request.form['input']
    return f'<h1>Você digitou: {user_input}</h1>'


@app.route('/block-xss', methods=['POST'])
def block_xss():
    user_input = escape(request.form['input'])
    return f'<h1>Você digitou: {user_input}</h1>'


if __name__ == '__main__':
    app.run(debug=True)

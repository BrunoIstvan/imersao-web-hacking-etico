from flask import Flask, request, render_template_string

from html import escape


app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Template Injection App</title>
    </head>
    <body>
        <h1>Template Injection App</h1>
        <form method="POST" action="/render">
            <label for="input">Enter your input:</label>
            <input type="text" id="input" name="input">
            <button type="submit">Render</button>
        </form>
        <div id="result">{{ result }}</div>

        <hr/>

        <h1>Template Injection App Tratado</h1>
        <form method="POST" action="/render-fixed">
            <label for="input">Enter your input:</label>
            <input type="text" id="input" name="input">
            <button type="submit">Render</button>
        </form>
        <div id="result">{{ result_fixed }}</div>


    </body>
    </html>
    '''

@app.route('/render', methods=['POST'])
def render():
    user_input = request.form.get('input')
    template = f'Hello, {{ {user_input} }}!'
    try:
        result = render_template_string(template)
    except Exception as e:
        result = str(e)
    
    return render_template_string(index(), result=result)

@app.route('/render-fixed', methods=['POST'])
def render_fixed():
    user_input = sanitize()
    template = f'Hello, {{ {user_input} }}!'
    try:
        result = render_template_string(template)
    except Exception as e:
        result = str(e)
    
    return render_template_string(index(), result_fixed=result)


def sanitize():
    user_input = escape(request.form.get('input'))
    if '{{' in user_input:
        user_input = user_input.replace('{{', '')
    if '}}' in user_input:
        user_input = user_input.replace('}}', '')
    return user_input

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010)

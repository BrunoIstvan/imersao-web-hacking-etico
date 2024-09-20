from flask import Flask, request, render_template_string

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
    </body>
    </html>
    '''

@app.route('/render', methods=['POST'])
def render():
    user_input = request.form.get('input')
    template = f'Hello, {{ {user_input} }}!'
    try:
        print(template)
        result = render_template_string(template)
        print(result)
    except Exception as e:
        result = str(e)
    
    data = render_template_string(index(), result=result)
    print(data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

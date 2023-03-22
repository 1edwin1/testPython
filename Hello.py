from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/hello">
            <input type="text" name="name">
            <input type="submit" value="Say Hello">
        </form>
    '''

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()

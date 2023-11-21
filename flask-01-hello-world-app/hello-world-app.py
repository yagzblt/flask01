from flask import Flask 
app = Flask(__name__)

@app.route('/')
def head():
    return "hello word"

@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page and I have written it!'

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)
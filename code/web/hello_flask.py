from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask!</h1>'

@app.route('/user/<fname>/<lname>')
def user(fname, lname):
    return '<h1>Hello, %s, %s!</h1>' % (lname, fname)

@app.route('/mybrowser')
def my_browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)

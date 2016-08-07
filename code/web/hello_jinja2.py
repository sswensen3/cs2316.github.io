from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/user')
@app.route('/user/<username>')
def user(username=None):
    return render_template('user.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)

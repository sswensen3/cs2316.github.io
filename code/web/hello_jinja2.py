from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user1.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)

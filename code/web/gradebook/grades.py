from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grades/<course>/<term>')
def gradebook(course, term):
    file_name = course + term + '.csv'
    rows = []
    with open(file_name, 'r') as fin:
        reader = csv.reader(fin)
        for record in reader:
            rows.append(record)
    return render_template('grades.html', course=course, term=term, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

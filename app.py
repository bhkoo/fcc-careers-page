from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Saint Louis, MO',
    'salary' : '100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Dallas, TX',
    'salary' : '150,000'
  },
  {
    'id': 3,
    'title': 'Front-end Engineer',
    'location': 'Houston, TX'
  },
  {
    'id': 4,
    'title': 'Back-end Engineer',
    'location': 'Austin, TX',
    'salary' : '110,000'
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'Cloud 9')

@app.route('api/jobs')
def list_jobs():
  return jsonify(JOBS);

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

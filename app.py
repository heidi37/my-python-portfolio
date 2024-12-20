from flask import Flask, render_template
from projects import projects

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', projects=projects)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/projects')
def show_projects():
  return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug = True, port = 3000, host='localhost')

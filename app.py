from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Overview')

@app.route('/expressions')
def expressions():
    return render_template('expressions.html', title='Expressions')

@app.route('/reference')
def reference():
    return render_template('reference.html', title='Reference')

@app.route('/locationpaths')
def location_paths():
    return render_template('location_paths.html', title='Location Paths')

@app.route('/axes')
def axes():
    return render_template('axes.html', title='Axes')




if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()

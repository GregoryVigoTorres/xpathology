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

@app.route('/locationpathreference')
def location_path_reference():
    return render_template('location_path_reference.html', title='Location Path Reference')

@app.route('/axes')
def axes():
    return render_template('axes.html', title='Axes')


@app.route('/nodetests')
def node_tests():
    return render_template('node_tests.html', title='Node Tests')


@app.route('/predicates')
def predicates():
    return render_template('predicates.html', title='Predicates')


@app.route('/functioncalls')
def function_calls():
    return render_template('function_calls.html', title='Function Calls')


@app.route('/functionreference')
def function_reference():
    return render_template('function_reference.html', title='Function Reference')



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()

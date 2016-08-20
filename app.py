from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expressions')
def expressions():
    return render_template('expressions.html')

@app.route('/reference')
def reference():
    return render_template('reference.html')

@app.route('/locationpaths')
def location_paths():
    return render_template('location_paths.html')



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()

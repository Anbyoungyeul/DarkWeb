from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/light_Sidenav')
def light_Sidenav():
    return render_template('layout-sidenav-light.html')

@app.route('/static_Navigation')
def static_Navigation():
    return render_template('layout-static.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
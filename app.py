from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/status")
def status():
    return render_template ("status.html")

@app.route("/paysetup")
def paysetup():
    return render_template ("paysetup.html")

@app.route("/switchsettings")
def switchsettings():
    return render_template ("switchsettings.html")

@app.route("/usersettings")
def usersettings():
    return render_template ("usersettings.html")

@app.route("/signup")
def signup():
    return render_template ("signup.html")

@app.route("/signin")
def signin():
    return render_template ("signin.html")

@app.route("/fbsignin")
def fbsignin():
    return render_template ("fbsignin.html")

@app.route("/googlesignin")
def googlesignin():
    return render_template ("googlesingin.html")

@app.route("/pairswitch")
def pairswitch():
    return render_template ("pairswitch.html")

@app.route("/firstlogin")
def firstlogin():
    return render_template ("firstlogin.html")

@app.route("/alertscreen")
def alertscreen():
    return render_template ("alertscreen.html")

@app.route("/confirmbuy")
def confirmbuy():
    return render_template ("confirmbuy.html")

@app.route("/confirmsell")
def confirmsell():
    return render_template ("confirmsell.html")

@app.route("/buyingstatus")
def buyingstatus():
    return render_template ("buyingstatus.html")

@app.route("/sellingstatus")
def sellingstatus():
    return render_template ("sellingstatus.html")
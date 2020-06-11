from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/signup")
def about():
    return render_template ("signup.html")

@app.route("/signin")
def about():
    return render_template ("signin.html")

@app.route("/fbsignin")
def about():
    return render_template ("fbsignin.html")

@app.route("/googlesignin")
def about():
    return render_template ("googlesingin.html")

@app.route("/UserHomeInfo")
def about():
    return render_template ("UserHomeInfo.html")

@app.route("/paysetup")
def about():
    return render_template ("paysetup.html")

@app.route("/pair-switch")
def about():
    return render_template ("pair-switch.html")

@app.route("/switchsettings")
def about():
    return render_template ("switchsettings.html")

@app.route("/mainstatus")
def about():
    return render_template ("mainstatus.html")

@app.route("/alertscreen")
def about():
    return render_template ("alertscreen.html")

@app.route("/confirmbuy")
def about():
    return render_template ("confirmbuy.html")

@app.route("/confirmsell")
def about():
    return render_template ("confirmsell.html")

@app.route("/buyingstatus")
def about():
    return render_template ("buyingstatus.html")

@app.route("/sellingstatus")
def about():
    return render_template ("sellingstatus.html")
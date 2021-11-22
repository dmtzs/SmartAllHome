try:
    from app import app
    from flask import render_template
    from datetime import datetime as dt
except ImportError as eImp:
    print(f"The following import ERROR occurred in file {__file__}: {eImp}")

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.now()
    }

# -------------Endpoints-------------
@app.route("/")# Welcome HTML template
def index():
    return render_template("welcome.html", pageTitle= "Home")

# @Description: Endpoint that is used for show contact information with us.
@app.route("/aboutus")
def contacto():
    global correoGDCode, nomApp, versionApp, descripcionApp

    return render_template('aboutus.html', correo=correoGDCode, nombreApp=nomApp, versionDeApp=versionApp, decApp=descripcionApp)
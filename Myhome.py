# Myhome.py
from flask import Flask, flash, render_template, request, url_for, redirect, abort
import os


app = Flask(__name__) 


# it does not need to be specified that the method is GET because it is the default method
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/espanol/")
def espanol():
    return render_template("espanol.html")

@app.route("/herramientas/")
def herramientas():
    return render_template("herramientas.html")

@app.route("/cs/")
def cs():
    return render_template("cs.html")

@app.route("/frases/")
def frases():
    return render_template("frases.html")


@app.route("/iremi/")
def iremi():
    return render_template("iremi.html")

@app.route("/mod1/")
def mod1():
    return render_template("mod1.html")

@app.route("/mod2/")
def mod2():
    return render_template("mod2.html")

if __name__ == "__main__":
    #app.run(debug=True)
    #for ducker the next line is used
    #app.run(host="0.0.0.0", port=5000, debug=True)
    # for runing the app in production, use a WSGI server like Gunicorn or uWSGI instead of the built-in Flask server.  
    #app.run()

    # Modifications for running in Railway
    #port = int(os.environ.get("PORT",5000))
    #app.run(host="0.0.0.0", port=port, debug=False)

    # Modifications for running in Railway
    # NEXT LINES ALLOWS TO RUN THE APP IN PRODUCTION MODE WHEN DEPLOYED IN RAILWAY
    # IN LAPTOP THE VALUE OF FLASK_ENV IS NOT SET, SO IT WILL RUN IN DEBUG MODE ALWAYS
    # CHECK IT WITH echo $FLASK_ENV y va a salir vacio
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug_mode)



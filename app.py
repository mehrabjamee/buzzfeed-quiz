# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=["GET", "POST"])
def results():
    print(request.form)
    props = model.get_results(request.form)
    return render_template("results.html", props=props)

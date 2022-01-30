"""
Run Editor server by using Flask
"""

import json
import copy
#from npito import open_folder
from flask import Flask, render_template, redirect, request, jsonify
from appdb import app, db
from dbctrl import DBCtrl
from models import User, Spec

dbc = DBCtrl(db)
MODELNAME = {"User": User, "Spec": Spec}

@app.route('/')
def route():
    #return redirect("index")
    return "<h1>hello</h1>"

@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2777, debug=True)


##################################################################################################################
###                                                                                                            ###
###                               import the nessecary libraries                                               ###
##################################################################################################################
from flask import (
    Flask,
    request,
    abort,
    session, 
    render_template
)
import json
import os
from os import listdir
from os.path import isfile, join
import datetime
from flask_googletrans import translator

STATIC_DIR = os.path.abspath('./static')
TEMPLATE_DIR = os.path.abspath('./views')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
ts = translator(app)
@app.route('/postXML', methods=['POST','GET'])
def postXML():
    my_json =[{
            'x': -2,
            'y': -2
        }, {
            'x': -1,
            'y': -1
        }, {
            'x': 1,
            'y': 1
        }, {
            'x': 2,
            'y': 2
        }]
    return json.dumps(my_json) #sending my dummy data

# Route the user to the homepage
@app.route('/')
def home():
    id=request.values.get("id")
    return render_template("index.html", id=id)

@app.route('/3d-plot')
def threeD():
    id=request.values.get("id")
    return render_template("3d.html", id=id)

@app.route('/faq')
def faq():
    id=request.values.get("id")
    return render_template("faq.html", id=id)

@app.route('/function-derivatives')
def function_derivatives():
    id=request.values.get("id")
    return render_template("function-derivatives.html", id=id)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)

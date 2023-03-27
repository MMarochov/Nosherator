from flask import Flask, request, render_template
import string
import random

app = Flask(__name__)

@app.route("/")
def name():
    return render_template('name.html')

@app.route('/', methods=['POST'])
def name_post():
    input_name = request.form['text']
    name_lower = input_name.lower()
    processed_name = f" ".join([x[1:] for x in name_lower.split(" ")])
    return processed_name

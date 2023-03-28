from flask import Flask, request, render_template
import string
import random
import re

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def name_prefixed():
    input_name = request.form['text']
    name_lower = input_name.lower()
    # replaces multiple spaces with single space for splitting on
    name_lower = re.sub(' +', ' ', name_lower)
    name_split = name_lower.split(" ")
    # remove any empty strings in list
    name_split = list(filter(None, name_split))
    vowels = ('a', 'e', 'i', 'o', 'u')
    prefixes = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Qu', 'R', 'S', 'T', 'V',
                'W', 'X', 'Y', 'Z', 'Sh', 'Fl', 'Ch', 'Th', 'Pl', 'Tw', 'Sl', 'Cl', 'Dw', 'Shr', 'Bl', 'Sm')
    prefix = random.choice(prefixes)
    name_list = []
    prefixed_name = " "

    for name in name_split:
        if name.startswith(vowels):
            name = f'{prefix}{name}'
            name_list.append(name)
        else:
            name = name.replace(name[0], prefix)
            name_list.append(name)
    prefixed_name = prefixed_name.join(name_list)
    return prefixed_name

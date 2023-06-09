# app.py

# Imports
from flask import Flask, request, render_template
import random
import re

app = Flask(__name__)
# app.run(debug=True)

phrases = (
    "The name's Shrond, Shrames Shrond.", 
    " ♫ ♩ ♬ *autotune* D𝓌ₐsₒₙ D𝓌ₑᵣᵤlₒoₒ",
    "A wizard is never late, Throdo Thraggins. Nor is he early. He arrives precisely when he means to. - Thrandalf, The Thord of the Things",
    "You're a wizard, Slarry! - Slagrid",
    "That'll do Plonkey, that'll do. - Plhrek",
    "(Smakira, Smakira) Oh baby, when you talk like that, you make a woman go mad. - Smakira",
    "You know nothing, Flon Flow. - Fgritte, Flame of Flones",
    "It's Twitney, b*tch. - Twitney Twears/Twichael Twcott",
    "Quolene, Quolene, Quolene, Quoleₑₑₑene, I'm begging of you please don't take my man. - Quolly Quarton",
    "Run, Zorrest, run! - Zenny, Zorrest Zump",
    "Blobby has no master. Blobby is a free elf, and Blobby has come to save Blarry Blotter and his friends! - Blobby",
    "Hello. My name is Frinigo Frontoya. You killed my father. Prepare to die. - Frinigo Frontoya, Frhe Frincess Fride",
    "I have a vewy gweat fwiend in Wome called 'Twiggus Twickus'. - Twilate, Twonty Twython's Twife of Twrian"
    )
vowels = ('a', 'e', 'i', 'o', 'u')
prefixes = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Qu', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'Sh', 'Fl', 'Ch', 'Th', 'Pl', 'Tw', 'Sl', 'Cl', 'Dw', 'Shr', 'Bl', 'Sm', 'Shw', 'Fr', 'Gr', 'Sch', 'Shl', 'Moo')

@app.route("/")
def index():
    global random_phrase  # this feels bad but I don't know how to make it better
    random_phrase = random.choice(phrases)
    return render_template('index.html', random_phrase=random_phrase)


@app.route('/', methods=['POST'])
def name_prefixed():
    input_name = request.form['text']
    name_lower = input_name.lower()
    # replaces multiple spaces with single space for splitting on
    name_lower = re.sub(' +', ' ', name_lower)
    name_split = name_lower.split(" ")
    # remove any empty strings in list
    name_split = list(filter(None, name_split))
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

    return render_template('index.html', prefixed_name=prefixed_name, random_phrase=random_phrase)

if __name__ == '__main__':
    app.run()
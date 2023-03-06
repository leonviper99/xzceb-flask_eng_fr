from machinetranslation.translator import *
from flask import Flask, render_template, request
import json
import machinetranslation


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    x = english_to_french(textToTranslate)
    return x

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    x = french_to_english(textToTranslate)
    return x

@app.route("/")
def renderIndexPage():
    return render_template('index.html', client_token="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")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

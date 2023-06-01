from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_To_French")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    en_to_fr=translator.english_to_french(textToTranslate)
    return en_to_fr
    # Write your code here
    #return "Translated text to French"

@app.route("/french_To_English")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    fr_to_en=translator.french_to_english(textToTranslate)
    return fr_to_en
    # Write your code here
    #return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

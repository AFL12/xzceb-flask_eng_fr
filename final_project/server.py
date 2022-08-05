from machinetranslation import translator
from flask import Flask, render_template, request
import json

#app = Flask("Web Translator")
app=Flask(__name__,template_folder='templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.english_to_french(textToTranslate)
    traducedtext = translated["translations"][0]["translation"]

    return traducedtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.french_to_english(textToTranslate)
    traducedtext = translated["translations"][0]["translation"]
    
    return traducedtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")
    

if __name__ == "__main__":
  
    #app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)

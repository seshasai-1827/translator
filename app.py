from flask import Flask, render_template, request, jsonify
from language_translator import Translate, record

app = Flask(__name__)

detected_text = ""

@app.route('/rec', methods=['GET'])
def rec():
    global detected_text
    detected_text = record()
    return jsonify({'detected_text': detected_text})

@app.route('/', methods=['POST', 'GET'])
def home():
    global detected_text
    translated_text = ""
    if request.method == 'POST':
        lang = request.form.get("language")
        translated_text = Translate(lang,detected_text)
    return render_template('index.html', detected_text=detected_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# настройка API Meta AI
genai.configure(api_key='34948ecd9c39437982bb6356b77515af')

# модель для генерации текста
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    # получение текста из запроса
    text = request.json['text']

    # генерация текста с помощью модели
    chat = model.start_chat(history=[])
    response = chat.send_message(text)

    # возвращение результата
    return jsonify({'text': response.text})

if __name__ == '__main__':
    app.run(debug=True)
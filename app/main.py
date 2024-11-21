from flask import Flask, render_template, request, jsonify
from .chatbot import GeminiBot

app = Flask(__name__)
chatbot = GeminiBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.generate_response(user_message)
    return jsonify({'response': response})

@app.route('/reset', methods=['POST'])
def reset():
    response = chatbot.reset_conversation()
    return jsonify({'status': response})
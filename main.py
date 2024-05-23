from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the generative AI model
os.environ['GOOGLE_API_KEY'] = "AIzaSyDUREkLbFjpAx9fys3l-TUPhciCqAoB2RQ"  # Ensure this key is set securely
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('chatbot.html')


@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    print(data)
    question = data['question']
    print(question)
    response = model.generate_content(question)
    answer = response.text
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

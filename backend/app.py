import os
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
from flask_cors import CORS
from openai import OpenAI
import requests

app = Flask(__name__)
CORS(app)

api_key = os.environ.get("OPENAI_API_KEY")

docai_api_key = "hack-with-upstage-docai-0407"
solar_api_key = "hack-with-upstage-solar-0407"

client = OpenAI(
    api_key=solar_api_key,
    base_url="https://api.upstage.ai/v1/solar"
)

def analyze_layout(filename):
    url = "https://api.upstage.ai/v1/document-ai/layout-analyzer"
    headers = {"Authorization": f"Bearer {docai_api_key}"}
    files = {"document": open(filename, "rb")}
    response = requests.post(url, headers=headers, files=files)
    return response.json()["html"]

def ask_solar(context, question):
    response = client.chat.completions.create(
        model="solar-1-mini-chat",
        messages=[
          {
            "role": "user",
            "content": "Answer the following question:" + question
                + "by using the following context:" + context
          }
        ]
    )
    return response.choices[0].message.content

def check_groundedness(context, question, answer):
    response = client.chat.completions.create(
        model="solar-1-mini-answer-verification",
        messages=[
            {"role": "user", "content": context},
            {"role": "assistant", "content": question + answer}
        ]
    )
    return response.choices[0].message.content == "grounded"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.files['image']
        context = analyze_layout(user_input)
        question = "What is the income?"
        for _ in range(3):
            answer = ask_solar(context, question)
            grounded = check_groundedness(context, question, answer)
            if grounded:
                return jsonify(f'''"Here is the answer {answer}"''')
        return jsonify(f'''"Here is the answer {answer}"''')

@app.route('/chat', methods=['GET', 'POST'])
def rag():
    if request.method == 'POST':
        user_input = request.files['image']
        context = analyze_layout(user_input)
        question = "What is the income?"
        for _ in range(3):
            answer = ask_solar(context, question)
            grounded = check_groundedness(context, question, answer)
            if grounded:
                return jsonify(f'''"Here is the answer {answer}"''')
        return jsonify(f'''"Here is the answer {answer}"''')

@app.route('/prompt', methods=['GET', 'POST'])
def prompts():
    if request.method == 'POST':
        user_input = request.form.get('prompt',None)
        token = int(request.form.get('token', 500))
        openai.api_key = api_key
        try:
            response = openai.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="gpt-3.5-turbo",
            )

            bot_response = response.choices[0].message.content.strip()
            return jsonify(bot_response)
        except Exception as e:
            return jsonify({"error":str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))        

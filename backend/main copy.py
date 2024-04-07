import openai, os, io
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

api_key = os.environ.get("OPENAI_API_KEY")

def generate_response(prompt,token):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=token,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route('/')
def helookup():
    return jsonify("HOLA EVERYONE")

@app.route('/prompt', methods=['GET', 'POST'])
def prompts():
    if request.method == 'POST':
        img_file = request.files['image']
        prompt_raw = request.form.get('prompt',None)
        subdomain =  request.form.get('subfolder')
        filename = request.form.get('filename')
        id = request.form.get('id').lower()
        site = request.form.get('site')
        article = request.form.get('article_dir').replace("\\", "/")
        token = int(request.form.get('token', 500))

        # b_name = name+"_"+id
        prefix_path = f"{site}/input/content"

        if subdomain == "None" :
            destination_blob = os.path.join(prefix_path,filename).replace("\\", "/")
        else :
            destination_blob = os.path.join(prefix_path,subdomain,filename).replace("\\", "/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))        

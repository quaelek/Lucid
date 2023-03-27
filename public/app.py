import os
import openai
from flask import Flask, render_template, request, jsonify

openai.api_key = os.environ["OPENAI_API_KEY"]
app = Flask(__name__)

messages = [
    {"role": "assistant", "content": "Hello! I'm here to help you interpret your dreams in an esoteric fashion. Tell me about a dream you had."}
]

def get_chatbot_response(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages + [{"role": "user", "content": user_input}]
    )

    response = completion.choices[0].message["content"]
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        messages.append({"role": "user", "content": user_input})
        response = get_chatbot_response(user_input)
        messages.append({"role": "assistant", "content": response})
    return render_template("index.html", conversation=messages)

@app.route('/interpret', methods=['GET', 'POST'])
def interpret():
    user_input = request.form['user_input']
    messages.append({"role": "user", "content": user_input})
    response = get_chatbot_response(user_input)
    messages.append({"role": "assistant", "content": response})
    return jsonify({"content": response})

if __name__ == '__main__':
    app.run(debug=True)

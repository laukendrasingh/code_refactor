#IT'S NOT USING IN POC. ADDED ONLY FOR LEARNING.

from flask import Flask, jsonify, request
from config import *
from models import OpenAIModel, ChatGptModel

app = Flask(__name__)
openai_model = OpenAIModel()
gpt_model = ChatGptModel()


def __mask_string(input):
    return '*' * len(input)

configs = {
    "LOG_LEVEL": LOG_LEVEL,
    "OPEN_AI_KEY": __mask_string(OPEN_AI_KEY),
    "OPEN_AI_BASE_URL": OPEN_AI_BASE_URL,
    "OPEN_AI_MODEL": OPEN_AI_MODEL,
    "OPENAI_API_KEY": __mask_string(OPENAI_API_KEY),
    "CHAT_GPT_MODEL": CHAT_GPT_MODEL
}

@app.route("/configs", methods=['GET'])
def get_configs():
    return jsonify(configs)

@app.route("/refactor", methods=['POST'])
def refactor_code():
    log.info(f'Refactor code, request: {request.get_json()}')

    if request.is_json:
        data = request.get_json()
        file_name=data.get('fileName')
        code = data.get('code')
        refactored_code = gpt_model.refactor_code(file_name, code)
        return jsonify(refactored_code), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

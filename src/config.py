import os
from dotenv import load_dotenv
import logging as log

load_dotenv()

LOG_LEVEL = os.environ['LOG_LEVEL']

OPEN_AI_KEY = os.environ['OPEN_AI_KEY']
OPEN_AI_BASE_URL = os.environ['OPEN_AI_BASE_URL']
OPEN_AI_MODEL = os.environ['OPEN_AI_MODEL']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
CHAT_GPT_MODEL = os.environ['CHAT_GPT_MODEL']

log.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s : %(filename)s #%(lineno)d - %(message)s',
    handlers=[log.StreamHandler()])

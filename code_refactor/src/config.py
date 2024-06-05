import os
from dotenv import load_dotenv
import logging as log

load_dotenv()
load_dotenv('.env.'+os.environ['ENVIRONMENT'])

LOG_LEVEL = os.environ['LOG_LEVEL']
LOG_FILE_PATH = os.environ['LOG_FILE_PATH']

OPEN_AI_KEY = os.environ['OPEN_AI_KEY']
OPEN_AI_BASE_URL = os.environ['OPEN_AI_BASE_URL']
OPEN_AI_MODEL = os.environ['OPEN_AI_MODEL']

log.basicConfig(
    level=LOG_LEVEL,

    format='%(asctime)s - %(levelname)s : %(filename)s #%(lineno)d - %(message)s',
    handlers=[
        # log.FileHandler(LOG_FILE_PATH),
        log.StreamHandler()
    ]
)

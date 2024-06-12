from langchain.prompts import ChatPromptTemplate as Prompt
from langchain.prompts import SystemMessagePromptTemplate as System
from langchain.prompts import HumanMessagePromptTemplate as User
from langchain.chat_models import ChatOpenAI
import os
import logging as log
from abc import ABC, abstractmethod
from openai import OpenAI
from config import OPEN_AI_KEY, OPEN_AI_BASE_URL, OPEN_AI_MODEL, OPENAI_API_KEY, CHAT_GPT_MODEL
from langchain.chains import LLMChain

LANGUAGE_EXTENSIONS = {
    '.java': 'Java',
    '.js': 'JavaScript',
    '.py': 'Python'
}

ESTIMATED_COSTS_USD = {CHAT_GPT_MODEL: 0.00006, OPEN_AI_MODEL: 0.00001}


class Model(ABC):
    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def refactor_code(self, file_name: str, code: str):
        pass

    def get_language(self, file_name: str):
        file_extension = os.path.splitext(file_name)[1]
        return LANGUAGE_EXTENSIONS.get(file_extension, 'Unknown')

    def get_cost(self, model_name, prompt):
        tokens = tokens = len(prompt.split())

        if model_name in ESTIMATED_COSTS_USD:
            cost_per_token = ESTIMATED_COSTS_USD[model_name]
            estimated_cost_usd = cost_per_token * tokens
            return f"TOKENS: {tokens} & ESTIMATED COST: ${format(estimated_cost_usd, '.5f')}"
        else:
            raise ValueError(f"Model: {model_name} not found")

# ........................model: meta-llama/Llama-2-70b-chat-hf........................#


class OpenAIModel(Model):
    def __init__(self):
        self.__open_ai = OpenAI(api_key=OPEN_AI_KEY, base_url=OPEN_AI_BASE_URL)

    def get_model(self):
        return OPEN_AI_MODEL

    def refactor_code(self, file_name: str, code: str):
        log.info(
            f'Start: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}')
        try:
            messages = [
                {"role": "system", "content": "You are an expert software engineer."},
                {"role": "user",
                    "content": f"Refactor the following {self.get_language(file_name)} code to improve its readability, performance, and maintainability:\n\n"},
                {"role": "user",
                    "content": f"Original {self.get_language(file_name)} Code:\n{code}\n\n"},
                {"role": "system",
                    "content": f"Refactored {self.get_language(file_name)} Code:"}
            ]

            chat_stream = self.__open_ai.chat.completions.create(
                model=OPEN_AI_MODEL,
                max_tokens=1000,
                stream=True,
                messages=messages
            )

            log.info(
                f'End: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}')
            return chat_stream, self.get_cost(OPEN_AI_MODEL, messages.__str__())
        except Exception as ex:
            log.error(
                f'Error: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}', exc_info=ex)
            raise ValueError(
                f'Failed code refactoring for file: {file_name} using model: {OPEN_AI_MODEL} due to error: {ex}')

# ........................model: chat-gpt/text-davinci-003........................#


class ChatGptModel(Model):
    def __init__(self):
        OpenAI.api_key = OPENAI_API_KEY
        self.__chat_prompt_template = Prompt.from_messages([
            System.from_template(
                "You are an expert software engineer."),
            User.from_template(
                "Refactor the following {language} code to improve its readability, performance, and maintainability:\n\n"
                "Original {language} Code:\n{code}\n\n"
                "Refactored {language} Code:"
            )
        ])
        self.__llm_chain = LLMChain(
            prompt=self.__chat_prompt_template, llm=ChatOpenAI(model=CHAT_GPT_MODEL))

    def get_model(self):
        return CHAT_GPT_MODEL

    def refactor_code(self, file_name: str, code: str):
        log.info(
            f'Start: refactor code for file: {file_name} using model: {CHAT_GPT_MODEL}')
        try:
            prompt = self.__chat_prompt_template.format(
                **{"language": "Java", "code": code})
            refactored_code = self.__llm_chain.run(
                {"language": "Java", "code": code})

            return refactored_code, self.get_cost(OPEN_AI_MODEL, prompt)
        except Exception as ex:
            log.error(
                f'Error: refactor code for file: {file_name} using model: {CHAT_GPT_MODEL}', exc_info=ex)
            raise ValueError(
                f'Failed code refactoring for file: {file_name} using model: {CHAT_GPT_MODEL} due to error: {ex}')

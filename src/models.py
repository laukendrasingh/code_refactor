import os
import logging as log
from abc import ABC, abstractmethod
from openai import OpenAI
from config import OPEN_AI_KEY, OPEN_AI_BASE_URL, OPEN_AI_MODEL


LANGUAGE_EXTENSIONS = {
    '.java': 'Java',
    '.js': 'JavaScript',
    '.py': 'Python'
}

class Model(ABC):
    @abstractmethod
    def refactor_code(self, file_name: str, code: str):
        pass

    def get_language(self, file_name: str):
        file_extension = os.path.splitext(file_name)[1]
        return LANGUAGE_EXTENSIONS.get(file_extension, 'Unknown')

#........................model: meta-llama/Llama-2-70b-chat-hf........................#
class OpenAIModel(Model):
    def __init__(self):
        self.__open_ai = OpenAI(api_key=OPEN_AI_KEY, base_url=OPEN_AI_BASE_URL)
        self.__refactoring_rules = (
            "1. Add access modifiers to the class and functions."
            "2. Refactoring by abstraction."
            "3. Simplifying methods."
            "4. Moving features between objects."
            "5. Remove unused imports."
            "6. Red-Green-Refactoring: Fix the failing tests and refactor them."
        )
        self.__cost_analysis_rules = (
            "1. Total tokens required to implement the refactoring."
            "2. Estimated cost in USD to implement the refactoring."
        )

    def refactor_code(self, file_name: str, code: str):
        log.info(
            f'Start: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}')

        try:
            messages = [
                {"role": "system",
                    "content": f"You are an expert {self.get_language(file_name)} developer so refactor the following code to enhance readability, maintainability, and efficiency."},
                {"role": "user", "content": code},
                {"role": "system", "content": "Refactor code based on the following refactoring rules:"},
                {"role": "system", "content": self.__refactoring_rules},
                {"role": "system", "content": "Analyze the cost of the refactorings based on the following criteria:"},
                {"role": "system", "content": self.__cost_analysis_rules}
            ]

            chat_stream = self.__open_ai.chat.completions.create(
                model=OPEN_AI_MODEL,
                max_tokens=1000,
                stream=True,
                messages=messages
            )

            log.info(
                f'End: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}')
            return chat_stream
        except Exception as ex:
            log.error(
                f'Error: refactor code for file: {file_name} using model: {OPEN_AI_MODEL}', exc_info=ex)
            raise ValueError(
                f'Failed code refactoring for file: {file_name} using model: {OPEN_AI_MODEL} due to error: {ex}')

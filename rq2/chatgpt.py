import openai
from decouple import config

from rq2.ll_model import LLModel


class ChatGPT(LLModel):

    def __init__(self):
        openai.api_key = config("openai-key")

    def ask_for_explanation(self, question, description, tags):
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=super().get_base_message(question, description, tags),
            temperature=0.6,
            max_tokens=2048
        )['choices'][0]['message']['content']

import openai
from decouple import config


class Request:

    def __init__(self):
        openai.api_key = config("openai-key")

    def generate_prompt(self, question, body):
        return f""" Please, explain how to fix the problem below. 
        {question}
        
        Below, you can find more details 
        {body}"""

    def ask_for_explanation(self, question, description):
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=self.generate_prompt(question, description),
            temperature=0.6,
            max_tokens=2048
        )
import openai
from decouple import config

from rq2.ll_model import LLModel


class ChatGPT(LLModel):

    def __init__(self, llm_version, model):
        self._model_name = model
        self._llm_version = llm_version
        openai.api_key = config("openai-key")


    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def _model_name_setter(self, new_model_name: str):
        self._model_name = new_model_name

    @property
    def llm_version(self):
        return self._llm_version

    @llm_version.setter
    def _llm_version_setter(self, new_llm_version: str):
        self._llm_version = new_llm_version

    def ask_for_explanation(self, question, description, tags):
        return openai.ChatCompletion.create(
            model=self._model_name,
            messages=super().get_base_message(question, description, tags),
            temperature=0.6,
            max_tokens=2048
        )['choices'][0]['message']['content']

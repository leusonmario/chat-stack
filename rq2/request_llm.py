from __future__ import annotations
from ll_model import LLModel

class Request_LLM():

    def __init__(self, ll_model: LLModel):
        self._ll_model = ll_model

    @property
    def ll_model(self):
        return self._ll_model

    def ll_model_set(self, ll_model: LLModel):
        self._ll_model = ll_model

    def ask_for_explanation(self, question, description, tags):
        return self._ll_model.ask_for_explanation(question, description, tags)
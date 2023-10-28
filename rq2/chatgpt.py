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

    def ask_for_similarity_analysis(self, original_answer, generated_answer, tags):
        return openai.ChatCompletion.create(
            model=self._model_name,
            messages=self.get_similarity_message(original_answer, generated_answer, tags),
            temperature=0.6,
            max_tokens=2048
        )['choices'][0]['message']['content']

    def get_similarity_message(self, original_answer, generated_answer, tags):
        base_messages = [
            {'role': 'system',
             'content': "You are an expert in software engineering with much experience on programming."},
            {'role': 'user', 'content': "Please, act as you have solid experience on these topics: " + tags + " ."},
            {'role': 'assistant', 'content': "Okay, I have a solid background on " + tags + " ."},
            {'role': 'user',
             'content': "This way, check the two inputs, A and B, provided below, analyze each of them, and finally, compute their similarity. For that, please consider not only the style of the inputs but also their semantics and context.\n" +
                        "When reporting the similarity, please consider an interval between VERY LOW to VERY HIGH (VERY LOW, LOW, MEDIUM, HIGH, VERY HIGH).\n" +
                        "Please, only report the similarity, and do it by reporting a JSON file with the property similarity, like this template: { \"similarity\": \"SIMILARITY\" } \n" +
                        "DO NOT provide any further information or explanation; just report the similarity, following the template informed, please.\n" +

                        "A = {" + original_answer + "}\n\n" +
                        "B = {" + generated_answer + "}"}]

        return base_messages

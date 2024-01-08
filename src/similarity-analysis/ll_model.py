from abc import ABC, abstractmethod

class LLModel(ABC):

    @property
    @abstractmethod
    def llm_version(self):
        pass

    @llm_version.setter
    def llm_version(self, new_llm_name: str):
        pass

    @abstractmethod
    def _llm_version_setter(self, new_llm_name):
        pass

    @property
    @abstractmethod
    def model_name(self):
        pass

    @model_name.setter
    def model_name(self, new_model_name: str):
        pass

    @abstractmethod
    def _model_name_setter(self, new_model_name):
        pass

    @abstractmethod
    def ask_for_explanation(self, question, description, tags):
        pass

    def get_base_message(self, question, description, tags):
        base_messages = [
            {'role': 'system', 'content': "You are an expert in software engineering with much experience on programming."},
            {'role': 'user', 'content': "Please, act as you have solid experience on these topics: "+tags+" ."},
            {'role': 'assistant', 'content': "Okay, I have a solid background on " + tags + " ."},
            {'role': 'user', 'content': "Please, explain how to fix the problem below. "
                                        ""+question+". "
                                        "Below, you can find more details. "
                                        ""+description+"."},
        ]

        return base_messages
from abc import ABC, abstractmethod

class LLModel(ABC):

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

    base_messages = [
        {'role': 'system', 'content': "You are an expert in software engineering with much experience on programming."},
        {'role': 'user', 'content': "Please, act as you have solid experience on these topics:  ."},
        {'role': 'assistant', 'content': "Okay, I have a solid background on  ."},
        {'role': 'user', 'content': "Please, explain how to fix the problem below. "
                                    ". "
                                                    "Below, you can find more details. "
                                      "."},
    ]
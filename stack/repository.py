from stack.question import Question


class Repository:

    def __init__(self):
        self.questions = []
        self.answers = []

    def save_question(self, question, answers):
        self.questions.append(Question(question, answers))
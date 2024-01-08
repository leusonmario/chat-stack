from stack.user import User


class Answer:

    def __init__(self, answer):
        self.id = answer[0]
        self.body = answer[8]
        self.score = answer[6]
        self.question_id = answer[3]
        self.owner = answer[9]
        self.creation_date = answer[4]
        self.activity = answer[14]


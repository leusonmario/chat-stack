from stack.user import User


class Answer:

    def __init__(self, answer):
        self.id = answer['answer_id']
        self.body = answer['body']
        self.is_accepted = answer['is_accepted']
        self.score = answer['score']
        self.question_id = answer['question_id']
        self.owner = User(answer['owner'])
        self.creation_date = answer['creation_date']
        self.activity = answer['last_activity_date']


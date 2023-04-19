from stack.answer import Answer
from stack.question import Question
from stack.tag import Tag
from stack.user import User


class Repository:

    def __init__(self):
        self.questions = []
        self.answers = []
        self.users = []
        self.tags = []

    def save_question(self, question, answers):
        user = User(question['owner'])
        self.compute_users(user)
        self.questions.append(Question(question, user.id))
        self.compute_answers(answers)
        self.compute_tags(question['tags'], question['question_id'])


    def compute_answers(self, answers):
        for answer in answers['items']:
            user = User(answer['owner'])
            self.answers.append(Answer(answer, user.id))
            self.compute_users(user)

    def compute_tags(self, tags, question_id):
        for tag in tags:
            self.tags.append(Tag(tag, question_id))

    def compute_users(self, user):
        if not user in self.users:
            self.users.append(user)
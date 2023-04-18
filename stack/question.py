from stack.tag import Tag
from stack.user import User


class Question:

    def __init__(self, question, answers):
        self.id = question['question_id']
        self.title = question['title']
        self.body = question['body']
        self.is_answered = question['is_answered']
        self.score = question['score']
        self.answers_number = ['answer_count']
        self.tags = []
        self.split_tags(question['tags'], self.id)
        self.creation_date = question['creation_date']
        self.activity = question['last_edit_date']
        self.link = question['link']
        self.owner = User(question['owner'])
        self.answers = []
        self.compute_answers(answers)

    def split_tags(self, tags, question_id):
        for tag in tags:
            self.tags.append(Tag(tag, question_id))

    def compute_answers(self, answers):
        for answer in answers['items']:
            self.answers.append(answer)
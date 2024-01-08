from stack.tag import Tag
from stack.user import User


class Question:

    def __init__(self, question):
        self.id = question[0]
        self.title = str(question[15])
        self.body = str(question[8])
        self.score = question[6]
        self.view_count = question[7]
        self.answers_number = question[17]
        self.creation_date = question[4]
        self.activity = question[14]
        self.owner = question[9]
        self.accepted_answer = question[2]
        self.tags = []
        self.split_tags(question[16], self.id)

    def split_tags(self, tags, question_id):
        tags = tags.split("><")
        for tag in tags:
            self.tags.append(Tag(tag.replace("<","").replace(">",""), question_id))

    def compute_answers(self, answers):
        for answer in answers['items']:
            self.answers.append(answer)
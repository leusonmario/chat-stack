import os
import csv
import datetime

class OutputGenerator:

    def __init__(self):
        self.report_path = self.get_base_output_path()
        self.create_main_directory()

    def get_base_output_path(self) -> str:
         return os.getcwd().replace("/output_generation", "/") + 'output/' if os.getcwd().__contains__(
            "/output_generation") else os.getcwd() + "/output/"

    def create_main_directory(self):
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)
    def create_directory(self, date):
        if not os.path.exists(self.report_path+date+"/"):
            os.mkdir(self.report_path+date+"/")

    def create_question_output_file(self,date):
        if not os.path.exists(self.report_path+date+"/questions.csv"):
            with open(self.report_path+date+"/questions.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['question_id', 'question_link', 'title','body','is_answered','score','answer_number','creation_date',
                                    'last_activity','owner_id'])

    def add_new_question_output_file(self, date, question):
        self.create_question_output_file(date)
        if os.path.exists(self.report_path+date+"/questions.csv"):
            with open(self.report_path+date+"/questions.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([question.id, question.link, question.title, question.body, question.is_answered, question.score,
                                    question.answers_number, datetime.datetime.fromtimestamp(question.creation_date),
                                    datetime.datetime.fromtimestamp(question.activity), question.owner])

    def create_answer_output_file(self,date):
        if not os.path.exists(self.report_path+date+"/answers.csv"):
            with open(self.report_path+date+"/answers.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['answer_id','body','is_accepted','score','question_id','creation_date',
                                    'last_activity','owner_id'])

    def add_new_answer_output_file(self, date, answer):
        self.create_answer_output_file(date)
        if os.path.exists(self.report_path+date+"/answers.csv"):
            with open(self.report_path+date+"/answers.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([answer.id, answer.body, answer.is_accepted, answer.score,
                                    answer.question_id, datetime.datetime.fromtimestamp(answer.creation_date),
                                    datetime.datetime.fromtimestamp(answer.activity), answer.owner])

    def create_user_output_file(self,date):
        if not os.path.exists(self.report_path+date+"/users.csv"):
            with open(self.report_path+date+"/users.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['user_id','reputation','profile_link','acceptance_rate'])

    def add_new_user_output_file(self, date, user):
        self.create_user_output_file(date)
        if os.path.exists(self.report_path+date+"/users.csv"):
            with open(self.report_path+date+"/users.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([user.id, user.reputation, user.profile_link, user.acceptance_rate])

    def create_tag_output_file(self,date):
        if not os.path.exists(self.report_path+date+"/tags.csv"):
            with open(self.report_path+date+"/tags.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['tag_id','question_id'])

    def add_new_tag_output_file(self, date, tag):
        self.create_tag_output_file(date)
        if os.path.exists(self.report_path+date+"/tags.csv"):
            with open(self.report_path+date+"/tags.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([tag.tag, tag.question_id])

    def save_question(self, question, date):
        self.create_directory(date)
        self.add_new_question_output_file(date, question)

    def save_answer(self, answer, date):
        self.create_directory(date)
        self.add_new_answer_output_file(date, answer)

    def save_user(self, user, date):
        self.create_directory(date)
        self.add_new_user_output_file(date, user)

    def save_tag(self, tag, date):
        self.create_directory(date)
        self.add_new_tag_output_file(date, tag)
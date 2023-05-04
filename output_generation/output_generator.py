import os
import csv
import datetime

class OutputGenerator:

    def __init__(self, output_directory):
        self.report_path = output_directory
        self.create_main_directory()

    def create_main_directory(self):
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)
    def create_directory(self, date):
        if not os.path.exists(self.report_path+date+"/"):
            os.mkdir(self.report_path+date+"/")

    def create_question_output_file(self):
        if not os.path.exists(self.report_path+"/questions.csv"):
            with open(self.report_path+"/questions.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['question_id', 'title','body','score','view_count','answer_number','creation_date',
                                    'last_activity','owner_id','accepted_answer'])

    def add_new_question_output_file(self, question):
        self.create_question_output_file()
        if os.path.exists(self.report_path+"/questions.csv"):
            with open(self.report_path+"/questions.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([question.id, question.title, question.body, question.score, question.view_count,
                                    question.answers_number, question.creation_date, question.activity, question.owner,
                                    question.accepted_answer])

    def create_comment_output_file(self):
        if not os.path.exists(self.report_path+"/comments.csv"):
            with open(self.report_path+"/comments.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['comment_id', 'post_id','score','text','creation_date','user_id'])

    def add_new_comment_output_file(self, comment):
        self.create_comment_output_file()
        if os.path.exists(self.report_path+"/comments.csv"):
            with open(self.report_path+"/comments.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([comment.id, comment.associated_post, comment.score, comment.text, comment.creation,
                                    comment.user_id])

    def create_answer_output_file(self):
        if not os.path.exists(self.report_path+"/answers.csv"):
            with open(self.report_path+"/answers.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['answer_id','body','score','question_id','owner_id','creation_date',
                                    'last_activity',])

    def add_new_answer_output_file(self, answer):
        self.create_answer_output_file()
        if os.path.exists(self.report_path+"/answers.csv"):
            with open(self.report_path+"/answers.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([answer.id, answer.body, answer.score, answer.question_id, answer.owner, answer.creation_date,
                                    answer.activity])

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

    def create_tag_output_file(self):
        if not os.path.exists(self.report_path+"/tags.csv"):
            with open(self.report_path+"/tags.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['tag_id','question_id'])

    def add_new_tag_output_file(self, tag):
        self.create_tag_output_file()
        if os.path.exists(self.report_path+"/tags.csv"):
            with open(self.report_path+"/tags.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([tag.tag, tag.question_id])

    def save_question(self, question):
        self.add_new_question_output_file(question)

    def save_answer(self, answer):
        self.add_new_answer_output_file(answer)

    def save_user(self, user, date):
        self.create_directory(date)
        self.add_new_user_output_file(date, user)

    def save_tag(self, tag):
        self.add_new_tag_output_file(tag)

    def save_comment(self, comment):
        self.add_new_comment_output_file(comment)
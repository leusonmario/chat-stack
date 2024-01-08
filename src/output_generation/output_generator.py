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

    def create_directory_by_category(self, type):
        if not os.path.exists(self.report_path+type):
            os.mkdir(self.report_path+type)

    def create_question_output_file(self, type):
        self.create_directory_by_category(type)
        if not os.path.exists(self.report_path+"/"+type+"/questions.csv"):
            with open(self.report_path+type+"/questions.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['question_id', 'title','body','score','view_count','answer_number','creation_date',
                                    'last_activity','owner_id','accepted_answer'])

    def add_new_question_output_file(self, question, type):
        self.create_question_output_file(type)
        if os.path.exists(self.report_path+"/"+type+"/questions.csv"):
            with open(self.report_path+"/"+type+"/questions.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([question.id, question.title, question.body, question.score, question.view_count,
                                    question.answers_number, question.creation_date, question.activity, question.owner,
                                    question.accepted_answer])

    def create_comment_output_file(self, type):
        self.create_directory_by_category(type)
        if not os.path.exists(self.report_path+"/"+type+"/comments.csv"):
            with open(self.report_path+"/"+type+"/comments.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['comment_id', 'post_id','score','text','creation_date','user_id'])

    def add_new_comment_output_file(self, comment, type):
        self.create_comment_output_file(type)
        if os.path.exists(self.report_path+"/"+type+"/comments.csv"):
            with open(self.report_path+"/"+type+"/comments.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([comment.id, comment.associated_post, comment.score, comment.text, comment.creation,
                                    comment.user_id])

    def create_answer_output_file(self, type):
        self.create_directory_by_category(type)
        if not os.path.exists(self.report_path+"/"+type+"/answers.csv"):
            with open(self.report_path+"/"+type+"/answers.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['answer_id','body','score','question_id','owner_id','creation_date',
                                    'last_activity',])

    def add_new_answer_output_file(self, answer, type):
        self.create_answer_output_file(type)
        if os.path.exists(self.report_path+"/"+type+"/answers.csv"):
            with open(self.report_path+"/"+type+"/answers.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([answer.id, answer.body, answer.score, answer.question_id, answer.owner, answer.creation_date,
                                    answer.activity])

    def create_generated_answer_output_file(self, type):
        self.create_directory_by_category(type)
        if not os.path.exists(self.report_path+"/"+type+"/generated_answers.csv"):
            with open(self.report_path+"/"+type+"/generated_answers.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['question_id','original_answer','generated_answer','cosine_metric'])

    def add_new_generated_answer_output_file(self, question_id, original_answer, generated_answer, cosine_metric, type):
        self.create_generated_answer_output_file(type)
        if os.path.exists(self.report_path+"/"+type+"/generated_answers.csv"):
            with open(self.report_path+"/"+type+"/generated_answers.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([question_id, original_answer, generated_answer, cosine_metric])

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

    def create_tag_output_file(self, type):
        self.create_directory_by_category(type)
        if not os.path.exists(self.report_path+"/"+type+"/tags.csv"):
            with open(self.report_path+"/"+type+"/tags.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(['tag_id','question_id'])

    def add_new_tag_output_file(self, tag, type):
        self.create_tag_output_file(type)
        if os.path.exists(self.report_path+"/"+type+"/tags.csv"):
            with open(self.report_path+"/"+type+"/tags.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([tag.tag, tag.question_id])

    def save_question(self, question, type):
        self.add_new_question_output_file(question, type)

    def save_answer(self, answer, type):
        self.add_new_answer_output_file(answer, type)

    def save_user(self, user, date):
        self.create_directory(date)
        self.add_new_user_output_file(date, user)

    def save_tag(self, tag, type):
        self.add_new_tag_output_file(tag, type)

    def save_comment(self, comment, type):
        self.add_new_comment_output_file(comment, type)

    def save_generated_answer(self, question_id, original_answer, generated_answer, cosine_metric, type):
        self.add_new_generated_answer_output_file(question_id, original_answer, generated_answer, cosine_metric, type)
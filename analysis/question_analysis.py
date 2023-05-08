import os

import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime

class QuestionAnalysis:

    def __init__(self, questions, target_directory):
        self.questions = questions
        self.question_users = {}
        self.answered_questions = []
        self.unanswered_questions = []
        self.accepted_answers_for_questions = []
        self.questions_by_date = {}
        self.target_directory = target_directory
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.target_directory+"/figures"):
            os.mkdir(self.target_directory+"/figures")

    def general_data_analysis(self):
        for question in self.questions:
            if question.owner != "":
                if question.owner in self.question_users:
                    value = self.question_users[question.owner] + 1
                    self.question_users.update({question.owner: value})
                else:
                    self.question_users[question.owner] = 1

            if int(question.answers_number) > 0:
                self.answered_questions.append(question.id)
                if question.accepted_answer != "":
                    self.accepted_answers_for_questions.append(question.accepted_answer)
            else:
                self.unanswered_questions.append(question.id)

            if question.creation_date.split(" ")[0] in self.questions_by_date:
                value = self.questions_by_date[question.creation_date.split(" ")[0]] + 1
                self.questions_by_date.update({question.creation_date.split(" ")[0]: value})
            else:
                self.questions_by_date[question.creation_date.split(" ")[0]] = 1

    def generate_bar_chart_user_questions(self):
        matplotlib.pyplot.clf()
        sorted_data = sorted(self.question_users.items(), key=lambda x: x[1], reverse=True)[:10]

        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]

        plt.bar(labels, values)
        plt.xticks(rotation=30, horizontalalignment="center")
        for i, v in enumerate(values):
            plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

        plt.savefig(self.target_directory+"/figures/bar-chat-question-users.png")

    def generate_line_chart_questions_over_time(self):
        matplotlib.pyplot.clf()
        dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in self.questions_by_date.keys()])
        values = [self.questions_by_date[date.strftime('%Y-%m-%d')] for date in dates]

        plt.plot(dates, values)

        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")

        plt.savefig(self.target_directory+"/figures/line-chart-questions-by-date.png")

        return dates, values

    def get_number_questions(self):
        return len(self.questions)

    def get_number_answered_questions(self):
        return len(self.answered_questions)

    def get_number_answered_questions_with_accepted_answers(self):
        return len(self.accepted_answers_for_questions)

    def get_number_unanswered_questions(self):
        return len(self.unanswered_questions)

    def get_number_users(self):
        return len(self.question_users)
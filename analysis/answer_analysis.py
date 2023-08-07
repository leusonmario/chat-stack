import csv
import os
from datetime import datetime

import matplotlib
from matplotlib import pyplot as plt


class AnswerAnalysis:

    def __init__(self, answers, target_directory):
        self.answer_users = {}
        self.answers_by_date = {}
        self.answers = answers
        self.target_directory = target_directory
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.target_directory + "/figures"):
            os.mkdir(self.target_directory + "/figures")

    def general_data_analysis(self):
        for answer in self.answers:
            if answer.creation_date.split(" ")[0] in self.answers_by_date:
                value = self.answers_by_date[answer.creation_date.split(" ")[0]] + 1
                self.answers_by_date.update({answer.creation_date.split(" ")[0]: value})
            else:
                self.answers_by_date[answer.creation_date.split(" ")[0]] = 1

            if answer.owner != "":
                if answer.owner in self.answer_users:
                    value = self.answer_users[answer.owner] + 1
                    self.answer_users.update({answer.owner: value})
                else:
                    self.answer_users[answer.owner] = 1

    def generate_bar_chart_user_answers(self):
        matplotlib.pyplot.clf()
        sorted_data = sorted(self.answer_users.items(), key=lambda x: x[1], reverse=True)[:10]

        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]

        plt.bar(labels, values)
        plt.xticks(rotation=30, horizontalalignment="center")
        for i, v in enumerate(values):
            plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

        plt.savefig(self.target_directory+"/figures/bar-chat-answer-users.png")

    def generate_line_chart_answers_over_time(self):
        matplotlib.pyplot.clf()
        dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in self.answers_by_date.keys()])

        values = [self.answers_by_date[date.strftime('%Y-%m-%d')] for date in dates]

        plt.plot(dates, values)

        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")

        plt.savefig(self.target_directory+"/figures/line-chart-answers-by-date.png")

        #self.create_output_file(dates, values)

        return dates, values

    def get_number_questions(self):
        return len(self.answers)

    def get_number_users(self):
        return len(self.answer_users)

    def create_output_file(self, dates, number_answers_per_day):
        with open(self.target_directory+"/answers-analysis.csv", 'w+') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(["Date", "Number of Answers"])
            for i in range(len(dates)):
                csvreader.writerow([dates[i], number_answers_per_day[i]])
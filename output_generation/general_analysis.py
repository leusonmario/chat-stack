import csv
import os
from datetime import datetime

import matplotlib
from matplotlib import pyplot as plt


class GeneralAnalysis:

    def __init__(self, target_directory):
        self.target_directory = target_directory
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.target_directory+"/general"):
            os.mkdir(self.target_directory+"/general")

    def create_question_output_file(self):
        if not os.path.exists(self.target_directory + "/general_analysis.csv"):
            with open(self.target_directory + "/general_analysis.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(
                    ['metric', 'value'])

    def add_new_metric_value(self, metric, value):
        self.create_question_output_file()
        if os.path.exists(self.target_directory + "/general_analysis.csv"):
            with open(self.target_directory + "/general_analysis.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([metric, value])


    def generate_bar_chart_user_questions(self, question_users):
        matplotlib.pyplot.clf()
        sorted_data = sorted(question_users.items(), key=lambda x: x[1], reverse=True)[:10]

        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]

        plt.bar(labels, values)
        plt.xticks(rotation=30, horizontalalignment="center")
        for i, v in enumerate(values):
            plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

        plt.savefig(self.target_directory+"/general/bar-chat-question-users.png")

    def generate_line_chart_questions_over_time(self, questions_by_date):
        matplotlib.pyplot.clf()
        dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in questions_by_date.keys()])
        values = [questions_by_date[date.strftime('%Y-%m-%d')] for date in dates]

        plt.plot(dates, values)

        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")

        plt.savefig(self.target_directory+"/general/line-chart-questions-by-date.png")
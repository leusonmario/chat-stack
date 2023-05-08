import os
from datetime import datetime

import matplotlib
from matplotlib import pyplot as plt


class CommentAnalysis:

    def __init__(self, comments, target_directory):
        self.comments = comments
        self.target_directory = target_directory
        self.comment_users = {}
        self.comment_by_date = {}
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.target_directory + "/figures"):
            os.mkdir(self.target_directory + "/figures")

    def general_data_analysis(self):
        for comment in self.comments:
            if comment.creation.split(" ")[0] in self.comment_by_date:
                value = self.comment_by_date[comment.creation.split(" ")[0]] + 1
                self.comment_by_date.update({comment.creation.split(" ")[0]: value})
            else:
                self.comment_by_date[comment.creation.split(" ")[0]] = 1

            if comment.user_id != "-1":
                if comment.user_id in self.comment_users:
                    value = self.comment_users[comment.user_id] + 1
                    self.comment_users.update({comment.user_id: value})
                else:
                    self.comment_users[comment.user_id] = 1

    def generate_bar_chart_user_answers(self):
        matplotlib.pyplot.clf()
        sorted_data = sorted(self.comment_users.items(), key=lambda x: x[1], reverse=True)[:10]

        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]

        plt.bar(labels, values)
        plt.xticks(rotation=30, horizontalalignment="center")
        for i, v in enumerate(values):
            plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

        plt.savefig(self.target_directory+"/figures/bar-chat-comment-users.png")


    def generate_line_chart_answers_over_time(self):
        matplotlib.pyplot.clf()
        dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in self.comment_by_date.keys()])

        values = [self.comment_by_date[date.strftime('%Y-%m-%d')] for date in dates]

        plt.plot(dates, values)

        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")

        plt.savefig(self.target_directory+"/figures/line-chart-comments-by-date.png")
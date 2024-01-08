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
        if not os.path.exists(self.target_directory + "/general/general_analysis.csv"):
            with open(self.target_directory + "/general/general_analysis.csv", 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(
                    ['metric', 'value'])

    def add_new_metric_value(self, metric, value):
        self.create_question_output_file()
        if os.path.exists(self.target_directory + "/general/general_analysis.csv"):
            with open(self.target_directory + "/general/general_analysis.csv", 'a') as file:
                csvreader = csv.writer(file)
                csvreader.writerow([metric, value])


    def generate_line_chart_posts_over_time(self, dates, values, type):
        matplotlib.pyplot.clf()
        for i in range(2):
            plt.plot(dates[i], values[i])

        plt.axvline(x=datetime.strptime('2022-11-30', '%Y-%m-%d').date(), color='r')
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")

        plt.savefig(self.target_directory+"general/line-chart-"+type+"-by-date.png")


    def generate_tag_usage_frequency(self, tags_dates, tags_values):
        matplotlib.pyplot.clf()
        colors = ['black', 'orange', 'blue', 'green', 'pink']
        legend_values = [0] * 5

        for i in range(2):
            j = 0
            for value in tags_values[i]:
                aux = tags_dates[i]
                plt.plot(tags_dates[i], tags_values[i][value], color=colors[j], label="" + value)
                legend_values[j] = value
                j += 1

        plt.axvline(x=datetime.strptime('2022-11-30', '%Y-%m-%d').date(), color='r')
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Values by Date")
        plt.legend(legend_values)

        plt.savefig(self.target_directory+"general/tag-line-chart-all.png")

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
        colors = ['black', 'orange', 'blue', 'green', 'pink', 'yellow', 'purple', 'brown', 'gray', 'red']
        legend_values = [0] * 10

        for i in range(2):
            j = 0
            languages = ["python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c"]

            frameworks = ["reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel",
                          "vue.js"]

            libraries = ["pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter"]

            #for value in tags_values[i]:
            for language in libraries:
                #aux = tags_dates[i]
                plt.plot(tags_dates[i], tags_values[i][language], color=colors[j], label="" + language)
                legend_values[j] = language
                j += 1

        plt.axvline(x=datetime.strptime('2022-11-30', '%Y-%m-%d').date(), color='r')
        plt.xlabel("Date")
        #plt.ylabel("Value")
        plt.title("Frequency of Posted Questions on the Top 10 Most Cited Libraries")
        plt.legend(legend_values)

        plt.savefig(self.target_directory+"general/tag-line-chart-all-libraries.pdf")

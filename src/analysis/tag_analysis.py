import csv
import os
from datetime import datetime

import matplotlib
from matplotlib import pyplot as plt
from wordcloud import WordCloud


class TagAnalysis:

    def __init__(self, questions, target_directory):
        self.tags = {}
        self.tags_by_question_id = {}
        self.questions_by_date = {}
        self._get_tags_from_questions(questions)
        self.target_directory = target_directory
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.target_directory+"/figures"):
            os.mkdir(self.target_directory+"/figures")

    def _get_tags_from_questions(self, questions):
        for question in questions:
            for tag in question.tags:
                if tag.tag in self.tags:
                    value = self.tags[tag.tag] + 1
                    self.tags.update({tag.tag: value})
                else:
                    self.tags[tag.tag] = 1

                if (tag.tag in self.tags_by_question_id):
                    self.tags_by_question_id[tag.tag].append(question.id)
                else:
                    self.tags_by_question_id[tag.tag] = [question.id]

                self.questions_by_date[question.id] = question.creation_date.split(" ")[0]

    def generate_word_cloud(self):
        matplotlib.pyplot.clf()
        wc = WordCloud(background_color="white", width=1000, height=1000, max_words=100, relative_scaling=0.5,
                       normalize_plurals=False).generate_from_frequencies(self.tags)
        plt.figure(figsize=(15, 8))
        plt.imshow(wc)
        # plt.show()
        plt.savefig(self.target_directory+"/figures/word-cloud-tags.png")

    def generate_bar_chart_tags(self):
        matplotlib.pyplot.clf()
        sorted_data = sorted(self.tags.items(), key=lambda x: x[1], reverse=True)[:10]

        labels = [item[0] for item in sorted_data]
        values = [item[1] for item in sorted_data]

        plt.bar(labels, values)
        plt.xticks(rotation=30, horizontalalignment="center")
        for i, v in enumerate(values):
            plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)

        plt.savefig(self.target_directory+"/figures/bar-chat.png")

    def generate_tag_usage_frequency(self):
        matplotlib.pyplot.clf()
        sorted_tags = dict(sorted(self.tags.items(), key=lambda x: x[1], reverse=True))
        general_dates = []
        tags_by_date = {}
        languages = ["python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c"]

        frameworks = ["reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel", "vue.js"]

        libraries = ["pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter"]

        for sorted_tag in sorted_tags:
            if sorted_tag in libraries:
                # for each question_id associated with a specific tag (all dates a specific date was used)
                for question_id in self.tags_by_question_id[sorted_tag]:
                    # check whether the date associated to a question is part of all general dates. If not, add it to the list.
                    if not self.questions_by_date[question_id] in general_dates:
                        general_dates.append(self.questions_by_date[question_id])
                    try:
                        # check whether the current selected tag is in the dict of tags associated with dates
                        if (sorted_tag in tags_by_date):
                            # if so, check whether the current question date is already in the dict of tags associated with dates
                            if self.questions_by_date[question_id] in tags_by_date[sorted_tag].keys():
                                # if so, update the number of tag usage in the related date by one
                                value = tags_by_date[sorted_tag][self.questions_by_date[question_id]] + 1
                                tags_by_date[sorted_tag][self.questions_by_date[question_id]] = value
                            else:
                                # if no, it means, there is no tag usage by that date. so, a new entry in the dict is required.
                                tags_by_date[sorted_tag][self.questions_by_date[question_id]] = 1
                        else:
                            # if not, add the sorted tag to the dict, and for the date associated with the question the value 1
                            tags_by_date[sorted_tag] = {self.questions_by_date[question_id]: 1}
                    except:
                        print("ERROR")

        values = {}
        dates = []
        for tag_by_date in tags_by_date:
            # dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in tags_by_date[tag_by_date].keys()])
            dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in general_dates])

            # Extract the values from the dictionary in the sorted order
            # values = [tags_by_date[tag_by_date][date.strftime('%Y-%m-%d')] for date in dates]
            if tag_by_date in tags_by_date is False:
                values[tag_by_date] = []
            else:
                final_values_frequency = []
                for date in dates:
                    if date.strftime('%Y-%m-%d') in tags_by_date[tag_by_date]:
                        final_values_frequency.append(tags_by_date[tag_by_date][date.strftime('%Y-%m-%d')])
                    else:
                        final_values_frequency.append(0)
                values[tag_by_date] = final_values_frequency

            # Create a line chart of the data
        for value in values:
            plt.plot(dates, values[value], label="" + value)
            self.save_associated_tag_occurrence(value, dates, values.get(value))

            # Add labels and title
        plt.xlabel("Date")
        #plt.ylabel("Value")
        plt.title("Distribution of Posted Questions on the Top 10 Most Cited Libraries")
        plt.legend()
        # Show the plot
        plt.savefig(self.target_directory+"/figures/tag-line-chart-all-libraries.pdf")

        return dates, values

    def save_associated_tag_occurrence(self, tag, dates, values):
        for i in range(len(dates)):
            self.save_tag_occurrence(tag, dates[i], values[i])

    def create_report_file(self, tag):
        if not os.path.exists(self.target_directory + "/" + tag + "-tag.csv"):
            with open(self.target_directory + "/" + tag + "-tag.csv", 'w') as f:
                csvreader = csv.writer(f)
                csvreader.writerow(
                    ["date", "value"])

    def save_tag_occurrence(self, tag, date, value):
        self.create_report_file(tag)
        if os.path.exists(self.target_directory + "/" + tag + "-tag.csv"):
            with open(self.target_directory + "/" + tag + "-tag.csv", 'a') as f:
                csvreader = csv.writer(f)
                csvreader.writerow([date, value])

    def get_number_tags(self):
        return len(self.tags)
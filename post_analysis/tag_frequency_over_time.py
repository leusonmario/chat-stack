import csv

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime

tags = {}

#check tag frequency - OK
with open("../output/tags-analysis.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
       tags[row[0]] = int(row[1])

#sort the list based on the frequency of tags, and return the first 5 elements
sorted_tags = dict(sorted(tags.items(), key=lambda x: x[1], reverse=True)[:5])
i = 0

#associate question_id to tag
tags = {}
with open("../output/tags.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
       if row[0] in sorted_tags:
           if (row[0] in tags):
               tags[row[0]].append(row[1])
           else:
               tags[row[0]] = [row[1]]

#associate question_id to its creation date
questions_by_date = {}
i = 0
with open("../output/questions.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        questions_by_date[row[0]] = row[6].split(" ")[0]


# {python : {'2022-12-02' : 2, '2022-12-03' : 3}, 'android' : {'2022-12-02' : 2, '2022-12-03' : 3}}
tags_by_date = {}
general_dates = []

#for each tag from the list of 5
for sorted_tag in sorted_tags:
    #for each question_id associated with a specific tag (all dates a specific date was used)
    for question_id in tags[sorted_tag]:
        #check whether the date associated to a question is part of all general dates. If not, add it to the list.
        if not questions_by_date[question_id] in general_dates:
            general_dates.append(questions_by_date[question_id])
        try:
            #check whether the current selected tag is in the dict of tags associated with dates
            if (sorted_tag in tags_by_date):
                #if so, check whether the current question date is already in the dict of tags associated with dates
                if questions_by_date[question_id] in tags_by_date[sorted_tag].keys():
                    #if so, update the number of tag usage in the related date by one
                    value = tags_by_date[sorted_tag][questions_by_date[question_id]] + 1
                    tags_by_date[sorted_tag][questions_by_date[question_id]] = value
                else:
                    #if no, it means, there is no tag usage by that date. so, a new entry in the dict is required.
                    tags_by_date[sorted_tag][questions_by_date[question_id]] = 1
            else:
                #if not, add the sorted tag to the dict, and for the date associated with the question the value 1
                tags_by_date[sorted_tag] = {questions_by_date[question_id] : 1}
        except:
            print("ERROR")

values = {}
dates = []
for tag_by_date in tags_by_date:
    aux = tags_by_date[tag_by_date].keys()
    #dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in tags_by_date[tag_by_date].keys()])
    dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in general_dates])

    # Extract the values from the dictionary in the sorted order
    # values = [tags_by_date[tag_by_date][date.strftime('%Y-%m-%d')] for date in dates]
    values[tag_by_date] = [tags_by_date[tag_by_date][date.strftime('%Y-%m-%d')] for date in dates]

    # Create a line chart of the data
for value in values:
    plt.plot(dates, values[value], label=""+value)

    # Add labels and title
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Values by Date")
plt.legend()
    # Show the plot
plt.savefig("output/figures/tag-line-chart-all2.png")
plt.show()


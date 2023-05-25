import csv

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime

answer_users = {}
answers_by_date = {}
answers = []

with open("/home/leuson/Downloads/finalOutput-not-including-last-days-april/before/answers.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
       answers.append(row[0])
       if row[5].split(" ")[0] in answers_by_date:
           value = answers_by_date[row[5].split(" ")[0]] + 1
           answers_by_date.update({row[5].split(" ")[0]: value})
       else:
           answers_by_date[row[5].split(" ")[0]] = 1

       if row[4] != "":
           if row[4] in answer_users:
               value = answer_users[row[4]] + 1
               answer_users.update({row[4]: value})
           else:
               answer_users[row[4]] = 1


with open("/home/leuson/PycharmProjects/chat-stack-mines/output/answers-analysis-new.csv", 'w+') as file:
    csvreader = csv.writer(file)
    csvreader.writerow(["user_ID", "number_answered_questions"])
    for key in answer_users:
        csvreader.writerow([key, answer_users[key]])

names = list(answer_users.keys())
values = list(answer_users.values())

sorted_data = sorted(answer_users.items(), key=lambda x: x[1], reverse=True)[:10]

# Extract the labels and values from the sorted dictionary
labels = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

# Plot the bar chart
plt.bar(labels, values)
plt.xticks(rotation=30, horizontalalignment="center")
for i, v in enumerate(values):
    plt.text(i, v+0.5, str(v), ha='center', fontsize=10)

plt.savefig("bar-chat-answer-users-new.png")

matplotlib.pyplot.clf()

dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in answers_by_date.keys()])

# Extract the values from the dictionary in the sorted order
values = [answers_by_date[date.strftime('%Y-%m-%d')] for date in dates]

# Create a line chart of the data
plt.plot(dates, values)

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Values by Date")

# Show the plot
#plt.show()
plt.savefig("line-chart-answers-by-date-new.png")

print("Number of Answers : " + str(len(answers)))
print("Number of Users : " + str(len(answer_users.keys())))
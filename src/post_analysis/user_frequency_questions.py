import csv

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
from collections import Counter

question_users = {}
answered_questions = []
unanswered_questions = []
accepted_answers_for_questions = []
questions_by_date = {}
questions = []

with open("../output/questions.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
       questions.append(row[0])
       if row[8] != "":
           if row[8] in question_users:
               value = question_users[row[8]] + 1
               question_users.update({row[8]: value})
           else:
               question_users[row[8]] = 1

       if int(row[5]) > 0:
           answered_questions.append(row[0])
           if row[9] != "":
               accepted_answers_for_questions.append(row[9])
       else:
           unanswered_questions.append(row[0])

       if row[6].split(" ")[0] in questions_by_date:
           value = questions_by_date[row[6].split(" ")[0]] + 1
           questions_by_date.update({row[6].split(" ")[0]: value})
       else:
           questions_by_date[row[6].split(" ")[0]] = 1

print("Number of Questions : " + str(len(questions)))
print("Number of Answered Questions : "+str(len(answered_questions)))
print("Number of Questions with Accepted Answers: "+str(len(accepted_answers_for_questions)))
print("Number of Unanswered Questions : "+str(len(unanswered_questions)))
print("Number of Users : "+str(len(question_users)))

#questions_by_date = sorted(questions_by_date.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

print(questions_by_date)

with open("/output/questions-analysis.csv", 'w+') as file:
    csvreader = csv.writer(file)
    csvreader.writerow(["User_ID", "Number of Questions"])
    for key in question_users:
        csvreader.writerow([key, question_users[key]])

names = list(question_users.keys())
values = list(question_users.values())

sorted_data = sorted(question_users.items(), key=lambda x: x[1], reverse=True)[:10]

# Extract the labels and values from the sorted dictionary
labels = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

# Plot the bar chart
plt.bar(labels, values)
plt.xticks(rotation=30, horizontalalignment="center")
for i, v in enumerate(values):
    plt.text(i, v+0.5, str(v), ha='center', fontsize=10)

plt.savefig("bar-chat-question-users.png")

matplotlib.pyplot.clf()

dates = sorted([datetime.strptime(date, '%Y-%m-%d').date() for date in questions_by_date.keys()])

# Extract the values from the dictionary in the sorted order
values = [questions_by_date[date.strftime('%Y-%m-%d')] for date in dates]

# Create a line chart of the data
plt.plot(dates, values)

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Values by Date")

# Show the plot
plt.savefig("line-chart-questions-by-date.png")
plt.show()







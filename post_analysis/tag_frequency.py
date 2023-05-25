import csv

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tags = {}

with open("../output/tags.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
       if row[0] in tags:
           value = tags[row[0]] + 1
           tags.update({row[0]: value})
       else:
           tags[row[0]] = 1

with open("../output/tags-analysis.csv", 'w+') as file:
    csvreader = csv.writer(file)
    for key in tags:
        csvreader.writerow([key, tags[key]])

wc = WordCloud(background_color="white",width=1000,height=1000, max_words=100,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(tags)
plt.figure(figsize=(15,8))
plt.imshow(wc)
#plt.show()
plt.savefig("word-cloud.png")
matplotlib.pyplot.clf()

names = list(tags.keys())
values = list(tags.values())

sorted_data = sorted(tags.items(), key=lambda x: x[1], reverse=True)[:10]

# Extract the labels and values from the sorted dictionary
labels = [item[0] for item in sorted_data]
values = [item[1] for item in sorted_data]

# Plot the bar chart
plt.bar(labels, values)
plt.xticks(rotation=30, horizontalalignment="center")
for i, v in enumerate(values):
    plt.text(i, v+0.5, str(v), ha='center', fontsize=10)

plt.savefig("bar-chat.png")

print("Number of Tags : " + str(len(tags.keys())))
from stackapi import StackAPI
from decouple import config
import os
import csv
import datetime
import random

def create_report_file(directory, file):
    if not os.path.exists(directory+file+".csv"):
        with open(directory+file+".csv", 'w') as f:
            csvreader = csv.writer(f)
            csvreader.writerow(["user_id", "reputation", "creation_date", "profile_before_chatgpt", "last_access",
                                "bronze_badge", "silver_badge", "gold_badge"])

def save_user(directory,file,user):
    create_report_file(directory, file)
    if os.path.exists(directory+file+".csv"):
        with open(directory+file+".csv", 'a') as f:
            csvreader = csv.writer(f)
            csvreader.writerow([user[0], user[1], user[2], user[3], user[4], user[5]])

def read_users(file):
    users = []
    if os.path.exists(file):
        with open(file, 'r') as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for i, row in enumerate(csvreader):
                users.append(row[0])

    return users

def random_selection_users(all_users, number_elements):
    random_users = []
    if (number_elements <= len(all_users)):
        random_users = random.sample(all_users, number_elements)
    return random_users

SITE = StackAPI('stackoverflow', key=config('KEY-STACK-TWO'))
chatgpt_release_date = datetime.datetime(2022, 11, 30)
selected_users = read_users("/home/leuson/Downloads/finalOutput/general/new-commentors.csv")

split_users = [selected_users[i:i+100] for i in range(0, len(selected_users), 100)]

before_chatgpt = 0
after_chatgpt = 0

for selected_user in split_users:
    users = SITE.fetch(endpoint='users', ids = selected_user)

    for user in users['items']:
        before_release = datetime.datetime.fromtimestamp(user['creation_date']) < chatgpt_release_date
        if (before_release):
            before_chatgpt += 1
        else:
            after_chatgpt += 1

        user = [user['user_id'], user['reputation'], datetime.datetime.fromtimestamp(user['creation_date']), before_release,
                datetime.datetime.fromtimestamp(user['last_access_date']), user['badge_counts']['bronze'],
                user['badge_counts']['silver'], user['badge_counts']['gold']]
        save_user("/home/leuson/Downloads/finalOutput/general/", "new-commentors-analysis", user)

print("Before - " + str(before_chatgpt))
print("After - " + str(after_chatgpt))
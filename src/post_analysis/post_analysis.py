import csv
import os
from datetime import datetime
from random import random
from time import sleep
from decouple import config

import matplotlib
import matplotlib.pyplot as pyplot
from stackapi import StackAPI


def distribution_answer_by_day(files, analysis_file):
    week_day = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    for one_file in files:
        dates = {}
        with open(one_file + analysis_file + ".csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[5].split(" ")[0] in dates):
                    aux = dates[row[5].split(" ")[0]]
                    dates.update({row[5].split(" ")[0]: (aux + 1)})
                else:
                    dates[row[5].split(" ")[0]] = 1

        analysis = one_file + analysis_file + "-analysis.csv"
        if not os.path.exists(analysis):
            with open(analysis, 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(["date", "number_answers", "week_day"])

        with open(analysis, 'a') as file:
            for value in dates:
                csvreader = csv.writer(file)
                csvreader.writerow([value, dates[value], week_day[datetime.strptime(value, "%Y-%m-%d").weekday()]])

def distribution_question_by_day(files, analysis_file):
    week_day = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    for one_file in files:
        dates = {}
        with open(one_file + analysis_file + ".csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[6].split(" ")[0] in dates):
                    aux = dates[row[6].split(" ")[0]]
                    dates.update({row[6].split(" ")[0]: (aux + 1)})
                else:
                    dates[row[6].split(" ")[0]] = 1

        analysis = one_file + analysis_file + "-analysis.csv"
        if not os.path.exists(analysis):
            with open(analysis, 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(["date", "number_questions", "week_day"])

        with open(analysis, 'a') as file:
            for value in dates:
                csvreader = csv.writer(file)
                csvreader.writerow([value, dates[value], week_day[datetime.strptime(value, "%Y-%m-%d").weekday()]])

def distribution_comments_by_day(files, analysis_file):
    week_day = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    for one_file in files:
        dates = {}
        with open(one_file + analysis_file + ".csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[4].split(" ")[0] in dates):
                    aux = dates[row[4].split(" ")[0]]
                    dates.update({row[4].split(" ")[0]: (aux + 1)})
                else:
                    dates[row[4].split(" ")[0]] = 1

        analysis = one_file + analysis_file + "-analysis.csv"
        if not os.path.exists(analysis):
            with open(analysis, 'w') as file:
                csvreader = csv.writer(file)
                csvreader.writerow(["date", "number_comments", "week_day"])

        with open(analysis, 'a') as file:
            for value in dates:
                csvreader = csv.writer(file)
                csvreader.writerow([value, dates[value], week_day[datetime.strptime(value, "%Y-%m-%d").weekday()]])

def get_tags_frequency(tags_file, analysis_file):
    tags = {}

    with open(tags_file + analysis_file + ".csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            if row[0] in tags:
                value = tags[row[0]] + 1
                tags.update({row[0]: value})
            else:
                tags[row[0]] = 1

    with open(tags_file+"tags_analysis.csv", 'w+') as file:
        csvreader = csv.writer(file)
        for key in tags:
            csvreader.writerow([key, tags[key]])

    return tags
def distribution_tags(files, analysis_file, main_directory):
    tags_before = get_tags_frequency(files[0], analysis_file)
    tags_after = get_tags_frequency(files[1], analysis_file)

    analysis = main_directory + analysis_file + "-analysis.csv"
    with open(analysis, 'w+') as file:
        csvreader = csv.writer(file)
        for key in tags_before:
            if (tags_after.get(key) is not None):
                csvreader.writerow([key, tags_before[key], tags_after[key]])

def users_analysis(paths, analysis_file):

    for path in paths:
        unique_users = []
        questions_users = {}
        answers_users = {}

        with open(path + "questions.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if row[8] != "" and row[8] != None:
                    if not row[8] in unique_users:
                        unique_users.append(row[8])

                    if row[8] in questions_users:
                        aux = questions_users[row[8]]
                        questions_users.update({row[8]: (aux + 1)})
                    else:
                        questions_users[row[8]] = 1

        with open(path + "answers.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if row[4] != "" and row[4] != None:
                    if not row[4] in unique_users:
                        unique_users.append(row[4])

                    if row[4] in answers_users:
                        aux = answers_users[row[4]]
                        answers_users.update({row[4]: (aux + 1)})
                    else:
                        answers_users[row[4]] = 1

        users_without_questions = 0
        users_without_answers = 0
        users_without_questions_answers = 0
        users_with_questions_answers = 0
        print("Time: "+str(path.split("/")[-1]))
        print("Unique Users : " + str(len(unique_users)))

        report_file = path + analysis_file + "_analysis.csv"
        for user in unique_users:
            if questions_users.get(user) != None:
                if answers_users.get(user) != None:
                    add_value_result_file(report_file, user, questions_users.get(user), answers_users.get(user), questions_users.get(user) / answers_users.get(user))
                    users_with_questions_answers += 1
                else:
                    add_value_result_file(report_file, user, questions_users.get(user), "NoAnswers", "-")
                    users_without_answers += 1
            elif answers_users.get(user) != None:
                 add_value_result_file(report_file, user, "NoQuestions", answers_users.get(user), "-")
                 users_without_questions += 1
            else:
                add_value_result_file(report_file, user, "NoQuestions", "NoAnswers", "-")
                users_without_questions_answers += 1

        print("Users without questions - "+str(users_without_questions))
        print("Users without answers - " + str(users_without_answers))
        print("Users without questions/answers - " + str(users_without_questions_answers))
        print("Users with questions/answers - " + str(users_with_questions_answers))

def create_file(directory, file_name, values):
    if not os.path.exists(directory+file_name+".csv"):
        with open(directory+file_name+".csv", 'w') as f:
            csvreader = csv.writer(f)
            csvreader.writerow(["user"])

    with open(directory+file_name+".csv", 'a') as f:
        csvreader = csv.writer(f)
        for value in values:
            csvreader.writerow([value])

def create_file_with_different_fields(directory, file_name, values):
    if not os.path.exists(directory+file_name+"-general-questions.csv"):
        with open(directory+file_name+"-general-questions.csv", 'w') as f:
            csvreader = csv.writer(f)
            csvreader.writerow(["user", "number_questions", "number_answers","account_before_chatgpt"])

    with open(directory+file_name+"-general-questions.csv", 'a') as f:
        csvreader = csv.writer(f)
        for value in values:
            csvreader.writerow([value[0], value[1], value[2], value[3]])

def add_value_result_file(file, user, questions, answers, metric):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            csvreader = csv.writer(f)
            csvreader.writerow(["user", "questions", "answers", "metric (questions/answers)"])

    with open(file, 'a') as f:
        csvreader = csv.writer(f)
        csvreader.writerow([user, questions, answers, metric])

def understand_missing_users(user_file, user_analysis_file):
    users_after = []
    with open(user_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            users_after.append(row[0])

    users_new = []
    with open(user_analysis_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            users_new.append(row[0])

    print(len(users_after))
    print(len(users_new))
    print(len(set(users_after).difference(set(users_new))))
    print(set(users_after).difference(set(users_new)))

def distribution_questions_answers_by_user(files, directory):
    values = []
    less_than_one = []
    greater_than_one = []
    greater_than_two = []
    users_no_questions = [[],[]]
    users_no_answers = [[], []]
    users_questions_answers = [[], []]

    users = [[],[]]

    index = 0
    for one_file in files:
        with open(one_file + "user_analysis.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                users[index].append(row[0])
                if row[3] != "-":
                    value = float(row[3])
                    values.append(value)

                    if value < 1:
                        less_than_one.append(value)
                    elif value < 2:
                        greater_than_one.append(value)
                    else:
                        greater_than_two.append(value)

                if row[1] == "NoQuestions":
                    users_no_questions[index].append(row[0])
                elif row[2] == "NoAnswers":
                    users_no_answers[index].append((row[0]))
                else:
                    users_questions_answers[index].append(row[0])

        matplotlib.pyplot.clf()
        #plt.boxplot(values)
        #plt.show()

        print("Cases - Less Than One - "+str(len(less_than_one)))
        print("Cases - Greater Than One - " + str(len(greater_than_one)))
        print("Cases - Greater Than Two - " + str(len(greater_than_two)))

        index += 1


    print(len(users[0]))
    print(len(users[1]))
    print("Difference between users before and after - "+str(len(set(users[0]) - set(users[1]))))
    print("Intersection between users before and after - " + str(len(set(users[0]).intersection(set(users[1])))))
    print("Intersection between users before and after - " + str(len(set(users[1]).intersection(set(users[0])))))

    print("Users No Answers: before - "+str(len(users_no_answers[0]))+" # after - "+str(len(users_no_answers[1])))
    print("Inactive Users with No Answers (before/after) - " + str(
        len(set(users_no_answers[0]).difference(set(users_no_answers[1])))))
    create_file(directory,"inactive-askers",set(users_no_answers[0]).difference(set(users_no_answers[1])))
    print("New Users with No Answers (before/after) - " + str(
        len(set(users_no_answers[1]).difference(set(users_no_answers[0])))))
    create_file(directory, "new-askers", set(users_no_answers[1]).difference(set(users_no_answers[0])))
    print("Intersection between Users with No Answers (before/after) - " + str(
        len(set(users_no_answers[0]).intersection(set(users_no_answers[1])))))

    print("Users No Questions: before - " + str(len(users_no_questions[0])) + " # after - " + str(len(users_no_questions[1])))
    print("Inactive Users with No Questions (before/after) - " + str(
        len(set(users_no_questions[0]).difference(set(users_no_questions[1])))))
    create_file(directory, "inactive-respondents", set(users_no_questions[0]).difference(set(users_no_questions[1])))
    print("New Users with No Questions (before/after) - " + str(
        len(set(users_no_questions[1]).difference(set(users_no_questions[0])))))
    create_file(directory, "new-respondents", set(users_no_questions[1]).difference(set(users_no_questions[0])))
    print("Intersection between Users with No Questions (before/after) - " + str(
        len(set(users_no_questions[0]).intersection(set(users_no_questions[1])))))

    print("Users Questions/Answers: before - " + str(len(users_questions_answers[0])) + " # after - " + str(
        len(users_questions_answers[1])))
    print("Inactive Users with Questions/Answers (before/after) - " + str(
        len(set(users_questions_answers[0]).difference(set(users_questions_answers[1])))))
    print("New Users with Questions/Answers (before/after) - " + str(
        len(set(users_questions_answers[1]).difference(set(users_questions_answers[0])))))
    print("Intersection between Users with Questions/Answers (before/after) - " + str(
        len(set(users_questions_answers[0]).intersection(set(users_questions_answers[1])))))
    create_file(directory, "new-respondents-QA", set(users_questions_answers[1]).difference(set(users_questions_answers[0])))

def analysis_user_commentors(files):

    users = [[],[]]

    index = 0
    for one_file in files:
        with open(one_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if not row[0] in users[index]:
                    users.append(row[0])

        index += 1


    print("Users - Commentors - "+str(len(users[0]))+" # after - "+str(len(users[1])))
    print("Inactive Commentors (before/after) - " + str(
        len(set(users[0]).difference(set(users[1])))))
    print("New Commentors (before/after) - " + str(
        len(set(users[1]).difference(set(users[0])))))
    print("Intersection between Commentors (before/after) - " + str(
        len(set(users[0]).intersection(set(users[1])))))


def distribution_commentors(files, directory):
    users_comments = [[], []]

    index = 0
    for one_file in files:
        with open(one_file + "comments.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if not row[5] in users_comments[index] and row[5] != "" and row[5] != None and row[5] != "-1":
                    users_comments[index].append(row[5])

        index += 1

    create_file(directory, "commentors-before", users_comments[0])
    create_file(directory, "commentors-after", users_comments[1])

    print("Users Comments Before - "+str(len(users_comments[0]))+" # After - "+str(len(users_comments[1])))
    print("Inactive Users (before/after) - " + str(
        len(set(users_comments[0]).difference(set(users_comments[1])))))
    print("New Users (before/after) - " + str(
        len(set(users_comments[1]).difference(set(users_comments[0])))))
    print("Intersection between Users (before/after) - " + str(
        len(set(users_comments[0]).intersection(set(users_comments[1])))))
    create_file(directory, "new-commentors", set(users_comments[1]).difference(set(users_comments[0])))

def check_difference_numbers_new_old_users(analysis_file, directory, file_name, general_directory):
    users = {}
    with open(analysis_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            questions = 0
            answers = 0
            if row[1] != "NoQuestions":
                questions = row[1]

            if row[2] != "NoAnswers":
                answers = row[2]

            users[row[0]] = [questions, answers]

    report = []
    with open(directory + file_name + ".csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            if row[0] in users:
                values = users[row[0]]
                report.append([row[0], values[0], values[1], row[3]])

    create_file_with_different_fields(general_directory, file_name, report)

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
            csvreader.writerow([user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]])

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

def run_analysis(target_directory, file):
    SITE = StackAPI('stackoverflow', key=config('KEY-STACK-TWO'))
    chatgpt_release_date = datetime(2022, 11, 30)
    selected_users = read_users(target_directory + file + ".csv")

    split_users = [selected_users[i:i+100] for i in range(0, len(selected_users), 100)]

    before_chatgpt = 0
    after_chatgpt = 0

    for selected_user in split_users:
        users = SITE.fetch(endpoint='users', ids = selected_user)

        for user in users['items']:
            before_release = datetime.fromtimestamp(user['creation_date']) < chatgpt_release_date
            if (before_release):
                before_chatgpt += 1
            else:
                after_chatgpt += 1

            user = [user['user_id'], user['reputation'], datetime.fromtimestamp(user['creation_date']), before_release,
                    datetime.fromtimestamp(user['last_access_date']), user['badge_counts']['bronze'],
                    user['badge_counts']['silver'], user['badge_counts']['gold']]
            save_user(target_directory, file+"-analysis", user)

    print("Before - " + str(before_chatgpt))
    print("After - " + str(after_chatgpt))

def main(directory):
    files = [directory + "before/", directory + "after/"]
    directory = directory + "general/"

    analysis_question_file = "questions"
    analysis_answer_file = "answers"
    analysis_comments_file = "comments"
    analysis_user_file = "user"
    analysis_tag_file = "tags"
    distribution_answer_by_day(files, analysis_answer_file)
    distribution_question_by_day(files, analysis_question_file)
    distribution_comments_by_day(files, analysis_comments_file)
    distribution_tags(files, analysis_tag_file, directory)


    users_analysis(files, analysis_user_file)
    distribution_questions_answers_by_user(files, directory)
    distribution_commentors(files, directory)
    run_analysis(directory, "new-respondents")
    run_analysis(directory, "new-askers")
    run_analysis(directory, "new-commentors")
    run_analysis(directory, "new-users")
    check_difference_numbers_new_old_users(files[1] + "user_analysis.csv", directory, "new-respondents-analysis", directory)
    #check_difference_numbers_new_old_users(files[1] + "user_analysis.csv", directory, "new-askers-analysis", directory)
    #understand_missing_users("/home/leuson/PycharmProjects/chat-stack/user-investigation.py", "/home/leuson/Downloads/finalOutput/general/new-askers-analysis.csv")
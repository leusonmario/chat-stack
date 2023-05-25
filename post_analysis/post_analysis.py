import csv
import os
from datetime import datetime
from time import sleep

import matplotlib
import matplotlib.pyplot as pyplot

def distribution_answer_by_day(files, analysis_file):
    week_day = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
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
    week_day = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
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
    week_day = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    for one_file in files:
        dates = {}
        with open(one_file + analysis_file + ".csv", 'r') as file:
            reader = csv.reader(file)
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

def users_analysis(paths):

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
        print("Unique Users : " + str(len(unique_users)))

        """for user in unique_users:
            if questions_users.get(user) != None:
                if answers_users.get(user) != None:
                    add_value_result_file(report_file, user, questions_users.get(user), answers_users.get(user), questions_users.get(user) / answers_users.get(user))
                else:
                    add_value_result_file(report_file, user, questions_users.get(user), "NoAnswers", "-")
                    users_without_answers += 1
            elif answers_users.get(user) != None:
                 add_value_result_file(report_file, user, "NoQuestions", answers_users.get(user), "-")
                 users_without_questions += 1
            else:
                add_value_result_file(report_file, user, "NoQuestions", "NoAnswers", "-")
                users_without_questions_answers += 1"""

        print("Users without questions - "+str(users_without_questions))
        print("Users without answers - " + str(users_without_answers))
        print("Users without questions/answers - " + str(users_without_questions_answers))

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
    if not os.path.exists(directory+file_name+".csv"):
        with open(directory+file_name+".csv", 'w') as f:
            csvreader = csv.writer(f)
            csvreader.writerow(["user", "number_questions", "number_answers","account_before_chatgpt"])

    with open(directory+file_name+".csv", 'a') as f:
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
    print("Difference between users before and before - " + str(len(set(users[0]).intersection(set(users[1])))))
    print("Difference between users after and before - " + str(len(set(users[1]).intersection(set(users[0])))))

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

def check_difference_numbers_new_old_users(analysis_file, all_active_users, directory):
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
    with open(all_active_users, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            if row[0] in users:
                values = users[row[0]]
                report.append([row[0], values[0], values[1], row[3]])

    create_file_with_different_fields(directory, "new-respondents-general-questions", report)

if __name__ == '__main__':
    directory = "/home/leuson/Downloads/finalOutput/general/"
    files = [
        "/home/leuson/Downloads/finalOutput/before/", "/home/leuson/Downloads/finalOutput/after/"]
    analysis_question_file = "questions"
    analysis_answer_file = "answers"
    analysis_comments_file = "comments"
    distribution_answer_by_day(files, analysis_answer_file)
    distribution_question_by_day(files, analysis_question_file)
    distribution_comments_by_day(files, analysis_comments_file)


    users_analysis(files)
    distribution_questions_answers_by_user(files, directory)
    distribution_commentors(files, directory)
    check_difference_numbers_new_old_users("/home/leuson/Downloads/finalOutput/after/user_analysis.csv", "/home/leuson/Downloads/finalOutput/general/new-respondents-analysis.csv", directory)
    understand_missing_users("/home/leuson/PycharmProjects/chat-stack/user-investigation.py", "/home/leuson/Downloads/finalOutput/general/new-askers-analysis.csv")
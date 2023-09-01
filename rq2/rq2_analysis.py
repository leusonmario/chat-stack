import csv
import os
from time import sleep

from analysis.llm_answer_analysis import GeneratedAnswerAnalysis
from input.sample_handler import SampleHandler
from rq2.chatgpt import ChatGPT


#from llm.request import Request


def read_unanswered_questions(file):
    answers = {}
    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            answers[row[0]] = [row[8], row[15]]

    return answers

def read_generated_answers(file):
    answers = {}
    question_ids = []
    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            answers[row[0]] = [row[0], row[1], row[2]]
            question_ids.append(row[0])

    return answers, question_ids

def get_related_posts(file, question_ids):
    related_questions = {}
    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            if (row[0] in question_ids):
                if related_questions.get(row[0]) is not None:
                    related_questions[row[0]].append(row[1])
                else:
                    related_questions[row[0]] = [row[1]]

    selected_answers = {}
    for key in related_questions.keys():
        selected_answers[key] = sorted(related_questions.get(key), key=lambda x: x[2], reverse=True)#return only one [:1]

    return selected_answers

def get_related_posts_answers(file, question_ids):
    answers = {}
    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            answers[row[3]] = [row[0], row[3], row[8]]

    selected_answers = {}
    for key in question_ids.keys():
        for related_question_id in question_ids.get(key):
            if answers.get(related_question_id) is not None:
                if selected_answers.get(key) is None:
                    selected_answers[key] = [answers.get(related_question_id)]
                else:
                    selected_answers[key].append(answers.get(related_question_id))
                #selected_answers[key] = answers.get(question_ids.get(key)[0])

    return selected_answers

def get_question_ids(questions):
    ids = []
    for question in questions:
        ids.append(question[0].replace("'",""))

    return ids

def get_answers(id, related_questions):
    for key in related_questions.keys():
        if id.replace("'","") == key:
            return related_questions.get(key)

    return None

def read_get_tags(file):
    tags = {}

    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            if tags.get(row[1]) is not None:
                tags[row[1]].append(row[0])
            else:
                tags[row[1]] = [row[0]]

    return tags

def read_related_tags(file):
    tags = {}

    with open(file, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            individual_tags = []
            for tag in row[16].split("><"):
                individual_tags.append(tag.replace("<","").replace(">",""))

            tags[row[0]] = individual_tags

    return tags

def check_for_tag_similarity(question_tags, related_question_tags):
    return any(element in question_tags for element in related_question_tags)

def get_closest_related_question(question_tags, related_tags, related_questions):
    selected_question = None
    match = 0
    for related_question in related_questions:
        if sum(element in question_tags for element in related_tags.get(related_question[1])) > match:
            selected_question = related_question
            match = sum(element in question_tags for element in related_tags.get(related_question[1]))

    return selected_question

def get_tags_as_string(tags):
    string_tags = ""
    i = 1
    for tag in tags:
        string_tags += str(tag)
        if (len(tags) > 1 and i < len(tags)):
            string_tags += ", "
        i += 1

    return string_tags

def create_generated_answer_output_file(report_path, type):
    if not os.path.exists(report_path+"/"+type+"/reliability_analysis.csv"):
        with open(report_path+"/"+type+"/reliability_analysis.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'question_title', 'question_description', 'original_answer',
                                'generated_answer', 'cosine_metric', 'tags'])

def save_generated_answer(report_path, question_id, question, description, original_answer, generated_answer, cosine_metric, tags, type):
    create_generated_answer_output_file(report_path, type)
    if os.path.exists(report_path + "/" + type + "/reliability_analysis.csv"):
        with open(report_path + "/" + type + "/reliability_analysis.csv", 'a') as file:
            csvreader = csv.writer(file)
            csvreader.writerow([question_id, question, description, original_answer, generated_answer, cosine_metric, tags])

def main(questions_file, answers_file, number_questions, tags_file, report_directory, time):

    sample = SampleHandler()
    selected_questions = sample.select_sample(questions_file,
                               answers_file, 3, number_questions)

    tags = read_get_tags(tags_file)

    request = ChatGPT()
    analysis = GeneratedAnswerAnalysis('all-MiniLM-L6-v2')
    for question in selected_questions:
        try:
            original_answer = sample.answers.get(question[9])

            if (original_answer is not None):
                generated_answer = request.ask_for_explanation(question[1], question[2], get_tags_as_string(tags.get(question[0])))
                cosine_metric = analysis.check_cosine_metric(original_answer, generated_answer)
                save_generated_answer(report_directory, question[0], question[1], question[2], original_answer, generated_answer,
                                                        cosine_metric.item(), get_tags_as_string(tags.get(question[0])), time)
                sleep(20)
        except Exception as e:
            print(e)
            print("Error")

if __name__ == '__main__':
    main("/home/leuson/Downloads/finalOutput/after/questions.csv", "/home/leuson/Downloads/finalOutput/after/answers.csv", 1,
         "/home/leuson/Downloads/finalOutput/after/tags.csv", "/home/leuson/Downloads/finalOutput/", 'after')
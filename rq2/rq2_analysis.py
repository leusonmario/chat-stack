import csv
import os
from time import sleep

from analysis.llm_answer_analysis import GeneratedAnswerAnalysis
from input.sample_handler import SampleHandler
from rq2.chatgpt import ChatGPT
from rq2.llama import Llama
from rq2.request_llm import Request_LLM


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

def get_tags_as_string(tags):
    string_tags = ""
    i = 1
    for tag in tags:
        string_tags += str(tag)
        if (len(tags) > 1 and i < len(tags)):
            string_tags += ", "
        i += 1

    return string_tags

def create_generated_sample_file(report_path, type):
    if not os.path.exists(report_path + "/" + type + "/final_sample.csv"):
        with open(report_path + "/" + type + "/final_sample.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'question_title', 'question_description', 'score'])

def create_generated_answer_output_file(report_path, type):
    if not os.path.exists(report_path + "/" + type + "/reliability_analysis.csv"):
        with open(report_path + "/" + type + "/reliability_analysis.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'question_title', 'question_description', 'original_answer',
                                'generated_answer', 'cosine_metric', 'tags'])

def save_generated_answer(report_path, question_id, question, description, original_answer, generated_answer, cosine_metric, tags, type):
    create_generated_answer_output_file(report_path, type)
    if os.path.exists(report_path + "/" + type + "/reliability_analysis.csv"):
        with open(report_path + "/" + type + "/reliability_analysis.csv", 'a') as file:
            csvreader = csv.writer(file)
            csvreader.writerow([question_id, question, description, original_answer, generated_answer, cosine_metric, tags])

def save_sample(report_path, type, questions):
    create_generated_sample_file(report_path, type)
    if os.path.exists(report_path + "/" + type + "/final_sample.csv"):
        with open(report_path + "/" + type + "/final_sample.csv", 'a') as file:
            csvreader = csv.writer(file)
            for question in questions:
                csvreader.writerow(
                    [question[0], question[1], question[2], question[3]])

def main(questions_file, answers_file, number_questions, tags_file, report_directory, time):

    sample = SampleHandler()
    selected_questions = sample.select_sample(questions_file,
                               answers_file, 3, number_questions)

    tags = read_get_tags(tags_file)

    save_sample(report_directory, time, selected_questions)
    chatGPT = ChatGPT()
    llama = Llama()
    request = Request_LLM(chatGPT)
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
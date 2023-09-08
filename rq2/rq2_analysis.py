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
            csvreader.writerow(['question_id', 'question_title', 'question_description', 'tags', 'score', 'answer_id', 'accepted_answer'])

def create_generated_answer_output_file(report_path, type):
    if not os.path.exists(report_path + "/" + type + "/reliability_analysis.csv"):
        with open(report_path + "/" + type + "/reliability_analysis.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'question_title', 'question_description', 'original_answer',
                                'generated_answer', 'cosine_metric', 'tags', 'llm', 'version'])

def save_generated_answer(report_path, question_id, question, description, original_answer, generated_answer, cosine_metric, tags, type, llm, version):
    create_generated_answer_output_file(report_path, type)
    if os.path.exists(report_path + "/" + type + "/reliability_analysis.csv"):
        with open(report_path + "/" + type + "/reliability_analysis.csv", 'a') as file:
            csvreader = csv.writer(file)
            csvreader.writerow([question_id, question, description, original_answer, generated_answer, cosine_metric, tags, llm, version])

def save_sample(report_path, type, questions, tags, sample):
    create_generated_sample_file(report_path, type)
    if os.path.exists(report_path + "/" + type + "/final_sample.csv"):
        with open(report_path + "/" + type + "/final_sample.csv", 'a') as file:
            csvreader = csv.writer(file)
            for question in questions:
                csvreader.writerow(
                    [question[0], question[1], question[2], get_tags_as_string(tags.get(question[0])), question[3], question[9], sample.answers.get(question[9])])

def get_random_sample(questions_file, answers_file, tags_file, number_questions, report_directory, time):
    sample = SampleHandler()
    selected_questions = sample.select_sample(questions_file,
                                              answers_file, 3, number_questions)

    tags = read_get_tags(tags_file)

    save_sample(report_directory, time, selected_questions, tags, sample)

    return sample

def read_sample(report_directory, time):
    selected_questions = []

    with open(report_directory + "/" + time + "/final_sample.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            selected_questions.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

    return selected_questions

def run_request(request, question, cosine, report_directory, time):
    try:
        original_answer = question[6]

        if (original_answer is not None):
            generated_answer = request.ask_for_explanation(question[1], question[2], question[3])
            cosine_metric = cosine.check_cosine_metric(original_answer, generated_answer)
            save_generated_answer(report_directory, question[0], question[1], question[2], original_answer,
                                  generated_answer, cosine_metric.item(), question[3], time,
                                  request.ll_model.model_name,
                                  request.ll_model.llm_version)
            sleep(20)
    except Exception as e:
        print(e)
        print("Error")

def run_requests_for_llms(selected_questions, report_directory, time):
    chatGPT = ChatGPT("chat-gpt-3.5", "gpt-3.5-turbo")
    llama = Llama("llama", "meta-llama/Llama-2-7b-chat-hf")
    request = Request_LLM(chatGPT)
    analysis = GeneratedAnswerAnalysis('all-MiniLM-L6-v2')
    for question in selected_questions:
        run_request(request, question, analysis, report_directory, time)
        request.ll_model_set(llama)
        run_request(request, question, analysis, report_directory, time)

def main(questions_file, answers_file, number_questions, tags_file, report_directory, time):

    get_random_sample(questions_file, answers_file, tags_file, number_questions, report_directory, time)

    selected_questions = read_sample(report_directory, time)

    run_requests_for_llms(selected_questions, report_directory, time)

if __name__ == '__main__':
    main("/home/leuson/Downloads/finalOutput/after/questions.csv", "/home/leuson/Downloads/finalOutput/after/answers.csv", 1,
         "/home/leuson/Downloads/finalOutput/after/tags.csv", "/home/leuson/Downloads/finalOutput/", 'after')
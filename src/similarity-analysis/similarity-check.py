import csv
import json
import os
from time import sleep

from chatgpt import ChatGPT
from llama import Llama

def create_generated_sample_file(report_path):
    if not os.path.exists(report_path + "/similarity-analysis-HL_final_gpt.csv"):
        with open(report_path + "/similarity-analysis-HL_final_gpt.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'manual_analysis', 'similarity', 'llm', 'version'])

def save_output_file(report_path, outputs):
    create_generated_sample_file(report_path)
    if os.path.exists(report_path + "/similarity-analysis-HL_final_gpt.csv"):
        with open(report_path + "/similarity-analysis-HL_final_gpt.csv", 'a') as file:
            csvreader = csv.writer(file)
            for output in outputs:
                csvreader.writerow(output)

def check_analysis_done_for_llm(llm, current_status):
    for value in current_status:
        if value == llm:
            return True
    return False

def read_previous_analysis():
    previous_analysis = {}

    with open("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity-analysis/similarity-analysis-HL_final_gpt.csv", 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            if previous_analysis.get(row[0]) is None:
                previous_analysis[row[0]] = [row[4]]
            elif check_analysis_done_for_llm(row[4], previous_analysis.get(row[0])) is False:
                previous_analysis[row[0]].append(row[4])

    return previous_analysis


def main(file_questions, report_path):
    chatGPT = ChatGPT("chat-gpt-3.5", "gpt-3.5-turbo")
    previous_analysis = read_previous_analysis()
    with open(file_questions, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            if previous_analysis.get(row[0]) is None or check_analysis_done_for_llm(row[8], previous_analysis.get(
                    row[0])) is False:
                output_file = []
                try:
                    similarity = json.loads(chatGPT.ask_for_similarity_analysis(row[3], row[4], row[6]))['similarity']
                    output_file.append([row[0], row[5], similarity, row[7], row[8]])
                    save_output_file(report_path, output_file)
                except Exception as e:
                    print(e)
                    print("ERROR")

if __name__ == '__main__':
    main("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity-analysis/sample/similarity-analysis.csv", "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity-analysis")
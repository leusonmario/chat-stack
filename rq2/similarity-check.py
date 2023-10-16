import csv
import json
import os
from time import sleep

from rq2.chatgpt import ChatGPT
from rq2.llama import Llama

def create_generated_sample_file(report_path):
    if not os.path.exists(report_path + "/similarity_analysis.csv"):
        with open(report_path + "/similarity_analysis.csv", 'w') as file:
            csvreader = csv.writer(file)
            csvreader.writerow(['question_id', 'manual_analysis', 'similarity', 'llm', 'version'])

def save_output_file(report_path, outputs):
    create_generated_sample_file(report_path)
    if os.path.exists(report_path + "/similarity_analysis.csv"):
        with open(report_path + "/similarity_analysis.csv", 'a') as file:
            csvreader = csv.writer(file)
            for output in outputs:
                csvreader.writerow(output)


def main(file_questions, report_path):
    chatGPT = ChatGPT("chat-gpt-3.5", "gpt-3.5-turbo")

    with open(file_questions, 'r') as questions_file:
        csvreader = csv.reader(questions_file)
        next(csvreader)
        for row in csvreader:
            output_file = []
            try:
                similarity = json.loads(chatGPT.ask_for_similarity_analysis(row[4], row[5], row[6]))['similarity']
                output_file.append([row[0], row[3], similarity, row[7], row[8]])
                save_output_file(report_path, output_file)
            except Exception:
                print("ERROR")

if __name__ == '__main__':
    main("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity_analysis.csv", "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity_analysis")
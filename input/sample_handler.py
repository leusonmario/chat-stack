import csv
import re

import torch

from analysis.llm_answer_analysis import GeneratedAnswerAnalysis
from llm.request import Request
from output_generation.output_generator import OutputGenerator


class SampleHandler:

   def __init__(self):
      self.answers = {}

   def _remove_tags(self, text):
      return re.sub('<.*?>', '', text)

   def compute_anwers(self, answers_file, accepted_answers):
      with open(answers_file, 'r') as file:
         csvreader = csv.reader(file)
         next(csvreader)
         for row in csvreader:
            if (row[0] in accepted_answers):
               self.answers[row[0]] = self._remove_tags(row[1])

   def select_sample(self, questions_file, answers_file, requirement, number_elements):
      questions = []
      accepted_answers = []
      i = 0
      with open(questions_file, 'r') as questions_file:
         csvreader = csv.reader(questions_file)
         next(csvreader)
         for row in csvreader:
            if (row[9] != None and row[9] != ""):
               questions.append([row[0],row[1],self._remove_tags(row[2]),row[3],row[4],row[5],row[6],row[7],row[8],row[9]])
               accepted_answers.append(row[9])

      selected_questions = sorted(questions, key=lambda x: x[requirement], reverse=True)[:number_elements]
      accepted_answers_ids = [sublist[9] for sublist in selected_questions]

      self.compute_anwers(answers_file, accepted_answers_ids)
      return selected_questions

#Add function that reads all the answers
#Add function that based on the answer id (accepted answer from question), it returns the answer
#Add answer that join the required question information (title, body, etc) with the answer accepted

"""sample = SampleHandler()
report_directory = "/home/leuson/Downloads/finalOutput/"
output_generation = OutputGenerator(report_directory)

aux = sample.select_sample("/home/leuson/Downloads/finalOutput/after/questions.csv", "/home/leuson/Downloads/finalOutput/after/answers.csv", 3, 5)
request = Request()
analysis = GeneratedAnswerAnalysis('all-MiniLM-L6-v2')
for question in aux:
   generated_answer = request.ask_for_explanation(question[1], question[2])
   original_answer = sample.answers.get(question[9])
   cosine_metric = analysis.check_cosine_metric(original_answer, generated_answer)
   output_generation.save_generated_answer(question[0], original_answer, generated_answer['choices'][0]['text'], cosine_metric.item(), 'after')
   
"""
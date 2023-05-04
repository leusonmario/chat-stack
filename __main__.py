import csv
import os

from analysis.answer_analysis import AnswerAnalysis
from analysis.comment_analysis import CommentAnalysis
from analysis.question_analysis import QuestionAnalysis
from analysis.tag_analysis import TagAnalysis
from output_generation.output_generator import OutputGenerator
from stack.answer import Answer
from stack.comment import Comment
from stack.question import Question

def main():
    questions_ids = []
    questions = []
    answers_ids = []
    answers = []

    target_directory = "/home/leuson/Downloads/aux-teste/"
    report_directory = "/home/leuson/Downloads/output/"
    target_directory_posts = target_directory+"posts/"
    target_directory_comments = target_directory + "comments/"

    files = os.listdir(target_directory_posts)
    for file_csv in files:
        with open(target_directory_posts+file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] == '1'):
                   questions.append(Question(row))
                   questions_ids.append(row[0])

    output_generation = OutputGenerator(report_directory)


    for question in questions:
        output_generation.save_question(question)
        for tag in question.tags:
            output_generation.save_tag(tag)

    question_analysis = QuestionAnalysis(questions, report_directory)
    question_analysis.general_data_analysis()
    question_analysis.generate_bar_chart_user_questions()
    question_analysis.generate_line_chart_questions_over_time()

    tag_analysis = TagAnalysis(questions, report_directory)
    tag_analysis.generate_word_cloud()
    tag_analysis.generate_bar_chart_tags()
    tag_analysis.generate_tag_usage_frequency()

    questions = []

    for file_csv in files:
        with open(target_directory_posts+file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] == '2' and row[3] in questions_ids):
                    answers.append(Answer(row))
                    answers_ids.append(row[0])

    for answer in answers:
        output_generation.save_answer(answer)

    answer_analysis = AnswerAnalysis(answers, report_directory)
    answer_analysis.general_data_analysis();
    answer_analysis.generate_bar_chart_user_answers()
    answer_analysis.generate_line_chart_answers_over_time()

    answers = []

    files = os.listdir(target_directory_comments)

    comments = []

    for file_csv in files:
        with open(target_directory_comments+file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] in questions_ids or row[1] in answers_ids):
                   comments.append(Comment(row))

    for comment in comments:
        output_generation.save_comment(comment)

    comment_analysis = CommentAnalysis(comments, report_directory)
    comment_analysis.general_data_analysis()
    comment_analysis.generate_bar_chart_user_answers()
    comment_analysis.generate_line_chart_answers_over_time()

if __name__ == '__main__':
    main()
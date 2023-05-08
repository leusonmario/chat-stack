import csv
import os

from analysis.answer_analysis import AnswerAnalysis
from analysis.comment_analysis import CommentAnalysis
from output_generation.general_analysis import GeneralAnalysis
from analysis.question_analysis import QuestionAnalysis
from analysis.tag_analysis import TagAnalysis
from output_generation.output_generator import OutputGenerator
from stack.answer import Answer
from stack.comment import Comment
from stack.question import Question

def main():

    questions = [[],[]]
    questions_ids = [[],[]]
    answers = [[],[]]
    answers_ids = [[],[]]
    comments = [[],[]]
    analysis_req = ["before","after"]

    target_directory = ["/home/leuson/Downloads/teste/data/data-before/", "/home/leuson/Downloads/teste/data/data-after/"]
    report_directory = "/home/leuson/Downloads/teste/output/"

    output_generation = OutputGenerator(report_directory)
    index = 0
    general_analysis = [None,None]

    for target_directory_entry in target_directory:
        general_analysis[index] = GeneralAnalysis(report_directory)
        target_directory_posts = target_directory_entry+"posts/"
        target_directory_comments = target_directory_entry + "comments/"

        questions[index], questions_ids[index] = get_questions(target_directory_posts)
        save_questions(output_generation, questions[index], analysis_req[index])
        general_analysis[index].add_new_metric_value("Questions - "+analysis_req[index], len(questions[index]))

        question_analysis = QuestionAnalysis(questions[index], report_directory+analysis_req[index])
        question_analysis.general_data_analysis()
        general_analysis[index].add_new_metric_value("Answered Questions - " + analysis_req[index],
                                              len(question_analysis.answered_questions))
        general_analysis[index].add_new_metric_value("Accepted Answered Questions - " + analysis_req[index],
                                              len(question_analysis.accepted_answers_for_questions))
        general_analysis[index].add_new_metric_value("Unanswered Questions - " + analysis_req[index],
                                              len(question_analysis.unanswered_questions))
        general_analysis[index].add_new_metric_value("Unique Users (Questioners) - " + analysis_req[index],
                                              len(question_analysis.question_users))
        question_analysis.generate_bar_chart_user_questions()
        question_analysis.generate_line_chart_questions_over_time()

        tag_analysis = TagAnalysis(questions[index], report_directory+analysis_req[index])
        tag_analysis.generate_word_cloud()
        tag_analysis.generate_bar_chart_tags()
        tag_analysis.generate_tag_usage_frequency()
        general_analysis[index].add_new_metric_value("Unique Tags - "+analysis_req[index], len(tag_analysis.tags))

        answers[index], answers_ids[index] = get_answers(questions_ids[index], target_directory_posts)
        save_answers(answers[index], output_generation, analysis_req[index])

        answer_analysis = AnswerAnalysis(answers[index], report_directory+analysis_req[index])
        answer_analysis.general_data_analysis()
        general_analysis[index].add_new_metric_value("Answers - " + analysis_req[index], len(answer_analysis.answers))
        general_analysis[index].add_new_metric_value("Unique Users (Respondents) - " + analysis_req[index], len(answer_analysis.answer_users))
        answer_analysis.generate_bar_chart_user_answers()
        answer_analysis.generate_line_chart_answers_over_time()

        comments[index] = get_comments(answers_ids[index], questions_ids[index], target_directory_comments)
        save_comments(comments[index], output_generation, analysis_req[index])

        comment_analysis = CommentAnalysis(comments[index], report_directory+analysis_req[index])
        comment_analysis.general_data_analysis()
        general_analysis[index].add_new_metric_value("Comments - " + analysis_req[index], len(comment_analysis.comments))
        general_analysis[index].add_new_metric_value("Unique Users (Commentors) - " + analysis_req[index],
                                                     len(answer_analysis.answer_users))
        comment_analysis.generate_bar_chart_user_answers()
        comment_analysis.generate_line_chart_answers_over_time()

        index += 1


def save_comments(comments, output_generation, type):
    for comment in comments:
        output_generation.save_comment(comment, type)

def get_comments(answers_ids, questions_ids, target_directory_comments):
    comments = []
    files = os.listdir(target_directory_comments)
    for file_csv in files:
        with open(target_directory_comments + file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] in questions_ids or row[1] in answers_ids):
                    comments.append(Comment(row))

    return comments


def save_answers(answers, output_generation, type):
    for answer in answers:
        output_generation.save_answer(answer, type)


def get_answers(questions_ids, target_directory_posts):
    answers = []
    answers_ids = []
    files = os.listdir(target_directory_posts)

    for file_csv in files:
        with open(target_directory_posts + file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] == '2' and row[3] in questions_ids):
                    answers.append(Answer(row))
                    answers_ids.append(row[0])

    return answers, answers_ids


def save_questions(output_generation, questions, type):
    for question in questions:
        output_generation.save_question(question, type)
        for tag in question.tags:
            output_generation.save_tag(tag, type)


def get_questions(target_directory_posts):
    questions = []
    questions_ids = []
    files = os.listdir(target_directory_posts)

    for file_csv in files:
        with open(target_directory_posts + file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                if (row[1] == '1'):
                    questions.append(Question(row))
                    questions_ids.append(row[0])

    return questions, questions_ids

if __name__ == '__main__':
    main()
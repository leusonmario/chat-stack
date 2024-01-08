import csv
import os

import post_analysis.post_analysis
from analysis.answer_analysis import AnswerAnalysis
from analysis.comment_analysis import CommentAnalysis
from output_generation.general_analysis import GeneralAnalysis
from analysis.question_analysis import QuestionAnalysis
from analysis.tag_analysis import TagAnalysis
from output_generation.output_generator import OutputGenerator
from stack.answer import Answer
from stack.comment import Comment
from stack.question import Question

def main(report_directory, target_directory):

    questions_analysis = [[],[]]
    answers_analysis = [[],[]]
    comments_analysis = [[],[]]
    tags_analysis = [[], []]
    analysis_req = ["before","after"]

    questions_dates = [[],[]]
    questions_values = [[], []]
    tags_dates = [[], []]
    tags_values = [[], []]
    answers_dates = [[], []]
    answers_values = [[], []]
    comments_dates = [[], []]
    comments_values = [[], []]

    output_generation = OutputGenerator(report_directory)
    index = 0
    general_analysis = GeneralAnalysis(report_directory)

    for target_directory_entry in target_directory:
        target_directory_posts = target_directory_entry+"posts/"
        target_directory_comments = target_directory_entry + "comments/"

        questions, questions_ids = get_questions(target_directory_posts)
        save_questions(output_generation, questions, analysis_req[index])
        general_analysis.add_new_metric_value("Questions - "+analysis_req[index], len(questions))

        questions_analysis[index] = QuestionAnalysis(questions, report_directory+analysis_req[index])
        questions_analysis[index].general_data_analysis()
        general_analysis.add_new_metric_value("Answered Questions - " + analysis_req[index],
                                              len(questions_analysis[index].answered_questions))
        general_analysis.add_new_metric_value("Accepted Answered Questions - " + analysis_req[index],
                                              len(questions_analysis[index].accepted_answers_for_questions))
        general_analysis.add_new_metric_value("Unanswered Questions - " + analysis_req[index],
                                              len(questions_analysis[index].unanswered_questions))
        general_analysis.add_new_metric_value("Unique Users (Questioners) - " + analysis_req[index],
                                              len(questions_analysis[index].question_users))
        questions_analysis[index].generate_bar_chart_user_questions()
        questions_dates[index], questions_values[index] = questions_analysis[index].generate_line_chart_questions_over_time()


        tags_analysis[index] = TagAnalysis(questions, report_directory+analysis_req[index])
        tags_analysis[index].generate_word_cloud()
        tags_analysis[index].generate_bar_chart_tags()
        tags_dates[index], tags_values[index] = tags_analysis[index].generate_tag_usage_frequency()
        general_analysis.add_new_metric_value("Unique Tags - "+analysis_req[index], len(tags_analysis[index].tags))

        answers, answers_ids = get_answers(questions_ids, target_directory_posts)
        save_answers(answers, output_generation, analysis_req[index])

        answers_analysis[index] = AnswerAnalysis(answers, report_directory+analysis_req[index])
        answers_analysis[index].general_data_analysis()
        general_analysis.add_new_metric_value("Answers - " + analysis_req[index], len(answers_analysis[index].answers))
        general_analysis.add_new_metric_value("Unique Users (Respondents) - " + analysis_req[index], len(answers_analysis[index].answer_users))
        answers_analysis[index].generate_bar_chart_user_answers()
        answers_dates[index], answers_values[index] = answers_analysis[index].generate_line_chart_answers_over_time()


        comments = get_comments(answers_ids, questions_ids, target_directory_comments)
        save_comments(comments, output_generation, analysis_req[index])

        comments_analysis[index] = CommentAnalysis(comments, report_directory+analysis_req[index])
        comments_analysis[index].general_data_analysis()
        general_analysis.add_new_metric_value("Comments - " + analysis_req[index], len(comments_analysis[index].comments))
        general_analysis.add_new_metric_value("Unique Users (Commentors) - " + analysis_req[index],
                                                     len(comments_analysis[index].comment_users))
        comments_analysis[index].generate_bar_chart_user_comments()
        comments_dates[index], comments_values[index] = comments_analysis[index].generate_line_chart_comments_over_time()

        index += 1

    general_analysis.generate_line_chart_posts_over_time(questions_dates, questions_values, "questions")
    general_analysis.generate_tag_usage_frequency(tags_dates, tags_values)
    general_analysis.generate_line_chart_posts_over_time(answers_dates, answers_values, "answers")
    general_analysis.generate_line_chart_posts_over_time(comments_dates, comments_values, "comments")

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
    target_directory = ["", ""]
    report_directory = ""
    main(report_directory, target_directory)
    post_analysis.post_analysis.main(report_directory)
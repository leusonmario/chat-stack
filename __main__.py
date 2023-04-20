import datetime

from decouple import config
from stackapi import StackAPI
from sentence_transformers import SentenceTransformer, util

from input.date_handler import DateHandler
from output_generation.output_generator import OutputGenerator
from stack.repository import Repository
from stack.stack_request import StackRequest

def main():
    from_date = datetime.datetime(2022, 12, 12)
    until_date = datetime.datetime(2022, 12, 15)
    date_handler = DateHandler(from_date, until_date)

    while(date_handler.is_there_valid_pair_of_days()):
        request = StackRequest('stackoverflow', config('KEY-STACK'), 1)
        questions = request.run_query_question(endpoint='questions', min='100', sort='votes', filter='withbody',
                                               from_date=date_handler.current_starting_date, until_date=date_handler.current_finishing_date)
        repository = Repository()
        output_generation = OutputGenerator()

        for question in questions['items']:
            answers = request.run_query_answers(endpoint='questions/{ids}/answers', ids=[question['question_id']], filter='withbody')
            repository.save_question(question, answers)

        for question in repository.questions:
            output_generation.save_question(question, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for answer in repository.answers:
            output_generation.save_answer(answer, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for user in repository.users:
           output_generation.save_user(user, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for tag in repository.tags:
            output_generation.save_tag(tag, date_handler.current_starting_date.strftime("%b-%d-%Y"))

if __name__ == '__main__':
    main()

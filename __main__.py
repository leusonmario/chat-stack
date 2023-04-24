import datetime

from decouple import config
from stackapi import StackAPI
from sentence_transformers import SentenceTransformer, util

from input.date_handler import DateHandler
from output_generation.output_generator import OutputGenerator
from stack.repository import Repository
from stack.stack_request import StackRequest

def main():
    from_date = datetime.datetime(2022, 11, 12)
    until_date = datetime.datetime(2022, 11, 14)
    date_handler = DateHandler(from_date, until_date)
    last_date = date_handler.current_starting_date

    while(check_current_state(last_date, date_handler.current_finishing_date) or date_handler.is_there_valid_pair_of_days()):
        request = StackRequest('stackoverflow', config('KEY-STACK'), 1)
        questions = request_question(request, last_date, date_handler.current_finishing_date)

        if (len(questions['items']) < 1):
            date_handler.is_there_valid_pair_of_days()
            questions = request_question(request, date_handler.current_starting_date, date_handler.current_finishing_date)

        repository = Repository()
        output_generation = OutputGenerator()

        for question in questions['items']:
            answers = request.run_query_answers(endpoint='questions/{ids}/answers', ids=[question['question_id']], filter='withbody')
            repository.save_question(question, answers)
            if (last_date < datetime.datetime.fromtimestamp(question['creation_date'])):
                last_date = datetime.datetime.fromtimestamp(question['creation_date']) + datetime.timedelta(seconds=1)

        for question in repository.questions:
            output_generation.save_question(question, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for answer in repository.answers:
            output_generation.save_answer(answer, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for user in repository.users:
           output_generation.save_user(user, date_handler.current_starting_date.strftime("%b-%d-%Y"))

        for tag in repository.tags:
            output_generation.save_tag(tag, date_handler.current_starting_date.strftime("%b-%d-%Y"))

def check_current_state(last_date, current_finishing_date):
    if (last_date < current_finishing_date):
        return True
    else:
        return False

def request_question(request, current_last_date, current_finishing_date):

    return request.run_query_question(endpoint='questions', min='100', sort='creation', filter='withbody',
                                           from_date=current_last_date, until_date=current_finishing_date)

if __name__ == '__main__':
    main()

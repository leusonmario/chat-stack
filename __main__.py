from decouple import config
from stackapi import StackAPI
from sentence_transformers import SentenceTransformer, util

from output_generation.output_generator import OutputGenerator
from stack.repository import Repository
from stack.stack_request import StackRequest

def main():
    request = StackRequest('stackoverflow', config('KEY-STACK'), 1)
    questions = request.run_query(endpoint='questions', min='100', sort='votes', filter='withbody')
    repository = Repository()
    output_generation = OutputGenerator()

    for question in questions['items']:
        answers = request.run_querytwo(endpoint='questions/{ids}/answers', ids=[question['question_id']], filter='withbody')
        repository.save_question(question, answers)

    for question in repository.questions:
        output_generation.save_question(question,"123456")

    for answer in repository.answers:
        output_generation.save_answer(answer, "123456")

    for user in repository.users:
       output_generation.save_user(user, "123456")

    for tag in repository.tags:
        output_generation.save_tag(tag, "123456")

if __name__ == '__main__':
    main()

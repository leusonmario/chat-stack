from decouple import config
from stackapi import StackAPI
from sentence_transformers import SentenceTransformer, util

from stack.repository import Repository
from stack.stack_request import StackRequest

def main():
    request = StackRequest('stackoverflow', config('KEY-STACK'), 1)
    questions = request.run_query(endpoint='questions', min='100', sort='votes', filter='withbody')
    repository = Repository()

    for question in questions['items']:
        answers = request.run_querytwo(endpoint='questions/{ids}/answers', ids=[question['question_id']], filter='withbody')
        repository.save_question(question, answers)

if __name__ == '__main__':
    main()

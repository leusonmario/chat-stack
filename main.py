import openai
from decouple import config
from stackapi import StackAPI
from sentence_transformers import SentenceTransformer, util

openai.api_key = config('APIKEY')

SITE = StackAPI('stackoverflow')
SITE.max_pages = 1

# Search for questions
questions = SITE.fetch('questions', tagged='java;junit', min=100, sort='votes', filter='withbody')

selected_question = questions['items'][0]
accepted_answer = []
most_voted_answer = []

answers = SITE.fetch('questions/{ids}/answers', ids=[selected_question['question_id']], filter='withbody', accepted='True')
for answer in answers['items']:
    if answer['is_accepted'] == True:
        accepted_answer = answer
    if (len(most_voted_answer) < 1 or answer['score'] > most_voted_answer['score']):
        most_voted_answer = answer

def generate_prompt(title, body):
    return f""" Please, explain how to fix the problem below. {title} 
     {body}"""

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(selected_question['title'], selected_question['body']),
    temperature=0.6,
    max_tokens=2048
)

model = SentenceTransformer('all-MiniLM-L6-v2')
embedding_accepted_answer_stack = []
embedding_most_voted_answer_stack = []
cosine_scores_accepted_generated = 0
cosine_scores_voted_generated = 0

def put_text_together(text):
    string_final = ""
    for line in text:
        string_final.join(line)
    return string_final

embedding_answer_chatgpt = model.encode([response.choices[0].text], convert_to_tensor=True)

if (len(accepted_answer) > 0):
    embedding_accepted_answer_stack = model.encode([accepted_answer['body']], convert_to_tensor=True)
    cosine_scores_accepted_generated = util.cos_sim(embedding_accepted_answer_stack, embedding_answer_chatgpt)
    print(cosine_scores_accepted_generated[0][0])
if (len(most_voted_answer) > 0):
    embedding_most_voted_answer_stack = model.encode([most_voted_answer['body']], convert_to_tensor=True)
    cosine_scores_voted_generated = util.cos_sim(embedding_most_voted_answer_stack, embedding_answer_chatgpt)
    print(cosine_scores_voted_generated[0][0])

print("QUESTION --- ")
print(selected_question['title'])
print(selected_question['link'])
print("GENERATED ANSWER --- ")
print(response.choices[0].text)
print("ACCEPTED ANSWER")
print(accepted_answer['body'])
print("MOST VOTED ANSWER")
print(most_voted_answer['body'])
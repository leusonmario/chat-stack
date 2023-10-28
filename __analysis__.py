from analysis.llm_answer_analysis import GeneratedAnswerAnalysis
from input.sample_handler import SampleHandler
from llm.request import Request
from output_generation.output_generator import OutputGenerator


def main():
    sample = SampleHandler()
    report_directory = ""
    output_generation = OutputGenerator(report_directory)

    aux = sample.select_sample("",
                               "", 3, 1)
    request = Request()
    analysis = GeneratedAnswerAnalysis('all-MiniLM-L6-v2')
    for question in aux:
        generated_answer = request.ask_for_explanation(question[1], question[2])
        original_answer = sample.answers.get(question[9])
        cosine_metric = analysis.check_cosine_metric(original_answer, generated_answer)
        output_generation.save_generated_answer(question[0], original_answer, generated_answer['choices'][0]['text'],
                                                cosine_metric.item(), 'after')

if __name__ == '__main__':
    main()
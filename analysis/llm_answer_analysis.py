from sentence_transformers import SentenceTransformer, util


class GeneratedAnswerAnalysis:

    def __init__(self, model):
        self.model = SentenceTransformer(model)


    def check_cosine_metric(self, original_answer, generated_answer):
        embedding_original_answer = self.model.encode(original_answer, convert_to_tensor=True)
        embedding_general_answer = self.model.encode(generated_answer, convert_to_tensor=True)

        cosine_metric_value = util.cos_sim(embedding_original_answer, embedding_general_answer)

        return cosine_metric_value[0][0]

from ll_model import LLModel
import fire
import gc
import torch
import warnings
from typing import List
from transformers import LlamaConfig, LlamaTokenizer, LlamaForCausalLM, LlamaModel

class Llama(LLModel):

    def __init__(self, model_name, llm_name):
        self._model_name = model_name
        self._llm_version = llm_name
        self.model = None
        self.tokenizer = None
        self.max_new_tokens = None
        self.do_sample = None
        self.top_p = None
        self.temperature = None
        self.use_cache = None
        self.top_k = None
        self.repetition_penalty = None
        self.length_penalty = None
        self.kwargs = None
        fire.Fire(self.run(model_name=model_name))

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def _model_name_setter(self, new_model_name):
        self._model_name = new_model_name

    @property
    def llm_version(self):
        return self._llm_version

    @llm_version.setter
    def _llm_version_setter(self, new_llm_version):
        self._llm_version = new_llm_version

    def ask_for_explanation(self, question, description, tags):
        messages = []
        messages.append(super().get_base_message(question, description, tags))
        chats = self.format_tokens(messages)

        with torch.no_grad():
            for idx, chat in enumerate(chats):
                tokens = torch.tensor(chat).long()
                tokens = tokens.unsqueeze(0)
                tokens = tokens.to("cuda:0")
                outputs = self.model_llm.generate(
                    input_ids=tokens,
                    max_new_tokens=1024,
                    do_sample=True,
                    use_cache=True,
                    top_p=1.0,
                    temperature=1.0,
                    top_k=50,
                    repetition_penalty=1.0,
                    length_penalty=1,
                )

                return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def format_tokens(self, dialogs):
        B_INST, E_INST = "[INST]", "[/INST]"
        B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
        DEFAULT_SYSTEM_PROMPT = """You are a helpful, respectful and honest assistant."""

        prompt_tokens = []
        for dialog in dialogs:
            if dialog[0]["role"] != "system":
                dialog = [
                             {
                                 "role": "system",
                                 "content": DEFAULT_SYSTEM_PROMPT,
                             }
                         ] + dialog
            dialog = [
                         {
                             "role": dialog[1]["role"],
                             "content": B_SYS
                                        + dialog[0]["content"]
                                        + E_SYS
                                        + dialog[1]["content"],
                         }
                     ] + dialog[2:]
            assert all([msg["role"] == "user" for msg in dialog[::2]]) and all(
                [msg["role"] == "assistant" for msg in dialog[1::2]]
            ), (
                "model only supports 'system','user' and 'assistant' roles, "
                "starting with user and alternating (u/a/u/a/u...)"
            )
            """
            Please verify that yout tokenizer support adding "[INST]", "[/INST]" to your inputs.
            Here, we are adding it manually.
            """
            dialog_tokens: List[int] = sum(
                [
                    self.tokenizer.encode(
                        f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} ",
                    )
                    for prompt, answer in zip(dialog[::2], dialog[1::2])
                ],
                [],
            )
            assert (
                    dialog[-1]["role"] == "user"
            ), f"Last message must be from user, got {dialog[-1]['role']}"
            dialog_tokens += self.tokenizer.encode(
                f"{B_INST} {(dialog[-1]['content']).strip()} {E_INST}",
            )
            prompt_tokens.append(dialog_tokens)

        return prompt_tokens


    def run(self,
            model_name="meta-llama/Llama-2-7b-chat-hf",
            peft_model: str = None,
            quantization: bool = False,
            max_new_tokens=1000,
            min_new_tokens: int = 0,
            prompt_file: str = None,
            seed: int = 42,
            safety_score_threshold: float = 0.5,
            do_sample: bool = True,
            use_cache: bool = True,
            top_p: float = 1.0,
            temperature: float = 1.0,  # [optional] The value used to modulate the next token probabilities.
            top_k: int = 50,
            repetition_penalty: float = 1.0,  # The parameter for repetition penalty. 1.0 means no penalty.
            length_penalty: int = 1,
            enable_azure_content_safety: bool = False,  # Enable safety check with Azure content safety api
            enable_sensitive_topics: bool = False,  # Enable check for sensitive topics using AuditNLG APIs
            enable_saleforce_content_safety: bool = True,
            prompt_messages: [str] = None,
            **kwargs
    ):
        access_token = ""
        self.max_new_tokens = max_new_tokens,
        self.do_sample = do_sample,
        self.top_p = top_p,
        self.temperature = temperature,
        self.use_cache = use_cache,
        self.top_k = top_k,
        self.repetition_penalty = repetition_penalty,
        self.length_penalty = length_penalty,
        self.kwargs = kwargs

        configuration = LlamaConfig()
        self.model_llm = LlamaModel(configuration)
        configuration = self.model_llm.config

        # Set the seeds for reproducibility
        torch.cuda.empty_cache()
        torch.cuda.memory_summary(device=None, abbreviated=False)
        torch.cuda.manual_seed(seed)
        torch.manual_seed(seed)
        gc.collect()
        self.model_llm = self.load_model(model_name, quantization, access_token)

        self.tokenizer = LlamaTokenizer.from_pretrained(model_name, use_auth_token=access_token)
        self.tokenizer.add_special_tokens(
            {

                "pad_token": "<PAD>",
            }
        )

    def load_model(self, model_name, quantization, access_token):
        model = LlamaForCausalLM.from_pretrained(
            model_name,
            return_dict=True,
            load_in_8bit=quantization,
            device_map="auto",
            low_cpu_mem_usage=True,
            use_auth_token=access_token,
        )
        return model

    def ask_for_similarity_analysis(self, original_answer, generated_answer, tags):
        messages = []
        messages.append(self.get_similarity_message(original_answer, generated_answer, tags))
        chats = self.format_tokens(messages)

        torch.cuda.empty_cache()
        torch.cuda.memory_summary(device=None, abbreviated=False)

        with torch.no_grad():
            for idx, chat in enumerate(chats):
                tokens = torch.tensor(chat).long()
                tokens = tokens.unsqueeze(0)
                tokens = tokens.to("cuda:0")
                outputs = self.model_llm.generate(
                    input_ids=tokens,
                    max_new_tokens=2048,
                    do_sample=True,
                    use_cache=True,
                    top_p=1.0,
                    temperature=1.0,
                    top_k=50,
                    repetition_penalty=1.0,
                    length_penalty=1,
                )

                torch.cuda.empty_cache()
                torch.cuda.memory_summary(device=None, abbreviated=False)

                return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def get_similarity_message(self, original_answer, generated_answer, tags):
        base_messages = [
            {'role': 'system',
             'content': "You are an expert in software engineering with much experience on programming."},
            {'role': 'user', 'content': "Please, act as you have solid experience on these topics: " + tags + " ."},
            {'role': 'assistant', 'content': "Okay, I have a solid background on " + tags + " ."},
            {'role': 'user',
             'content': "This way, check the two inputs, A and B, provided below, analyze each of them, and finally, compute their similarity. For that, please consider not only the style of the inputs but also their semantics and context.\n" +
                        "When reporting the similarity, please consider an interval between VERY LOW to VERY HIGH (VERY LOW, LOW, MEDIUM, HIGH, VERY HIGH).\n" +
                        "Please, only report the similarity, and do it by reporting a JSON file with the property similarity, like this template: { \"similarity\": \"\" } \n" +
                        "DO NOT provide any further information or explanation; just report the similarity, following the template informed, please.\n" +

                        "A = {" + original_answer + "}\n\n" +
                        "B = {" + generated_answer + "}"}]

        return base_messages

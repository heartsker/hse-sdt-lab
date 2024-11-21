from abc import ABC, abstractmethod

from torch import torch
from transformers import BertForQuestionAnswering, BertTokenizer, logging

logging.set_verbosity_error()

class BaseQAModel(ABC):
    """Abstract class for QA model
    """

    def __init__(self) -> None:
        """Initialize QA model
        """
        pass

    @abstractmethod
    def predict(self, question: str, context: str) -> str:
        pass

class DefaultQAModel(BaseQAModel):
    """Default QA model
    """

    model: BertForQuestionAnswering
    tokenizer: BertTokenizer

    def __init__(self) -> None:
        """Initialize default QA model
        """
        super().__init__()

        pretrained_name = 'bert-large-uncased-whole-word-masking-finetuned-squad'
        tokenizer_name = 'bert-large-uncased-whole-word-masking-finetuned-squad'
        self.model = BertForQuestionAnswering.from_pretrained(pretrained_name)
        self.tokenizer = BertTokenizer.from_pretrained(tokenizer_name)

    def predict(self, question: str, context: str) -> str:
        """Predict answer for question and context

        Args:
            question (str): question to predict answer for
            context (str): context to predict answer from

        Returns:
            str: predicted answer

        """

        input_ids = self.tokenizer.encode(question, context)
        tokens = self.tokenizer.convert_ids_to_tokens(input_ids)

        # segment IDs
        # first occurence of [SEP] token
        sep_idx = input_ids.index(self.tokenizer.sep_token_id)
        # number of tokens in segment A (question)
        num_seg_a = sep_idx + 1
        # number of tokens in segment B (text)
        num_seg_b = len(input_ids) - num_seg_a

        # list of 0s and 1s for segment embeddings
        segment_ids = [0] * num_seg_a + [1] * num_seg_b
        assert len(segment_ids) == len(input_ids)

        # model output using input_ids and segment_ids
        output = self.model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))

        # reconstructing the answer
        answer_start = torch.argmax(output.start_logits)
        answer_end = torch.argmax(output.end_logits)
        answer = '[CLS]'
        if answer_end >= answer_start:
            answer = tokens[answer_start]
            for i in range(answer_start + 1, answer_end + 1):
                if tokens[i][0:2] == "##":
                    answer += tokens[i][2:]
                else:
                    answer += " " + tokens[i]

        if answer.startswith("[CLS]"):
            answer = "Unable to find the answer to your question."

        return answer

    # def __predict_indices(self, question: str, context: str) -> Tuple[int, int]:
    #     """Predict answer indices for question and context
    #
    #     Args:
    #         question (str): question to predict answer for
    #         context (str): context to predict answer from
    #
    #     Returns:
    #         Tuple[int, int]: predicted answer indices
    #
    #     """
    #
    #     output = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))
    #     answer_start = torch.argmax(output.start_logits)
    #     answer_end = torch.argmax(output.end_logits)
    #
    #     return Tuple(answer_start, answer_end)

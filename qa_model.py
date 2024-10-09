from abc import ABC, abstractmethod
from transformers import BertForQuestionAnswering, BertTokenizer
from typing import Tuple
from torch import torch


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

        self.model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        self.tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

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

        answer_start, answer_end = self.__predict_indices(question=question, context=context)

        if answer_start > answer_end:
            return "no_answer"

        return " ".join(tokens[answer_start:answer_end+1])

    def __predict_indices(self, question: str, context: str) -> Tuple[int, int]:
        """Predict answer indices for question and context

        Args:
            question (str): question to predict answer for
            context (str): context to predict answer from

        Returns:
            Tuple[int, int]: predicted answer indices

        """

        answer_start = torch.argmax(output.start_logits)
        answer_end = torch.argmax(output.end_logits)

        return Tuple(answer_start, answer_end)
from services.dataset import DefaultDataset
from services.qa_model import DefaultQAModel


class Runner:
    """Runner
    Responsible for running requests to QA model on dataset
    """

    def __init__(self) -> None:
        """Initialize runner with default QA model and dataset
        """
        self.model = DefaultQAModel()
        self.dataset = DefaultDataset([])

    def run(self, question: str, context: str) -> str:
        """Run request to QA model on dataset

        Args:
            question (str): question to predict answer for
            context (str): context to predict answer from

        Returns:
            str: predicted answer

        """
        return self.model.predict(question, context)

    def start(self) -> None:
        """Start runner
        """

        context = None

        while True:
            question = None
            while not question:
                question = input("Please enter question: ")

            context = input("Please enter context (or press Enter to use previous one):") or context
            while not context:
                context = input("Please enter context: ")

            answer = self.run(question, context)

            print(f"Answer: {answer}")

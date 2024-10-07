from abc import ABC, abstractmethod
from typing import Any, Tuple, List


class Dataset(ABC):
    """Abstract class for dataset
    """

    @abstractmethod
    def __call__(self, *args: Any) -> Tuple[str, str, str]:
        """Get data by index

        Returns:
            Tuple[str, str, str]: data
        """
        pass

class DefaultDataset(Dataset):
    """Default dataset
    """

    __data: List[Tuple[str, str, str]]

    def __init__(self, data: List[Tuple[str, str, str]]) -> None:
        """Initialize dataset with data

        Args:
            *args (Any): Data to initialize dataset with

        """
        assert args, "No data provided"
        assert type(args) == list, "Data must be a list"

        if args:
            self.__data = args

    def __call__(self, *args: Any, **kwds: Any) -> Tuple[str, str, str]:
        return self.__data[args]

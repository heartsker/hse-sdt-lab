from abc import ABC, abstractmethod
from typing import List, Tuple


class Dataset(ABC):
    """Abstract class for dataset
    """

    @abstractmethod
    def __getitem__(self, index: int) -> Tuple[str, str, str]:
        pass


class DefaultDataset(Dataset):
    """Default dataset
    """

    __data: List[Tuple[str, str, str]]

    def __init__(self, data: List[Tuple[str, str, str]]) -> None:
        """Initialize dataset with data

        Args:
            data (List[Tuple[str, str, str]]): data to initialize dataset with

        """

        self.__data = data

    def __getitem__(self, index: int) -> Tuple[str, str, str]:
        """Get item by index

        Args:
            index (int): index of item

        Returns:
            Tuple[str, str, str]: item at index

        """

        return self.__data[index]

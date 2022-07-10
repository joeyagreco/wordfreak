import string
from abc import abstractmethod, ABC


class Parser(ABC):

    @classmethod
    @abstractmethod
    def getWordFrequency(cls, pathToFile: str) -> dict[str, int]:
        ...

    @classmethod
    def _getWordFrequencyFromLines(cls, lines: list[str]) -> dict[str, int]:
        wordFrequency: dict[str, int] = dict()
        for line in lines:
            line = line.strip()
            words = line.split()
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                if word in wordFrequency:
                    wordFrequency[word] += 1
                else:
                    wordFrequency[word] = 1
        return wordFrequency

import json

from src.parser.DocParser import DocParser
from src.parser.DocxParser import DocxParser
from src.parser.PdfParser import PdfParser
from src.parser.TxtParser import TxtParser


class FrequencyService:
    TXT_FILE_EXTENSION = ".txt"
    PDF_FILE_EXTENSION = ".pdf"
    DOC_FILE_EXTENSION = ".doc"
    DOCX_FILE_EXTENSION = ".docx"

    @classmethod
    def extractWordFrequencies(cls, inputFilePath: str, outputFilePath: str) -> None:
        """
        Takes a file and saves all word frequencies to a JSON file.
        """

        if inputFilePath.lower().endswith(cls.TXT_FILE_EXTENSION):
            wordFrequencies = TxtParser.getWordFrequency(inputFilePath)
        elif inputFilePath.lower().endswith(cls.PDF_FILE_EXTENSION):
            wordFrequencies = PdfParser.getWordFrequency(inputFilePath)
        elif inputFilePath.lower().endswith(cls.DOCX_FILE_EXTENSION):
            wordFrequencies = DocxParser.getWordFrequency(inputFilePath)
        elif inputFilePath.lower().endswith(cls.DOC_FILE_EXTENSION):
            wordFrequencies = DocParser.getWordFrequency(inputFilePath)
        else:
            raise ValueError(f"Filetype not supported for parsing (tried to parse file at '{inputFilePath}').")

        # sort word frequencies by number of occurrences
        orderedWordFreq = dict(sorted(wordFrequencies.items(), reverse=True, key=lambda item: item[1]))

        # save to JSON file
        with open(outputFilePath, "w+") as file:
            json.dump(orderedWordFreq, file)

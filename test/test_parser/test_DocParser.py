import os
import unittest

from src.parser.DocParser import DocParser


class TestDocParser(unittest.TestCase):
    PATH_TO_TEST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files", "parser"))

    def test_getWordFrequency_docFile_happyPath(self):
        docxFilePath = os.path.join(self.PATH_TO_TEST_DIR, "test.doc")
        wf = DocParser.getWordFrequency(docxFilePath)
        self.assertIsInstance(wf, dict)
        self.assertEqual(6, len(wf.keys()))
        self.assertEqual(2, wf["hello"])
        self.assertEqual(2, wf["world"])
        self.assertEqual(1, wf["this"])
        self.assertEqual(1, wf["is"])
        self.assertEqual(1, wf["a"])
        self.assertEqual(1, wf["test"])
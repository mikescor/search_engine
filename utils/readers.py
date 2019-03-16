from PyPDF2 import PdfFileReader
from docx import Document


class PdfReader:
    def __init__(self):
        self._data = ''

    def to_process(self, file):
        input_file = open(file, 'rb')
        pdf_reader = PdfFileReader(input_file)

        for page in pdf_reader.pages:
            self._data += page.extractText()

        return self._data


class DocxReader:
    def __init__(self):
        self._data = ''

    def to_process(self, file):
        document = Document(file)

        for paragraph in document.paragraphs:
            self._data += paragraph.text

        return self._data


class EpubReader:
    pass

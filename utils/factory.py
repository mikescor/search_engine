from utils.readers import PdfReader, DocxReader


class DocumentFactory:
    def __init__(self):
        self._readers = {}

    def register_format(self, format, reader):
        self._readers[format] = reader

    def get_reader(self, format):
        reader = self._readers.get(format)
        if not reader:
            raise ValueError(format)
        return reader()


factory = DocumentFactory()
factory.register_format('pdf', PdfReader)
factory.register_format('docx', DocxReader)

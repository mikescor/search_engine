from utils.factory import factory


class Document:
    def __init__(self, document_id, file, format):
        self.document_id = document_id
        self.file = file
        self.format = format

    def get_data(self):
        reader = factory.get_reader(self.format)
        return reader.to_process(self.file)

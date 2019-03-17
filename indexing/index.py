from collections import defaultdict

from nltk import word_tokenize


class InvertedIndex:
    def __init__(self, tokenizer, stemmer, stopwords):
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.index = defaultdict(list)
        self.documents = {}
        self.__unique_id = 0
        if not stopwords:
            self.stopwords = set()
        else:
            self.stopwords = set(stopwords)

    def add(self, document):

        text = [t.lower for t in word_tokenize(document)]
        for token in text:
            if token in self.stopwords:
                continue

            if self.stemmer:
                token = self.stemmer.stem(token)

            if self.__unique_id not in self.index[token]:
                self.index[token].append(self.__unique_id)

        self.documents[self.__unique_id] = document
        self.__unique_id += 1
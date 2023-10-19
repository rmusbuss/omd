class CountVectorizer:
    """
    Это класс, который имеет два метода fit_transform и get_feature_names
    Принимает на вход строки со словами и возвращает встречаемость слов
    в виде списке для каждой строки
    """

    def __init__(self):
        """
        Это конструктор, в котором мы инициализируем переменные
        для обработки предложений
        """
        self.feature_names = None
        self.corpus = None
        self.dictionary = {}

    def fit_transform(self, corpus: list[str]) -> list[str]:
        """
        Этот метод принимает на вход предложения из слов
        и возвращает уникальные слова в виде списка
        """
        self.corpus = corpus
        sentences_num = len(corpus)
        for sent_num, sentence in enumerate(corpus):
            for word in sentence.split():
                word = word.lower()
                self.dictionary[word] = \
                    self.dictionary.get(word, [0] * sentences_num)
                self.dictionary[word][sent_num] += 1
        self.feature_names = list(self.dictionary.keys())
        return self.feature_names

    def get_feature_names(self) -> list[list[int]]:
        """
        Этот метод ничего не принимает на вход, строит терм-документную матрицу
        и возвращает ее
        """
        sentences_num = len(self.corpus)
        words_num = len(self.feature_names)
        term_matrix = [[0] * words_num for _ in range(sentences_num)]
        word_indices = dict(zip(self.feature_names,
                                range(len(self.feature_names))))
        for sent_num, sentence in enumerate(self.corpus):
            sentence = sentence.split()
            for word in sentence:
                word = word.lower()
                term_matrix[sent_num][word_indices[word]] = \
                    self.dictionary[word][sent_num]
        return term_matrix


if __name__ == '__main__':
    # пример реализации
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())

    print(count_matrix)

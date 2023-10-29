import numpy as np


# Задание #1: count vectorizer
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

    def get_feature_names(self) -> list[str]:
        """
        Этот метод ничего не принимает на вход
        и возвращает уникальные слова в виде списка
        """
        return self.feature_names

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Этот метод принимает на вход предложения из слов,
        строит терм-документную матрицу и возвращает ее
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


# Задание #2: term frequency
def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
    """
    Функция принимает на вход терм-документную матрицу
    преобразует ее в tf и возвращает tf
    """
    count_matrix = np.array(count_matrix)
    tf = count_matrix / np.sum(count_matrix, axis=1, keepdims=True)
    return np.around(tf, 3)


# Задание #3: inverse document-frequency
def idf_transform(count_matrix: list[list[int]]) -> list[float]:
    """
    Функция принимает на вход терм-документную матрицу
    преобразует ее в idf и возвращает idf
    """
    count_matrix = np.array(count_matrix)
    count_matrix[count_matrix > 0] = 1
    idf = np.log((count_matrix.shape[0] + 1) / (count_matrix.sum(axis=0)
                                                + 1)) + 1
    return np.around(idf, 3)


# Задание #4: tf-idf transformer
class TfidfTransformer:
    """
    Класс объединяет результат двух функций выше в виде
    tdidf = tf * idf и возвращает этот результат
    """
    def __init__(self):
        pass

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """
        Метод принимает на вход терм-документную матрицу
        преобразует ее в idf и возвращает idf
        """
        count_matrix = np.array(count_matrix)
        count_matrix[count_matrix > 0] = 1
        idf = np.log((count_matrix.shape[0] + 1) / (count_matrix.sum(axis=0)
                                                    + 1)) + 1
        return idf

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Метод принимает на вход терм-документную матрицу
        преобразует ее в tf и возвращает tf
        """
        count_matrix = np.array(count_matrix)
        tf = count_matrix / np.sum(count_matrix, axis=1, keepdims=True)
        return tf

    def fit_transform(self,
                      count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Метод принимает на вход терм-документную матрицу
        преобразует ее в tf, в преобразует ее в idf
        и возвращает произведение tfidf = tf*idf
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tfidf = []
        for tf_row in tf:
            tfidf.append([tf_j * idf_j for tf_j, idf_j in zip(tf_row, idf)])
        return np.around(tfidf, 3)


# Задание #5: tf-idf vectorizer
class TfidfVectorizer(CountVectorizer):
    """
    Класс наследуется от класса CountVectorizer
    Принимает на вход строки со словами и возвращает
    tfidf матрицу
    """

    def __init__(self):
        """
        Это конструктор, в котором мы инициализируем переменные
        из класса CountVectorizer для обработки предложений
        а также определяем transformer - TfidfTransformer()
        необходимый для построения tdidf
        """
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Этот метод принимает на вход предложения из слов,
        строит терм-документную матрицу, отдает ее на вход
        трансформеру (TfidfTransformer()) и возвращает
        получившуюся матрицу tfidf
        """
        term_matrix = super().fit_transform(corpus)
        tfidf = self.transformer.fit_transform(term_matrix)
        return tfidf


if __name__ == '__main__':
    # 1. пример реализации для класса Count Vectorizer
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print('1. пример вывода для класса Count Vectorizer')
    print(vectorizer.get_feature_names())

    print(count_matrix)

    # 2. пример реализации для функции tf_transform
    print('\n2. пример вывода для функции tf_transform')
    print(tf_transform(count_matrix))

    # 3. пример реализации для функции idf_transform
    print('\n3. пример вывода для функции idf_transform')
    print(idf_transform(count_matrix))

    # 4. пример реализации для класса TfidfTransformer
    print('\n4. пример вывода для класса TfidfTransformer')
    tfidf = TfidfTransformer()
    print(tfidf.fit_transform(count_matrix))

    # 5. пример реализации для класса TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print('\n5. пример вывода для класса TfidfVectorizer')
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)

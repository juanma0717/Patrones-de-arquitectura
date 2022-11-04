class Word1:
    @staticmethod
    def method():
        return "Solo se"


class Word2:
    @staticmethod
    def method():
        return " que no"


class Word3:
    @staticmethod
    def method():
        return " se nada."


# facade
class Facade:
    def __init__(self):
        self.word_1 = Word1()
        self.word_2 = Word2()
        self.word_3 = Word3()

    def create(self):
        phrase = self.word_1.method()
        phrase += self.word_2.method()
        phrase += self.word_3.method()
        return phrase


# client
facade = Facade()
phrase1 = facade.create()
print(f'La frase es: {phrase1}')
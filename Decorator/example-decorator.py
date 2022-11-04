from abc import ABCMeta, abstractmethod

class First(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method():
        pass

class Object(First):
    def method(self):
        return "Primer objeto"

class Decorator(First):
    def __init__(self, objt):
        self.object = objt

    def method(self):
        return f"Metodo decorador({self.object.method()})"

# The Client
object1 = Object()
print(object1.method())
print(Decorator(object1).method())
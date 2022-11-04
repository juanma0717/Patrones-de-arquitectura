from abc import ABCMeta, abstractstaticmethod

class Animals (metaclass=ABCMeta):
    @abstractstaticmethod
    def adopt_cat():
        pass

class Pets(Animals):
    def adopt_cat (self):
        print ("Tengo un gato")
        
class ProxyAnimals (Animals) :
    def __init__ (self) :
        self.animals= Pets()

    def adopt_cat (self):
        self.animals.adopt_cat()
        print('El proxy esta en funcionamiento')
        


p1 = Pets ()
p1.adopt_cat()
p2 = ProxyAnimals ()
p2.adopt_cat()
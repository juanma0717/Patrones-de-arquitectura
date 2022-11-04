from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def create_chasis_renault(self):
        pass

    @abstractmethod
    def create_chasis_ford(self):
        pass




class Chasis_Car(Car):
    def create_chasis_renault(self):
        print("Renault creado")

    def create_chasis_ford(self):
        print("Ford creado")



class Save_Car(Car):
    def create_chasis_renault(self):
        print("Se ha creado el chasis del renault")

    def create_chasis_ford(self):
        print("Se ha creado el chasis del ford")




class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class Chasis_Factory(AbstractFactory):
    def create_car(self):
        return Chasis_Car()



class Save_Chasis_Factory(AbstractFactory):
    def create_car(self):
        return Save_Car()



def main():
    for factory in (Chasis_Factory(), Save_Chasis_Factory()):
        product_a = factory.create_car()
        product_a.create_chasis_ford()
        product_a.create_chasis_renault()


if __name__ == "__main__":
    main()
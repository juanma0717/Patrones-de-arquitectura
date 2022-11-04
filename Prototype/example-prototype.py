from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone():
        ""


class Copy(Prototype):
    def __init__(self, field):
        self.field = field  

    def clone(self):
        return type(self)(
            self.field
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


array_teams = Copy(["Bayern", "Barcelona", "Juventus", "Porto"])  
print(f"Arreglo 1 {array_teams}")

array_teams2 = array_teams.clone()  
array_teams2.field[1] = "Villareal"

print(f"Arreglo2 {array_teams2}")
print(f"Arreglo1 {array_teams}")
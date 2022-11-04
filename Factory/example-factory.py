class Olimpica:
    def __init__(self):
        self.prices = {"mango": "15000", "guayaba": "12300","pera":"10000"}
 
    def find(self, message):
        return self.prices.get(message, message)
 
class Exito:
    def __init__(self):
        self.prices = {"mango": "4000", "guayaba": "10000", "pera":"35000"}
 
    def find(self, message):
        return self.prices.get(message, message)
 
class Fruit:
    def find(self, message):
        return message
 
def Factory(buy ="Fruta"):
    seeker = {"Olimpica": Olimpica, "Exito": Exito, "Fruta": Fruit}
    return seeker[buy]()
 
if __name__ == "__main__":
    ol = Factory("Olimpica")
    ex = Factory("Exito")
    ft = Factory("Fruta")
    name1 = "Olimpica"
    name2 = "Exito"
    name3 = "Fruta"
    messages = ["mango", "guayaba", "pera"]
    for message in messages:
        print(f"{name3} {ft.find(message)}")
        print(f"{name1} {ol.find(message)}")
        print(f"{name2} {ex.find(message)}")


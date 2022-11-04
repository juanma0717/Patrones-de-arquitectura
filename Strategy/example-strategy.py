class Item:
    def __init__(self, phone, offer = None):
        self.phone = phone
        self.offer = offer
 
    def discount(self):
        if self.offer:
            discount = self.offer(self)
        else:
            discount = 0   
        return self.phone - discount
 
    def __repr__(self):
        statement = "Precio inicial {}, precio con oferta {}"
        return statement.format(self.phone, self.discount())
 
def offer_40(order):    
    return order.phone * 0.40
 
def offer_20(order):  
    return order.phone * 0.20

if __name__ == "__main__":
    print(Item(1000000))
    print(Item(1000000, offer = offer_40))
    print(Item(1000000, offer = offer_20))
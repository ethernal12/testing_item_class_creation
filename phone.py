from item import Item
class Broken_phone(Item):

    def __init__(self, name: str, price: int, quantity:int, broke_phone=1):
        super().__init__(
            name, price, quantity
        )
        self.broken_phone = broke_phone

    def __repr__(self):
        print(self.broken_phone, 'broken_phone')
        # how to override the repr method from item.class to add additional broken_phone attribute
        return f"{self.__class__.__name__}({self.__name},{self.__price},{self.quantity},{self.broken_phone})"

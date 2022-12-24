from item import Item
class Broken_phone(Item):

    def __init__(self, name: str, price: int, quantity=1, broke_phone=1):
        super().__init__(
            name, price, quantity
        )
        self.broken_phone = broke_phone
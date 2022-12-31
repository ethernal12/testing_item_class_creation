import csv


class Item:
    pay_rate = 0.8  # discount
    item_list = []

    def __init__(self, name: str, price: int, quantity: int):

        assert price > 0, f'{price} is not greater than 0'
        assert quantity > 0, f'{quantity} is not greater than 0'
        self._name = name
        self._price = price
        self.quantity = quantity
        self.item_list.append(self)  # self is contructed in __repr__

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def restrict_quantity(self):
        return self.quantity

    @restrict_quantity.setter
    def set_new_quantity(self, value):
        if value > 10:
            raise Exception('Quantity amount is too high')
        else:
            self.quantity = value

    @property
    def restrict_name(self):
        print('restricitng name')
        return self.__name

    @restrict_name.setter
    def set_name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Count out the floats that are point zero
        # i.e. : 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __eq__(self, other):
        return self._name == other._name
    def __repr__(self):

        return f"{self.__class__.__name__}({self._name},{self._price},{self.quantity})"

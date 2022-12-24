import unittest
from phone import Broken_phone
from item import Item
import csv


class MyTestCase(unittest.TestCase):
    def test_price_restriction(self):
        with self.assertRaises(AssertionError) as err:
            Item('Phone', 500, 0)
        self.assertEqual(str(err.exception), '0 is not greater than 0')

        with self.assertRaises(AssertionError) as err:
            Item('Phone', 200, -1)

        self.assertEqual(str(err.exception), '-1 is not greater than 0')

    def test_quantity_restriction(self):
        with self.assertRaises(AssertionError) as err:
            Item('Phone', 500, 0)
        self.assertEqual(str(err.exception), '0 is not greater than 0')

        with self.assertRaises(AssertionError) as err:
            Item('Phone', 500, -1)
        self.assertEqual(str(err.exception), '-1 is not greater than 0')

    def test_creating_item_with__repr__(self):
        itm1 = Item('Phone', 200, 1)
        self.assertEqual(str(itm1), 'Item(Phone,200,1)')

    def test_creating_item_and_adding_to_list(self):
        Item('Phone', 200, 1)
        Item('Desktop', 500, 1)
        self.assertEqual(str(Item.item_list[0]), 'Item(Phone,200,1)')
        self.assertEqual(str(Item.item_list[1]), 'Item(Desktop,500,1)')

    def test_item_name_setter_ristrictions(self):
        itm1 = Item('Phone', 200, 1)
        with self.assertRaises(Exception) as err:
            itm1.set_name = 'new_name_is_to_long'
        self.assertEqual(str(err.exception), 'The name is too long')

    def test_price_renaming_setter(self):
        itm1 = Item('Phone', 200, 1)
        itm1.set_name = 'New_phone'
        self.assertEqual(itm1.restrict_name, 'New_phone')

    def test_quantity_renaming_restriction(self):
        itm1 = Item('Phone', 200, 1)
        with self.assertRaises(Exception) as err:
            itm1.set_new_quantity = 12
        self.assertEqual(str(err.exception), 'Quantity amount is too high')

    def test_quantity_renaming_setter(self):
        itm1 = Item('Phone', 200, 1)
        itm1.set_new_quantity = 9
        self.assertEqual(itm1.restrict_quantity, 9)

    def test_create_class_items_from_csv_file(self):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            Item(
                name=items[0].get('name'),
                price=int(items[0].get('price')),
                quantity=int(items[0].get('quantity'))
            )

        result = str(Item.item_list[0])
        print(result)
        self.assertEqual(result, 'Item(Phone,100,1)')


if __name__ == '__main__':
    unittest.main()

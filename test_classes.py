import unittest
from phone import Broken_phone
from item import Item

class MyTestCase(unittest.TestCase):
    def test_price_restriction(self):
        with self.assertRaises(AssertionError) as err:
            itm1 = Item('Phone', 500, 0)
        self.assertEqual(str(err.exception), '0 is not greater than 0')

        with self.assertRaises(AssertionError) as err:
            itm1 = Item('Phone', 200, -1)

        self.assertEqual(str(err.exception), '-1 is not greater than 0')

    def test_quantity_restriction(self):
        with self.assertRaises(AssertionError) as err:
            itm1 = Item('Phone', 500, 0)
        self.assertEqual(str(err.exception), '0 is not greater than 0')

        with self.assertRaises(AssertionError) as err:
            itm1 = Item('Phone', 500, -1)
        self.assertEqual(str(err.exception), '-1 is not greater than 0')
    def test_creating_item_with__repr__(self):
        itm1 = Item('Phone', 200, 1)
        self.assertEqual(str(itm1),'Item(Phone,200,1)')
    def test_creating_item_and_adding_to_list(self):
        itm1 = Item('Phone', 200, 1)
        itm2 = Item('Desktop', 500, 1)
        self.assertEqual(str(Item.item_list[0]), 'Item(Phone,200,1)')
        self.assertEqual(str(Item.item_list[1]), 'Item(Desktop,500,1)')
    def test_price_name_renaming_restriction(self):
        itm1 = Item('Phone', 200, 1)
        with self.assertRaises(Exception) as err:
            itm1.set_name = 'new_name_is_to_long'
        self.assertEqual(str(err.exception), 'The name is too long')

if __name__ == '__main__':
    unittest.main()

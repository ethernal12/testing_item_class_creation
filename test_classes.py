import unittest
from phone import Broken_phone
from item import Item

class MyTestCase(unittest.TestCase):
    def test_creating_item(self):
        itm1 = Item('Phone', 200, 1)


if __name__ == '__main__':
    unittest.main()

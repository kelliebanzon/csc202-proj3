import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    list_1 = Pair(0, None)
    list_2 = Pair(0, Pair(1, Pair(2, None)))
    list_none = Pair(0, Pair(None, Pair(2, None)))

    def test_repr(self):
        self.assertEqual(self.list_1.__repr__(), "0, None")

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        self.assertEqual(add(self.list_1, 0, 4), Pair(4, Pair(0, None)))
        self.assertEqual(add(self.list_1, 1, 4), Pair(0, Pair(4, None)))
        self.assertRaises(IndexError, add, self.list_1, 4, 6)
        self.assertRaises(IndexError, add, empty_list(), 1, 12)

    def test_length(self):
        self.assertEqual(length(Pair(0, Pair(1, Pair(2, Pair(3, None))))), 4)
        self.assertEqual(length(None), 0)

    def test_get(self):
        self.assertEqual(get(self.list_1, 0), 0)
        self.assertEqual(get(self.list_none, 1), None)
        self.assertEqual(get(Pair(None, Pair(1, Pair(2, None))), 0), None)
        self.assertRaises(IndexError, get, self.list_1, 4)
        self.assertRaises(IndexError, get, empty_list(), 0)
        self.assertRaises(IndexError, get, add(add(add(add(empty_list(), 0, 87), 0, 2), 0, 4), 0, 3), 4)
        self.assertRaises(IndexError, get, add(add(add(add(empty_list(), 0, 87), 0, 2), 0, 4), 0, 3), -2)

    def test_set(self):
        self.assertEqual(set(self.list_1, 0, 12), Pair(12, None))
        self.assertRaises(IndexError, set, empty_list(), 0, 23)
        self.assertRaises(IndexError, set, self.list_1, 4, 12)
        self.assertRaises(IndexError, set, add(add(add(empty_list(), 0, 42), 0, "z"), 0, 2), 3, "abc")

    def test_remove(self):
        self.assertEqual(remove(self.list_2, 1), (1, Pair(0, Pair(2, None))))
        self.assertRaises(IndexError, remove, self.list_2, 8)
        self.assertRaises(IndexError, remove, add(add(add(empty_list(), 0, 5), 0, 4), 0, 3), 3)


if __name__ == '__main__':
    unittest.main()
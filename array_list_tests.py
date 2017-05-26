import unittest
from array_list import *

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



    list_1 = ArrayList([0, 1, 2, 3])
    list_2 = ArrayList([0, 1, 2, 3])
    list_nones = ArrayList([0, 1, None, 3])
    list_all_nones = ArrayList([None, None, None])

    def test_repr(self):
        self.assertEqual(ArrayList([0, 1, 2, 3]).__repr__(), "0, 1, 2, 3")

    def test_eq(self):
        self.assertEqual(self.list_1.__eq__("string"), False)
        self.assertEqual(self.list_1.__eq__(ArrayList([0, 13])), False)

    def test_empty_list(self):
        self.assertEqual(empty_list(), ArrayList([]))

    def test_add(self):
        self.assertEqual(add(ArrayList([0, 1, 2, 3]), 1, 1), ArrayList([0, 1, 1, 2, 3]))
        self.assertEqual(add(ArrayList([0, 1, 2, 3]), 0, "a"), ArrayList(["a", 0, 1, 2, 3]))
        self.assertEqual(add(ArrayList([0, 1, 2, 3]), 4, 4), ArrayList([0, 1, 2, 3, 4]))
        self.assertEqual(add(add(ArrayList([0, 1, 2, 3]), 4, 4), 2, "a"), ArrayList([0, 1, "a", 2, 3, 4]))
        self.assertRaises(IndexError, add, self.list_1, 7, 2)
        self.assertRaises(IndexError, add, self.list_1, -7, 2)
        self.assertEqual((add(add(add(add(empty_list(), 0, "bc"), 0, 87), 0, 2), 0, 3) == add(
            add(add(add(empty_list(), 0, "bc"), 0, 87), 0, 2), 0, 3)), True)
        self.assertEqual((add(add(add(add(empty_list(), 0, "bc"), 0, 87), 0, 2), 0, 3) == add(
            add(add(add(empty_list(), 0, "bc"), 0, 87), 0, 3), 0, 3)), False)
        self.assertEqual(add(add(add(add(empty_list(), 0, "bc"), 0, 87), 0, 2), 0, 3), ArrayList([3, 2, 87, "bc"]))

    def test_length(self):
        self.assertEqual(length(ArrayList([0, 1, 2, 3])), 4)
        self.assertEqual(length(add(ArrayList([0, 1, 2, 3]), 4, 4)), 5)
        self.assertEqual(length(empty_list()), 0)
        self.assertEqual(length(remove_index(ArrayList([0, 1, 2, 3]), 0)), 3)

    def test_get(self):
        self.assertEqual(get(self.list_1, 0), 0)
        self.assertEqual(get(ArrayList([None, 1, 2]), 0), None)
        self.assertEqual(get(self.list_all_nones, 1), None)
        self.assertEqual(get(self.list_all_nones, 2), None)
        self.assertEqual(get(add(self.list_1, 0, 0), 0), 0)
        self.assertEqual(get(add(ArrayList([0, 1, 2, 3]), 0, 0), 4), 3)
        temp = add(ArrayList([0, 1, 2, 3]), 0, 0)
        self.assertRaises(IndexError, get, temp, 5)
        self.assertRaises(IndexError, get, self.list_1, 12)
        self.assertRaises(IndexError, get, self.list_1, -1)
        self.assertRaises(IndexError, get, empty_list(), 12)
        self.assertRaises(IndexError, get, empty_list(), 0)

    def test_set(self):
        self.assertEqual(set(ArrayList([0, 1, 2, 3]), 0, 16), ArrayList([16, 1, 2, 3]))
        self.assertRaises(IndexError, set, self.list_1, 27, 0)

    def test_increment(self):
        self.assertEqual(increment(ArrayList([0,1,2,3]), 2), ArrayList([0,1,3,3]))
        self.assertRaises(IndexError, increment, empty_list(), 2)
        self.assertRaises(IndexError, increment, ArrayList([0,1,2,3]), 16)
        self.assertEqual(increment(increment(ArrayList([0,1,2,3]), 2), 0), ArrayList([1,1,3,3]))

    def test_remove(self):
        self.assertEqual(remove(ArrayList([0, 1, 2, 3]), 0), (0, ArrayList([1, 2, 3])))
        self.assertEqual(remove(ArrayList([0, 1, 2, 3]), 2), (2, ArrayList([0, 1, 3])))
        self.assertRaises(IndexError, remove, self.list_1, 12)
        self.assertRaises(IndexError, remove, add(add(add(empty_list(), 0, 5), 0, 4), 0, 3), 3)

    def test_remove_index(self):
        self.assertEqual(remove_index(ArrayList([0, 1, 2, 3]), 0), ArrayList([1, 2, 3]))
        self.assertEqual(remove_index(ArrayList([0, 1, 2, 3]), 2), ArrayList([0, 1, 3]))
        self.assertRaises(IndexError, remove_index, self.list_1, 12)

    def test_foreach(self):
        self.assertEqual(foreach(self.list_1, print), None)

    def test_less_than(self):
        self.assertEqual(less_than(1, 2), True)
        self.assertEqual(less_than(2, 1), False)

    def test_sort(self):
        self.assertEqual(sort(ArrayList([20, 11, 82, 3]), less_than, empty_list()), ArrayList([3, 11, 20, 82]))
        self.assertEqual(sort(add(sort(ArrayList([20, 11, 82, 3]), less_than, empty_list()), 2, -6), less_than, empty_list()),
                         ArrayList([-6, 3, 11, 20, 82]))


if __name__ == '__main__':
    unittest.main()
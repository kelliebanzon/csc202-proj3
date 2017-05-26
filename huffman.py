from array_list import *

# a Huffman Tree is either:
# - a Huffman node (one or more children)
# - a Huffman leaf (no children)


#TODO: data defn
class Leaf:
    def __init__(self, char, freq):
        self.char = char        # TODO: char or ASCII value?
        self.freq = freq        # the frequency of occurrences
    def __eq__(self, other):
        return type(other) == Leaf and self.char == other.char and self.freq == other.freq
    def __repr__(self):
        return "{}, freq = {}".format(self.char, self.freq)


#TODO: data defn
class Node:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __eq__(self, other):
        return type(other) == Node and self.char == other.char and self.freq == other.freq and self.left == other.left and self.right == other.right
    def __repr__(self):
        return "{}, freq = {}\n\tleft = {}\n\t{}".format(self.char, self.freq, self.left.__repr__(), self.right.__repr__())


# given a text file, returns a list with the number of times each character within that file appears
# file -> list
def freq_counter(input):
    ls = ArrayList([None]*250)
    file = open(input, "r")
    for line in file:
        for char in line:
            increment(ls, ord(char))
    # read and map frequencies
    file.close()
    return ls






import unittest

class TestList(unittest.TestCase):

    def test_freq_counter(self):
        self.assertRaises(FileNotFoundError, freq_counter, "fake_file.txt")
        al_first = ArrayList([None]*250)
        set(al_first, 97, 3)
        set(al_first, 98, 2)
        set(al_first, 99, 1)
        self.assertEqual(freq_counter("first.txt"), al_first)




if __name__ == '__main__':
    unittest.main()
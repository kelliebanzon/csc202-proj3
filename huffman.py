from array_list import *


# a Huffman Tree is either:
# - a Huffman node (one or more children)
# - a Huffman leaf (no children)


# a Leaf has:
# - char: the ASCII value of the character
# - freq: the number of times that character occurs
class Leaf:
    def __init__(self, char, freq):
        self.char = char        # an int
        self.freq = freq        # an int
    def __eq__(self, other):
        return type(other) == Leaf and self.char == other.char and self.freq == other.freq
    def __repr__(self):
        return "{}, freq = {}".format(self.char, self.freq)


# a Node has:
# - char: the ASCII value of the character
# - freq: the number of times that character occurs
# - left: a Huffman Tree #TODO: fix this data defn
# - right: a Huffman Tree #TODO: fix this data defn
class Node:
    def __init__(self, char, freq, left, right):
        self.char = char        # an int
        self.freq = freq        # an int
        self.left = left        # a Huffman Tree
        self.right = right      # a Huffman Tree
    def __eq__(self, other):
        return type(other) == Node and self.char == other.char and self.freq == other.freq and self.left == other.left and self.right == other.right
    def __repr__(self):
        return "{}, freq = {}\n\tleft = {}\n\t{}".format(self.char, self.freq, self.left.__repr__(), self.right.__repr__())


# given a text file, returns a list with the number of times each character within that file appears
# file -> ArrayList
def freq_counter(input):
    ls = ArrayList([None]*250)
    file = open(input, "r")
    for line in file:
        for char in line:
            increment(ls, ord(char))
    file.close()
    return ls


# creates a string of the characters in a Huffman tree in a pre-order traversal
# tree -> string
def tree_values(tree):
    fin = ""
    if type(tree) == Leaf:
        fin += chr(tree.char)
        return fin
    elif type(tree) == Node:
        fin += tree_values(tree.left)
        fin += tree_values(tree.right)
    return fin


# compares two Huffman trees first by frequency, then by ASCII values
# tree tree -> boolean
def comes_before(a, b):
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if a.char < b.char:
            return True
        else:
            return False




import unittest

class TestList(unittest.TestCase):

    huff_example = Node(32, 13,
                        Node(32, 6, Leaf(32, 3), Leaf(98, 3)),
                        Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4)))
    tree0 = Node(32, 6, Leaf(32, 3), Leaf(98, 3))
    tree1 = Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))

    def test_freq_counter(self):
        self.assertRaises(FileNotFoundError, freq_counter, "fake_file.txt")
        al_first = ArrayList([None]*250)
        set(al_first, 97, 3)
        set(al_first, 98, 2)
        set(al_first, 99, 1)
        self.assertEqual(freq_counter("first.txt"), al_first)

    def test_tree_values(self):
        self.assertEqual(tree_values(self.tree0), " b")
        self.assertEqual(tree_values(self.tree1), "dca")
        self.assertEqual(tree_values(self.huff_example), " bdca")

    def test_comes_before(self):
        self.assertEqual(comes_before(self.tree0, self.tree1), True)
        self.assertEqual(comes_before(self.huff_example, self.tree0), False)
        self.assertEqual(comes_before(Leaf(32, 3), Leaf(98, 3)), True)


if __name__ == '__main__':
    unittest.main()
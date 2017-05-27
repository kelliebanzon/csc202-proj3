import array_list as al
import linked_list as ll


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
        return "[ {}, freq = {} ]".format(self.char, self.freq)


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
        return "{}, freq = {}\n\tleft = {}\n\tright = {}".format(self.char, self.freq, self.left.__repr__(), self.right.__repr__())


# given a text file, returns a list with the number of times each character within that file appears
# file -> ArrayList
def freq_counter(input):
    ls = al.ArrayList([None]*250)
    file = open(input, "r")
    for line in file:
        for char in line:
            al.increment(ls, ord(char))
    file.close()
    return ls


# creates a string of the characters in a Huffman tree in a pre-order traversal
# tree -> string
def tree_traversal(tree):
    fin = ""
    if type(tree) == Leaf:
        fin += chr(tree.char)
        return fin
    elif type(tree) == Node:
        fin += tree_traversal(tree.left)
        fin += tree_traversal(tree.right)
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


# given a list of frequencies, builds sorted linked_list of leaves
# list -> list
def build_sorted_leaves(list):
    sorted = ll.empty_list()
    for i in range(0, 250):
        if list.values[i] != None:
            sorted = ll.insert_sorted(sorted, Leaf(i, list.values[i]), comes_before)
    return sorted


# given a list of character occurrences, builds a Huffman tree
# list -> tree
def build_tree(list):
    sorted = build_sorted_leaves(list)  # TODO: re-nest build_sorted_leaves
    while ll.length(sorted) > 1:        # TODO: inefficient
        tup = ll.remove(sorted, 0)
        first = tup[0]
        sorted = tup[1]
        tup = ll.remove(sorted, 0)
        second = tup[0]
        sorted = tup[1]
        if first.char < second.char:
            char = first.char
        else:
            char = second.char
        node = Node(char, first.freq+second.freq, first, second)
        sorted = ll.insert_sorted(sorted, node, comes_before)
    return node


# given a Huffman tree, returns a list of the keys for each Leaf
# tree -> list
def build_codes(tree, ls = al.ArrayList([None]*250), acc = ""):
    if type(tree) == Leaf:
        al.set(ls, tree.char, acc)
    else:
        build_codes(tree.left, ls, acc+"0")
        build_codes(tree.right, ls, acc+"1")
    return ls




# ----------------------------------------------------------------------------------------------------------------------

import unittest

class TestList(unittest.TestCase):

    huff_list = al.set(al.set(al.set(al.set(al.set(al.ArrayList([None]*250), 97, 4), 98, 3), 99, 2), 100, 1), 32, 3)
    huff_tree = Node(32, 13,
                     Node(32, 6, Leaf(32, 3), Leaf(98, 3)),
                     Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4)))
    tree0 = Node(32, 6, Leaf(32, 3), Leaf(98, 3))
    tree1 = Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))

    def test_freq_counter(self):
        self.assertRaises(FileNotFoundError, freq_counter, "fake_file.txt")
        al_first = al.ArrayList([None]*250)
        al.set(al_first, 97, 3)
        al.set(al_first, 98, 2)
        al.set(al_first, 99, 1)
        self.assertEqual(freq_counter("first.txt"), al_first)

    def test_tree_traversal(self):
        self.assertEqual(tree_traversal(self.tree0), " b")
        self.assertEqual(tree_traversal(self.tree1), "dca")
        self.assertEqual(tree_traversal(self.huff_tree), " bdca")

    def test_comes_before(self):
        self.assertEqual(comes_before(self.tree0, self.tree1), True)
        self.assertEqual(comes_before(self.huff_tree, self.tree0), False)
        self.assertEqual(comes_before(Leaf(32, 3), Leaf(98, 3)), True)

    def test_build_sorted_leaves(self):
        self.assertEqual(build_sorted_leaves(self.huff_list),
                         ll.Pair(Leaf(100, 1), ll.Pair(Leaf(99, 2), ll.Pair(Leaf(32, 3), ll.Pair(Leaf(98, 3), ll.Pair(Leaf(97, 4)))))))

    def test_build_tree(self):
        self.assertEqual(build_tree(self.huff_list), self.huff_tree)
        self.assertEqual(build_tree(al.set(al.set(al.ArrayList([None]*250), 32, 3), 98, 3)), self.tree0)
        self.assertEqual(build_tree(freq_counter("first.txt")),
                         Node(97, 6, Leaf(97, 3), Node(98, 3, Leaf(99, 1), Leaf(98, 2))))

    def test_build_codes(self):
        self.assertEqual(build_codes(self.huff_tree),
                         al.set(al.set(al.set(al.set(al.set(al.ArrayList([None]*250), 32, "00"), 98, "01"), 100, "100"), 99, "101"), 97, "11"))
        self.assertEqual(build_codes(build_tree(self.huff_list)),
                         al.set(al.set(al.set(al.set(al.set(al.ArrayList([None] * 250), 32, "00"), 98, "01"), 100, "100"), 99, "101"), 97, "11"))



if __name__ == '__main__':
    unittest.main()
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
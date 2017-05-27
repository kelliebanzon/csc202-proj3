# AnyList is either:
# - None
# - Pair(value, AnyList)

class Pair:
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))


# returns an empty list
#     -> AnyList
def empty_list():
    return None


# inserts a given value at a given position in a given list
# AnyList integer value -> AnyList
def add(list, index, value):
    if (list == None and index >= 1) or index < 0:
        raise IndexError
    elif index == 0:
        return Pair(value, list)
    else:
        return Pair(list.first, add(list.rest, index-1, value))


# returns the length of a given list
# AnyList -> int
def length(list):
    if list == None:
        return 0
    else:
        return 1 + length(list.rest)



# returns the value of the list at a given index
# AnyList int -> value
def get(list, index):
    if (list == None and index >= 0) or index < 0:
        raise IndexError
    elif index == 0:
        return list.first
    else:
        return get(list.rest, index-1)


# replaces the value at a given index with the given value
# AnyList int value -> AnyList
def set(list, index, value):
    if (list == None and index >= 0) or index < 0:
        raise IndexError
    elif index == 0:
        return Pair(value, list.rest)
    else:
        return Pair(list.first, set(list.rest, index-1, value))


# removes the value at a given index
# returns a tuple with the old value and the updated list
# AnyList int -> value AnyList
def remove(list, index):
    if list == None:
        raise IndexError()
    elif index == 0:
        return list.first, list.rest
    else:
        fin = remove(list.rest, index - 1)
        return fin[0], Pair(list.first, fin[1])


# inserts a value into a sorted list in ascending order according to a given comparison function
# AnyList value function -> AnyList
def insert_sorted(list, val, func):
    if list == None or func(val, list.first):
        return Pair(val, list)
    else:
        return Pair(list.first, insert_sorted(list.rest, val, func))
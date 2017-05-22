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




# Iterator
class Iterator:
    def __init__(self, list):
        self.list = list        # a Linked List
    def __eq__(self, other):
        return type(other) == Iterator and self.list == other.list
    def __repr__(self):
        return self.list.__repr__()


# given a list, returns an Iterator of that list
# list -> Iterator
def object_iterator(list):
    return Iterator(list)


# checks whether there is another value in the iterator
# list -> boolean
def has_next(itr):
    return (itr.list != None)


# returns the next value in the iterator
# iterator -> value
def next(itr):
    if not has_next(itr):
        raise StopIteration()
    else:
        f = itr.list.first
        itr.list = itr.list.rest
        return f


# returns the next value in the list
# list -> value
def yield_iterator(list):
    if list != None:
        yield list.first
        yield from yield_iterator(list.rest)
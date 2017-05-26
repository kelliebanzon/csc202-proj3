# an ArrayList has:
# - values: a list of values
# - length: a length (an int representing the number of values in the list)
# - fixed: the capacity of the list
class ArrayList:
    def __init__(self, ls = []):
        count = 0
        for value in ls:
            count = count + 1
        self.length = count               # the length of the list (the number of values)
        self.fixed = count                # the fixed length of the list (the number of spaces)
        self.values = [None] * count      # the list of values
        for i in range(0, count):
            self.values[i] = ls[i]

    def __eq__(self, other):
        if type(other) != ArrayList:
            return False
        for i in range(0, self.length):
            if self.values[i] != other.values[i]:
                return False
        return True

    def __repr__(self):
        fin = ""
        for i in range(0, self.length):
            if i != self.length - 1:
                fin += str(self.values[i]) + ", "
            else:
                fin += str(self.values[i])
        return fin


# returns an empty list
#        -> ArrayList
def empty_list():
    return ArrayList([])


"""def insert(list, func, val):
    if list.length == 0:
        raise IndexError
    else:
        new = [None] * (list.length+1)
        for i in range(list.length):
            if func(val, list.values[i]):
                list = add_double(list, i, val)
                return list
        list = add_double(list, i+1, val)
        return list"""



# adds a given value to a given index in the list
# ArrayList int value -> ArrayList
def add(curr, index, val):
    if index > curr.length or index < 0:
        raise IndexError
    else:
        new = [None] * (curr.length+1)
        for i in range(0, index):
            new[i] = curr.values[i]
        new[index] = val
        for i in range(index, curr.length):
            new[i+1] = curr.values[i]
        curr.values = new
        curr.length = curr.length + 1
        curr.fixed = curr.length
        return curr

def add_grow20(curr, index, val):
    if index > curr.length or index < 0:
        raise IndexError
    elif curr.length == curr.fixed:
        curr.fixed = curr.fixed + 20
        new = [None] * curr.fixed
        for i in range(0, index):
            new[i] = curr.values[i]
        new[index] = val
        for i in range(index, curr.length):
            new[i + 1] = curr.values[i]
        curr.values = new
        curr.length = curr.length + 1
    elif curr.values[index] == None:
        curr.values[index] = val
        curr.length = curr.length + 1
    else:
        new = [None]*(curr.fixed)
        for i in range(0, index):
            new[i] = curr.values[i]
        new[index] = val
        for i in range(index+1, curr.length+1):
            new[i] = curr.values[i-1]
        curr.values = new
        curr.length = curr.length + 1
    return curr

def add_double(curr, index, val):
    if index > curr.length or index < 0:
        raise IndexError
    elif curr.length == curr.fixed:
        if curr.fixed == 0:
            curr.fixed = 1
        else:
            curr.fixed = (curr.fixed * 2)
        test = [None] * curr.fixed
        for i in range(0, index):
            test[i] = curr.values[i]
        test[index] = val
        for i in range(index, curr.length):
            test[i + 1] = curr.values[i]
        curr.values = test
        curr.length = curr.length + 1
    elif curr.length != 0 and curr.values[index] == None:
        curr.values[index] = val
        curr.length = curr.length + 1
    else:
        new = [None]*(curr.fixed)
        for i in range(0, index):
            new[i] = curr.values[i]
        new[index] = val
        for i in range(index+1, curr.length+1):
            new[i] = curr.values[i-1]
        curr.values = new
        curr.length = curr.length + 1
    return curr


# returns the length of a given list
# ArrayList -> int
def length(list):
    return list.length


# returns the value of the list at a given index
# ArrayList int -> value
def get(list, index):
    if index >= list.length or index < 0:
        raise IndexError
    else:
        return list.values[index]


# replaces the value at a given index
# ArrayList int value -> ArrayList
def set(list, index, value):
    if index >= list.length or index < 0:
        raise IndexError
    else:
        list.values[index] = value
        return list

# increments the value at a given index by 1
# note: only works for an ArrayList of numbers
# note: uses mutation
# ArrayList -> ArrayList
def increment(list, index):
    if index < 0 or index > list.length-1:
        raise IndexError
    elif list.values[index] == None:
        list.values[index] = 1
    else:
        list.values[index] += 1
    return list


# removes the value at a given index
# return the old value and the updated list
# ArrayList int -> value ArrayList
def remove(list, index):
    if index >= list.length or index < 0:
        raise IndexError
    else:
        temp = list.values[index]
        return (temp, remove_index(list, index))


# removes the value at a given index
# returns the updated list
# ArrayList int -> ArrayList
def remove_index(list, index):
    if index >= list.length or index < 0:
        raise IndexError
    else:
        ls = [None] * list.fixed
        for i in range(0, index):
            ls[i] = list.values[i]
        for i in range(index+1, list.length):
            ls[i-1] = list.values[i]
        for i in range(list.length, list.fixed):
            ls[i] = None
        list.values = ls
        list.length -= 1
        return list


# execute a given function on every object of a given list
# ArrayList function -> None
def foreach(list, func):
    for val in list.values:
        func(val)
    return None


# returns True if the first value is less than the second, returns False otherwise
# value value -> boolean
def less_than(a, b):
    if a <= b:
        return True
    else:
        return False


# sort a list by a given function
# ex. [20, 11, 82, 3] -> [3, 11, 20, 82]
# [20]
# [11, 20]
# [11, 20, 82]
# [3, 11, 20, 82]
# ArrayList -> ArrayList
def sort(list, func, new = empty_list()):
    for i in range(0, list.length):
        j = 0
        while j <= new.length-1 and func(list.values[i], new.values[j]) == False:
            j += 1
        new = add(new, j, list.values[i])
    list = ArrayList(new.values)
    return list


def sort_no_mute(list, func, new = empty_list()):
    for i in range(0, list.length):
        j = 0
        while j <= new.length-1 and func(list.values[i], new.values[j]) == False:
            j += 1
        new = add(new, j, list.values[i])
    new_list = ArrayList(new.values)
    return new_list
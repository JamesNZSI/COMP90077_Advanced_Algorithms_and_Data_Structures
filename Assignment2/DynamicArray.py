import random


class ArrayObject:
    def __init__(self):
        self.array = []
        # next insert value index
        self.index = 0


def insert(array:ArrayObject, x):
    if(array.index == 0):
        array.array = [x]
    else:
        resize(array)
        array.array[array.index] = x

    array.index += 1
    return array


def resize(array:ArrayObject):
    if(len(array.array) > (array.index * 4)):
        # shrink array
        new_array_len = int(len(array.array) / 2)
        # print("DA shrink to ", new_array_len)
    elif(array.index == (len(array.array))):
        # expand array
        new_array_len = len(array.array) * 2
        # print("DA expand to ", new_array_len)
    else:
        # no need to resize
        return

    new_array = [None for i in range(new_array_len)]
    # copy all elements from old array to new array
    for i in range(array.index):
        new_array[i] = array.array[i]
        array.array[i] = None
    # replace old array
    array.array = new_array
    return array


def delete(array:ArrayObject, key):
    key_idx = -1
    for i in range(array.index):
        # element (id, key)
        if(array.array[i][1] == key):
            key_idx = i
            break
    # swap key and the last value
    if(key_idx != -1):
        array.array[key_idx] = array.array[array.index - 1]
        array.array[array.index - 1] = None
        array.index -= 1
    # shrink array if necessary
    resize(array)
    return array


def search(array:ArrayObject, key):
    key_idx = -1
    for i in range(array.index):
        # element (id, key)
        if(array.array[i][1] == key):
            key_idx = i
            break
    if(key_idx == -1):
        return None
    else:
        return array.array[key_idx]


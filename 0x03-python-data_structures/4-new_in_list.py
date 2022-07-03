#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listLen = len(my_list)
    newList = my_list[:]
    if idx < 0:
        return newList
    elif idx >= listLen:
        return newList
    else:
        newList[idx] = element
        return newList

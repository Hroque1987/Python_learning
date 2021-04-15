def unique_in_order(iterable):
    unique_list = []
    n = None
    for item in iterable:
        if n == None:
            unique_list.append(item)
            n = 0

        elif item == unique_list[n]:
            pass

        else:
            unique_list.append(item)
            n += 1

    return unique_list

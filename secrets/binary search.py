def binary_search(items, search_item):
    index = -1
    first = 0
    last = len(items) - 1
    found = False
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            index = midpoint
            found = True
        elif items[midpoint] < search_item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return index

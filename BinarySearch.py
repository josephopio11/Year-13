def binary_search(list_of_items, search_item):
    found = False
    search_failed = False

    # //Set boundaries of our search
    first = 0
    last = len(list_of_items) - 1

    while not found and not search_failed:
        middle = (first + last) // 2
        if list_of_items[middle] == search_item:
            found = True
        elif first >= last:
            search_failed = True
        elif list_of_items[middle] > search_item:
            last = middle - 1
        else:
            first = middle + 1
    if found:
        return middle
    else:
        return -1


our_list = [6, 8, 15, 19, 22, 23, 52, 53, 55, 57, 63, 66, 70, 77, 78, 81, 88, 90, 93, 94, 95, 96, 112, 119, 122, 138, 140, 145, 148, 154, 156, 161, 173, 174, 179, 208, 210, 213, 217, 225, 226, 229, 230, 236, 249, 257, 264, 273, 274, 278, 282, 284, 292, 293, 298, 306, 311, 312, 314, 315, 329, 333, 336, 337, 339, 343, 344, 357, 358, 363, 372, 381, 387, 388, 392, 402, 410, 422, 425, 433, 441, 461, 465, 479, 481, 486, 487, 494]

user_search = int(input("Enter the number you want to search for: "))

print(binary_search(our_list, user_search))

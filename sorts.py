def insertion_sort(items):
    number_of_items = len(items)
    for value in range(number_of_items):
        item_to_be_inserted = items[value]
        current_item = value - 1
        while items[current_item] > item_to_be_inserted and current_item > -1:
            items[current_item + 1] = items[current_item]
            current_item = current_item - 1
        items[current_item + 1] = item_to_be_inserted

def bubble_sort(items):
    number_of_items = len(items)
    passes = 1
    swapped = True
    while swapped:
        swapped = False
        for index in range(number_of_items - 1):
            if items[index] > items[index+1]:
                # temp = items[index]
                # items[index] = items[index+1]
                # items[index+1] = temp
                items[index], items[index+1] = items[index+1], items[index]
                swapped = True
        passes += 1


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
    


def linear_search(Items, SearchItem):
    MaxIndex = len(Items)
    Found = False
    Index = -1
    while not Found or Index >= MaxIndex:
        Index = Index + 1
        if str(Items[Index]) == SearchItem:
            Found = True

    if Found == True:
        return True
    else:
        return False
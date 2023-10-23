def bubble_sort(items):
    num_items = len(items)
    passes = 1

    while passes < num_items:

        for current in range(num_items - 1):
            if items[current] > items[current+1]:
                temp = items[current]
                items[current] = items[current+1]
                items[current+1] = temp 

        passes = passes + 1


# better code for bubble sort:
def bubble_sort(items):
    num_items = len(items)
    passes = 1
    swapped = True
    while swapped == True:
        swapped = False
        for current in range(num_items - passes):
            if items[current] > items[current+1]:
                temp = items[current]
                items[current] = items[current+1]
                items[current+1] = temp
                swapped = True 
        passes = passes + 1

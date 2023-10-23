items = [4, 12, 0, 7, 1, 8, 6, 15, 18, 13]

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

print(items)
bubble_sort(items)
print(items)
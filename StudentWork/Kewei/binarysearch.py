def binarySearch(array, value):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2

    output = 0
    found = False

    if value < array[0] or value > array[len(array) - 1]:
        output = -1

    while found == False and output != -1:
        if value == array[mid]:
            output = mid
            found = True
        elif value < array[mid]:
            mid = (mid + low) // 2
        else:
            mid = (mid + high) // 2

    return output

searchitem = int(input("What are you searching for? "))
array = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(binarySearch(array, searchitem))

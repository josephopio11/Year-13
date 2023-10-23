def insertion_sort(items):
    number_of_items = len(items)
    for value in range(number_of_items):
        item_to_be_inserted = items[value]
        current_item = value - 1
        while items[current_item] > item_to_be_inserted and current_item > -1:
            items[current_item + 1] = items[current_item]
            current_item = current_item - 1
        items[current_item + 1] = item_to_be_inserted

my_items = [4, 12, 0, 7, 1, 8, 6, 15, 18, 13]

print(my_items)
insertion_sort(my_items)
print(my_items)
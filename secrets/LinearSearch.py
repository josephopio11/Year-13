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


# test values
Items = [8, 7, 1, 5, 2, 9, 10, 4, 6, 3]
SearchValue = input("Please enter the value you are searching for: ")

linear_search(Items,SearchValue)

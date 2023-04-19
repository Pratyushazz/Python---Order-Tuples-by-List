from operator import itemgetter

# input
original_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# sort the list using the sorted() function with itemgetter() function as its key parameter
ordered_list = sorted(original_list, key=itemgetter(1))

# output
print(ordered_list)

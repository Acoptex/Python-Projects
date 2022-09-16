# check for duplicates in the list
my_list=['a','b','c','d','b','m','n','n']
duplicates=[]
for value in my_list:
    if my_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]



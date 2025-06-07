'''
List
'''

# remove items --------------------------------------------------------------------------------------------------------------------------------------------------------
lis1 = list(range(1,11))
print(f"Orignial list : {lis1}")
# output :- Orignial list : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. remove()
# remove method takes only one argument, that exists in the list
lis1.remove(2) 
print(f"Remove method : {lis1}")
#print(f"Remove method : {lis1.remove(2)}")  : output = None
# output :- Remove method : [1, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. pop()
lis1.pop(5) # we pass the index of the element we wish to remove
print(f"Pop method : {lis1}")
# output :- Pop method : [1, 3, 4, 5, 6, 8, 9, 10]

# 3. del()
del lis1[2]     # if we don't pass any index, leave it empty, it will delete the entire list
print(f"del method : {lis1}")
# output :- del method : [1, 3, 5, 6, 8, 9, 10]

# 4. clear()
# this method clears the list
lis1.clear()
print(f"Clear method : {lis1}")
# output :- Clear method : []

# to copy a list ------------------------------------------------------------------------------------------------------------------------------------------------------------
lis1 = list(range(1,11))
print(f"The original list :\n{lis1}\n")
# output :- The original list :
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. copy()
lis2 = lis1.copy()
print(f"Copy method. Copied list :\n{lis2}\n")
# output :-Copy method. Copied list :
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2. list()
lis3 = list(lis1)
print(f"List method. New list from this method :\n{lis3}\n")
# output :- List method. New list from this method :
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3. slice operator
lis4 = lis1[:]
print(f"Slice operator method. New list from this method :\n{lis4}\n")
# output :- Slice operator method. New list from this method :
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


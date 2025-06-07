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

# to join two list ------------------------------------------------------------------------------------------------------------------------------------------------------------
lis1 = list(range(1,5))
lis2 = list(range(5,11))
print(f"The original list 1: {lis1}")
print(f"The original list 2: {lis2}")
# output : The original list 1: [1, 2, 3, 4]
# The original list 2: [5, 6, 7, 8, 9, 10]


# 1. + operator
lis3 = lis1+lis2
print(f"Using + operator : {lis3}")
# output : Using + operator : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2. append() method
for x in lis2:
    lis1.append(x)
print(f"Using append method : {lis1}")
# output : Using append method : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# 3. extend() method
#lis4 = lis1.extend(lis2) # output = None
lis1.extend(lis2)
print(f"Using extend method : {lis1}")
# output :Using extend method : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]


# 4. list comprehension
lis4 = [item for sublis in [lis1,lis2] for item in sublis]
print(f"Using list comprehension : {lis4}")
# output :Using list comprehension : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]

# Index -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# syntax : list.index(elmnt, start, end)
# only takes one element of the list as argument
fruit = ['apple', 'banana', 'cherry']

x = fruit.index("cherry")
print(x)    # it returns the index of the element specified in the provided list
# output  : 2

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
y = fruits.index("cherry", 4)
print(y) # here search begins from the index 4
# output  : 6

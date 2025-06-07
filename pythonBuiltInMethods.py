'''
method : bin()
args : only take one argument of type `Integer` only
returns : (string) binary form of the integer. Data 
'''
x = bin(36) # input must need to be an integer
print(x)  # The result will always have the prefix 0b
# output : 0b100100
print(type(x)) # the result type is `string`
# output : <class 'str'>
print(x[2:])  # trimming to get the bits only
# output : 100100

'''
method : abs()
description: The abs() function returns the absolute value of the specified number.
args : n	Required. A number
return : (float) the absolute value of the specified number
'''
x = abs(3+5j) # Return the absolute value of a complex number
print(x)
# output : 5.830951894845301

print(type(x)) 
# output : <class 'float'>

y = abs(-13+45-30)
print(y)
# output : 2

'''
method : all()
description : The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
When used on a dictionary, the all() function checks if all the keys are true, not the values.
args : An iterable object 
returns : (bool) True or False
'''
# suppose below variables are output of different functions
out1 = "There is a river."
out2 = True
out3 = 12

mytuple = (out1, out2, out3)
x = all(mytuple)
print(f"For the tuple {mytuple} the output of all : {x}")
# output : For the tuple ('There is a river.', True, 12) the output of all : True

# for an empty iterable
empty_iter = {}
y = all(empty_iter)
print(f"For an empty iterable : {y}")
# output : For an empty iterable : True

'''
method : any()
description : The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False.
When used on a dictionary, the any() function checks if any of the keys are true, not the values.
args : 	An iterable object (list, tuple, dictionary)
returns : (bool) True or False
'''
mylist = [False, True, False]
x = any(mylist)
print(x) 
# output : True

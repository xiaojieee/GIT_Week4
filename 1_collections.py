# generic built-in functions
numbers = [45, 66, 12, 3, 99, 3.142, 42]
# number is a variable storing a list
print("min:", min(numbers), "max:", max(numbers))
# prints the minimum and maximum number
print("sum:", sum(numbers))
# prints the sum of all the numbers
print(f"Min: {min(numbers)} \tMax: {max(numbers)} \tSum: {sum(numbers)}")
# using a f-string to write it in one line
print("\n" + "#" * 50)

names_lucky_numbers = {'fred': 3, 'jim': 8, 'dave': 42}
print("min:", min(names_lucky_numbers), "max:", max(names_lucky_numbers))
print(f"Min: {min(names_lucky_numbers)} Max: {max(names_lucky_numbers)}")
print("Dictionaries implement min, max and sum on the KEYS not the VALUES!")
# min and max works on the keys, which is sorting the names by alphabetical

print("\n" + "#" * 50)

# useful tuple operations
a = 'hello'
b = 'goodbye'
print(f"a: {a} \t b: {b}")

a, b = b, a
# swapping the variables over
print(f"a: {a} \t b: {b}")

Gouda, Edam, Caithness = range(3)
print(Gouda, Edam, Caithness)
print(f"Gouda: {Gouda} \t Edam: {Edam} \t Caithness: {Caithness}")
print(f"Gouda: {1}")
# That also works

mytuple = 'a', 'b', 'c'
another = mytuple * 4
# This is operator overload
print(another)

thing = ('Hello')
print(type(thing))

thing = ('Hello',)
print(type(thing))
# be careful with trailing comma, it turns it into a tuple
thing = 'Hello',
print(type(thing))

print("\n" + "#" * 50)
# Python Lists

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[1])
# index notation, subscript notation
cheese[-1] = 'Red Leicester'
# minus -1 is counting from the right
# cheese[-1] assign a new value on the right index
print(cheese)

print("\n" + "#" * 50)

# Tuple and List Slicing
mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
print(mytuple[2:4])
# This slices it from 2 to 4 but not 4
# ('spam', 'tea')

print(mytuple[-4])
# bacon
# list is a constructor
# make my tuple into a list
mylist = list(mytuple)
print(mylist[1:])
# ['bacon', 'spam', 'tea', 'beans']
print(mylist[:2])
# ['eggs', 'bacon']
# slice from 0 to 1 (not including 2)


cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']
print("\n")
print(cheese)

del cheese[1:3]
# del is a statement deletes from 1 to 3 (so it deletes 1 and 2)
print(cheese)

print("\n" + "#" * 50)

# Extended Iterable Unpacking
# Iterable, something we can step over and over again

food_and_drink = 'eggs', 'bacon', 'spam', 'tea', 'coffee'
# this is a tuple
# x, y, z = food_and_drink
# above doesn't work because there's too many values to unpack

x, y, *z = food_and_drink
# the * on z means, take whatever is left shove it in z
print(f"x: {x} \t y:{y} \t z:{z}")
# while it is a tuples the extended iterable unpacking put it nicely in a list

x, *y, z = food_and_drink
print(f"x: {x} \t y:{y} \t z:{z}")

*x, y, z = food_and_drink
print(f"x: {x} \t y:{y} \t z:{z}")
# only one thing can have the asterisk

print("\n" + "#" * 50)

t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'

# *b will just scoop up whatever is in the middle
for a, *b, c in t1, t2:
    print(a, b, c)

print("\n" + "#" * 50)

# Adding Items to a List
#  on the left
print(cheese)
cheese[:0] = ['Cheshire', 'Ilchester']
# It slices the list and added cheshire and ilchester to the beginning
print(cheese)

# on the right
cheese += ['Oke', 'Devon Blue']
# += take my cheese list and concatenate oke and devon blue at the end
print(cheese)

cheese.extend(['Oke', 'Devon Blue'])
# extend method works with a list, need the square brackets or else it won't work
print(cheese)

# append - one item only
cheese.append('Red Fox')
# append - adding one object, so it doesn't need to be a list
print(cheese)

# anywhere
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print("New cheese list:", cheese)
cheese.insert(2, 'Cornish Brie')
# insert the new cheese cornish brie at position 2
print(cheese)
cheese[2:2] = ['Dairy Lea Triangles']
# slices it and insert dairy lea triangles in
print(cheese)
cheese.insert(0, 'Laughing Cow Triangles')
print(cheese)

print("\n" + "#" * 50)

# Removing items by position

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

saved = cheese.pop(1)
# pop off the thing at position 1
print("Saved1:", saved, ", Result:", cheese)

saved = cheese.pop()
print("Saved2:", saved, ", Result:", cheese)

print("\n" + "#" * 50)

# Removing items by content
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
print(cheese)
cheese.remove('Oke')
# left most first, it'll remove the first one it comes across
print(cheese)

# raise exception
# cheese.remove('Brie')

print("\n" + "#" * 50)

# Sorting
# list.sort sorts the list in place. Lists are mutable.
cheese = ['Cornish Yarg', 'Oke', 'Edam', 'Stilton']
print(f"Cheese before sorting: {cheese}")


cheese.sort()
print(f"Cheese after sorting: {cheese}")

cheese.sort(key=len)
# this is sorting it out from the shortest name to longest name

print(f"Cheese after sorting by length: {cheese}")

cheese.sort(key=len, reverse=True)
print(f"Cheese after sorting by length in reverse order: {cheese}")

# sorted is for any iterable
# it returns a list
# sorted is a function
hobby_tuple = 'Yoga', 'Pilates', 'Gardening', 'Baking', 'Rubiks Cubing'
print(hobby_tuple)


hobby_list_sorted = sorted(hobby_tuple)
print(f"Hobbies sorted using the sorted function (becomes a LIST): {hobby_list_sorted}")
# sorted can sort it in alphabetical

hobby_list_sorted = sorted(hobby_tuple, key=len)
print(f"Hobbies sorted using the sorted function by length: {hobby_list_sorted}")

hobby_list_sorted = sorted(hobby_tuple, reverse=True)
print(f"Hobbies sorted using the sorted function in reverse: {hobby_list_sorted}")
print("\n" + "#" * 50)


# Miscellaneous List Methods
print(cheese)
edam_count = cheese.count('Edam')
print(f"Edam appears {edam_count} time(s).")

edam_index = cheese.index('Edam')
print(f"Edam appears at position {edam_index}.")

# reverse the list in place
print(f"Before reverse: {cheese}")
cheese.reverse()
print(f"After reverse: {cheese}")

print("\n" + "#" * 50)

# List Methods

if cheese:
    # this checks if there's anything in the cheese list
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

# clear a list
cheese.clear()
# This clears the list
if cheese:
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

print(cheese)
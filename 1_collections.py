# generic built-in functions
numbers = [45, 66, 12, 3, 99, 3.142, 42]
print("min:", min(numbers), "max:", max(numbers))
print("sum:", sum(numbers))
print(f"Min: {min(numbers)} \tMax: {max(numbers)} \tSum: {sum(numbers)}")
print("\n" + "#" * 50)

names_lucky_numbers = {'fred': 3, 'jim': 8, 'dave': 42}
print("min:", min(names_lucky_numbers), "max:", max(names_lucky_numbers))
print(f"Min: {min(names_lucky_numbers)} Max: {max(names_lucky_numbers)}")
print("Dictionaries implement min, max and sum on the KEYS not the VALUES!")

print("\n" + "#" * 50)

# useful tuple operations
a = 'hello'
b = 'goodbye'
print(f"a: {a} \t b: {b}")

a, b = b, a

print(f"a: {a} \t b: {b}")

Gouda, Edam, Caithness = range(3)
print(Gouda, Edam, Caithness)

mytuple = 'a', 'b', 'c'
another = mytuple * 4
print(another)

thing = ('Hello')
print(type(thing))

thing = ('Hello',)
print(type(thing))

print("\n" + "#" * 50)
# Python Lists

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[1])
cheese[-1] = 'Red Leicester'
print(cheese)

print("\n" + "#" * 50)

# Tuple and List Slicing
mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
print(mytuple[2:4])
# ('spam', 'tea')

print(mytuple[-4])
# bacon
mylist = list(mytuple)
print(mylist[1:])
# ['bacon', 'spam', 'tea', 'beans']
print(mylist[:2])
# ['eggs', 'bacon']


cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']
print("\n")
print(cheese)

del cheese[1:3]
print(cheese)

print("\n" + "#" * 50)

# Extended Iterable Unpacking

food_and_drink = 'eggs', 'bacon', 'spam', 'tea'
# x, y, z = food_and_drink

x, y, *z = food_and_drink
print(f"x: {x} \t y:{y} \t z:{z}")

t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'

for a, *b, c in t1, t2:
    print(a, b, c)

print("\n" + "#" * 50)

# Adding Items to a List
#  on the left
print(cheese)
cheese[:0] = ['Cheshire', 'Ilchester']
print(cheese)

# on the right
cheese += ['Oke', 'Devon Blue']
print(cheese)

cheese.extend(['Oke', 'Devon Blue'])
print(cheese)

# append - one item only
cheese.append('Red Fox')
print(cheese)

# anywhere
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print("New cheese list:", cheese)
cheese.insert(2, 'Cornish Brie')
cheese[2:2] = ['Dairy Lea Triangles']
print(cheese)

print("\n" + "#" * 50)

# Removing items by position

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

saved = cheese.pop(1)
print("Saved1:", saved, ", Result:", cheese)

saved = cheese.pop()
print("Saved2:", saved, ", Result:", cheese)

print("\n" + "#" * 50)

# Removing items by content
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
print(cheese)
cheese.remove('Oke')
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
print(f"Cheese after sorting by length: {cheese}")

cheese.sort(key=len, reverse=True)
print(f"Cheese after sorting by length in reverse order: {cheese}")

# sorted is for any iterable
# it returns a list
hobby_tuple = 'Yoga', 'Pilates', 'Gardening', 'Baking', 'Rubiks Cubing'
print(hobby_tuple)

hobby_list_sorted = sorted(hobby_tuple)
print(f"Hobbies sorted using the sorted function (becomes a LIST): {hobby_list_sorted}")

hobby_list_sorted = sorted(hobby_tuple, key=len)
print(f"Hobbies sorted using the sorted function by length: {hobby_list_sorted}")

print("\n" + "#" * 50)

# Miscellaneous List Methods
print(cheese)
edam_count = cheese.count('Edam')
print(f"Edam appears {edam_count} time(s).")

edam_index = cheese.index('Edam')
print(f"Edam appears at opsition {edam_index}.")

# reverse the list in place
print(f"Before reverse: {cheese}")
cheese.reverse()
print(f"After reverse: {cheese}")

print("\n" + "#" * 50)

# List Methods

if cheese:
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

# clear a list
cheese.clear()
if cheese:
    print(f"Cheese list: {cheese}")
else:
    print("The cheese list is empty.")

print(cheese)
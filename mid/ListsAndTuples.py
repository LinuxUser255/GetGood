# fruits apple orange banana coconut
# list[] are mutable, most flexible data types in Python
# tuple() are immutable, less flexible data types in Python
# set() are unordered collections of unique elements, faster lookups

# list example
fruits = ["apple", "orange", "banana", "coconut"]

# tuple exampl
#fruits = ["apple", "orange", "banana", "coconut"]

# set example
# {"apple", "orange", "banana", "coconut"}

fruits[0] = "mango"
fruits.append("grape")
fruits.remove("coconut")
fruits.pop(0)
fruits.clear()

for fruit in fruits:
    print(fruit, end=" ")
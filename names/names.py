import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# provided algorithm had an O(n^2) runtime.
# Searching through a list is O(n) time, and for every entry in the first list, another O(n) search is done for every element in the second list.

duplicates = []  # Return the list of duplicates in this data structure

# store all names in a binary search tree. Initialize with the first name in names_1
names_tree = BinarySearchTree(names_1[0])

# add all names from the second to the end
for name_1 in names_1[1:]:
    names_tree.insert(name_1)

# seach for a repeated name in the tree. If found, append to the array
for name_2 in names_2:
    if names_tree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

print("\nStretch goal times:")

start_time = time.time()

# dictionary lookup is constant time, so store names in a dictionary
names_dictionary = dict()

# store discovered duplicates in an array
stretch_duplicates = []

# add all names in the first list to the dictionary
for name_1 in names_1:
    names_dictionary[name_1] = 1

# check if each name in the second list is in the dictionary
for name_2 in names_2:
    if name_2 in names_dictionary:
        stretch_duplicates.append(name_2)

# print time and duplicates
end_time = time.time()
print (f"{len(stretch_duplicates)} stretch_duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

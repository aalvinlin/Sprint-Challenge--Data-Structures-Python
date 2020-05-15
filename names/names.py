import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

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

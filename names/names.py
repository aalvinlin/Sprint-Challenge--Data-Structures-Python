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

# duplicates = []  # Return the list of duplicates in this data structure

# # store all names in a binary search tree. Initialize with the first name in names_1
# names_tree = BinarySearchTree(names_1[0])

# # add all names from the second to the end
# for name_1 in names_1[1:]:
#     names_tree.insert(name_1)

# # seach for a repeated name in the tree. If found, append to the array
# for name_2 in names_2:
#     if names_tree.contains(name_2):
#         duplicates.append(name_2)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

print("\nStretch goal times:")

# start_time = time.time()

# # dictionary lookup is constant time, so store names in a dictionary
# names_dictionary = dict()

# # store discovered duplicates in an array
# stretch_duplicates = []

# # add all names in the first list to the dictionary
# for name_1 in names_1:
#     names_dictionary[name_1] = 1

# print(names_dictionary)

# # check if each name in the second list is in the dictionary
# for name_2 in names_2:
#     if name_2 in names_dictionary:
#         stretch_duplicates.append(name_2)

# # print time and duplicates
# end_time = time.time()
# print (f"{len(stretch_duplicates)} stretch_duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

###################### Array implementation ######################

start_time = time.time()

# Strategy: use a probabilistic approach to determine whether searching is necessary
# assumption is that the number of duplicate names is far fewer than the number of total names

# store two-letter sequences from each name
# 1. first initial + last initial
# 2. second letter from first name + second letter from last name
# 3. third letter from first name + third letter from last name
# etc.

# If all five letter pairs match (or there aren't enough letters in the first or last name),
# then there is a high chance that the name is a duplicate. Only then will a conclusive search be carried out.

letter_pairs_to_check = 20

letter_pairs_lookup = [[0 for value in range(26 ** 2)] for value in range(letter_pairs_to_check)]

duplicates = []

# convert name to array of ASCII numbers
for name in names_1:
    
    # split first and last names
    split = name.lower().split(" ")
    first_name = split[0]
    last_name = split[1]

    # process up to the specified number of letter pairs, or up to the total number of letters in either first or last name
    for nth_letter_pair in range(min(letter_pairs_to_check, len(first_name), len(last_name))):

        first_letter = first_name[0]
        last_letter = last_name[0]

        # turn the first and last initial combination into an integer from 0-675
        # ex: AV would be 21, JR would be 251
        index = 26 * (ord(first_letter) - 97) + (ord(last_letter) - 97)

        # mark this combination as seen
        letter_pairs_lookup[nth_letter_pair][index] += 1

# print(letter_pairs_lookup)

possible_matches = 0

for name in names_2:

    # split first and last names
    split = name.lower().split(" ")
    first_name = split[0]
    last_name = split[1]

    # keep track for matches for letter pairs
    letter_pair_matches = 0

    # check up to the max length of the name
    max_letters_that_can_be_checked = min(letter_pairs_to_check, len(first_name), len(last_name))
    
    # process up to the specified number of letter pairs, or up to the total number of letters in either first or last name
    # for nth_letter_pair in range(min(letter_pairs_to_check, len(first_name), len(last_name))):
    for nth_letter_pair in range(max_letters_that_can_be_checked):

        first_letter = first_name[nth_letter_pair]
        last_letter = last_name[nth_letter_pair]

        # turn the first and last initial combination into an integer from 0-675
        # ex: AV would be 21, JR would be 251
        index = 26 * (ord(first_letter) - 97) + (ord(last_letter) - 97)

        # see if the current combination matches a combination stored in the other list
        if letter_pairs_lookup[nth_letter_pair][index] > 0:
            letter_pair_matches += 1

    # if all pairs matched, carry out a definitive search
    if letter_pair_matches == max_letters_that_can_be_checked:
        possible_matches += 1
        # print("possible match!", first_name, last_name)

print("possible matches", possible_matches)

print("doesn't work...number of false positives increases with more letter pairs checked, because pairs are checked independently of one another")

# print time and duplicates
end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print("possible matches:", possible_matches)
print (f"runtime: {end_time - start_time} seconds")


### test with built-in functions ###

# start_time = time.time()

# duplicates = set(names_1).intersection(set(names_2))

# end_time = time.time()
# # print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
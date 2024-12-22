age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
length_age = len(age)
length_age_set = len(age_set)
print(length_age)
print(length_age_set)       # The length of the list is bigger than the length of the set  

# Explain the difference between the following data types: string, list, tuple and set
 
 
# string: a sequence of characters, immutable, ordered, indexed, and supports slicing

# list: a collection of items, mutable, ordered, indexed, and supports slicing

# tuple: a collection of items, immutable, ordered, indexed, and supports slicing

# set: a collection of items, unordered, unindexed, mutable, and does not allow duplicate items

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_list = sentence.split()
sentence_set = set(sentence_list)
print(len(sentence_set))    # 9 unique words have been used

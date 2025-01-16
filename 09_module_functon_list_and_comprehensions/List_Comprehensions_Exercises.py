# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero_numbers = [i for i in numbers if i <= 0 and i % 2 == 0]
print(negative_and_zero_numbers)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

one_dimensional_list = [i for x in list_of_lists for y in x for i in y ]
print(one_dimensional_list)

# Using list comprehension create the following list of tuples:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
list_of_tuple = [
    tuple(i ** j if j > 0 else i for j in range(7))
    for i in range(11)
]
print(list_of_tuple)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [j for x in countries for j in x]
print(new_list)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dictionaies = dict([j for x in countries for j in x])
print(list_of_dictionaies)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# Transform to a list of concatenated strings
concatenated_names = [' '.join(name) for sublist in names for name in sublist]
print(concatenated_names)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_property = lambda points, property: (
    (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if property == 'slope' else
    points[0][1] - ((points[1][1] - points[0][1]) / (points[1][0] - points[0][0])) * points[0][0]
)

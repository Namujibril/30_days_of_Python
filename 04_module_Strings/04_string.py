# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding" + " " + "For" + " " + "All")

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
changed_to_upper = company.upper()
print(changed_to_upper)

# Change all the characters to lowercase letters using lower() method.
changed_to_lower = company.lower()
print(changed_to_lower)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalized = company.capitalize()
print(capitalized)
titled = company.title()
print(titled)
swapped = company.swapcase()
print(swapped)

# Cut(slice) out the first word of Coding For All string.
first_word = company[0]
print(first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Coding' in company) #True

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
language = "Python for Everyone"
print(language.replace('Everyone', "All"))

# Split the string 'Coding For All' using space as the separator (split()).
Coding = "Coding For All"
print(Coding.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# What is the character at index 0 in the string Coding For All?
print(companies[0])

# What is the last index of the string Coding For All?
print(len(Coding) - 1)

# What character is at index 10 in "Coding For All" string?
print(Coding[10])     #space

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = "pfe"
print(acronym.upper())

# Create an acronym or an abbreviation for the name 'Coding For All'.
acronym = "cfa"
print(acronym.upper())

# Use index to determine the position of the first occurrence of C in Coding For All.
print(Coding.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(Coding.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
Coding = "Coding For All People"
print(Coding.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[30:54])

# Does ''Coding For All' start with a substring Coding?
#  answer yes!

# Does 'Coding For All' end with a substring coding?
# answer No!

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
remove_space = '   Coding For All      '
print(remove_space.strip())

# Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
#answer is thirty_days_of_python

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
languages = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(languages))

# Use the new line escape sequence to separate the following sentences.
#1. I am enjoying this challenge.
#2. I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
#1. Name      Age      Country      City
#2. Asabeneh  250       Finland      Helsinki

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b)) 
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** { } = {}".format(a, b, a ** b))
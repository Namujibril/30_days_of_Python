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
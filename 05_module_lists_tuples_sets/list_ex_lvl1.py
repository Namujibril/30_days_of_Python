## Declare an empty ist
empty_lst = []

# declare a list with more than 5 items
football_plyrs = ['Ranaldo', 'Messi', 'Carlos', 'Figo', 'Kanu', 'Henry']

# Find the length of your list
length_lst = len(football_plyrs)

# Get the first item, the middle item and the last item of the list
print(football_plyrs[0])
print(football_plyrs[3])
print(football_plyrs[-1])

# Declare a list called mixed_data_types, put your name(name, age, height, maritalstatus, addresss)
mixed_data_types = ['Nazifi', 20, 71, 'single', 'No 223 zaria road']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of the companies in the list
length_it_companies = len(it_companies)

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[2] = "Tesla"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Nvidia")

# Insert an IT company in the middle of the companies list
it_companies[3] = "Microsoft"

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()

# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# Check if a certain company exists in the it_companies list.
check_company = 'Facebook' in it_companies       #True

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# slice out the middle IT company or companies from the list
print(it_companies[2:4])

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list 
it_companies.pop(2)

# remove the last IT company from the list
it_companies.pop(-1)

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
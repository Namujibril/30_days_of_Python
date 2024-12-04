# Exercise level 1

# Day 2: 30 Days of python programming
first_name = "Nazifi"
last_name = "Jibril"
full_name = "Nazifi Jibril"
country = "Nigeria"
city = "Kano"
age = 32
year = 1992
is_married = False
is_true = True
is_light_on = True
first_name, last_name, age = "Nazifi", "Jibril", 32

# Exercise level 2
print(type(first_name))   # <class 'str'>
print(type(last_name))    # <class 'str'>
print(type(age))          # <class 'int'> 
print(type(is_light_on))  # <class 'bool'>
print(type(is_true))      # <class 'bool'>
print(type(is_married))   # <class 'bool'>
print(type(year))         # <class 'int'>
print(type(country))      # <class 'str'>
print(type(city))         # <class 'str'>

# length build-in function
length_first_name = len(first_name)
print(length_first_name)
length_last_name = len(last_name)
print(length_last_name)

# compare length of first_name and last_name
print(length_first_name > length_last_name)

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

# calculate the radius of a circle
radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

# calculate the area of a circle from user
input_radius = int(input("Enter the radius of a circle: "))
area_of_circle = 3.14 * input_radius ** 2
print(area_of_circle)

# getting input from a user using build-in input function
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country name: ")
age = int(input("Enter your age: "))

# using help build-in function

reserve_words = help('keywords')
print(reserve_words)
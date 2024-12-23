# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'rita'
dog['color'] = 'black'
dog['breed'] = 'pug'
dog['legs'] = 4
dog['age'] = 2

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Nazifi', 'last_name': 'Jibril', 'gender': 'male', 'age': 32, 'marital status': 'single', 'skills': ['python', 'React', 'javascript'], 'country': 'Nigeria', 'city': 'Kano', 'address': 'No 723  Gwammaja'}

# Get the length of the student dictionary
lenth_student = (len(student))

# Get the value of skills and check the data type
skills_value = student['skills']
skills_data_type = (type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')

# Get the dictionary keys as a list
dict_keys_list = list(student.keys())

# Get the dictionary values as a list
dict_values_list = list(student.values()

# Change the dictionary to a list of tuples using items()
dict_items_list = list(student.items())
 
# Delete one of the items in dictionary
del student['marital status']

# Delete one of the dictionaries
del student

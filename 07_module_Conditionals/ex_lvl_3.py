
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,  # Corrected key
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Adding  new skill to the skills list
person['skills'].append('C++')

# Modifying the street in the address
person['address']['street'] = ' Musa UAC street'

# Printing the modified person dictionary
print(person)

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_list = person['skills']
# length of skill list
    if len(skills_list) % 2 != 0:
        middle_index = len(skills_list) // 2
        print(f"Middle skill: {skills_list[middle_index]}")
    else:
        print("Skills list is empty.")
else:
        print("No skills information in the person dictionary.")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")
else:
    print("No skills information in the person dictionary.")

# Check the person's skills to determine their title
if 'skills' in person:
    if 'skills' in person:
        skills = person['skills']  # Access the skills list
        if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
            print("He is a backend developer")
        elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
            print("He is a fullstack developer")
    else:
        print("Unknown title")
else:
    print("No skills information in the person dictionary.")

# If the person is married and if he lives in Finland.
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married .")
else:
    print("The person is either not married or does not live in Finland.")
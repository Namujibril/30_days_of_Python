 # Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('zainab', 'zahra', 'Aisha')
brothers = ('Ali', 'Hassan', 'umar') 

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
len(siblings)     # 6

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Muhammad', 'Khadija')
print(family_members)    # ('zainab', 'zahra', 'Aisha', 'Ali', 'Hassan', 'umar', 'Muhammad', 'Khadija')

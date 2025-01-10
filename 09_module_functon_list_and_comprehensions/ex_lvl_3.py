# Write a function called is_prime, which checks if a number is prime.
def is_prime (number):
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

# Write a functions which checks if all items are unique in the list.
def is_unique (list):
  return len(set(list)) == len(list)

# Write a function which checks if all the items of the list are of the same data type.
def is_homo (list):
  return len(set(type(item) for item in list)) == 1 

# Write a function which check if provided variable is a valid python variable.
def is_valid_variable (variable):
  return variable.isidentifier()

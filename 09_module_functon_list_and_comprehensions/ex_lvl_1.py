# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (a, b):
  sum = a + b
  return sum

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
  area = 3.14 * r * r
  return area 

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*args):
  sum = 0
  for i in args:
    if type(i) == int or type(i) == float:
      sum += i
    else:
      return "Please enter only numbers"
  return sum 

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit (c):
  f = (c * 9/5) + 32
  return f 

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season (month):
  if month == "March" or month == "April" or month == "May":
    return "Spring"
  elif month == "June" or month == "July" or month == "August": 
    return "Summer"
  elif month == "September" or month == "October" or month == "November": 
    return "Autumn"
  else:
    return "Winter" 
  
  # Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope (x1, y1, x2, y2):
  slope = (y2 - y1) / (x2 - x1)
  return slope

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn (a, b, c):
  x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return x1, x2

# Declare a function called print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list (list):
  for i in list:
    print(i) 

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list (list):
  reversed_list = []
  for i in range(len(list) - 1, -1, -1):
    reversed_list.append(list[i])
  return reversed_list 

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of item
def capitalize_list_items (list):
  capitalized_list = []
  for i in list:
    capitalized_list.append(i.upper())
  return capitalized_list

  # Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item (food_stuff, item):
  food_stuff.append(item)
  return food_stuff 

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item (food_stuff, item):
  food_stuff.remove(item)
  return food_stuff

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers (number):
  sum = 0
  for i in range(number + 1):
    sum += i
  return sum

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds (number):
  sum = 0
  for i in range(number + 1):
    if i % 2 != 0:
      sum += i
  return sum 

# Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens (number):
  sum = 0
  for i in range(number + 1):
    if i % 2 == 0:
      sum += i
  return sum 

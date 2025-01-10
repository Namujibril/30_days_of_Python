# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds (number):
 evens = 0
 odds = 0
 for i in range(number + 1):
  if i % 2 == 0:
   evens += 1
  else:
   odds += 1
 return evens, odds

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial (number):
  factorial = 1
  for i in range(1, number + 1):
    factorial *= i
  return factorial

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty (list):
  if len(list) == 0:
    return True
  else:
    return False 
  
  # Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean (list):
  mean = sum(list) / len(list)
  return mean

def calculate_median (list):
  list.sort()
  if len(list) % 2 == 0:
    median = (list[len(list) // 2] + list[(len(list) // 2) - 1]) / 2
  else:
    median = list[len(list) // 2]
  return median

def calculate_mode (list):
  mode = max(set(list), key = list.count)
  return mode

def calculate_range (list):
  list.sort()
  range = list[-1] - list[0]
  return range 

def calculate_variance (list):
  mean = calculate_mean(list)
  variance = sum((x - mean) ** 2 for x in list) / len(list)
  return variance 

def calculate_std (list):
  std = calculate_variance(list) ** 0.5
  return std 
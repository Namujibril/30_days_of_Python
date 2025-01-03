# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numbers is {sum}") 

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all even numbers is {sum_even}")
print(f"The sum of all odd numbers is {sum_odd}")
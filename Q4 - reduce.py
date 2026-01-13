from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_numbers = list(map(lambda x: x * x, even_numbers))

sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

print("Squared even numbers:", squared_numbers)
print("Sum of squared even numbers:", sum_of_squares)

"""
squares = []
for value in range(1,11):
    sqaure = value ** 2
    squares.append(sqaure)
print(squares)
"""
#better
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#list comprehension
squares=[value**2 for value in range(1,11)]
print(squares)
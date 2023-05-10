def make_sandwich(*ingredients):
    print("Making your sandwich with the following: ")
    for ingredient in ingredients:
        print(f"-{ingredient}")

make_sandwich('ham', 'pepperoni', 'lettuce', 'spinach')

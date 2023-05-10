print("Give me twonumbers, and I'll divide them.")
print("Enter 'q' to quit.")
#code depends on the try block executing successfully goes in the else block
while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num)/ int(second_num)
    except ZeroDivisionError:
        print("You ca't divide by 0!")
    else:
        print(answer)

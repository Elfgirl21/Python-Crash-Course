print("Give me twonumbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    answer = int(first_num)/ int(second_num)
    print(answer)

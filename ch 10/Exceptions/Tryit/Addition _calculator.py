print("Enter two numbers you wish to add. Enter 'q' to quit at anytime.")

while True:
    first_num = input("1st number: ")
    if first_num == 'q':
        break
    second_num = input("2nd number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("Please enter a number.")
    else:
        print(answer)
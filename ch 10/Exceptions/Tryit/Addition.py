print("Enter two numbers you wish to add.")


first_num = input("1st number: ")
    
second_num = input("2nd number: ")
   
try:
    answer = int(first_num) + int(second_num)
except ValueError:
    print("Please enter a number.")
else:
    print(answer)
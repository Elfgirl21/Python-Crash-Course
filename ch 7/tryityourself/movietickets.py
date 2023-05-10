message = "Please enter your age: "
age = input(message)
age = int(age)

active = True
while active:
   
    if age < 3:
        print("\nYour ticket is free.")
    elif (age >= 3 ) and (age <= 12):
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")
        repeat = input("\nWould like another ticket? (y/n)")
        if repeat == 'n':
            active = False
        else:
            active = True
        
print("\nThank you for buying tickets!")


    

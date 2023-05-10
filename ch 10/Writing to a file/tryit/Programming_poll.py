
filename = 'ch 10/Writing to a file/tryit/reason.txt'

with open(filename, 'a') as file_object:
    active = True
    while active:
        guest_input = input("What is the reason why you like programing? ")
        file_object.write(f"{guest_input}\n")
        repeat = input("Is there another quest that wish to take our poll? (y/n)")
        if repeat == 'n':
            active = False
        elif repeat == 'y':
            active = True
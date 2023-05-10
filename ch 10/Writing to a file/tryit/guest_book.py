
filename = 'ch 10\guest_book.txt'

with open(filename, 'a') as file_object:
    active = True
    while active:
        guest_input = input("Please enter your name: ")
        print(f"Hello {guest_input}!")
        file_object.write(f"{guest_input}\n")
        repeat = input("Is there another guest? (y/n)")
        if repeat == 'n':
            active = False
        else:
            active = True

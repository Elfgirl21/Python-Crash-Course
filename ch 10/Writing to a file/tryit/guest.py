guest_input = input("Please enter your name: ")
filename = 'ch 10\guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(guest_input)
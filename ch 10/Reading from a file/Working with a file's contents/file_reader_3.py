#once read file into memory, can do whatever w/ data

file_name = 'ch 10\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() #removes that whitespace on left of digit
    #rstrip() removes whitespace right of string

print(pi_string)
print(len(pi_string))
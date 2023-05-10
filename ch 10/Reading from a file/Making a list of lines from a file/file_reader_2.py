file_name = 'ch 10\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlins()

for line in lines:
    print(line.rstrip())
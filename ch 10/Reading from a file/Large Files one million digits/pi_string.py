
file_name = 'ch 10\pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() 

print(f"{pi_string[:52]}. . ")
print(len(pi_string))
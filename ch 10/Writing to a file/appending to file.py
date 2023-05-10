#append mode - nothing is erased, any new line will be added
filename = 'ch 10\Writing to a file\programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large atasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
file_name = 'ch 10\Reading from a file\Tryit\learned_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
    for line in lines:
        line = line.replace('Python', 'C')
        print(line)

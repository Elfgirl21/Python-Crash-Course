#General code for this type of program
filename = 'filename.txt'

with open(filename, 'r') as f:
    repeat = f.count('word')
    print(repeat)
    lower = f.lower().count('word')
    #catch all the instance of the word in lowercase as well
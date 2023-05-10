"""Reads multiple files"""

def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} is missing.")
    else:
        print(contents)

filenames = ['ch 10/Exceptions/Tryit/cats.txt', 'ch 10/Exceptions/Tryit/dogs.txt']
for filename in filenames:
    read_file(filename)
#Handling the fileNotFoundError Exception
#missing or mispelled or diff location
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f: #f or file_object encoding needed if system's default doesn't match file's
    contents =f.read()

"""
expection created by python is 
    FileNotFound: [Errno 2] No such file or directory: 'alice.txt'
"""

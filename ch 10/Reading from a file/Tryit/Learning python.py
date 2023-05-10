file_name = 'ch 10\Reading from a file\Tryit\learned_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

    lines = file_object.readlines()
    for line in lines:
        print(line)

    text = ''
    for content in contents:
        text += content.rstrip()

    print(text)

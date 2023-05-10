filename = 'alice.txt'

try: #if succeeds goes to else block
    with open(filename, encoding='utf-8') as f: 
        contents =f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    #count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has abou {num_words} words.")
    """
    Output:
        The file alice.txt has about 29465 words.
    """



# working w/ myltiple files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] #the 2nd text is left out for this ex
for filename in filenames:
    count_words(filenames)

"""
OutPut:
    The file alice.txt has about 29465 words.
    Sorry, the file siddhartha.txt doesn't exist.
    The file moby_dick.txt has about 215830 words.
    The file little_women.txt has about 189079 words.
"""
#two advantages: prevent users from seing trackback & program continue on
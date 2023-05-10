#write ()- doesn't add any newlines, write right next to each. use \n
filename = 'ch 10\Writing to a file\programming.txt'

with open(filename, 'w') as file_object: #'w' is write mode - if file exist, everything is earsed. 
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")
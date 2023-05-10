#writing to an empty file
#can write programs that read text back into memeory & work with it again later

#write text to file, open() with 2nd arg, tells python you want to write to file
filename = 'ch 10\Writing to a file\programming.txt'

with open(filename, 'w') as file_object: #'w' is write mode - if file exist, everything is earsed. 
    file_object.write("I love programing.")

#modes 'r' - read mode
#      'a' - appemd mode
#      'r+' - read & write mode
# w/out 2nd arg, default is read-only mode
#python only write strings to txt files, have to use str() when wanting to store numbers

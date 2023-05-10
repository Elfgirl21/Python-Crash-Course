# print(5/0) product a ZeroDivisionError Exception
#Using expection helps nontechinal users & projects your program from attackers
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
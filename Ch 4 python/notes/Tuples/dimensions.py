dimensions = (200,50) #tuple cannot change list or immutable
print(dimensions[0])   #tuple are simple data structure, only use to store data that shouldn't be changed
print(dimensions[1])
print("\n")
#dimensions[0]=250 trying to change the list but can't
for dimension in dimensions:
    print(dimension)
print("\n")
#writing over a tuple
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print("\n")
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
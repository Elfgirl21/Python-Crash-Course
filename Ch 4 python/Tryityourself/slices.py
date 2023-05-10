cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print("The first three items in the list are:")
print(cubes[0:3])
print("Three items from the middle of the list are:")
print(cubes[3:6])
print("The last three items in the list are:")
print(cubes[-3:])
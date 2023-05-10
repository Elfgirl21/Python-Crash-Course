from die import Die

#create a D6
die = Die() #we can always pass a different number for different die

#Make some rolls, and store results in alist
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
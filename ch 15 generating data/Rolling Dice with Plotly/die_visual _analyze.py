from die import Die

#create a D6
die = Die() #we can always pass a different number for different die

#Make some rolls, and store results in alist
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
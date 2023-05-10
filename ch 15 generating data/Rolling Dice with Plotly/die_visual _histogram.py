from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

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

#visualize the results
x_values = list(range(1, die.num_sides+1)) #Plotly doesn't accept results of range() directly
data = [Bar(x=x_values, y =frequencies)] #Bar()-class respresents a data set formatted as bar chart
    #class must be wrapped in square brackets b.c data set can have multiple elements

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config) #Layout()-class returns object specifies layout and config of graph
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
#offline() -function generate plot, needs dictionary containing the data and layout objects
#also accepts  filename
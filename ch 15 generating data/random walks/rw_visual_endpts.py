import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s = 15) 

    #Emphasize the endpoints
    ax.scattor(0, 0, c='green', edgecolors='none', s=100)
    ax.scattor(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100) #these points are drawn on top of all other points
    
    plt.show()

    #keep making new walks, as long as program is active
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break

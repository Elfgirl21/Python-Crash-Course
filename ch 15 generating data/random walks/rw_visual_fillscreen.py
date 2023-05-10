import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,7))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s = 1) 

    #Emphasize the endpoints
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100) #these points are drawn on top of all other points
    
    #Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    #keep making new walks, as long as program is active
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break

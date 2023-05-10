import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()

    #keep making new walks, as long as program is active
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break

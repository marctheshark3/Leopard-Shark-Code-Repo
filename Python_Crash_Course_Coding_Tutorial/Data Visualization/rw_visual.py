import matplotlib.pyplot as plt

from random_walks import RandomWalk

while True:
    # make the random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()
    # plotting the points
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15,9))
    points_numbers = range(rw.num_points)
    ax.scatter(rw.x, rw.y, c=points_numbers, cmap = plt.cm.Blues, edgecolors='none', s=1)

    #highlighting the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=100)

    #removing the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    #ax.scatter(rw.x, rw.y, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break



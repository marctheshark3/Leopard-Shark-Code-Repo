from random import choice

class RandomWalk:
    """Generating random walks"""

    def __init__(self, num_points = 5000):
        """ initializing the attributes for random walks"""
        self.num_points = num_points

        #walks start at 0,0
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """Calculate the walk"""

        #walk until we reach some length
        while len(self.x) < self.num_points:

            #decide which direction to go and how far
            x_direction = choice([1,-1])

            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_dist

            y_direction = choice([1, -1])

            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_dist

            # if we dont move then skip turn
            if x_step == 0 and y_step == 0:
                continue
            #get a new position
            new_x = self.x[-1] + x_step
            new_y = self.y[-1] + y_step

            self.x.append(new_x)
            self.y.append(new_y)



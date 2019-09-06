from random import randint

class Dice:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        for roll in range(10):
            my_roll = randint(1,self.sides)
            print(f"You rolled a {my_roll}")
    def change_dice_sides(self,new_sides):
        self.sides = new_sides
Dice().roll_die()

#change dice to 10 sides
print('\n 10 sided Die \n')
Dice().change_dice_sides(10)
Dice().roll_die()

#20 sided
print('\n 20 sided \n')
Dice().change_dice_sides(20)
Dice().roll_die()


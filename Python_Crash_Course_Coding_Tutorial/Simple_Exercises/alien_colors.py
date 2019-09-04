
def get_points(alien_color):
    if alien_color == 'green':
        print("You just earned 5 points for shooting an alien")
    elif alien_color =='yellow':
        print("You earned 10 points!")
    elif alien_color =='red':
        print("You earned 15 points!")
    else:
        print("You just earned 10 points")

get_points('red')
get_points('green')

def stage_of_life(age):
    if age < 2:
        print("The person of interest is a baby")
    elif age > 2 and age <= 4:
        print("The person of interest is a tolder")
    elif age > 4 and age <= 13:
        print("The person of interest is a kid")
    elif age > 13 and age <= 20:
        print("The person of interest is a teenager")
    elif age > 20 and age <= 65:
        print("The person of interest is an adult")
    else:
        print("The person of interest is an elder")

stage_of_life(15)
stage_of_life(7)
stage_of_life(33)
stage_of_life(99)
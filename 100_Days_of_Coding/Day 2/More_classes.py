from Classes_exercises import Restaurant, IceCreamStand

joes_icee = Restaurant(" Joe's Ice Cream and ICEEs",'Ice Cream')
joes_icee.describe_restraunt()
joes_icee.open_restraunt()

marios = IceCreamStand('Marios Ice Cream', 'Ice Cream')
marios_flavors = IceCreamStand('Marios Ice Cream', 'Ice Cream').get_flavors()

print("Mario's Current Flavors are:")
for flavor in marios_flavors:
    print(flavor)

marios.open_restraunt()
#sandwhich function with one parameter

def make_sammy(*ingredients):

    print("The ingredients for you Sammy are:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

make_sammy('tomatoes', 'mushrooms','avacado',' rye bread')
make_sammy('steak', 'mushrooms','onions', 'lettuce wrap', 'tomatoes')
make_sammy('Bacon', 'Lettuce','tomatoes',' white bread', '1000 island','mayo')


def make_car(car_make,car_model,**options):

    options[car_make] = 'Car Make'
    options[car_model] = 'Car Model'

    return options

car = make_car('subaru','outback',color = 'blue', tow_package = True)
print(car)



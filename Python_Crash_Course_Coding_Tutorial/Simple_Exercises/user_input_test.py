restaurant_input = input("How many people are in your party?")

restaurant_input = int(restaurant_input)

if restaurant_input >= 8:
    print("You will have to wait 15 minutes for the next table")
else:
    print("Your table is ready!")
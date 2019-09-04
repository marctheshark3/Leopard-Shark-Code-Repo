class Restaurant:

    def __init__(self,restraunt_name,cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restraunt(self):
        print(f"The restraunts name is: {self.restraunt_name} and the Cuisine is: {self.cuisine_type}")

    def open_restraunt(self):
        print(f"The {self.restraunt_name} is Open!")
    def set_number_served(self,served):
        self.number_served = served
    def increment_served(self,step):
        self.number_served += step

restaurant = Restaurant('Papa Johns','Pizza')

print(restaurant.restraunt_name)
print(restaurant.cuisine_type)

restaurant.describe_restraunt()
restaurant.open_restraunt()

jersey_mike = Restaurant('J Mikes',"Sandwhiches")
chipotle = Restaurant("Chipotle", 'Mexican')

jersey_mike.describe_restraunt()
chipotle.describe_restraunt()

jersey_mike.set_number_served(100)
print(jersey_mike.number_served)
jersey_mike.increment_served(5)
print(f"Jersey Mikes has served: {jersey_mike.number_served} guest")


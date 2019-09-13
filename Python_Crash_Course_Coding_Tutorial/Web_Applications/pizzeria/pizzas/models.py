from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A topic for our pizzas at the pizzeria"""
    name = models.CharField(max_length = 100)

    def __str__(self):
        """Return the name of the pizzas"""
        return self.name

class Topping(models.Model):
    """a topic for storing the toppings for the pizza"""
    # Cascade is used so that when the topic is deleted all entries
    # associated are deleted with this topic
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        """Return  the toppings for the pizza"""
        return f"{self.name}"
from django.db import models

# Create your models here.
class Pizza(models.Model):
    """"Stores the different types fo pizzas"""
    name = models.CharField(max_length = 50)

    def __str__(self):
        """Returns the name of the pizza"""
        return self.name

class Topping(models.Model):
    """Storing the toppings relative to the pizza class"""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)

    name = models.CharField(max_length = 50)

    def __str__(self):
        """Return the toppings of the pizza"""
        return f"{self.name}"
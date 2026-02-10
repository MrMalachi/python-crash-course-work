from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A name the user wants to assign to their pizza."""
    name = models.CharField(max_length=25)

    def __str__(self):
        """Returns a string representation of the 'Pizza' model (class)."""
        return self.name

class Topping(models.Model):
    """A user's toppings they want to add to their created pizza."""

    # Create a one-to-many relationship: one pizza with many toppings.
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)

    def __str__(self):
        """Returns a string representation of the 'Toppings' model (class)."""
        return self.name
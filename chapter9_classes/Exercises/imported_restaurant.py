"""A program that utilizes the restaurant module."""

from restaurant import Restaurant as Resto

# Create an instance (instantiation) using the imported Restaurant class.
mando_sando = Resto("mando-sando", "sandwich")


# Call one of the Restaurant's methods to show that the import works properly.
mando_sando.describe_restaurant()
mando_sando.open_restaurant()



# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, null=True)
    year_founded = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    HATCHBACK = "Hatchback"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupe"
    TRUCK = "Truck"

    CAR_TYPES = [
        ('SEDAN', "Sedan"),
        ('SUV', "SUV"),
        ('WAGON', "Wagon"),
        ('TRUCK', "Truck"),
        ('CONVERTIBLE', "Convertible"),
        ('COUPE', "Coupe"),
    ]

    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="models"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2024,
        validators=[MaxValueValidator(2024), MinValueValidator(1950)]
    )
    color = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

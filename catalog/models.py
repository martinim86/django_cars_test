from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
import datetime
class Cars(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="car name")
    image = models.ImageField(upload_to='images/')
    date_on = models.DateField()
    date_off = models.DateField(("Date"), default="2020-10-01")

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('cars-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

import uuid # Required for unique book instances

# class CarsInstance(models.Model):
#     """
#     Model representing a specific copy of a book (i.e. that can be borrowed from the library).
#     """
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
#     cars = models.CharField(max_length=200)
   
#     LOAN_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )

#     status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

#     class Meta:
#         ordering = ["id"]
        

#     def __str__(self):
#         """String for representing the Model object."""
#         return '{0} ({1})'.format(self.id, self.cars.name)
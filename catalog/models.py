from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        return self.name
import datetime
class Cars(models.Model):

    name = models.CharField(max_length=200, help_text="car name")
    image = models.ImageField(upload_to='images/')
    date_on = models.DateField()
    date_off = models.DateField(("Date"), default="2020-10-01")

    def get_absolute_url(self):

         return reverse('cars-detail', args=[str(self.id)])
    
    def __str__(self):

        return self.name


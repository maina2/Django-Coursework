from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    title = models.CharField(max_length=200)  # Add title field
    author = models.CharField(max_length=100)  # Add author field
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name  = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()  # Add title field
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")  # Renamed field name
    is_bestseller = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
     

    def __str__(self):
        return f"{self.title} ({self.rating})"
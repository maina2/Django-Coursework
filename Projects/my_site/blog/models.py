from django.db import models
from django.utils.text import slugify


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adress = models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title= models.CharField(max_length=150)
    excerpt= models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=100, blank=True)  # Allow blank for auto-generation
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)








from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def save(self, *args, **kwargs):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating must be between 1 and 5.")
        super().save(*args, **kwargs)
 
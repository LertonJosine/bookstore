from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_details", args=[str(self.pk)])
    
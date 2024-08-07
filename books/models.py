from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
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
    cover = models.ImageField(upload_to="cover/", blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_details", args=[str(self.pk)])
    
    class Meta:
        permissions = [
            ("special_status", "can read all books")   ]
        indexes = [models.Index(fields=['id'], name='id_index'),]

class Review(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    review = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"{self.review[:70]}..."
    
    
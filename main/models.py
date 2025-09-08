import uuid
from django.db import models

CATEGORY_CHOICES = [
    ("shoes", "Football Shoes"),
    ("jersey", "Jerseys & Kits"),
    ("ball", "Footballs"),
    ("gloves", "Goalkeeper Gloves"),
    ("accessories", "Accessories"),
    ("training", "Training Equipment"),
]


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="update"
    )
    brand = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.forms import ModelForm
from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "category",
            "brand",
            "stock",
            "rating",
            "thumbnail",
            "is_featured",
        ]

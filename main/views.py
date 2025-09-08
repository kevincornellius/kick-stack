from django.shortcuts import render

from main.models import Product


# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        "npm": "2406428781",
        "name": "Kevin Cornellius Widjaja",
        "class": "PBP E",
        "products": products,
    }

    return render(request, "main.html", context)

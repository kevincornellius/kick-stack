from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers

from main.forms import ProductForm
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

    return render(request, "pages/main/main.html", context)


def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "pages/main/add_product.html", context)


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {"product": product}

    return render(request, "pages/main/product_detail.html", context)


def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products_list = Product.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, product_id):
    try:
        products_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        products_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [products_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

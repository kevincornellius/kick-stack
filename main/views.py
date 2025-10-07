from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


# Create your views here.
@login_required(login_url="/login")
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        "npm": "2406428781",
        "name": "Kevin Cornellius Widjaja",
        "class": "PBP E",
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "username": request.user.username,
    }

    return render(request, "pages/main/main.html", context)


@login_required(login_url="/login")
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:show_main")

    context = {"form": form}
    return render(request, "pages/main/add_product.html", context)


@login_required(login_url="/login")
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
    data = [
        {
            "id": str(product.id),
            "name": product.name,
            "price": str(product.price),
            "description": product.description,
            "stock": product.stock,
            "user_id": product.user_id,
            "created_at": product.created_at.isoformat(),
            "updated_at": product.updated_at.isoformat(),
            "category": product.category,
            "brand": product.brand,
            "rating": str(product.rating),
            "thumbnail": product.thumbnail,
            "is_featured": product.is_featured,
        }
        for product in products_list
    ]
    return JsonResponse(data, safe=False)


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
        data = {
            "id": str(products_item.id),
            "name": products_item.name,
            "price": str(products_item.price),
            "description": products_item.description,
            "thumbnail": products_item.thumbnail,
            "is_featured": products_item.is_featured,
            "rating": str(products_item.rating),
            "stock": products_item.stock,
            "user_id": products_item.user_id,
            "created_at": products_item.created_at.isoformat(),
            "updated_at": products_item.updated_at.isoformat(),
            "category": products_item.category,
            "brand": products_item.brand,
            "username": products_item.user.username if products_item.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "pages/main/register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "pages/main/login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {"form": form}

    return render(request, "pages/main/edit_product.html", context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))


# @csrf_exempt
@require_POST
@login_required(login_url="/login")
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    stock = strip_tags(request.POST.get("stock"))
    category = strip_tags(request.POST.get("category"))
    brand = strip_tags(request.POST.get("brand"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured", "false").lower() == "true"
    rating = request.POST.get("rating", 0)
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        category=category,
        brand=brand,
        thumbnail=thumbnail,
        is_featured=is_featured,
        rating=rating,
        user=user,
    )

    new_product.save()
    return HttpResponse(b"Product created successfully", status=201)


# @csrf_exempt
@require_POST
@login_required(login_url="/login")
def edit_product_entry_ajax(request):
    product_id = strip_tags(request.POST.get("id"))
    product = get_object_or_404(Product, pk=product_id)

    if request.user != product.user:
        return HttpResponse(b"Unauthorized", status=401)

    if product is None:
        return HttpResponse(b"Product not found", status=404)

    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    stock = strip_tags(request.POST.get("stock"))
    category = strip_tags(request.POST.get("category"))
    brand = strip_tags(request.POST.get("brand"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured", "false").lower() == "true"
    rating = request.POST.get("rating", 0)

    product.name = name
    product.price = price
    product.description = description
    product.stock = stock
    product.category = category
    product.brand = brand
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.rating = rating

    product.save()
    return HttpResponse(b"Product updated successfully", status=200)


# @csrf_exempt
@require_POST
@login_required(login_url="/login")
def delete_product_entry_ajax(request):
    product_id = strip_tags(request.POST.get("id"))

    if not product_id:
        return HttpResponse(b"Product ID is required", status=400)

    product = get_object_or_404(Product, pk=product_id)

    if request.user != product.user:
        return HttpResponse(b"Unauthorized", status=401)

    if product is None:
        return HttpResponse(b"Product not found", status=404)

    product.delete()
    return HttpResponse(b"Product deleted successfully", status=200)


# @csrf_exempt
@require_POST
def register_ajax(request):
    try:
        username = strip_tags(request.POST.get("username"))
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            return JsonResponse(
                {"success": False, "message": "All fields are required"}, status=400
            )

        if password1 != password2:
            return JsonResponse(
                {"success": False, "message": "Passwords do not match"}, status=400
            )

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"success": False, "message": "Username already exists"}, status=400
            )

        # Create user using UserCreationForm for validation
        form_data = {
            "username": username,
            "password1": password1,
            "password2": password2,
        }
        form = UserCreationForm(form_data)

        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    "success": True,
                    "message": "Your account has been successfully created!",
                    "redirect": reverse("main:login"),
                },
                status=201,
            )
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            return JsonResponse(
                {"success": False, "message": "; ".join(errors)}, status=400
            )

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during registration"},
            status=500,
        )


# @csrf_exempt
@require_POST
def login_ajax(request):
    try:
        username = strip_tags(request.POST.get("username"))
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse(
                {"success": False, "message": "Username and password are required"},
                status=400,
            )

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Set last login cookie
            response = JsonResponse(
                {
                    "success": True,
                    "message": "Login successful!",
                    "redirect": reverse("main:show_main"),
                    "user": {"id": user.id, "username": user.username},
                }
            )
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse(
                {"success": False, "message": "Invalid username or password"},
                status=401,
            )

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during login"}, status=500
        )


# @csrf_exempt
@require_POST
def logout_ajax(request):
    try:
        logout(request)
        response = JsonResponse(
            {
                "success": True,
                "message": "Logout successful!",
                "redirect": reverse("main:login"),
            }
        )
        response.delete_cookie("last_login")
        return response

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during logout"}, status=500
        )

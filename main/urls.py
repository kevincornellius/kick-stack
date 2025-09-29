from django.urls import path
from main.views import (
    add_product,
    login_user,
    show_json,
    show_json_by_id,
    show_main,
    show_product,
    show_xml,
    show_xml_by_id,
    register,
    logout_user,
    edit_product,
    delete_product,
)


app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("add-product/", add_product, name="add_product"),
    path("product/<str:id>", show_product, name="show_product"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:product_id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:product_id>/", show_json_by_id, name="show_json_by_id"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("product/<str:id>/edit", edit_product, name="edit_product"),
    path("product/<str:id>/delete", delete_product, name="delete_product"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ResHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("checkout/", views.checkout, name="Checkout"),

]

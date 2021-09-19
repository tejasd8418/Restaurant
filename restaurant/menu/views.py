from django.shortcuts import render
from .models import foodItems, Contact, Orders
from math import ceil
import json

# Create your views here.
from django.http import HttpResponse


def index(request):
    allitems = []
    categoryItems = foodItems.objects.values('category', 'id')
    cats = {item['category'] for item in categoryItems}
    for cat in cats:
        fItems = foodItems.objects.filter(category=cat)
        n = len(fItems)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allitems.append([fItems, range(1, nSlides), nSlides])
    params = {'allitems':allitems}
    return render(request, 'menu/index.html', params)


def about(request):
    return render(request, 'menu/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'menu/contact.html')


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        ordern= Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                     zip_code=zip_code, phone=phone)
        ordern.save()
        thank = True
        id = ordern.order_id
        return render(request, 'menu/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'menu/checkout.html')

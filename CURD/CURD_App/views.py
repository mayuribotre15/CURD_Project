from django.shortcuts import render, redirect
from .models import Product
from .forms import InsertFrom
from django.http import HttpResponseRedirect
# Create your views here.

def show(r):
    prod = Product.objects.all()
    return render(r, 'CURD_App/index.html', {'prod': prod})

def insert(r):
    form = InsertFrom()
    if r.method == 'POST':
        form = InsertFrom(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(r, 'CURD_App/insert.html', {'form': form})

def delete(r, id):
    prod = Product.objects.get(id=id)
    prod.delete()
    return HttpResponseRedirect('/')

def update(r, id):
    prod = Product.objects.get(id=id)
    if r.method == 'POST':
        form = InsertFrom(r.POST, instance=prod)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(r, 'CURD_App/update.html', {'prod': prod})
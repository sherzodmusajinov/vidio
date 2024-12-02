from django.shortcuts import render
from django.template import loader
from .models import Book

# Create your views here.
def home_page(request):
    data = Book.objects.all()
    return render(request, 'index.html', {'d': data})
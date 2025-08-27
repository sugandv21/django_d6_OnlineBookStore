from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})

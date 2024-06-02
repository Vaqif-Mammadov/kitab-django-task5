# catalog/views.py

from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'catalog/register.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog/add_book.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from .forms import AddBookForm

# Create your views here.
def get_index(request):
    books = Book.objects.all()
    return render(request, "index.html", {'books':books})
    
def add_book(request):
    if request.method=="POST":
        form=AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = AddBookForm()
    return render(request, "books/addbook.html", {'form': form})
    
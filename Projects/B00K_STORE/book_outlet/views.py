from django.shortcuts import render
from book_outlet.models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html",{
          "book": books,
    })

def book_details (request,id):
    books = Book.objects.get(id=id)
    return render(request,"book_outlet/book-detail.html",{
        "title": books.title,
        "rating":books.rating,
        "is_bestseller":books.is_bestseller,
        "author":books.author


    })
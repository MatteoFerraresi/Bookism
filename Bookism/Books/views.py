from django.shortcuts import render
from .models import Books
from django.http import HttpResponse

# Create your views here.
def books_list(request):
    books = Books.objects.all().order_by('date')
    return render(request, 'books/books_list.html',{'books':books})

def book_detail(request, slug):
    #return HttpResponse(slug)

    book = Books.objects.get(slug=slug)
    return render(request, 'books/books_detail.html', {'book':book})
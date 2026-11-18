from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

SORT_FIELDS = {'title', 'author', 'genre'}


def index(request):
    sort = request.GET.get('sort', 'title')
    if sort not in SORT_FIELDS:
        sort = 'title'
    books = Book.objects.order_by(sort)
    form = BookForm()
    return render(request, 'todo_app/index.html',
                  {'books': books, 'form': form, 'sort': sort})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')


def mark_read(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.is_read = True
    book.save()
    return redirect('index')


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('index')
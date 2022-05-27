from django.shortcuts import render,redirect
from books.models import Books
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from books.forms import BookForm
from django.urls import reverse_lazy
# Create your views here.

class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "book_add.html"
    success_url =reverse_lazy("book-all")

class BookListView(ListView):
    model = Books
    template_name = "book_list.html"
    context_object_name ="Books"

class BookEditView(UpdateView):
    model = Books
    template_name = "book_edit.html"
    form_class = BookForm
    success_url = "book-all"
    pk_url_kwarg = "id"

class BookDetailView(DetailView):
    model = Books
    template_name = "book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

def bookdelete(request,*args,**kwargs):
    id=kwargs.get('id')
    Books.objects.get(id=id).delete()
    return redirect('book-all')






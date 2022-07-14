from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from books.models import Book, Author, Publisher


class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        return context

class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/author_detail.html'


class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'books/publisher_detail.html'

from .models import Book
from simple_search import search_form_factory

SearchForm = search_form_factory(Book.objects.all(),
                                 ['book_title'])

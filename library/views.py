from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from library.models import Book, DVD, Magazine

def book_list(request):
    context_dict = {'book_list': Book.objects.all()}
    return render(request, 'library/book_list.html', context_dict)


def book_details(request, book_id):
	context_dict = {'book_details': Book.objects.get(pk=book_id)}
	return render(request, 'library/book_details.html', context_dict)


def dvd_list(request):
    context_dict = {'dvd_list': DVD.objects.all()}
    return render(request, 'library/dvd_list.html', context_dict)


def dvd_details(request, dvd_id):
	context_dict = {'dvd_details': DVD.objects.get(pk=dvd_id)}
	return render(request, 'library/dvd_details.html', context_dict)


def magazine_list(request):
    context_dict = {'magazine_list': Magazine.objects.all()}
    return render(request, 'library/magazine_list.html', context_dict)


def magazine_details(request, magazine_id):
    context_dict = {'magazine_details': Magazine.objects.get(pk=magazine_id)}
    return render(request, 'library/magazine_details.html', context_dict)


def index(request):
    context_dict = {'avail_books': Book.objects.all(), 'avail_DVDs': DVD.objects.all(),
                    'avail_mags': Magazine.objects.all()}
    return render(request, 'library/index.html', context_dict)


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book

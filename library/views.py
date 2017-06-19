from library.models import Book, DVD, Magazine
from django.shortcuts import render



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

def genresearch(request):
    context_dict = {}
    return render(request, 'library/genresearch.html', context_dict)

def genresearchresults(request):
    search = request.GET.get('genre',"")
    context_dict = {'results': Book.objects.filter(genre=search),
                    'results2': DVD.objects.filter(genre=search),
                    'results3': Book.objects.filter(ISBN=search)}
    return render(request, 'library/genresearchresults.html', context_dict)



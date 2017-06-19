from library.models import Book, DVD, Magazine, Rental, User
from django.shortcuts import render
import datetime


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


def order_results(request):
    item_id = request.GET.get('item_id', "")
    my_id = request.GET.get('my_id', "")
    my_borrower = User.objects.get(pk=my_id)
    my_book = Book.objects.get(pk=item_id)
    my_rental = Rental(borrower=my_borrower, borrowed_item=my_book, status=1)
    my_rental.save()
    context_dict = {"my_book": my_book, "my_borrower": my_borrower}
    return render(request, 'library/thankyou.html', context_dict)


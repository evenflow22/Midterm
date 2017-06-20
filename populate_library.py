import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'midterm.settings')

import django
django.setup()
from library.models import Book, DVD, Magazine, Rental, User



def add_book(book_title, author, ISBN, genre, image):
    b = Book.objects.get_or_create(book_title=book_title)[0]
    b.author = author
    b.ISBN = ISBN
    b.genre = genre
    b.image =image
    b.save()

def add_dvd(dvd_title, director, genre, image):
    d = DVD.objects.get_or_create(dvd_title=dvd_title)[0]
    d.director = director
    d.genre = genre
    d.image = image
    d.save()

def add_magazine(magazine_title, magazine_publisher, image):
    m = Magazine.objects.get_or_create(magazine_title=magazine_title)[0]
    m.magazine_publisher=magazine_publisher
    m.image=image
    m.save()

def add_user(customer_firstname, customer_lastname, customer_balance):
    u = User.objects.get_or_create(
            customer_firstname=customer_firstname)[0]
    u.customer_lastname=customer_lastname
    u.customer_blanace=customer_balance
    u.save()
    # r.borrower=borrower
    # r.borrower_item=borrower_item
    # r.status=status
    # r.date_due=date_due

def populate():
    add_book("Hatchet", "Mr Anonymous", "4flk4", "fiction", None)
    add_dvd("Mighty Ducks", "Unnown", "Fiction", None)
    add_magazine("Popular Macanics", "Newburry", None)
    add_user("Rob", "McGinley", 20)

if __name__ == '__main__':

    populate()


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', midterm.settings)

import.django
django.setup()
from library.models import Book, DVD, Magazine, Rental, User



def add_book(book_title, author, ISBN, genre, image):
    b=Book.objects.getorcreate
    b.book_title = book_title
    b.author = author
    b.ISBN = ISBN
    b.genre = genre
    b.image =image

def add_dvd(dvd_title, director, genre, image):
    d=DVD.objects.getorcreate
    d.dvd_title = dvd_title
    d.director = director
    d.genre = genre
    d.image = image

def add_magazine(magazine_title, magazine_publisher, image):
    m=Magazine.objects.getorcreate
    m.magazine_title=magazine_title
    m.magazine_publisher=magazine_publisher
    m.image=image

def add_user(customer_firstname, customer_lastname, customer_balance):
    u=User.objects.getorcreate
    u.customer_firstname=customer_firstname
    u.customer_lastname=customer_lastname
    u.customer_blanace=customer_balance

def add_rental(borrower, borrower_item, status, date_due):
    r=Rental.objects.getorcreate
    r.borrower=borrower
    r.borrower_item=borrower_item
    r.status=status
    r.date_due=date_due

if __name__ == '__main__':

    populate()


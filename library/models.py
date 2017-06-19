from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    book_title = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=13, null=True)
    image = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.book_title + ' - ' + self.author + ' _ ' + self.ISBN



class DVD(models.Model):
    dvd_title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.dvd_title + ' - ' + self.director


class Magazine(models.Model):
    magazine_title = models.CharField(max_length=200)
    magazine_publisher = models.CharField(max_length=200)
    image = models.CharField(max_length=10000, null=True)

    # mag_date = models.CharField(max_length=200)

    def __str__(self):
        return self.magazine_title + ' - ' + self.magazine_publisher

class User(models.Model):
    customer_firstname = models.CharField(max_length=10)
    customer_lastname = models.CharField(max_length=10)
    customer_balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.customer_firstname + ' - ' + self.customer_lastname + '- ' + str(self.customer_balance)

class Rental(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="borrower")
    borrowed_item = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name="borrowed_item")
    status = models.BooleanField(default=True)
    date_due = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.borrower) + ' - ' + str(self.borrowed_item) + ' - ' + str(self.status) + ' - ' + str(self.date_due)


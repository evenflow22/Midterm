from django.db import  models

# Create your models here.
class Media(models.Model):
    media_type = models.CharField(max_length=200)
    book_title = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)

class DVD(models.Model):
    dvd_title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Magazine(models.Model):
    magazine_title = models.CharField(max_length=200)
    magazine_publisher = models.CharField(max_length=200)
    #mag_date = models.CharField(max_length=200)
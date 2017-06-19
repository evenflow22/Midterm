from django.contrib import admin
from .models import Book, DVD, Magazine, Rental, User

admin.site.register(Book)
admin.site.register(DVD)
admin.site.register(Magazine)
admin.site.register(User)
admin.site.register(Rental)

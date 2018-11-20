from django.contrib import admin
from mangaLibrary.models import Manga, Genre, Author

# Register your models here.
""" superuser, name: "admin" pass: "admin" NEVER WRITE YOUR PASS ON REAL CASES! """

admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(Author)
'''
Created on 20 nov. 2018

@author: A735843
'''
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('manga/', views.MangaListView.as_view(), name='mangas'),
    path('book/<int:pk>', views.MangaDetailView.as_view(), name='manga-detail'),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
]
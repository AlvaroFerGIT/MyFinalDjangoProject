from django.shortcuts import render
from mangaLibrary.models import Manga, Author
from django.views import generic

# Create your views here.

def index(request):
    
    context = {'hi':'hi'}
    
    return render(request, 'index.html', context=context)



# Clases heredadas de generic buscan su html dentro de app/templates/appname/class_generic/type
class MangaListView(generic.ListView):
    model = Manga
    paginate_by = 5
    
class MangaDetailView(generic.DetailView):
    model = Manga
    
class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author
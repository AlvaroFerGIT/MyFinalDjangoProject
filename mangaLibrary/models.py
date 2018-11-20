from django.db import models
from django.urls.base import reverse

# Create your models here.

""" Main Model of my Project """
class Manga(models.Model):
    name = models.CharField(max_length= 200, help_text="Name of the Manga")
    """ Foreign Key used OneToMany"""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'media/root', help_text="Image of the Manga")
    resume =  models.TextField(max_length=1000, help_text="Summary")
    """ Genre is ManytoMany """
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book. Este es el nombre que asignamos en urls!!!!!!!!!"""
        return reverse('book-detail', args=[str(self.id)])
    
class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Genre of the Manga')
     
    """String for representing the Model object."""
    def __str__(self):
        return self.name

class Author(models.Model):
    name =  models.CharField(max_length= 200, help_text="Name of the Author")
    alias = models.CharField(max_length= 50, help_text="Alias of the author, optional",null=True)
    author_image = models.ImageField(upload_to = 'media/root', help_text="Image of the Manga",null=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name
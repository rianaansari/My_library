from django.db import models
from django.db.models import deletion
from django.urls import reverse 
import uuid 
from django.contrib.auth.models import User



class Book(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('app1:book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('W', 'Want to read'),
        ('R', 'Read'),
        ('C', 'Currantly reading')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('app1:author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
#from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import permission_required
#from django.shortcuts import get_object_or_404
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

#import datetime

#from .forms import RenewBookForm
from . import models


class Index(generic.TemplateView):

    template_name='app1/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_authors'] =models.Author.objects.count()
        return context

class BookListView(generic.ListView):
    model=models.Book
    template_name='app1/book_list.html'

class BookDetailView(generic.DetailView):
    model = models.Book
    template_name='app1/book_detail.html'


class AuthorListView(generic.ListView):
    model = models.Author
    template_name ='app1/author_list.html'




class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    
    model = models.BookInstance
    template_name ='app1/bookinstances_list_books_user.html'
    paginate_by = 10

    def get_queryset(self):
        return models.BookInstance.objects.filter(reader=self.request.user)

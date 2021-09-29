from django.urls.conf import path
from django.urls.resolvers import URLPattern
from django.conf.urls import url
from . import views


app_name= 'app1'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-books'),
 #   url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian')
]


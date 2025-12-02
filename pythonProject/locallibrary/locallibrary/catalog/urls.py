from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    path('book//', views.BookDetailView.as_view(), name='book-detail'),

]

# from django.urls import path
# from . import views
#
# urlpatterns = [
# path('', views.index, name='index'),
# path('books/', views.BookListView.as_view(), name='books'),
# path('book//', views.BookDetailView.as_view(), name='book-detail'),
# path('authors/', views.AuthorListView.as_view(), name='authors'),
# path('books/authors/', views.AuthorListView.as_view(), name='books-authors'),
# path('author//', views.AuthorDetailView.as_view(), name='author-detail'),
#
# path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
# path('all-borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'),
# path('book//renew/', views.renew_book_librarian, name='renew-book-librarian'),
#
# path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
# path('author//update/', views.AuthorUpdate.as_view(), name='author-update'),
# path('author//delete/', views.AuthorDelete.as_view(), name='author-delete'),
#
# path('book/create/', views.BookCreate.as_view(), name='book-create'),
# path('book//update/', views.BookUpdate.as_view(), name='book-update'),
# path('book//delete/', views.BookDelete.as_view(), name='book-delete'),
# ]


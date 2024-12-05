"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import re_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view(), name='books-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(),
         name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(),
         name='authors-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(),
         name='my-borrowed'),
    path('edit_authors/', views.edit_authors, name='edit_authors'),
    path('authors_add/', views.add_author, name='authors_add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit_author/<int:id>/', views.edit_author, name='edit_author'),
    path('edit_books/', views.edit_books, name='edit_books'),
    path('edit_books/', views.edit_books, name='edit_books'), 
    path('book/create/', views.BookCreate.as_view(), name='book_create'), 
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), 
         name='book_update'), 
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), 
         name='book_delete'), 
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
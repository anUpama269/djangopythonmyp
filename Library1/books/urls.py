"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from books import  views
app_name="books"
urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.HomeView.as_view(),name="home"),
    # path('add_book',views.add_book,name="add_book"),
    path('add_book',views.AddBookView.as_view(),name="add_book"),
    # path('add_book1',views.add_book1,name="add_book1"),
    path('add_book1',views.AddBook1View.as_view(),name="add_book1"),
    #path('view_book',views.view_book,name="view_book"),
    path('view_book', views.ViewBookView.as_view(), name="view_book"),
    # path('edit_view/<int:i>',views.edit_view,name="edit_view"),
    path('edit_view/<int:i>',views.EditBookView.as_view(),name="edit_view"),
    # path('detail_view/<int:i>',views.detail_view,name="detail_view"),
    path('detail_view/<int:i>',views.BookDetailView.as_view(),name="detail_view"),
    # path('deletebook/<int:i>', views.deletebook, name="deletebook"),
    path('deletebook/<int:i>', views.DeleteBookView.as_view(), name="deletebook"),
    # path('search',views.search,name="search"),
    path('search',views.BookSearchView.as_view(),name="search"),

]

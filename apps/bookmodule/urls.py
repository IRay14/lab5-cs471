from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.index, name= "books.index"), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='books.links'),
    path('html5/text/formatting/', views.text_formatting_page, name='books.text_formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),
    path('html5/tables/', views.tables_page, name='books.tables'),
]